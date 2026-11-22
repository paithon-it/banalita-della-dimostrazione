"""Le fasi che passano dalla Batch API: come costruiscono le richieste, dove scrivono, quanto
si stima che costino (ingresso equivalente e uscita attesa, da aggiornare dopo il pilota).

`input_tokens` è l'ingresso pagato a prezzo pieno equivalente: le fonti in cache costano un
ventesimo, quindi 150.000 token letti dalla cache valgono circa 7.500 token pieni.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from banalita.requests import LEVELS, custom_id, explain_request

SAMPLES = 8


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


PHASES: dict[str, Phase] = {
    "explain": Phase(build_explain, "explanations_claude.jsonl", input_tokens=8_000, expected_output_tokens=10_000),
}
