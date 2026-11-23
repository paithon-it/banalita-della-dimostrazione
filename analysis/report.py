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
from banalita.metrics import ARMS, LEVELS, Cell, coverage, error_rate, pooled_shares, verdicts, wilson
from banalita.phases import RESULTS, explanations, load_results
from banalita.readability import gulpease
from banalita.requests import parse_custom_id

META_CLAIMS = Path(__file__).resolve().parent.parent / "data" / "posthoc" / "meta_claims.json"


def build_table(results_dir: Path = RESULTS, exclude: frozenset = frozenset(),
                letter_ends_sentence: bool = False) -> tuple[dict, dict]:
    """`exclude`: affermazioni (id del giudizio, indice) che non contano come errori;
    `letter_ends_sentence`: la variante del conteggio delle frasi. Le due opzioni servono solo
    alle analisi aggiunte dopo; senza, la tabella è quella del protocollo."""
    facts = load_facts()
    acc = defaultdict(lambda: {"g": [], "cov": [], "err": 0, "n": 0, "intro": 0, "ver": 0})
    notes = {"giudizi_scartati": 0, "giudizi": 0}
    for r in explanations(results_dir):
        _, arm, level, _ = parse_custom_id(r.custom_id)
        acc[(arm, level)]["g"].append(gulpease(r.text, letter_ends_sentence))
    for r in load_results(Path(results_dir) / "judgments.jsonl"):
        _, arm, level, _ = parse_custom_id(r.custom_id)
        expected = [f.id for f in facts_for_level(facts, level)]
        parsed = r.parsed or {}
        if exclude and parsed.get("claims"):
            parsed = {**parsed, "claims": [{**c, "label": "supported"} if (r.custom_id, i) in exclude else c
                                           for i, c in enumerate(parsed["claims"])]}
        try:
            j = parse_judgment(parsed, expected)
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
        kind, arm, level, _ = parse_custom_id(r.custom_id)
        if kind != "verify" or arm not in ARMS:  # P5 riguarda il solo critico principale
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
    lines += ["", "## Quote con intervallo di Wilson al 95%", ""] + _shares_lines(table)
    lines += ["", "## Analisi aggiunte dopo (23/11/2026)", "",
              "Non sono previsioni registrate: dicono quanto i verdetti dipendono da due scelte di misura.", ""]
    meta = _meta_claims()
    lines.append(f"**Affermazioni sul materiale.** {len(meta)} affermazioni di claude_overview dicono che cosa "
                 "le fonti dello spiegatore contengono o non contengono (`data/posthoc/meta_claims.json`): vere "
                 "per il suo materiale, false per le fonti del giudice. Se non contano come errori:")
    t2, _ = build_table(results_dir, exclude=meta)
    v2 = verdicts(t2)
    lines += ["", f"- P3: {_esito(v2['P3']['passa'])}", f"- P6, metà valutabile: {_esito(_p6_half(t2))}", ""]
    lines += _shares_lines(t2, only=("P3", "P6"))
    t3, _ = build_table(results_dir, letter_ends_sentence=True)
    v3 = verdicts(t3)
    lines += ["", "**Conteggio delle frasi.** Se il punto dopo una lettera sola chiude la frase (una variabile, "
              f"«fino a x.»): P1 {_esito(v3['P1']['passa'])}, Gulpease per livello "
              + ", ".join(f"{g:.2f}" for g in v3["P1"]["dettaglio"]) + "."]
    out = results_dir / "report.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def _esito(passa) -> str:
    return "non valutabile" if passa is None else ("passa" if passa else "non passa")


def _p6_half(table: dict):
    by = pooled_shares(table)["P6"]
    if not all(by.get(a, (0, 0))[1] for a in ("claude_full", "claude_overview")):
        return None
    return by["claude_full"][0] / by["claude_full"][1] < by["claude_overview"][0] / by["claude_overview"][1]


def _fmt(share: tuple) -> str:
    e, n, lo, hi = share
    return f"{e}/{n} = {100 * e / n:.2f}% ({100 * lo:.2f}-{100 * hi:.2f}%)" if n else "nessun dato"


def _shares_lines(table: dict, only=("P3", "P5", "P6")) -> list[str]:
    s = pooled_shares(table)
    out = []
    if "P3" in only:
        out += [f"- P3, errori a L{l}: {_fmt(s['P3'][l])}" for l in LEVELS]
    if "P5" in only:
        out.append(f"- P5, segnalazioni introdotte a L1-L2: {_fmt(s['P5'])}")
    if "P6" in only:
        out += [f"- P6, errori di {a}: {_fmt(sh)}" for a, sh in s["P6"].items()]
    return out


def _meta_claims() -> frozenset:
    if not META_CLAIMS.exists():
        return frozenset()
    doc = json.loads(META_CLAIMS.read_text(encoding="utf-8"))
    return frozenset((c["judgment"], c["index"]) for c in doc["claims"])


if __name__ == "__main__":
    print(write_report())
    sys.exit(0)
