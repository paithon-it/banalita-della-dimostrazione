import json

import pytest

from banalita.facts import facts_for_level, load_facts
from banalita.judge import JUDGE_SCHEMA, JudgmentError, blind, judge_request, parse_judgment
from banalita.sources import load_sources

needs_sources = pytest.mark.skipif(
    not all(s.local.exists() for s in load_sources().values()), reason="fonti non scaricate")


def test_blind_removes_model_names_and_markdown():
    text = "## Titolo\n\n**Ciao!** Sono Qwen, un assistente. La dimostrazione l'ha scritta Alpöge con *Claude*."
    out = blind(text)
    assert "#" not in out and "*" not in out
    assert "Qwen" not in out and "Sono" not in out
    assert "Claude" in out  # è contenuto, non una firma
    assert out.startswith("Titolo")


def _parsed(fact_ids, label="supported"):
    return {"claims": [{"text": "x", "kind": "proof", "label": label, "source": "F1", "page": 1,
                        "quote": "q", "note": ""}],
            "coverage": [{"fact_id": f, "verdict": "yes"} for f in fact_ids]}


def test_schema_rejects_unknown_label():
    with pytest.raises(JudgmentError):
        parse_judgment(_parsed(["S1"], label="forse"), expected_fact_ids=["S1"])
    assert "forse" not in json.dumps(JUDGE_SCHEMA)


def test_coverage_must_match_level_facts():
    with pytest.raises(JudgmentError):
        parse_judgment(_parsed(["S1"]), expected_fact_ids=["S1", "T1"])
    with pytest.raises(JudgmentError):
        parse_judgment(_parsed(["S1", "I2"]), expected_fact_ids=["S1"])


@needs_sources
def test_request_lists_only_level_facts():
    req = judge_request("explain-claude_full-L1-s00", "Testo.", level=1)
    msg = req["messages"][0]["content"][-1]["text"]
    for f in load_facts():
        assert (f"- {f.id}:" in msg) == (f.min_level <= 1)


@needs_sources
def test_request_has_no_arm_information():
    req = judge_request("explain-qwen_overview-L2-s03", "Testo semplice.", level=2)
    # il base64 dei PDF può contenere qualunque sequenza di lettere: si guarda il testo
    texts = [b["text"] for b in req["messages"][0]["content"] if b["type"] == "text"]
    texts += [b.get("title", "") for b in req["messages"][0]["content"]]
    dump = json.dumps({"system": req["system"], "texts": texts}, ensure_ascii=False)
    for word in ("qwen", "claude_full", "_overview", "braccio", "explain-"):
        assert word not in dump.lower()


@needs_sources
def test_request_uses_structured_output_and_cached_sources():
    req = judge_request("x", "Testo.", level=3)
    assert req["output_config"]["format"]["type"] == "json_schema"
    blocks = req["messages"][0]["content"]
    assert [b["type"] for b in blocks[:2]] == ["document", "document"]
    assert blocks[-2]["cache_control"] == {"type": "ephemeral", "ttl": "1h"}


def test_parse_judgment_roundtrip():
    ids = [f.id for f in facts_for_level(load_facts(), 2)]
    j = parse_judgment(_parsed(ids), expected_fact_ids=ids)
    assert j.coverage == {i: "yes" for i in ids}
    assert j.claims[0].label == "supported" and j.claims[0].kind == "proof"
