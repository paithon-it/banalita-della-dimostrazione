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
    assert LLM_ARGS["max_model_len"] <= 24576  # 32.768 non entrava: 1,32 GiB di cache contro 0,98
    assert LLM_ARGS["max_num_seqs"] <= 2


def test_context_leaves_room_for_prompt_and_full_output():
    """Il prompt di qwen_overview vale 11.798 token con il tokenizer di Qwen (misurato il
    22/11/2026, L4): deve restare spazio per MAX_TOKENS."""
    from gpu.qwen import LLM_ARGS, MAX_TOKENS
    assert LLM_ARGS["max_model_len"] - MAX_TOKENS >= 11798


def test_setup_installs_precompiled_kernels():
    """Senza CUDA toolkit FlashInfer non può compilare i kernel al primo avvio (22/11/2026)."""
    setup = (Path(__file__).parent.parent / "gpu" / "setup.sh").read_text()
    assert "vllm download-kernels" in setup
