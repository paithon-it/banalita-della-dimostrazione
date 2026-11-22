"""Le fasi che passano dalla Batch API: come costruiscono le richieste, dove scrivono, quanto
si stima che costino (ingresso equivalente e uscita attesa, da aggiornare dopo il pilota).

`input_tokens` è l'ingresso pagato a prezzo pieno equivalente: le fonti in cache costano un
ventesimo, quindi 150.000 token letti dalla cache valgono circa 7.500 token pieni.
"""
from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from banalita.batch import Result
from banalita.judge import judge_request
from banalita.requests import LEVELS, custom_id, explain_request, parse_custom_id
from banalita.sources import ROOT

SAMPLES = 8
SEED = 20261122
RESULTS = ROOT / "results"
EXPLANATION_FILES = ("explanations_claude.jsonl", "explanations_qwen.jsonl")


@dataclass(frozen=True)
class Phase:
    build: Callable[[], dict[str, dict]]
    out: str
    input_tokens: int
    expected_output_tokens: int


def build_explain() -> dict[str, dict]:
    return {custom_id("explain", arm, level, s): explain_request(arm, level, s)
            for arm in ("claude_full", "claude_overview")
            for level in LEVELS
            for s in range(SAMPLES)}


def load_results(path: Path) -> list[Result]:
    if not Path(path).exists():
        return []
    return [Result.from_json(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]


def explanations(results_dir: Path = RESULTS) -> list[Result]:
    """Le spiegazioni riuscite di tutti i bracci, in ordine di custom_id."""
    out = [r for f in EXPLANATION_FILES for r in load_results(Path(results_dir) / f) if r.status == "succeeded"]
    return sorted(out, key=lambda r: r.custom_id)


def _judge_id(kind: str, explanation_id: str) -> str:
    _, arm, level, sample = parse_custom_id(explanation_id)
    return custom_id(kind, arm, level, sample)


def build_judge(results_dir: Path = RESULTS) -> dict[str, dict]:
    reqs = {}
    for r in explanations(results_dir):
        level = parse_custom_id(r.custom_id)[2]
        reqs[_judge_id("judge", r.custom_id)] = judge_request(r.custom_id, r.text, level)
    return reqs


def build_judge2(results_dir: Path = RESULTS, n: int = 24, seed: int = SEED) -> dict[str, dict]:
    """Il secondo giudice (Sonnet 5.5) su un campione estratto con il seme del protocollo."""
    pool = explanations(results_dir)
    chosen = sorted(random.Random(seed).sample(pool, min(n, len(pool))), key=lambda r: r.custom_id)
    return {_judge_id("judge2", r.custom_id): judge_request(r.custom_id, r.text, parse_custom_id(r.custom_id)[2],
                                                           model="claude-sonnet-5-5")
            for r in chosen}


PHASES: dict[str, Phase] = {
    "explain": Phase(build_explain, "explanations_claude.jsonl", input_tokens=8_000, expected_output_tokens=10_000),
    "judge": Phase(build_judge, "judgments.jsonl", input_tokens=9_000, expected_output_tokens=14_000),
    "judge2": Phase(build_judge2, "judgments2.jsonl", input_tokens=9_000, expected_output_tokens=14_000),
}
