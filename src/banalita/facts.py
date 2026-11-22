"""I fatti di riferimento sulla dimostrazione: che cosa una spiegazione dovrebbe trasmettere.

Ogni fatto ha la fonte, la pagina, la citazione letterale da cui viene e un livello minimo:
il livello più semplice al quale una spiegazione dovrebbe trasmetterlo (1 bambino, 2 liceo,
3 laureato in matematica, 4 teorico dei numeri). Il file si congela prima delle prove.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
GROUPS = ("statement", "architecture", "ingredients", "status", "limits")
SOURCES = ("F1", "F2", "F3a", "F3b")


class FactError(ValueError):
    """Un fatto non rispetta lo schema."""


@dataclass(frozen=True)
class Fact:
    id: str
    group: str
    text: str
    source: str
    page: int
    quote: str
    min_level: int


def _check(raw: dict) -> Fact:
    try:
        fact = Fact(id=str(raw["id"]), group=raw["group"], text=str(raw["text"]).strip(),
                    source=raw["source"], page=int(raw["page"]), quote=str(raw["quote"]).strip(),
                    min_level=int(raw["min_level"]))
    except (KeyError, TypeError, ValueError) as e:
        raise FactError(f"fatto malformato {raw!r}: {e}") from e
    if fact.group not in GROUPS:
        raise FactError(f"{fact.id}: gruppo sconosciuto {fact.group!r}")
    if fact.source not in SOURCES:
        raise FactError(f"{fact.id}: fonte sconosciuta {fact.source!r}")
    if not 1 <= fact.min_level <= 4:
        raise FactError(f"{fact.id}: livello minimo fuori da 1-4")
    if not fact.quote or not fact.text:
        raise FactError(f"{fact.id}: testo o citazione vuoti")
    return fact


def load_facts(path: Path | str = ROOT / "data" / "facts.yaml") -> list[Fact]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    facts = [_check(r) for r in data["facts"]]
    ids = [f.id for f in facts]
    if len(ids) != len(set(ids)):
        raise FactError("id ripetuti")
    return facts


def facts_for_level(facts: list[Fact], level: int) -> list[Fact]:
    return [f for f in facts if f.min_level <= level]
