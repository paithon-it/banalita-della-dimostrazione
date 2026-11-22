"""Le chiamate a Claude in batch (metà prezzo), con il tetto di spesa.

Prima di inviare si stima il costo e si chiede al registro della spesa; i risultati arrivano
in ordine sparso e si abbinano per `custom_id`; quelli in errore o scaduti si rimettono in coda
una volta sola; un rifiuto o un'uscita troncata si registrano con quello stato, senza fermare
la fase. Ogni risultato è una riga JSONL in `out`, ogni batch una riga in `batches.jsonl`.
"""
from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from banalita.costs import PRICES, Ledger

OUTPUT_MARGIN = 1.5
RETRYABLE = ("errored", "expired", "canceled")


@dataclass
class Result:
    custom_id: str
    status: str
    text: str | None
    parsed: dict | None
    usage: dict
    stop_reason: str | None

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    @classmethod
    def from_json(cls, line: str) -> "Result":
        return cls(**json.loads(line))


def estimate_cost(requests: list[dict], input_tokens: int, expected_output_tokens: int) -> float:
    total = 0.0
    for req in requests:
        p = PRICES[req["model"]]
        total += (input_tokens * p["input"] + expected_output_tokens * OUTPUT_MARGIN * p["output"]) / 1e6
    return total / 2


def _usage(msg) -> dict:
    u = msg.usage
    return {k: int(getattr(u, k, 0) or 0) for k in
            ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")}


def _to_result(item) -> Result:
    kind = item.result.type
    if kind != "succeeded":
        return Result(item.custom_id, kind, None, None, {}, None)
    msg = item.result.message
    text = "".join(b.text for b in msg.content if getattr(b, "type", None) == "text")
    status = msg.stop_reason if msg.stop_reason in ("refusal", "max_tokens") else "succeeded"
    parsed = None
    if status == "succeeded":
        try:
            parsed = json.loads(text)
        except (json.JSONDecodeError, TypeError):
            parsed = None
    return Result(item.custom_id, status, text, parsed, _usage(msg), msg.stop_reason)


def _submit_and_wait(client, requests: dict[str, dict], poll_seconds: int, log: Path) -> list:
    batch = client.messages.batches.create(
        requests=[{"custom_id": cid, "params": params} for cid, params in requests.items()])
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"batch_id": batch.id, "n": len(requests),
                            "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}) + "\n")
    while client.messages.batches.retrieve(batch.id).processing_status != "ended":
        time.sleep(poll_seconds)
    return list(client.messages.batches.results(batch.id))


def run_batch(requests: dict[str, dict], phase: str, ledger: Ledger, client, out: Path,
              poll_seconds: int = 60, input_tokens: int = 0, expected_output_tokens: int = 8000,
              expect_cache: bool = True, dry_run: bool = False) -> dict[str, Result]:
    out = Path(out)
    estimate = estimate_cost(list(requests.values()), input_tokens, expected_output_tokens)
    if dry_run:
        print(f"{phase}: {len(requests)} richieste, stima {estimate:.2f} $, spesi {ledger.spent():.2f} $")
        return {}
    ledger.require(estimate, phase)
    out.parent.mkdir(parents=True, exist_ok=True)
    log = out.parent / "batches.jsonl"
    results: dict[str, Result] = {}
    pending = dict(requests)
    for attempt in range(2):
        failed = set()
        for item in _submit_and_wait(client, pending, poll_seconds, log):
            res = _to_result(item)
            if res.status in RETRYABLE and attempt == 0:
                failed.add(res.custom_id)
                continue
            results[res.custom_id] = res
            if res.usage:
                ledger.record(phase, res.usage, pending[res.custom_id]["model"], batch=True,
                              expect_cache=expect_cache, custom_id=res.custom_id)
            with out.open("a", encoding="utf-8") as f:
                f.write(res.to_json() + "\n")
        if not failed:
            break
        pending = {cid: params for cid, params in pending.items() if cid in failed}
    return results
