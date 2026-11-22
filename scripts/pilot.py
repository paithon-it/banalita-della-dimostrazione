"""Prova pilota, fuori dai risultati: quattro spiegazioni (claude_full e claude_overview, L1 e
L4) e due giudizi, in batch. Serve a misurare la cache, i token d'uscita e il costo reale, per
aggiornare le stime delle fasi prima delle corse. La spesa entra nel registro del tetto.

Uso: uv run python scripts/pilot.py
"""
import json
import sys

from banalita.batch import run_batch
from banalita.costs import Ledger, cost
from banalita.judge import judge_request
from banalita.requests import custom_id, explain_request
from banalita.sources import ROOT

sys.path.insert(0, str(ROOT / "scripts"))
from run_phase import _api_key  # noqa: E402


def main() -> int:
    import anthropic
    client = anthropic.Anthropic(api_key=_api_key())
    ledger = Ledger(ROOT / "results" / "spend.jsonl")
    out = ROOT / "results" / "pilot"
    reqs = {custom_id("explain", arm, level, 0): explain_request(arm, level, 0)
            for arm in ("claude_full", "claude_overview") for level in (1, 4)}
    ex = run_batch(reqs, "pilot-explain", ledger, client, out / "explanations.jsonl", poll_seconds=30,
                   input_tokens=8_000, expected_output_tokens=10_000)
    jreqs = {custom_id("judge", "claude_full", level, 0):
             judge_request("x", ex[custom_id("explain", "claude_full", level, 0)].text, level)
             for level in (1, 4) if ex.get(custom_id("explain", "claude_full", level, 0), None)
             and ex[custom_id("explain", "claude_full", level, 0)].status == "succeeded"}
    ju = run_batch(jreqs, "pilot-judge", ledger, client, out / "judgments.jsonl", poll_seconds=30,
                   input_tokens=9_000, expected_output_tokens=14_000)
    for name, rs in (("spiegazioni", ex), ("giudizi", ju)):
        for cid, r in rs.items():
            print(name, cid, r.status, json.dumps(r.usage), f"{cost(r.usage, 'claude-opus-5-5', batch=True):.3f} $",
                  f"{len((r.text or '').split())} parole")
    print(f"spesi in tutto: {ledger.spent():.2f} $")
    return 0


if __name__ == "__main__":
    sys.exit(main())
