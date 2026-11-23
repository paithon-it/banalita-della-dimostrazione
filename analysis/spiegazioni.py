"""Le 64 spiegazioni di Claude in una forma che si legge, con la misura di ciascuna.

Uso:
    uv run python -m analysis.spiegazioni              # scrive results/spiegazioni.md
    uv run python -m analysis.spiegazioni --html ID    # l'HTML di una spiegazione, per citarla

Il testo dei modelli è in markdown (grassetti, corsivi, elenchi): `to_html` lo porta in HTML
senza cambiare una parola, e protegge i segni come «<» delle disuguaglianze.
"""
from __future__ import annotations

import html
import re
import sys
from collections import Counter
from pathlib import Path

from banalita.facts import facts_for_level, load_facts
from banalita.judge import parse_judgment
from banalita.metrics import coverage, error_rate
from banalita.phases import RESULTS, load_results
from banalita.readability import gulpease
from banalita.requests import LEVELS, parse_custom_id

ARM_NAMES = {"claude_full": "nota intera", "claude_overview": "panoramica"}
_BULLET = re.compile(r"^\s*[-*] +(.*)$")
_NUMBER = re.compile(r"^\s*\d+[.)] +(.*)$")


def _inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", t)
    return t


def to_html(text: str) -> str:
    out: list[str] = []
    for block in re.split(r"\n\s*\n", text.strip()):
        para: list[str] = []
        items: list[str] = []
        kind = None

        def flush_para():
            if para:
                out.append(f"<p>{_inline(' '.join(para))}</p>")
                para.clear()

        def flush_list():
            nonlocal kind
            if items:
                tag = "ul" if kind == "ul" else "ol"
                out.append(f"<{tag}>\n" + "\n".join(f"<li>{_inline(i)}</li>" for i in items) + f"\n</{tag}>")
                items.clear()
            kind = None

        for line in block.split("\n"):
            m_b, m_n = _BULLET.match(line), _NUMBER.match(line)
            if m_b or m_n:
                new_kind = "ul" if m_b else "ol"
                flush_para()
                if kind and kind != new_kind:
                    flush_list()
                kind = new_kind
                items.append((m_b or m_n).group(1).strip())
            elif line.strip():
                flush_list()
                para.append(line.strip())
        flush_para()
        flush_list()
    return "\n".join(out)


def _measures(results_dir: Path) -> dict[str, dict]:
    facts = load_facts()
    judg = {r.custom_id.replace("judge-", "explain-", 1): r for r in load_results(results_dir / "judgments.jsonl")}
    intro, flags = Counter(), Counter()
    for r in load_results(results_dir / "verifications.jsonl"):
        if not r.custom_id.startswith("verify-"):
            continue
        cid = r.custom_id.replace("verify-", "explain-", 1)
        for v in (r.parsed or {}).get("verdicts", []):
            flags[cid] += 1
            intro[cid] += v["category"] == "introduced"
    out = {}
    for r in load_results(results_dir / "explanations_claude.jsonl"):
        _, _, level, _ = parse_custom_id(r.custom_id)
        j = parse_judgment(judg[r.custom_id].parsed, [f.id for f in facts_for_level(facts, level)])
        e, n = error_rate(j)
        verdicts = Counter(j.coverage.values())
        out[r.custom_id] = {
            "text": r.text, "level": level, "coverage": coverage(j), "facts": verdicts, "errors": e, "base": n,
            "analogies": sum(c.label == "declared_analogy" for c in j.claims),
            "flags": flags[r.custom_id], "introduced": intro[r.custom_id],
            "words": len(r.text.split()), "gulpease": gulpease(r.text),
        }
    return out


def _it(x: float, digits: int) -> str:
    return f"{x:.{digits}f}".replace(".", ",")


def _line(m: dict) -> str:
    f = m["facts"]
    return (f"Fatti del livello: {f.get('yes', 0)} sì, {f.get('partial', 0)} in parte, {f.get('no', 0)} no "
            f"(copertura {_it(m['coverage'], 2)}) · errori {m['errors']} su {m['base']} · analogie dichiarate "
            f"{m['analogies']} · segnalazioni del critico {m['flags']}, errori introdotti {m['introduced']} · "
            f"{m['words']} parole (limite {LEVELS[m['level']][1]}) · Gulpease {_it(m['gulpease'], 1)}")


def write_markdown(results_dir: Path = RESULTS, out: Path | None = None) -> Path:
    results_dir = Path(results_dir)
    out = Path(out) if out else results_dir / "spiegazioni.md"
    ms = _measures(results_dir)
    lines = ["# Le 64 spiegazioni di Claude", "",
             "Il testo esatto di ogni spiegazione, raggruppato per lettore e per condizione, con la misura che "
             "ne danno il giudice, il critico e il verificatore. Generato da `analysis/spiegazioni.py` a partire "
             "da `results/`: i file JSONL restano la fonte.", ""]
    for level, (reader, cap) in LEVELS.items():
        lines += [f"## Livello {level}: {reader} (al più {cap} parole)", ""]
        for cid in sorted(c for c, m in ms.items() if m["level"] == level):
            _, arm, _, s = parse_custom_id(cid)
            lines += [f"### {cid.removeprefix('explain-')}", "",
                      f"*{ARM_NAMES.get(arm, arm)}, spiegazione {s + 1} di 8.* {_line(ms[cid])}", "",
                      ms[cid]["text"].strip(), ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--html":
        print(to_html(_measures(RESULTS)[sys.argv[2]]["text"]))
    else:
        print(write_markdown())
