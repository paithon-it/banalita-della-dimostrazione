"""La caccia all'errore (progetto, § 6, M4).

Il critico legge il testo da solo, senza fonti, e segnala i passi che non reggono. Poi un
verificatore, con le fonti in cache come il giudice, mette ogni segnalazione in una di tre
caselle: introdotta dal testo, già presente nella fonte, falso allarme.
"""
from __future__ import annotations

from banalita.judge import OPUS, SOURCE_IDS, _f3_text, blind
from banalita.requests import CACHE, MAX_TOKENS, PROMPTS, _pdf_b64
from banalita.sources import load_sources

CATEGORIES = ("introduced", "in_source", "false_alarm")

CRITIC_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["alerts"],
    "properties": {"alerts": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["passage", "problem"],
        "properties": {"passage": {"type": "string"}, "problem": {"type": "string"}}}}},
}

VERIFY_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["verdicts"],
    "properties": {"verdicts": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["index", "category", "reason", "source", "page"],
        "properties": {
            "index": {"type": "integer"},
            "category": {"type": "string", "enum": list(CATEGORIES)},
            "reason": {"type": "string"},
            "source": {"type": "string", "enum": list(SOURCE_IDS)},
            "page": {"type": "integer"},
        }}}},
}


def _system(name: str) -> list[dict]:
    return [{"type": "text", "text": (PROMPTS / name).read_text(encoding="utf-8").strip()}]


def critic_request(target_id: str, text: str, model: str = OPUS, blinded: bool = True) -> dict:
    """`blinded=False` per la fonte stessa (la panoramica di F2), che non va ripulita."""
    return {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": CRITIC_SCHEMA}},
        "system": _system("critic_system.it.md"),
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": f"TESTO DA ESAMINARE:\n<<<\n{blind(text) if blinded else text}\n>>>"}]}],
    }


def verify_request(target_id: str, text: str, alerts: list[dict], model: str = OPUS, blinded: bool = True) -> dict:
    src = load_sources()
    listing = "\n".join(f"[{i}] PASSAGGIO: {a['passage']}\n    PROBLEMA SEGNALATO: {a['problem']}"
                        for i, a in enumerate(alerts))
    task = f"TESTO ESAMINATO:\n<<<\n{blind(text) if blinded else text}\n>>>\n\nSEGNALAZIONI DEL CRITICO:\n{listing}"
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
        "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": VERIFY_SCHEMA}},
        "system": _system("verify_system.it.md"),
        "messages": [{"role": "user", "content": content}],
    }
