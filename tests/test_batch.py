import json
from types import SimpleNamespace as NS

import pytest

from banalita.batch import Result, estimate_cost, run_batch
from banalita.costs import BudgetExceeded, Ledger

OPUS = "claude-opus-5-5"


def _msg(text, stop="end_turn", out=100):
    return NS(content=[NS(type="thinking", thinking=""), NS(type="text", text=text)],
              stop_reason=stop,
              usage=NS(input_tokens=10, output_tokens=out, cache_read_input_tokens=1000,
                       cache_creation_input_tokens=0))


class FakeBatches:
    """Restituisce i risultati in ordine inverso; `script` dice il tipo per custom_id e giro."""

    def __init__(self, script):
        self.script = script  # {custom_id: [tipo al primo giro, tipo al secondo, ...]}
        self.created = []

    def create(self, requests):
        self.created.append([r["custom_id"] for r in requests])
        return NS(id=f"batch_{len(self.created)}")

    def retrieve(self, batch_id):
        return NS(id=batch_id, processing_status="ended", request_counts=NS(processing=0))

    def results(self, batch_id):
        round_ = int(batch_id.split("_")[1]) - 1
        out = []
        for cid in reversed(self.created[round_]):
            kind = self.script[cid][min(round_, len(self.script[cid]) - 1)]
            if kind in ("succeeded", "refusal", "max_tokens"):
                stop = {"succeeded": "end_turn"}.get(kind, kind)
                out.append(NS(custom_id=cid, result=NS(type="succeeded", message=_msg(f"testo {cid}", stop))))
            else:
                out.append(NS(custom_id=cid, result=NS(type=kind, error=NS(type="api_error"))))
        return out


def _client(script):
    return NS(messages=NS(batches=FakeBatches(script)))


def _reqs(*ids):
    return {cid: {"model": OPUS, "max_tokens": 1000, "messages": []} for cid in ids}


def test_results_matched_by_custom_id_out_of_order(tmp_path):
    client = _client({"a": ["succeeded"], "b": ["succeeded"]})
    res = run_batch(_reqs("a", "b"), "explain", Ledger(tmp_path / "s.jsonl"), client,
                    tmp_path / "out.jsonl", poll_seconds=0, expected_output_tokens=100)
    assert res["a"].text == "testo a" and res["b"].text == "testo b"


def test_errored_resubmitted_once(tmp_path):
    client = _client({"a": ["succeeded"], "b": ["errored", "errored"], "c": ["expired", "succeeded"]})
    res = run_batch(_reqs("a", "b", "c"), "explain", Ledger(tmp_path / "s.jsonl"), client,
                    tmp_path / "out.jsonl", poll_seconds=0, expected_output_tokens=100)
    assert client.messages.batches.created == [["a", "b", "c"], ["b", "c"]]
    assert res["b"].status == "errored"
    assert res["c"].status == "succeeded"


def test_refusal_recorded_not_raised(tmp_path):
    client = _client({"a": ["refusal"], "b": ["max_tokens"]})
    res = run_batch(_reqs("a", "b"), "explain", Ledger(tmp_path / "s.jsonl"), client,
                    tmp_path / "out.jsonl", poll_seconds=0, expected_output_tokens=100)
    assert res["a"].status == "refusal"
    assert res["b"].status == "max_tokens"


def test_refuses_when_estimate_exceeds_cap(tmp_path):
    client = _client({"a": ["succeeded"]})
    with pytest.raises(BudgetExceeded):
        run_batch(_reqs("a"), "explain", Ledger(tmp_path / "s.jsonl", cap=0.0001), client,
                  tmp_path / "out.jsonl", poll_seconds=0, expected_output_tokens=10_000)
    assert client.messages.batches.created == []


def test_dry_run_sends_nothing(tmp_path):
    client = _client({"a": ["succeeded"]})
    res = run_batch(_reqs("a"), "explain", Ledger(tmp_path / "s.jsonl"), client,
                    tmp_path / "out.jsonl", poll_seconds=0, expected_output_tokens=100, dry_run=True)
    assert res == {}
    assert client.messages.batches.created == []


def test_jsonl_written_one_line_per_result_and_spend_recorded(tmp_path):
    client = _client({"a": ["succeeded"], "b": ["refusal"]})
    led = Ledger(tmp_path / "s.jsonl")
    run_batch(_reqs("a", "b"), "explain", led, client, tmp_path / "out.jsonl",
              poll_seconds=0, expected_output_tokens=100)
    lines = [json.loads(l) for l in (tmp_path / "out.jsonl").read_text().splitlines()]
    assert sorted(l["custom_id"] for l in lines) == ["a", "b"]
    assert led.spent() > 0


def test_estimate_cost_uses_expected_output_and_batch_price():
    req = {"model": OPUS, "max_tokens": 32000, "messages": []}
    # 1.000 token di ingresso stimati, 10.000 in uscita, margine 1,5, in batch
    est = estimate_cost([req], input_tokens=1000, expected_output_tokens=10_000)
    assert est == pytest.approx((1000 * 4 + 15_000 * 20) / 1e6 / 2)


def test_result_from_jsonl_roundtrip(tmp_path):
    r = Result(custom_id="a", status="succeeded", text="x", parsed={"k": 1},
               usage={"input_tokens": 1}, stop_reason="end_turn")
    assert Result.from_json(r.to_json()) == r
