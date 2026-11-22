import pytest

from banalita.requests import (ARMS, LEVELS, custom_id, explain_request, overview_prompt_text,
                               parse_custom_id)
from banalita.sources import load_sources

needs_sources = pytest.mark.skipif(
    not all(s.local.exists() for s in load_sources().values()),
    reason="fonti non scaricate (scripts/fetch_sources.py)",
)


def _blocks(req):
    return req["messages"][0]["content"]


@needs_sources
def test_full_arm_has_two_documents_cached():
    req = explain_request("claude_full", 1, 0)
    docs = [b for b in _blocks(req) if b["type"] == "document"]
    assert len(docs) == 2
    assert all(b["source"]["media_type"] == "application/pdf" for b in docs)
    assert docs[-1]["cache_control"] == {"type": "ephemeral", "ttl": "1h"}
    # i documenti vengono prima dell'istruzione
    assert _blocks(req)[-1]["type"] == "text"
    assert req["model"] == "claude-opus-5-5"


@needs_sources
def test_overview_arm_has_text_overview():
    req = explain_request("claude_overview", 2, 0)
    blocks = _blocks(req)
    assert not any(b["type"] == "document" for b in blocks)
    sources_block = blocks[0]
    assert "Mathematical overview" in sources_block["text"]
    assert "Stepanov" in sources_block["text"]  # dalla nota di Alpöge
    assert "Detecting zeros from sums over prime powers" not in sources_block["text"].split("Contents")[-1]
    assert sources_block["cache_control"] == {"type": "ephemeral", "ttl": "1h"}


@needs_sources
@pytest.mark.parametrize("level", [1, 2, 3, 4])
def test_prompt_states_reader_and_word_cap(level):
    reader, words = LEVELS[level]
    task = _blocks(explain_request("claude_full", level, 0))[-1]["text"]
    assert reader in task
    assert f"{words} parole" in task


@needs_sources
def test_prefix_identical_across_levels():
    """Sistema e fonti uguali a ogni livello: la cache si legge, non si riscrive."""
    a, b = explain_request("claude_full", 1, 0), explain_request("claude_full", 4, 3)
    assert a["system"] == b["system"]
    assert _blocks(a)[:-1] == _blocks(b)[:-1]


@needs_sources
def test_overview_prompt_text_matches_overview_arm():
    """Il modello aperto riceve esattamente il testo del braccio claude_overview."""
    req = explain_request("claude_overview", 3, 0)
    system, user = overview_prompt_text(3)
    assert system == req["system"][0]["text"]
    assert user == "\n\n".join(b["text"] for b in _blocks(req))


def test_custom_id_roundtrip():
    cid = custom_id("explain", "claude_overview", 2, 7)
    assert parse_custom_id(cid) == ("explain", "claude_overview", 2, 7)
    assert len(cid) <= 64


def test_unknown_arm_raises():
    with pytest.raises(ValueError):
        explain_request("gpt", 1, 0)


def test_arms_and_levels_as_in_spec():
    assert ARMS == ("claude_full", "claude_overview", "qwen_overview")
    assert LEVELS == {1: ("un bambino di dieci anni", 300),
                      2: ("uno studente di liceo", 600),
                      3: ("un laureato in matematica che non si occupa di teoria dei numeri", 1000),
                      4: ("un teorico dei numeri", 1500)}


def test_custom_id_accepts_source_arm_with_digits():
    assert parse_custom_id("critic-source_f2-L4-s00") == ("critic", "source_f2", 4, 0)
