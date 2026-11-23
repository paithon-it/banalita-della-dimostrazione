import pytest

from banalita.judge import Claim, Judgment
from banalita.metrics import (Cell, cohen_kappa, coverage, error_rate, p4_cell, verdicts, wilson)


def _claim(label, kind="proof"):
    return Claim(text="x", kind=kind, label=label, source="none", page=0, quote="", note="")


def test_wilson_known_values():
    lo, hi = wilson(5, 100)
    assert lo == pytest.approx(0.0215, abs=1e-4) and hi == pytest.approx(0.1118, abs=1e-4)


def test_wilson_zero_successes():
    lo, hi = wilson(0, 30)
    assert lo == 0.0 and 0.10 < hi < 0.12
    assert wilson(0, 0) == (0.0, 1.0)


def test_kappa_perfect_and_chance():
    assert cohen_kappa(["a", "b", "a"], ["a", "b", "a"]) == pytest.approx(1.0)
    assert cohen_kappa(["a", "b", "a", "b"], ["a", "a", "b", "b"]) == pytest.approx(0.0)


def test_coverage_partial_half():
    j = Judgment(claims=[], coverage={"S1": "yes", "T1": "partial", "A1": "no", "T2": "yes"})
    assert coverage(j) == pytest.approx((1 + 0.5 + 0 + 1) / 4)


def test_error_rate_counts_errors_and_skips_declared_analogies():
    j = Judgment(claims=[_claim("supported"), _claim("contradicted"), _claim("analogy_as_fact"),
                         _claim("declared_analogy"), _claim("unsupported"),
                         _claim("supported", kind="context"), _claim("contradicted", kind="context")],
                 coverage={})
    # errori: 2 sulla dimostrazione + 1 di contesto; base: 4 sulla dimostrazione + 1 errore di contesto
    assert error_rate(j) == (3, 5)


def test_p4_needs_upper_bound():
    assert p4_cell(coverage=0.7, errors=4, claims=100)
    assert not p4_cell(coverage=0.7, errors=1, claims=30)   # 3,3% ma limite superiore 0,167
    assert not p4_cell(coverage=0.5, errors=0, claims=200)  # copertura sotto 0,6


def _table(**over):
    base = {}
    for arm in ("claude_full", "claude_overview", "qwen_overview"):
        for level in (1, 2, 3, 4):
            base[(arm, level)] = Cell(gulpease=80 - 10 * level, coverage=0.4 + 0.1 * level,
                                      errors=10 - 2 * level, claims=100, alerts_introduced=8, alerts_verified=10)
    base.update(over)
    return base


def test_verdicts_follow_the_rules():
    v = verdicts(_table())
    assert v["P1"]["passa"] and v["P2"]["passa"] and v["P3"]["passa"]
    assert not v["P4"]["passa"]  # errori 8% a L1, 6% a L2
    assert v["P5"]["passa"]      # 80% introdotte
    assert not v["P6"]["passa"]  # bracci identici: nessuno più fedele


def test_p6_needs_both_comparisons():
    t = _table()
    for level in (1, 2, 3, 4):
        t[("claude_full", level)] = Cell(60, 0.8, 1, 100, 0, 0)
        t[("claude_overview", level)] = Cell(60, 0.7, 3, 100, 0, 0)
        t[("qwen_overview", level)] = Cell(60, 0.6, 9, 100, 0, 0)
    assert verdicts(t)["P6"]["passa"]


def test_p6_not_testable_without_the_open_model():
    """Chiusura del 23/11/2026: senza il braccio di Qwen, P6 non passa né fallisce."""
    t = {}
    for level in (1, 2, 3, 4):
        t[("claude_full", level)] = Cell(60, 0.8, 1, 100, 0, 0)
        t[("claude_overview", level)] = Cell(60, 0.7, 3, 100, 0, 0)
    v = verdicts(t)
    assert v["P6"]["passa"] is None
    assert v["P6"]["dettaglio"]["claude_full"] < v["P6"]["dettaglio"]["claude_overview"]


def test_pooled_shares_with_wilson_intervals():
    from banalita.metrics import pooled_shares
    t = {}
    for level in (1, 2, 3, 4):
        t[("claude_full", level)] = Cell(60, 0.8, 1, 100, 2, 4)
        t[("claude_overview", level)] = Cell(60, 0.7, 3, 100, 1, 2)
    s = pooled_shares(t)
    assert s["P3"][1][:2] == (4, 200)
    lo, hi = s["P3"][1][2:]
    assert lo < 0.02 < hi
    assert s["P5"][:2] == (6, 12)
    assert s["P6"]["claude_full"][:2] == (4, 400) and s["P6"]["claude_overview"][:2] == (12, 400)
