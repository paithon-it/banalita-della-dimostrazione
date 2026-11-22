"""Il modello aperto sulla L4: Qwen3.8-27B quantizzato a 4 bit, con vLLM.

Due compiti: spiegare la dimostrazione (braccio `qwen_overview`, lo stesso testo del braccio
`claude_overview`, otto volte per livello) e fare da secondo critico su tutte le spiegazioni e
sulla panoramica di F2. Il ragionamento del modello è acceso, come per Claude, e si toglie
dall'uscita. vLLM si importa solo dentro `main`, così il resto si prova senza GPU.

Uso, sulla macchina con la GPU: bash gpu/run.sh explain | bash gpu/run.sh critic
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from banalita.batch import Result
from banalita.phases import RESULTS, SOURCE_ARM, SOURCE_SAMPLES, _source_text, explanations, SAMPLES
from banalita.requests import LEVELS, PROMPTS, custom_id, overview_prompt_text, parse_custom_id

MODEL = "cyankiwi/Qwen3.8-27B-AWQ-INT4"
MAX_TOKENS = 12000
LLM_ARGS = dict(model=MODEL, max_model_len=24576, max_num_seqs=4, gpu_memory_utilization=0.92,
                enable_prefix_caching=True, enforce_eager=True, kv_cache_dtype="fp8")
# I valori consigliati per Qwen3 con il ragionamento acceso.
SAMPLING = dict(temperature=0.6, top_p=0.95, top_k=20, max_tokens=MAX_TOKENS)
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


def _generate(prompts: dict[str, tuple[str, str]]):
    from vllm import LLM, SamplingParams  # solo sulla macchina con la GPU
    llm = LLM(**LLM_ARGS)
    tok = llm.get_tokenizer()
    texts = [tok.apply_chat_template([{"role": "system", "content": sy}, {"role": "user", "content": us}],
                                     tokenize=False, add_generation_prompt=True, enable_thinking=True)
             for sy, us in prompts.values()]
    return zip(prompts, llm.generate(texts, SamplingParams(**SAMPLING)))


def main(kind: str, results_dir: Path = RESULTS) -> Path:
    prompts = explain_prompts() if kind == "explain" else critic_prompts(results_dir)
    out = Path(results_dir) / ("explanations_qwen.jsonl" if kind == "explain" else "critic_qwen.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as f:
        for cid, gen in _generate(prompts):
            o = gen.outputs[0]
            text = strip_thinking(o.text)
            status = "max_tokens" if o.finish_reason == "length" else "succeeded"
            parsed = parse_json(text) if kind == "critic" else None
            usage = {"input_tokens": len(gen.prompt_token_ids), "output_tokens": len(o.token_ids)}
            f.write(Result(cid, status, text, parsed, usage, o.finish_reason).to_json() + "\n")
    return out


if __name__ == "__main__":
    print(main(sys.argv[1]))
