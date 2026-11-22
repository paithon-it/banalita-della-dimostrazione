"""Lancia una fase dell'esperimento sulla Batch API.

Uso: ANTHROPIC_API_KEY=... uv run python scripts/run_phase.py --phase explain [--dry-run]

Le fasi costruiscono le loro richieste in `banalita.phases`; i risultati vanno in `results/`,
la spesa in `results/spend.jsonl` con il tetto di 60 dollari.
"""
import argparse
import os
import sys
from pathlib import Path

from banalita.batch import run_batch
from banalita.claude_code import run_claude_code
from banalita.costs import Ledger
from banalita.phases import PHASES
from banalita.sources import ROOT


# Con Claude Code non si paga a token: il tetto vale sul costo a listino dichiarato, come
# freno al consumo dell'abbonamento (stima di tutte le fasi a listino: circa 90 dollari).
CC_CAP = 150.0

KEY_FILE = Path.home() / ".config" / "banalita-della-dimostrazione" / "chiave.env"


def _api_key() -> str | None:
    """Dall'ambiente, o dal file scritto da scripts/imposta_chiave.sh (mai nel repository)."""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    if KEY_FILE.exists():
        for line in KEY_FILE.read_text().splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip()
    return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True, choices=sorted(PHASES))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--poll", type=int, default=60)
    ap.add_argument("--backend", choices=("claude-code", "api"), default="claude-code",
                    help="claude-code: claude -p con l'abbonamento (predefinito); api: Batch API con la chiave")
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args(argv)
    phase = PHASES[args.phase]
    requests = phase.build()
    out = ROOT / "results" / phase.out
    if args.backend == "claude-code":
        ledger = Ledger(ROOT / "results" / "spend.jsonl", cap=CC_CAP)
        run_claude_code(requests, args.phase, ledger, out, workers=args.workers, dry_run=args.dry_run)
        return 0
    client = None
    if not args.dry_run:
        import anthropic
        client = anthropic.Anthropic(api_key=_api_key())
    run_batch(requests, args.phase, Ledger(ROOT / "results" / "spend.jsonl"), client, out,
              poll_seconds=args.poll, input_tokens=phase.input_tokens,
              expected_output_tokens=phase.expected_output_tokens, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
