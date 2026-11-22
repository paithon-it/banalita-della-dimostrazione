"""Quanto il giudice concorda con l'autore sulle affermazioni etichettate a mano.

Le etichette del giudice si portano su quelle della pagina: supported → sostenuta,
unsupported → non_sostenuta, contradicted e analogy_as_fact → contraddetta («errore»).
"""
from __future__ import annotations

from banalita.metrics import cohen_kappa

TO_HUMAN = {"supported": "sostenuta", "unsupported": "non_sostenuta",
            "contradicted": "contraddetta", "analogy_as_fact": "contraddetta"}
CLASSES = {"errore": "contraddetta", "sostenuta": "sostenuta", "non_sostenuta": "non_sostenuta"}


def human_vs_judge(human: dict[str, str], sample: list[dict]) -> dict:
    pairs = [(TO_HUMAN[x["judge_label"]], human[x["id"]]) for x in sample if x["id"] in human]
    out = {"n": len(pairs)}
    for name, cls in CLASSES.items():
        tp = sum(j == cls and h == cls for j, h in pairs)
        pred = sum(j == cls for j, _ in pairs)
        true = sum(h == cls for _, h in pairs)
        out[name] = {"precisione": tp / pred if pred else float("nan"),
                     "richiamo": tp / true if true else float("nan")}
    if pairs:
        out["kappa"] = cohen_kappa([j for j, _ in pairs], [h for _, h in pairs])
    return out
