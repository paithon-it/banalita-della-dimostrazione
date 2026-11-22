"""Il giudice (progetto, § 6): scompone una spiegazione in affermazioni, ne giudica la fedeltà
alle fonti e decide la copertura dei fatti di riferimento del suo livello.

Alla cieca: riceve la spiegazione ripulita da `blind`, il lettore a cui era rivolta e i fatti
del livello, mai il braccio. Le fonti (F1 e F2 in PDF, F3a e F3b in testo) vengono prima e
stanno in cache; l'uscita è JSON vincolato da `JUDGE_SCHEMA`.
"""
from __future__ import annotations

import html
import re
from dataclasses import dataclass
from functools import lru_cache

from banalita.facts import facts_for_level, load_facts
from banalita.requests import CACHE, LEVELS, MAX_TOKENS, PROMPTS, _pdf_b64
from banalita.sources import load_sources

OPUS = "claude-opus-5-5"
LABELS = ("supported", "unsupported", "contradicted", "declared_analogy", "analogy_as_fact")
KINDS = ("proof", "context")
VERDICTS = ("yes", "partial", "no")
SOURCE_IDS = ("F1", "F2", "F3a", "F3b", "none")
ERROR_LABELS = ("contradicted", "analogy_as_fact")

JUDGE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["claims", "coverage"],
    "properties": {
        "claims": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["text", "kind", "label", "source", "page", "quote", "note"],
            "properties": {
                "text": {"type": "string"},
                "kind": {"type": "string", "enum": list(KINDS)},
                "label": {"type": "string", "enum": list(LABELS)},
                "source": {"type": "string", "enum": list(SOURCE_IDS)},
                "page": {"type": "integer"},
                "quote": {"type": "string"},
                "note": {"type": "string"},
            }}},
        "coverage": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["fact_id", "verdict"],
            "properties": {
                "fact_id": {"type": "string"},
                "verdict": {"type": "string", "enum": list(VERDICTS)},
            }}},
    },
}


class JudgmentError(ValueError):
    """Un giudizio non rispetta lo schema o i fatti attesi."""


@dataclass(frozen=True)
class Claim:
    text: str
    kind: str
    label: str
    source: str
    page: int
    quote: str
    note: str


@dataclass(frozen=True)
class Judgment:
    claims: list[Claim]
    coverage: dict[str, str]


_SELF = re.compile(r"(?i)\b(?:io\s+)?sono\s+(?:qwen|claude|un\s+(?:modello|assistente)[^.!?]*)[^.!?]*[.!?]\s*")


def blind(text: str) -> str:
    """Toglie markdown e autopresentazioni; lascia i nomi che fanno parte del contenuto."""
    t = _SELF.sub("", text)
    t = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", t)
    t = re.sub(r"(\*\*|__|\*|_|`)", "", t)
    t = re.sub(r"\bQwen\w*\b", "", t)
    return " ".join(t.split())


def _html_text(path) -> str:
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", path.read_text(encoding="utf-8"))
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", raw)).split())


@lru_cache(maxsize=None)
def _f3_text() -> str:
    src = load_sources()
    return ("F3a. Dichiarazione congiunta delle comunità di Lean e Mathlib, 21 novembre 2026:\n\n"
            + _html_text(src["F3a"].local)
            + "\n\nF3b. Pagina dei controlli di Andrew Sutherland (MIT), copia del 22 novembre 2026:\n\n"
            + _html_text(src["F3b"].local))


def _system() -> list[dict]:
    return [{"type": "text", "text": (PROMPTS / "judge_system.it.md").read_text(encoding="utf-8").strip()}]


def judge_request(explanation_id: str, text: str, level: int, model: str = OPUS) -> dict:
    src = load_sources()
    facts = facts_for_level(load_facts(), level)
    reader = LEVELS[level][0]
    listing = "\n".join(f"- {f.id}: {f.text}" for f in facts)
    task = (f"FATTI DI RIFERIMENTO (giudica la copertura di tutti e soli questi):\n{listing}\n\n"
            f"SPIEGAZIONE DA VALUTARE, scritta per {reader}:\n<<<\n{blind(text)}\n>>>")
    content = [
        {"type": "document", "title": "F1. Alpöge, nota del 20 novembre 2026",
         "source": {"type": "base64", "media_type": "application/pdf", "data": _pdf_b64(src["F1"].local)}},
        {"type": "document", "title": "F2. Zhang, nota preliminare sulla dimostrazione di Alpöge",
         "source": {"type": "base64", "media_type": "application/pdf", "data": _pdf_b64(src["F2"].local)}},
        {"type": "text", "text": _f3_text(), "cache_control": CACHE},
        {"type": "text", "text": task},
    ]
    return {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
        "system": _system(),
        "messages": [{"role": "user", "content": content}],
    }


def parse_judgment(parsed: dict, expected_fact_ids: list[str]) -> Judgment:
    try:
        claims = [Claim(**c) for c in parsed["claims"]]
        coverage = {c["fact_id"]: c["verdict"] for c in parsed["coverage"]}
    except (KeyError, TypeError) as e:
        raise JudgmentError(f"giudizio malformato: {e}") from e
    for c in claims:
        if c.label not in LABELS or c.kind not in KINDS:
            raise JudgmentError(f"etichetta o tipo sconosciuti: {c.label}, {c.kind}")
    if set(coverage) != set(expected_fact_ids):
        raise JudgmentError(f"copertura su {sorted(coverage)}, attesi {sorted(expected_fact_ids)}")
    if any(v not in VERDICTS for v in coverage.values()):
        raise JudgmentError("verdetto di copertura sconosciuto")
    return Judgment(claims=claims, coverage=coverage)
