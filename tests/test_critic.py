import json

import pytest

from banalita.critic import CRITIC_SCHEMA, VERIFY_SCHEMA, critic_request, verify_request
from banalita.sources import load_sources

needs_sources = pytest.mark.skipif(
    not all(s.local.exists() for s in load_sources().values()), reason="fonti non scaricate")


def test_critic_request_has_no_sources():
    req = critic_request("critic-claude_full-L1-s00", "Una spiegazione semplice.")
    blocks = req["messages"][0]["content"]
    assert all(b["type"] == "text" for b in blocks)
    joined = " ".join(b["text"] for b in blocks)
    assert "Una spiegazione semplice." in joined
    assert "Mathematical overview" not in joined and "Stepanov" not in joined
    assert req["output_config"]["format"]["schema"] == CRITIC_SCHEMA


def test_verify_categories_closed_set():
    enum = VERIFY_SCHEMA["properties"]["verdicts"]["items"]["properties"]["category"]["enum"]
    assert enum == ["introduced", "in_source", "false_alarm"]


@needs_sources
def test_verify_request_lists_alerts_in_order_with_sources():
    alerts = [{"passage": "p1", "problem": "x"}, {"passage": "p2", "problem": "y"}]
    req = verify_request("verify-claude_full-L1-s00", "Testo.", alerts)
    blocks = req["messages"][0]["content"]
    assert [b["type"] for b in blocks[:2]] == ["document", "document"]
    task = blocks[-1]["text"]
    assert task.index("[0]") < task.index("p1") < task.index("[1]") < task.index("p2")


@needs_sources
def test_source_target_uses_overview():
    from banalita.phases import build_critic
    reqs = build_critic(results_dir=load_sources()["F1"].local.parent.parent / "results-assenti")
    src = [cid for cid in reqs if cid.startswith("critic-source_f2-")]
    assert len(src) == 3
    text = reqs[src[0]]["messages"][0]["content"][-1]["text"]
    assert "Mathematical overview" in text


def test_empty_alert_list_skips_verify(tmp_path):
    from banalita.batch import Result
    from banalita.phases import build_verify
    d = tmp_path / "results"
    d.mkdir()
    rows = [Result("critic-claude_full-L1-s00", "succeeded", "{}", {"alerts": []}, {}, "end_turn"),
            Result("critic-claude_full-L2-s01", "succeeded", "{}", {"alerts": [{"passage": "a", "problem": "b"}]}, {}, "end_turn")]
    (d / "critic_claude.jsonl").write_text("\n".join(r.to_json() for r in rows) + "\n")
    (d / "explanations_claude.jsonl").write_text("\n".join(
        Result(f"explain-claude_full-L{l}-s0{s}", "succeeded", f"Testo {l}.", None, {}, "end_turn").to_json()
        for l, s in ((1, 0), (2, 1))) + "\n")
    try:
        reqs = build_verify(results_dir=d)
    except FileNotFoundError:
        pytest.skip("fonti non scaricate")
    assert list(reqs) == ["verify-claude_full-L2-s01"]
