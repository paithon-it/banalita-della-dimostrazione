"""Legge i risultati in `results/` e scrive le tabelle e i verdetti sulle previsioni.

Uso: uv run python -m analysis.report

Scrive `results/report.md` e `results/tables/cells.csv` (una riga per braccio e livello).
Un giudizio che non rispetta lo schema o i fatti attesi non entra nelle misure: si conta,
e il resoconto lo dice.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

from banalita.facts import facts_for_level, load_facts
from banalita.judge import JudgmentError, parse_judgment
from banalita.metrics import ARMS, LEVELS, Cell, coverage, error_rate, verdicts, wilson
from banalita.phases import RESULTS, explanations, load_results
from banalita.readability import gulpease
from banalita.requests import parse_custom_id


def build_table(results_dir: Path = RESULTS) -> tuple[dict, dict]:
    facts = load_facts()
    acc = defaultdict(lambda: {"g": [], "cov": [], "err": 0, "n": 0, "intro": 0, "ver": 0})
    notes = {"giudizi_scartati": 0, "giudizi": 0}
    for r in explanations(results_dir):
        _, arm, level, _ = parse_custom_id(r.custom_id)
        acc[(arm, level)]["g"].append(gulpease(r.text))
    for r in load_results(Path(results_dir) / "judgments.jsonl"):
        _, arm, level, _ = parse_custom_id(r.custom_id)
        expected = [f.id for f in facts_for_level(facts, level)]
        try:
            j = parse_judgment(r.parsed or {}, expected)
        except JudgmentError:
            notes["giudizi_scartati"] += 1
            continue
        notes["giudizi"] += 1
        e, n = error_rate(j)
        a = acc[(arm, level)]
        a["cov"].append(coverage(j))
        a["err"] += e
        a["n"] += n
    for r in load_results(Path(results_dir) / "verifications.jsonl"):
        _, arm, level, _ = parse_custom_id(r.custom_id)
        if arm not in ARMS:
            continue
        for v in (r.parsed or {}).get("verdicts", []):
            acc[(arm, level)]["ver"] += 1
            acc[(arm, level)]["intro"] += v["category"] == "introduced"
    table = {}
    for key, a in acc.items():
        table[key] = Cell(
            gulpease=sum(a["g"]) / len(a["g"]) if a["g"] else float("nan"),
            coverage=sum(a["cov"]) / len(a["cov"]) if a["cov"] else float("nan"),
            errors=a["err"], claims=a["n"], alerts_introduced=a["intro"], alerts_verified=a["ver"])
    return table, notes


def write_report(results_dir: Path = RESULTS) -> Path:
    results_dir = Path(results_dir)
    table, notes = build_table(results_dir)
    v = verdicts(table)
    (results_dir / "tables").mkdir(parents=True, exist_ok=True)
    with (results_dir / "tables" / "cells.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["arm", "level", "gulpease", "coverage", "errors", "claims", "error_rate",
                    "wilson_low", "wilson_high", "alerts_introduced", "alerts_verified"])
        for arm in ARMS:
            for level in LEVELS:
                c = table.get((arm, level))
                if c is None:
                    continue
                lo, hi = wilson(c.errors, c.claims)
                w.writerow([arm, level, f"{c.gulpease:.2f}", f"{c.coverage:.3f}", c.errors, c.claims,
                            f"{(c.errors / c.claims if c.claims else float('nan')):.4f}",
                            f"{lo:.4f}", f"{hi:.4f}", c.alerts_introduced, c.alerts_verified])
    lines = ["# Risultati", "", f"Giudizi usati: {notes['giudizi']}; scartati: {notes['giudizi_scartati']}.", "",
             "| Previsione | Esito | Dettaglio |", "|---|---|---|"]
    for k, d in v.items():
        esito = "non valutabile" if d["passa"] is None else ("passa" if d["passa"] else "non passa")
        lines.append(f"| {k} | {esito} | {json.dumps(d['dettaglio'], default=str)} |")
    out = results_dir / "report.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    print(write_report())
    sys.exit(0)
