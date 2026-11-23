import os
import subprocess
from pathlib import Path

import pytest

from banalita.sources import ROOT, load_sources

GPU = ROOT / "gpu"
needs_sources = pytest.mark.skipif(
    not all(s.local.exists() for s in load_sources().values()), reason="fonti non scaricate")


def _bash(script: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", "-c", script], capture_output=True, text=True, env={**os.environ, **env})


def test_clean_refuses_other_paths(tmp_path):
    for bad in (tmp_path / "x" / "rnd", tmp_path / "rnd", tmp_path / "rnd" / "goldenet"):
        bad.mkdir(parents=True)
        r = _bash(f"bash {GPU / 'clean.sh'}", {"RND": str(bad)})
        assert r.returncode != 0 and bad.exists(), bad
    good = tmp_path / "rnd" / "banalita"
    (good / "hf").mkdir(parents=True)
    r = _bash(f"bash {GPU / 'clean.sh'}", {"RND": str(good)})
    assert r.returncode == 0 and not good.exists()
    assert (tmp_path / "rnd" / "goldenet").exists()  # il lavoro degli altri resta


def test_env_keeps_caches_inside_rnd(tmp_path):
    rnd = tmp_path / "rnd" / "banalita"
    r = _bash(f". {GPU / 'env.sh'} && env", {"RND": str(rnd)})
    env = dict(l.split("=", 1) for l in r.stdout.splitlines() if "=" in l)
    for var in ("HF_HOME", "XDG_CACHE_HOME", "TRITON_CACHE_DIR", "VLLM_CACHE_ROOT", "TMPDIR", "PIP_CACHE_DIR"):
        assert env[var].startswith(str(rnd)), var
    assert env["VLLM_NO_USAGE_STATS"] == "1"


def test_run_refuses_busy_gpu(tmp_path):
    fake = tmp_path / "bin"
    fake.mkdir()
    (fake / "nvidia-smi").write_text("#!/bin/sh\necho 123771\n")
    (fake / "nvidia-smi").chmod(0o755)
    r = _bash(f"bash {GPU / 'run.sh'} explain", {"PATH": f"{fake}:{os.environ['PATH']}",
                                                   "RND": str(tmp_path / "rnd" / "banalita")})
    assert r.returncode == 3
    assert "occupata" in r.stdout + r.stderr


def test_strip_thinking_and_parse_json():
    from gpu.qwen import parse_json, strip_thinking
    assert strip_thinking("<think>ragiono a lungo</think>\n\nEcco il testo.") == "Ecco il testo."
    assert strip_thinking("Solo testo.") == "Solo testo."
    assert parse_json('```json\n{"alerts": []}\n```') == {"alerts": []}
    assert parse_json("nessun json qui") is None


@needs_sources
def test_qwen_prompt_matches_claude_overview_prompt():
    from banalita.requests import overview_prompt_text
    from gpu.qwen import explain_prompts
    prompts = explain_prompts()
    assert len(prompts) == 32
    cid, (system, user) = next(iter(prompts.items()))
    assert cid == "explain-qwen_overview-L1-s00"
    assert (system, user) == overview_prompt_text(1)


def test_nli_pairs_only_contradicted_with_quote(tmp_path):
    from banalita.batch import Result
    from gpu.nli_check import contradicted_pairs
    d = tmp_path / "results"
    d.mkdir()
    parsed = {"claims": [
        {"text": "a", "label": "contradicted", "quote": "passo", "kind": "proof"},
        {"text": "b", "label": "contradicted", "quote": "", "kind": "proof"},
        {"text": "c", "label": "supported", "quote": "q", "kind": "proof"}], "coverage": []}
    (d / "judgments.jsonl").write_text(Result("judge-claude_full-L1-s00", "succeeded", "{}", parsed, {}, "end_turn").to_json() + "\n")
    assert contradicted_pairs(d) == [("judge-claude_full-L1-s00#0", "passo", "a")]


def test_vllm_loads_text_only_and_fits_the_l4():
    """22/11/2026: con il codificatore di immagini la passata di prova di vLLM andava in OOM
    sulla L4 (pesi 19,07 GiB su 22). L'esperimento usa solo il testo."""
    from gpu.qwen import LLM_ARGS
    assert LLM_ARGS["language_model_only"] is True
    assert LLM_ARGS["max_num_batched_tokens"] <= 1024
    assert LLM_ARGS["max_model_len"] <= 26624  # 32.768 non entrava: 1,32 GiB di cache contro 0,98
    assert LLM_ARGS["max_num_seqs"] <= 2


def test_context_fits_prompt_thinking_and_answer():
    """Il prompt di qwen_overview vale fino a 11.808 token con il tokenizer di Qwen (misurato
    il 22/11/2026): dopo ci stanno il ragionamento al tetto, la frase di chiusura e la risposta."""
    from gpu.qwen import ANSWER_TOKENS, LLM_ARGS, THINK_BUDGET
    assert LLM_ARGS["max_model_len"] >= 11808 + THINK_BUDGET + 64 + ANSWER_TOKENS


def test_budget_keeps_every_successful_first_run_answer():
    """Nella prima corsa il ragionamento più lungo fra le risposte riuscite è di 9.937 token
    (L3-s04): con un tetto più alto quelle risposte sarebbero uscite identiche."""
    from gpu.qwen import THINK_BUDGET
    assert THINK_BUDGET >= 9937


class WordTok:
    """Tokenizzatore finto: un token per parola."""

    def __call__(self, text):
        return {"input_ids": text.split()}

    def decode(self, ids):
        return " ".join(ids)


def test_close_thinking_unfinished_gets_qwen_stop_instruction():
    """La frase del rapporto tecnico di Qwen3 (arXiv 2505.09388), punto dopo </think> compreso."""
    from gpu.qwen import EARLY_STOP, close_thinking
    assert EARLY_STOP == ("\n\nConsidering the limited time by the user, I have to give the solution "
                          "based on the thinking directly now.\n</think>.\n\n")
    assert close_thinking("penso ancora", finished=False) == "penso ancora" + EARLY_STOP


def test_close_thinking_finished_keeps_its_own_tag():
    from gpu.qwen import close_thinking
    assert close_thinking("penso</think>", finished=True) == "penso</think>\n\n"


def test_truncate_tokens_keeps_the_first_n():
    from gpu.qwen import truncate_tokens
    assert truncate_tokens("a b c d", WordTok(), 2) == "a b"
    assert truncate_tokens("a b", WordTok(), 5) == "a b"


def test_salvage_plan_sorts_the_first_run():
    """Le riuscite entro il tetto restano; il solo ragionamento si chiude e si completa; il resto
    (ragionamento oltre il tetto ma perduto, o risposta tagliata) si rifà da capo."""
    from banalita.batch import Result
    from gpu.qwen import salvage_plan
    runs = [
        Result("keep", "succeeded", "r r", None, {"input_tokens": 9, "output_tokens": 6}, "stop"),
        Result("long", "succeeded", "r", None, {"input_tokens": 9, "output_tokens": 8}, "stop"),
        Result("think", "max_tokens", " ".join(["t"] * 10), None,
               {"input_tokens": 9, "output_tokens": 10}, "length"),
        Result("cut", "max_tokens", "r r", None, {"input_tokens": 9, "output_tokens": 10}, "length"),
    ]
    assert salvage_plan(runs, WordTok(), budget=5) == {
        "keep": "keep", "long": "redo", "think": "continue", "cut": "redo"}


def test_setup_installs_precompiled_kernels():
    """Senza CUDA toolkit FlashInfer non può compilare i kernel al primo avvio (22/11/2026)."""
    setup = (Path(__file__).parent.parent / "gpu" / "setup.sh").read_text()
    assert "vllm download-kernels" in setup
