"""Lancia una fase dell'esperimento sulla Batch API.

Uso: ANTHROPIC_API_KEY=... uv run python scripts/run_phase.py --phase explain [--dry-run]

Le fasi costruiscono le loro richieste in `banalita.phases`; i risultati vanno in `results/`,
la spesa in `results/spend.jsonl` con il tetto di 60 dollari.
"""
import argparse
import sys

from banalita.batch import run_batch
from banalita.costs import Ledger
from banalita.phases import PHASES
from banalita.sources import ROOT


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True, choices=sorted(PHASES))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--poll", type=int, default=60)
    args = ap.parse_args(argv)
    phase = PHASES[args.phase]
    requests = phase.build()
    client = None
    if not args.dry_run:
        import anthropic
        client = anthropic.Anthropic()
    run_batch(requests, args.phase, Ledger(ROOT / "results" / "spend.jsonl"), client,
              ROOT / "results" / phase.out, poll_seconds=args.poll, input_tokens=phase.input_tokens,
              expected_output_tokens=phase.expected_output_tokens, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
