"""Il campione di affermazioni che l'autore etichetta a mano (progetto, § 6).

Solo spiegazioni L1 e L2; le analogie dichiarate non si etichettano. Strati sulle etichette
del giudice (sostenuta, non sostenuta, contraddetta, analogia presa per fatto), in parti
uguali finché ce ne sono; l'estrazione usa il seme del protocollo. L'etichetta del giudice
resta nel campione per il confronto, ma non arriva mai nella pagina.
"""
from __future__ import annotations

import random

from banalita.requests import parse_custom_id

SEED = 20261122
STRATA = ("supported", "unsupported", "contradicted", "analogy_as_fact")


def sample_claims(judgments: dict, n: int = 60, seed: int = SEED) -> list[dict]:
    pool = {s: [] for s in STRATA}
    for jid in sorted(judgments):
        _, arm, level, sample = parse_custom_id(jid)
        if level not in (1, 2):
            continue
        for i, c in enumerate(judgments[jid].claims):
            if c.label in pool:
                pool[c.label].append({"ref": f"{jid}#{i}", "explanation_id": jid.replace("judge-", "explain-", 1),
                                      "level": level, "text": c.text, "judge_label": c.label})
    rng = random.Random(seed)
    for items in pool.values():
        rng.shuffle(items)
    chosen, k = [], 0
    while len(chosen) < n and any(pool.values()):
        stratum = STRATA[k % len(STRATA)]
        if pool[stratum]:
            chosen.append(pool[stratum].pop())
        k += 1
    rng.shuffle(chosen)
    # id opachi: nella pagina non deve trasparire da quale braccio viene un'affermazione
    for k, x in enumerate(chosen, 1):
        x["id"] = f"a{k:02d}"
    return chosen
