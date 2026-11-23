import csv
import json

from analysis.report import build_table, write_report
from banalita.batch import Result
from banalita.facts import facts_for_level, load_facts
from banalita.requests import custom_id

ARMS = ("claude_full", "claude_overview", "qwen_overview")


def _fake_results(d):
    facts = load_facts()
    rows = {"explanations_claude.jsonl": [], "explanations_qwen.jsonl": [], "judgments.jsonl": [],
            "verifications.jsonl": []}
    for arm in ARMS:
        for level in (1, 2, 3, 4):
            eid = custom_id("explain", arm, level, 0)
            target = "explanations_qwen.jsonl" if arm == "qwen_overview" else "explanations_claude.jsonl"
            rows[target].append(Result(eid, "succeeded", "Il gatto dorme. Il cane corre.", None, {}, "end_turn"))
            judgment = {"claims": [{"text": "x", "kind": "proof", "label": "supported", "source": "F1",
                                    "page": 1, "quote": "q", "note": ""},
                                   {"text": "y", "kind": "proof", "label": "contradicted", "source": "F1",
                                    "page": 1, "quote": "q", "note": "n"}],
                        "coverage": [{"fact_id": f.id, "verdict": "yes"} for f in facts_for_level(facts, level)]}
            rows["judgments.jsonl"].append(Result(custom_id("judge", arm, level, 0), "succeeded",
                                                  json.dumps(judgment), judgment, {}, "end_turn"))
            ver = {"verdicts": [{"index": 0, "category": "introduced", "reason": "r", "source": "F1", "page": 1}]}
            rows["verifications.jsonl"].append(Result(custom_id("verify", arm, level, 0), "succeeded",
                                                      json.dumps(ver), ver, {}, "end_turn"))
    for name, rs in rows.items():
        (d / name).write_text("\n".join(r.to_json() for r in rs) + "\n")


def test_report_builds_twelve_cells_and_writes_files(tmp_path):
    d = tmp_path / "results"
    d.mkdir()
    _fake_results(d)
    table, notes = build_table(d)
    assert len(table) == 12
    cell = table[("claude_full", 1)]
    assert (cell.errors, cell.claims) == (1, 2)
    assert cell.coverage == 1.0
    assert cell.gulpease > 100
    write_report(d)
    assert "P4" in (d / "report.md").read_text()
    with (d / "tables" / "cells.csv").open() as f:
        assert len(list(csv.DictReader(f))) == 12


def test_report_says_not_testable(tmp_path, monkeypatch):
    import analysis.report as rep
    fake = {k: {"passa": True, "dettaglio": [0, 0, 0, 0]} for k in ("P1", "P2", "P3", "P4", "P5")}
    fake["P6"] = {"passa": None, "dettaglio": {}}
    monkeypatch.setattr(rep, "verdicts", lambda table: fake)
    monkeypatch.setattr(rep, "build_table", lambda d, **kw: ({}, {"giudizi": 0, "giudizi_scartati": 0}))
    out = rep.write_report(tmp_path)
    assert "| P6 | non valutabile |" in out.read_text()


def test_p5_counts_only_the_main_critic(tmp_path):
    """Le verifiche del critico Qwen (verifyq) non entrano in P5, che riguarda il critico principale."""
    d = tmp_path / "results"
    d.mkdir()
    _fake_results(d)
    ver = {"verdicts": [{"index": 0, "category": "false_alarm", "reason": "r", "source": "F1", "page": 1}]}
    extra = Result(custom_id("verifyq", "claude_full", 1, 0), "succeeded", json.dumps(ver), ver, {}, "end_turn")
    with (d / "verifications.jsonl").open("a") as f:
        f.write(extra.to_json() + "\n")
    table, _ = build_table(d)
    assert table[("claude_full", 1)].alerts_verified == 1


def test_build_table_can_leave_listed_claims_out_of_the_errors(tmp_path):
    d = tmp_path / "results"
    d.mkdir()
    _fake_results(d)
    jid = custom_id("judge", "claude_full", 1, 0)
    table, _ = build_table(d, exclude=frozenset({(jid, 1)}))
    assert table[("claude_full", 1)].errors == 0
    assert table[("claude_full", 2)].errors == 1


def test_report_has_intervals_and_posthoc_sections(tmp_path):
    d = tmp_path / "results"
    d.mkdir()
    _fake_results(d)
    text = write_report(d).read_text()
    assert "Quote con intervallo di Wilson al 95%" in text
    assert "Analisi aggiunte dopo" in text
