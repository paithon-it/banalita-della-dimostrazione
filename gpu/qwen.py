"""Il modello aperto sulla L4: Qwen3.8-27B quantizzato a 4 bit, con vLLM.

Due compiti: spiegare la dimostrazione (braccio `qwen_overview`, lo stesso testo del braccio
`claude_overview`, otto volte per livello) e fare da secondo critico su tutte le spiegazioni e
sulla panoramica di F2. Il ragionamento del modello è acceso, come per Claude, e si toglie
dall'uscita. Ha un tetto, con il metodo del rapporto tecnico di Qwen3 (arXiv 2505.09388): al
tetto si inserisce la frase di chiusura, e il modello risponde con ciò che ha pensato fin lì.
vLLM si importa solo dove serve, così il resto si prova senza GPU.

Uso, sulla macchina con la GPU: bash gpu/run.sh explain | critic | salvage
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from banalita.batch import Result
from banalita.phases import (RESULTS, SAMPLES, SOURCE_ARM, SOURCE_SAMPLES, _source_text, explanations,
                              load_results)
from banalita.requests import LEVELS, PROMPTS, custom_id, overview_prompt_text, parse_custom_id

MODEL = "cyankiwi/Qwen3.8-27B-AWQ-INT4"
# Il tetto del ragionamento: nella prima corsa (12.000 token in tutto) 21 uscite su 32 non sono
# arrivate alla risposta, e il ragionamento più lungo fra le riuscite era di 9.937 token.
THINK_BUDGET = 10_000
ANSWER_TOKENS = 4_500  # la risposta dopo il ragionamento (L4: 1.500 parole, circa 2.600 token)
EARLY_STOP = ("\n\nConsidering the limited time by the user, I have to give the solution "
              "based on the thinking directly now.\n</think>.\n\n")
# Sulla L4 (22 GiB) i pesi ne occupano 18,2: niente codificatore di immagini (l'esperimento usa
# solo il testo), prefill a lotti piccoli, due sequenze alla volta. Il modello è ibrido (16
# strati di attenzione piena su 64), e la cache vale circa 41 KB per token: 1,32 GiB tengono
# una sequenza intera. Il prompt vale fino a 11.808 token.
LLM_ARGS = dict(model=MODEL, max_model_len=26624, max_num_seqs=2, max_num_batched_tokens=1024,
                gpu_memory_utilization=0.97, language_model_only=True,
                enable_prefix_caching=True, enforce_eager=True, kv_cache_dtype="fp8")
# I valori consigliati per Qwen3 con il ragionamento acceso.
SAMPLING = dict(temperature=0.6, top_p=0.95, top_k=20)
CRITIC_JSON = ('\n\nRispondi con un solo oggetto JSON, senza altro testo, nella forma '
               '{"alerts": [{"passage": "...", "problem": "..."}]}.')


def strip_thinking(text: str) -> str:
    if "</think>" in text:
        text = text.rsplit("</think>", 1)[1]
    return text.strip()


def parse_json(text: str) -> dict | None:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def explain_prompts() -> dict[str, tuple[str, str]]:
    return {custom_id("explain", "qwen_overview", level, s): overview_prompt_text(level)
            for level in LEVELS for s in range(SAMPLES)}


def critic_prompts(results_dir: Path = RESULTS) -> dict[str, tuple[str, str]]:
    from banalita.judge import blind
    system = (PROMPTS / "critic_system.it.md").read_text(encoding="utf-8").strip() + CRITIC_JSON
    out = {}
    for r in explanations(results_dir):
        _, arm, level, s = parse_custom_id(r.custom_id)
        out[custom_id("critic", arm, level, s)] = (system, f"TESTO DA ESAMINARE:\n<<<\n{blind(r.text)}\n>>>")
    for s in range(SOURCE_SAMPLES):
        out[custom_id("critic", SOURCE_ARM, 4, s)] = (system, f"TESTO DA ESAMINARE:\n<<<\n{_source_text()}\n>>>")
    return out


def close_thinking(thinking: str, finished: bool) -> str:
    """Il ragionamento chiuso, pronto per la risposta: il suo </think>, o la frase di Qwen al tetto."""
    return thinking + ("\n\n" if finished else EARLY_STOP)


def truncate_tokens(text: str, tok, n: int) -> str:
    ids = tok(text)["input_ids"]
    return text if len(ids) <= n else tok.decode(ids[:n])


def salvage_plan(runs: list[Result], tok, budget: int = THINK_BUDGET) -> dict[str, str]:
    """Che cosa fare di ogni uscita di una corsa senza tetto: «keep» se è riuscita ragionando entro
    il tetto (con il tetto sarebbe uscita uguale), «continue» se è tutta ragionamento (si tronca al
    tetto e si chiude: i primi `budget` token di un campione sono un campione dei primi `budget`),
    «redo» negli altri casi, dove il ragionamento oltre il tetto è andato perduto."""
    plan = {}
    for r in runs:
        out, n = r.usage["output_tokens"], len(tok(r.text)["input_ids"])
        if r.status == "succeeded":
            plan[r.custom_id] = "keep" if out - n <= budget else "redo"
        else:
            plan[r.custom_id] = "continue" if n >= 0.99 * out else "redo"
    return plan


def _llm():
    from vllm import LLM  # solo sulla macchina con la GPU
    return LLM(**LLM_ARGS)


def _chat(tok, system: str, user: str) -> str:
    return tok.apply_chat_template([{"role": "system", "content": system}, {"role": "user", "content": user}],
                                   tokenize=False, add_generation_prompt=True, enable_thinking=True)


def _records(llm, prompts: dict[str, tuple[str, str]], kind: str,
             thoughts: dict[str, str] | None = None):
    """Due tempi: il ragionamento fino a </think> o al tetto (o quello già scritto, troncato al
    tetto), poi la risposta."""
    from vllm import SamplingParams
    tok = llm.get_tokenizer()
    chats = {cid: _chat(tok, *p) for cid, p in prompts.items()}
    thoughts = thoughts or {}
    think = {cid: (truncate_tokens(t, tok, THINK_BUDGET), False) for cid, t in thoughts.items() if cid in chats}
    fresh = [cid for cid in chats if cid not in think]
    if fresh:
        first = SamplingParams(**SAMPLING, max_tokens=THINK_BUDGET, stop=["</think>"],
                               include_stop_str_in_output=True)
        for cid, gen in zip(fresh, llm.generate([chats[cid] for cid in fresh], first)):
            text = gen.outputs[0].text
            think[cid] = (text, text.rstrip().endswith("</think>"))
    order = list(chats)
    second = SamplingParams(**SAMPLING, max_tokens=ANSWER_TOKENS)
    answers = llm.generate([chats[cid] + close_thinking(*think[cid]) for cid in order], second)
    for cid, gen in zip(order, answers):
        o = gen.outputs[0]
        text = strip_thinking(o.text)
        status = "max_tokens" if o.finish_reason == "length" else "succeeded"
        parsed = parse_json(text) if kind == "critic" else None
        n_think = len(tok(think[cid][0])["input_ids"])
        usage = {"input_tokens": len(tok(chats[cid])["input_ids"]), "output_tokens": n_think + len(o.token_ids),
                 "thinking_tokens": n_think, "thinking_capped": int(not think[cid][1])}
        yield Result(cid, status, text, parsed, usage, o.finish_reason)


def main(kind: str, results_dir: Path = RESULTS) -> Path:
    prompts = explain_prompts() if kind == "explain" else critic_prompts(results_dir)
    out = Path(results_dir) / ("explanations_qwen.jsonl" if kind == "explain" else "critic_qwen.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    records = list(_records(_llm(), prompts, kind))
    with out.open("a", encoding="utf-8") as f:
        for r in records:
            f.write(r.to_json() + "\n")
    return out


def salvage(results_dir: Path = RESULTS) -> Path:
    """Porta la prima corsa delle spiegazioni (senza tetto, `explanations_qwen_run1.jsonl`) al
    metodo con il tetto, rifacendo solo quello che serve (`salvage_plan`)."""
    runs = load_results(Path(results_dir) / "explanations_qwen_run1.jsonl")
    llm = _llm()
    tok = llm.get_tokenizer()
    plan = salvage_plan(runs, tok)
    prompts = explain_prompts()
    todo = {r.custom_id: prompts[r.custom_id] for r in runs if plan[r.custom_id] != "keep"}
    thoughts = {r.custom_id: r.text for r in runs if plan[r.custom_id] == "continue"}
    records = list(_records(llm, todo, "explain", thoughts))
    out = Path(results_dir) / "explanations_qwen.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for r in runs:
            if plan[r.custom_id] == "keep":
                n = len(tok(r.text)["input_ids"])
                usage = {**r.usage, "thinking_tokens": r.usage["output_tokens"] - n, "thinking_capped": 0}
                f.write(Result(r.custom_id, r.status, r.text, r.parsed, usage, r.stop_reason).to_json() + "\n")
        for r in records:
            f.write(r.to_json() + "\n")
    return out


if __name__ == "__main__":
    print(salvage() if sys.argv[1] == "salvage" else main(sys.argv[1]))
