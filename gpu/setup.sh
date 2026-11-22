#!/usr/bin/env bash
# Prepara la macchina con la GPU: un ambiente virtuale con vLLM e transformers dentro $RND, e i
# due modelli (Qwen3.8-27B quantizzato a 4 bit, il modello NLI multilingue).
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
. "$here/env.sh"
python3 -m venv "$RND/venv"
. "$RND/venv/bin/activate"
pip install -q --no-cache-dir --upgrade pip
pip install -q --no-cache-dir vllm "transformers>=4.45" sentencepiece pyyaml numpy
pip install -q --no-cache-dir -e "$here/.." --no-deps
python -c "import vllm, torch; print('vllm', vllm.__version__, 'torch', torch.__version__, 'cuda', torch.cuda.is_available())"
hf download "${QWEN:-cyankiwi/Qwen3.8-27B-AWQ-INT4}" > /dev/null
hf download "${NLI:-MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7}" > /dev/null
du -sh "$RND/hf"
