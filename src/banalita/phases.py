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
from banalita.critic import critic_request, verify_request
from banalita.judge import judge_request
from banalita.requests import LEVELS, custom_id, explain_request, parse_custom_id
from banalita.sources import ROOT, load_sources, overview_text

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
    """Un risultato per custom_id: il riuscito se c'è (una ripresa può aver scritto prima un
    errore), altrimenti l'ultimo."""
    if not Path(path).exists():
        return []
    best: dict[str, Result] = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = Result.from_json(line)
        prev = best.get(r.custom_id)
        if prev is None or prev.status != "succeeded":
            best[r.custom_id] = r
    return list(best.values())


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


SOURCE_ARM = "source_f2"
SOURCE_SAMPLES = 3
CRITIC_FILES = {"critic_claude.jsonl": "verify", "critic_qwen.jsonl": "verifyq"}


def _source_text() -> str:
    return overview_text(load_sources()["F2"].local)


def build_critic(results_dir: Path = RESULTS) -> dict[str, dict]:
    """Il critico su ogni spiegazione riuscita, e tre volte sulla panoramica di F2."""
    reqs = {_judge_id("critic", r.custom_id): critic_request(r.custom_id, r.text) for r in explanations(results_dir)}
    for s in range(SOURCE_SAMPLES):
        cid = custom_id("critic", SOURCE_ARM, 4, s)
        reqs[cid] = critic_request(cid, _source_text(), blinded=False)
    return reqs


def build_verify(results_dir: Path = RESULTS) -> dict[str, dict]:
    """La verifica delle segnalazioni dei due critici; chi non ha segnalato niente non passa."""
    texts = {_judge_id("x", r.custom_id): r.text for r in explanations(results_dir)}
    reqs = {}
    for fname, kind in CRITIC_FILES.items():
        for r in load_results(Path(results_dir) / fname):
            alerts = (r.parsed or {}).get("alerts") or []
            if r.status != "succeeded" or not alerts:
                continue
            _, arm, level, sample = parse_custom_id(r.custom_id)
            vid = custom_id(kind, arm, level, sample)
            if arm == SOURCE_ARM:
                reqs[vid] = verify_request(vid, _source_text(), alerts, blinded=False)
            else:
                reqs[vid] = verify_request(vid, texts[custom_id("x", arm, level, sample)], alerts)
    return reqs


PHASES: dict[str, Phase] = {
    "explain": Phase(build_explain, "explanations_claude.jsonl", input_tokens=8_000, expected_output_tokens=10_000),
    "judge": Phase(build_judge, "judgments.jsonl", input_tokens=9_000, expected_output_tokens=14_000),
    "judge2": Phase(build_judge2, "judgments2.jsonl", input_tokens=9_000, expected_output_tokens=14_000),
    "critic": Phase(build_critic, "critic_claude.jsonl", input_tokens=1_500, expected_output_tokens=8_000),
    "verify": Phase(build_verify, "verifications.jsonl", input_tokens=9_000, expected_output_tokens=8_000),
}
