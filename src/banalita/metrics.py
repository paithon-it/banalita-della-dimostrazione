"""Le misure e i verdetti sulle previsioni (progetto, § 7; soglie fissate nel protocollo).

Regole dei verdetti, calcolate sulle celle braccio × livello:
- P1: la leggibilità media (Gulpease, media dei bracci) scende strettamente da L1 a L4.
- P2: la copertura media è più bassa a L1 che a L4.
- P3: la quota di errori, sommata sui bracci, è più alta a L1 che a L4.
- P4: in almeno un braccio, a L1 o a L2: copertura almeno 0,6, errori al più il 5% delle
  affermazioni e limite superiore di Wilson al 95% non oltre il 10%.
- P5: delle segnalazioni del critico verificate sulle spiegazioni L1 e L2, almeno l'80% è
  «introdotta» dalla semplificazione.
- P6: sommando i livelli, errori di claude_overview < qwen_overview e claude_full < claude_overview.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import sqrt

from banalita.judge import ERROR_LABELS, Judgment

ARMS = ("claude_full", "claude_overview", "qwen_overview")
LEVELS = (1, 2, 3, 4)
P4_COVERAGE, P4_ERRORS, P4_UPPER = 0.6, 0.05, 0.10
P5_SHARE = 0.8
VERDICT_SCORE = {"yes": 1.0, "partial": 0.5, "no": 0.0}


@dataclass(frozen=True)
class Cell:
    gulpease: float
    coverage: float
    errors: int
    claims: int
    alerts_introduced: int
    alerts_verified: int


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def cohen_kappa(a: list[str], b: list[str]) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("liste di lunghezza diversa o vuote")
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def coverage(judgment: Judgment) -> float:
    if not judgment.coverage:
        return 0.0
    return sum(VERDICT_SCORE[v] for v in judgment.coverage.values()) / len(judgment.coverage)


def error_rate(judgment: Judgment) -> tuple[int, int]:
    """(errori, base): errori sulla dimostrazione e di contesto; base = affermazioni sulla
    dimostrazione che non sono analogie dichiarate, più gli errori di contesto."""
    proof = [c for c in judgment.claims if c.kind == "proof" and c.label != "declared_analogy"]
    ctx_err = [c for c in judgment.claims if c.kind == "context" and c.label in ERROR_LABELS]
    errors = sum(c.label in ERROR_LABELS for c in proof) + len(ctx_err)
    return errors, len(proof) + len(ctx_err)


def p4_cell(coverage: float, errors: int, claims: int) -> bool:
    if claims == 0:
        return False
    return (coverage >= P4_COVERAGE and errors / claims <= P4_ERRORS
            and wilson(errors, claims)[1] <= P4_UPPER)


def _pooled(table: dict, level: int, attr: str) -> float:
    cells = [table[(a, level)] for a in ARMS if (a, level) in table]
    return sum(getattr(c, attr) for c in cells) / len(cells)


def _err(table: dict, keys) -> float:
    e = sum(table[k].errors for k in keys if k in table)
    n = sum(table[k].claims for k in keys if k in table)
    return e / n if n else float("nan")


def verdicts(table: dict) -> dict[str, dict]:
    g = [_pooled(table, l, "gulpease") for l in LEVELS]
    cov = [_pooled(table, l, "coverage") for l in LEVELS]
    err = [_err(table, [(a, l) for a in ARMS]) for l in LEVELS]
    p4_hits = [(a, l) for a in ARMS for l in (1, 2) if (a, l) in table
               and p4_cell(table[(a, l)].coverage, table[(a, l)].errors, table[(a, l)].claims)]
    intro = sum(table[(a, l)].alerts_introduced for a in ARMS for l in (1, 2) if (a, l) in table)
    verified = sum(table[(a, l)].alerts_verified for a in ARMS for l in (1, 2) if (a, l) in table)
    by_arm = {a: _err(table, [(a, l) for l in LEVELS]) for a in ARMS}
    return {
        "P1": {"passa": all(g[i] > g[i + 1] for i in range(3)), "dettaglio": g},
        "P2": {"passa": cov[0] < cov[3], "dettaglio": cov},
        "P3": {"passa": err[0] > err[3], "dettaglio": err},
        "P4": {"passa": bool(p4_hits), "dettaglio": p4_hits},
        "P5": {"passa": verified > 0 and intro / verified >= P5_SHARE,
               "dettaglio": (intro, verified)},
        "P6": {"passa": by_arm["claude_overview"] < by_arm["qwen_overview"]
                        and by_arm["claude_full"] < by_arm["claude_overview"], "dettaglio": by_arm},
    }
