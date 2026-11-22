import subprocess
import sys

import pytest

from banalita.phases import PHASES
from banalita.requests import parse_custom_id
from banalita.sources import ROOT, load_sources

needs_sources = pytest.mark.skipif(
    not all(s.local.exists() for s in load_sources().values()), reason="fonti non scaricate")


@needs_sources
def test_explain_phase_builds_64_claude_requests():
    reqs = PHASES["explain"].build()
    assert len(reqs) == 64
    arms = {parse_custom_id(cid)[1] for cid in reqs}
    assert arms == {"claude_full", "claude_overview"}


@needs_sources
def test_dry_run_cli_prints_estimate():
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "run_phase.py"), "--phase", "explain", "--dry-run"],
                         capture_output=True, text=True, check=True).stdout
    assert "explain: 64 richieste" in out
