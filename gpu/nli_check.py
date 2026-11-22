"""Il controllo meccanico delle affermazioni «contraddette» (progetto, § 6).

Per ogni affermazione che il giudice dice contraddetta da un passo delle fonti, un modello NLI
multilingue (mDeBERTa addestrato su XNLI) legge il passo come premessa e l'affermazione come
ipotesi, e dà le probabilità di implicazione, neutralità e contraddizione. È un compito
testuale, alla portata di un modello piccolo: dice se il passo citato contraddice davvero.

Uso: bash gpu/run.sh nli  (gira anche su CPU, più lento)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from banalita.phases import RESULTS, load_results

MODEL = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7"


def contradicted_pairs(results_dir: Path = RESULTS) -> list[tuple[str, str, str]]:
    """(id dell'affermazione, passo della fonte, affermazione) per le contraddette con citazione."""
    out = []
    for r in load_results(Path(results_dir) / "judgments.jsonl"):
        for i, c in enumerate((r.parsed or {}).get("claims", [])):
            if c.get("label") == "contradicted" and c.get("quote", "").strip():
                out.append((f"{r.custom_id}#{i}", c["quote"], c["text"]))
    return out


def main(results_dir: Path = RESULTS) -> Path:
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device).eval()
    labels = {i: l.lower() for i, l in model.config.id2label.items()}
    out = Path(results_dir) / "nli.jsonl"
    with out.open("w", encoding="utf-8") as f, torch.no_grad():
        for cid, premise, hypothesis in contradicted_pairs(results_dir):
            enc = tok(premise, hypothesis, truncation=True, max_length=512, return_tensors="pt").to(device)
            probs = torch.softmax(model(**enc).logits[0], dim=-1).tolist()
            f.write(json.dumps({"claim_id": cid, **{labels[i]: round(p, 4) for i, p in enumerate(probs)}}) + "\n")
    return out


if __name__ == "__main__":
    print(main())
    sys.exit(0)
