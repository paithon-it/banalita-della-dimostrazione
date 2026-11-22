"""Quanto costa ogni chiamata a Claude, e il tetto di spesa dell'esperimento.

Prezzi in dollari per milione di token, quelli del 22/11/2026 (progetto, § 9). La Batch API
costa la metà di ogni voce. La scrittura in cache costa 1,25 volte l'ingresso con il TTL di
cinque minuti, il doppio con quello di un'ora. Il registro della spesa è un file JSONL, una
riga per chiamata: si somma da lì, così un'interruzione non perde il conto.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

PRICES = {
    "claude-opus-5-5": {"input": 4.0, "output": 20.0, "cache_read": 0.20,
                        "cache_write_5m": 5.0, "cache_write_1h": 8.0},
    "claude-sonnet-5-5": {"input": 2.0, "output": 10.0, "cache_read": 0.10,
                          "cache_write_5m": 2.5, "cache_write_1h": 4.0},
}

CAP_DOLLARS = 60.0


class BudgetExceeded(Exception):
    """Una fase supererebbe il tetto di spesa."""


def cost(usage: dict, model: str, batch: bool, cache_ttl: str = "1h") -> float:
    p = PRICES[model]
    write_price = p["cache_write_1h"] if cache_ttl == "1h" else p["cache_write_5m"]
    dollars = (
        usage.get("input_tokens", 0) * p["input"]
        + usage.get("output_tokens", 0) * p["output"]
        + usage.get("cache_read_input_tokens", 0) * p["cache_read"]
        + usage.get("cache_creation_input_tokens", 0) * write_price
    ) / 1_000_000
    return dollars / 2 if batch else dollars


class Ledger:
    def __init__(self, path: Path | str, cap: float = CAP_DOLLARS):
        self.path = Path(path)
        self.cap = cap

    def _lines(self) -> list[dict]:
        if not self.path.exists():
            return []
        return [json.loads(l) for l in self.path.read_text(encoding="utf-8").splitlines() if l.strip()]

    def spent(self) -> float:
        return sum(l["dollars"] for l in self._lines())

    def can_afford(self, estimate: float) -> bool:
        return self.spent() + estimate <= self.cap

    def require(self, estimate: float, phase: str) -> None:
        if not self.can_afford(estimate):
            raise BudgetExceeded(
                f"{phase}: stima {estimate:.2f} $, già spesi {self.spent():.2f} $, tetto {self.cap:.2f} $")

    def record(self, phase: str, usage: dict, model: str, batch: bool,
               expect_cache: bool = False, cache_ttl: str = "1h", custom_id: str | None = None) -> float:
        dollars = cost(usage, model, batch, cache_ttl)
        line = {"time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "phase": phase,
                "custom_id": custom_id, "model": model, "batch": batch, "usage": usage,
                "dollars": round(dollars, 6)}
        if expect_cache and not usage.get("cache_read_input_tokens") and not usage.get("cache_creation_input_tokens"):
            line["warning"] = "cache_miss"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
        return dollars
