import json

import pytest

from banalita.costs import BudgetExceeded, Ledger, cost

OPUS = "claude-opus-5-5"
SONNET = "claude-sonnet-5-5"


def _usage(inp=0, out=0, read=0, write=0):
    return {"input_tokens": inp, "output_tokens": out,
            "cache_read_input_tokens": read, "cache_creation_input_tokens": write}


def test_cost_opus_standard():
    assert cost(_usage(inp=1_000_000, out=1_000_000), OPUS, batch=False) == pytest.approx(24.0)


def test_cost_opus_batch_halves():
    assert cost(_usage(inp=1_000_000, out=1_000_000), OPUS, batch=True) == pytest.approx(12.0)


def test_cache_read_and_write_priced():
    assert cost(_usage(read=1_000_000), OPUS, batch=False) == pytest.approx(0.20)
    assert cost(_usage(write=1_000_000), OPUS, batch=False, cache_ttl="1h") == pytest.approx(8.0)
    assert cost(_usage(write=1_000_000), OPUS, batch=False, cache_ttl="5m") == pytest.approx(5.0)
    assert cost(_usage(write=1_000_000), OPUS, batch=True, cache_ttl="1h") == pytest.approx(4.0)


def test_cost_sonnet():
    assert cost(_usage(inp=1_000_000, out=1_000_000, read=1_000_000), SONNET, batch=False) == pytest.approx(12.10)


def test_unknown_model_raises():
    with pytest.raises(KeyError):
        cost(_usage(inp=1), "claude-sconosciuto", batch=False)


def test_ledger_refuses_over_cap(tmp_path):
    led = Ledger(tmp_path / "spend.jsonl", cap=60.0)
    led.record("explain", _usage(inp=2_000_000, out=2_000_000), OPUS, batch=True)  # 24
    led.record("judge", _usage(inp=2_000_000, out=2_000_000), OPUS, batch=False)  # 48
    assert led.spent() == pytest.approx(72.0)
    assert not led.can_afford(0.01)


def test_ledger_can_afford_within_cap(tmp_path):
    led = Ledger(tmp_path / "spend.jsonl", cap=60.0)
    led.record("explain", _usage(inp=1_000_000, out=2_500_000), OPUS, batch=False)  # 4 + 50 = 54
    assert led.can_afford(5.9)
    assert not led.can_afford(6.1)


def test_ledger_persists_across_instances(tmp_path):
    path = tmp_path / "spend.jsonl"
    Ledger(path).record("explain", _usage(inp=1_000_000), OPUS, batch=False)
    assert Ledger(path).spent() == pytest.approx(4.0)


def test_require_raises_budget_exceeded(tmp_path):
    led = Ledger(tmp_path / "spend.jsonl", cap=1.0)
    with pytest.raises(BudgetExceeded):
        led.require(1.5, phase="judge")


def test_cache_miss_warning(tmp_path):
    path = tmp_path / "spend.jsonl"
    led = Ledger(path)
    led.record("judge", _usage(inp=150_000, out=1_000), OPUS, batch=True, expect_cache=True)
    line = json.loads(path.read_text().splitlines()[-1])
    assert line["warning"] == "cache_miss"
