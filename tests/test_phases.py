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


def _write_explanations(tmp_path, statuses):
    from banalita.batch import Result
    d = tmp_path / "results"
    d.mkdir()
    lines = []
    for i, st in enumerate(statuses):
        arm = "claude_full" if i % 2 == 0 else "qwen_overview"
        lines.append(Result(custom_id=f"explain-{arm}-L{1 + i % 4}-s{i:02d}", status=st,
                            text=f"Spiegazione {i}." if st == "succeeded" else None, parsed=None,
                            usage={}, stop_reason=None).to_json())
    (d / "explanations_claude.jsonl").write_text("\n".join(lines[::2]) + "\n")
    (d / "explanations_qwen.jsonl").write_text("\n".join(lines[1::2]) + "\n")
    return d


@needs_sources
def test_judge_phase_skips_failed_explanations(tmp_path):
    from banalita.phases import build_judge
    d = _write_explanations(tmp_path, ["succeeded", "succeeded", "refusal", "succeeded"])
    reqs = build_judge(results_dir=d)
    assert sorted(reqs) == ["judge-claude_full-L1-s00", "judge-qwen_overview-L2-s01", "judge-qwen_overview-L4-s03"]
    assert all(r["model"] == "claude-opus-5-5" for r in reqs.values())


@needs_sources
def test_judge2_is_sonnet_on_a_seeded_sample(tmp_path):
    from banalita.phases import build_judge2
    d = _write_explanations(tmp_path, ["succeeded"] * 40)
    a, b = build_judge2(results_dir=d, n=10), build_judge2(results_dir=d, n=10)
    assert list(a) == list(b) and len(a) == 10
    assert all(cid.startswith("judge2-") for cid in a)
    assert all(r["model"] == "claude-sonnet-5-5" for r in a.values())
