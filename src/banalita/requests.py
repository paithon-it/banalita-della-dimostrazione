"""Le richieste degli spiegatori (progetto, § 5).

Tre bracci: `claude_full` legge F1 e F2 in PDF; `claude_overview` e `qwen_overview` leggono
F1 e la sola panoramica di F2 in testo, identici, così la differenza fra i due misura il
modello e non la fonte. Sistema e fonti vengono prima dell'istruzione, uguali a ogni livello:
la cache (TTL di un'ora, quello che regge dentro un batch) si scrive una volta e si legge.
"""
from __future__ import annotations

import base64
import re
from functools import lru_cache
from pathlib import Path

from banalita.sources import ROOT, load_sources, overview_text, pdf_text

MODEL = "claude-opus-5-5"
ARMS = ("claude_full", "claude_overview", "qwen_overview")
LEVELS = {
    1: ("un bambino di dieci anni", 300),
    2: ("uno studente di liceo", 600),
    3: ("un laureato in matematica che non si occupa di teoria dei numeri", 1000),
    4: ("un teorico dei numeri", 1500),
}
CACHE = {"type": "ephemeral", "ttl": "1h"}
EFFORT = "high"
MAX_TOKENS = 32000
PROMPTS = ROOT / "prompts"

_ID = re.compile(r"^(?P<kind>[a-z0-9]+)-(?P<arm>[a-z_]+)-L(?P<level>[1-4])-s(?P<sample>\d{2})$")


def custom_id(kind: str, arm: str, level: int, sample: int) -> str:
    return f"{kind}-{arm}-L{level}-s{sample:02d}"


def parse_custom_id(cid: str) -> tuple[str, str, int, int]:
    m = _ID.match(cid)
    if not m:
        raise ValueError(f"custom_id non valido: {cid}")
    return m["kind"], m["arm"], int(m["level"]), int(m["sample"])


def _prompt(name: str) -> str:
    return (PROMPTS / name).read_text(encoding="utf-8").strip()


def task_text(level: int) -> str:
    reader, words = LEVELS[level]
    return _prompt("explain_task.it.md").format(reader=reader, words=words)


@lru_cache(maxsize=None)
def _pdf_b64(path: Path) -> str:
    return base64.standard_b64encode(Path(path).read_bytes()).decode("ascii")


@lru_cache(maxsize=None)
def overview_sources_text() -> str:
    """F1 e la panoramica di F2, in testo: il materiale dei bracci «overview»."""
    src = load_sources()
    f1 = pdf_text(src["F1"].local)
    f2 = overview_text(src["F2"].local)
    return ("FONTE 1. Levent Alpöge, nota del 20 novembre 2026 (testo estratto dal PDF):\n\n" + f1.strip()
            + "\n\nFONTE 2. Robin Zhang, nota preliminare sulla dimostrazione di Alpöge, "
              "sezione 1 «Mathematical overview» (testo estratto dal PDF):\n\n" + f2.strip())


def _system() -> list[dict]:
    return [{"type": "text", "text": _prompt("explain_system.it.md")}]


def overview_prompt_text(level: int) -> tuple[str, str]:
    """(sistema, utente) in testo semplice: lo stesso materiale per Claude e per Qwen."""
    return _system()[0]["text"], overview_sources_text() + "\n\n" + task_text(level)


def explain_request(arm: str, level: int, sample: int) -> dict:
    if arm not in ARMS or arm == "qwen_overview":
        raise ValueError(f"braccio non servito dall'API: {arm}")
    if level not in LEVELS:
        raise ValueError(f"livello sconosciuto: {level}")
    if arm == "claude_full":
        src = load_sources()
        content = [
            {"type": "document", "title": "Alpöge, nota del 20 novembre 2026",
             "source": {"type": "base64", "media_type": "application/pdf", "data": _pdf_b64(src["F1"].local)}},
            {"type": "document", "title": "Zhang, nota preliminare sulla dimostrazione di Alpöge",
             "source": {"type": "base64", "media_type": "application/pdf", "data": _pdf_b64(src["F2"].local)},
             "cache_control": CACHE},
        ]
    else:
        content = [{"type": "text", "text": overview_sources_text(), "cache_control": CACHE}]
    content.append({"type": "text", "text": task_text(level)})
    return {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "output_config": {"effort": EFFORT},
        "system": _system(),
        "messages": [{"role": "user", "content": content}],
    }
