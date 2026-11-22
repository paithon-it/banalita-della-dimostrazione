"""Prova pilota, fuori dai risultati: quattro spiegazioni (claude_full e claude_overview, L1 e
L4) e due giudizi, attraverso Claude Code. Serve a misurare la cache, i token d'uscita, il
consumo e la forma delle risposte prima delle corse.

Uso: uv run python scripts/pilot.py
"""
import json
import sys

from banalita.claude_code import run_claude_code
from banalita.costs import Ledger, cost
from banalita.judge import judge_request
from banalita.requests import custom_id, explain_request
from banalita.sources import ROOT


def main() -> int:
    ledger = Ledger(ROOT / "results" / "spend.jsonl", cap=150.0)
    out = ROOT / "results" / "pilot"
    reqs = {custom_id("explain", arm, level, 0): explain_request(arm, level, 0)
            for arm in ("claude_full", "claude_overview") for level in (1, 4)}
    ex = run_claude_code(reqs, "pilot-explain", ledger, out / "explanations.jsonl", workers=2)
    jreqs = {}
    for level in (1, 4):
        r = ex.get(custom_id("explain", "claude_full", level, 0))
        if r and r.status == "succeeded":
            jreqs[custom_id("judge", "claude_full", level, 0)] = judge_request("x", r.text, level)
    ju = run_claude_code(jreqs, "pilot-judge", ledger, out / "judgments.jsonl", workers=2)
    for name, rs in (("spiegazioni", ex), ("giudizi", ju)):
        for cid, r in sorted(rs.items()):
            print(name, cid, r.status, json.dumps(r.usage),
                  f"listino {cost(r.usage, 'claude-opus-5-5', batch=False, cache_ttl='1h'):.3f} $",
                  f"{len((r.text or '').split())} parole")
    print(f"a listino in tutto: {ledger.spent():.2f} $")
    return 0


if __name__ == "__main__":
    sys.exit(main())
