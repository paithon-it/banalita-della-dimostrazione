#!/usr/bin/env bash
# Lancia una fase sulla L4: explain (32 spiegazioni di Qwen), critic (il critico Qwen), nli.
# Uso, sulla macchina con la GPU, dalla copia del repository in $RND/repo:
#   bash gpu/run.sh explain|critic|salvage|nli
# Si rifiuta di partire se la GPU ha già processi al lavoro: la macchina è dell'autore, e un
# altro lavoro in corso ha la precedenza.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
. "$here/env.sh"
busy="$(nvidia-smi --query-compute-apps=pid --format=csv,noheader 2>/dev/null | tr -d ' ' || true)"
if [ -n "$busy" ]; then
  echo "GPU occupata da altri processi ($busy): non parto." >&2
  exit 3
fi
. "$RND/venv/bin/activate"
export HF_HUB_OFFLINE="${HF_HUB_OFFLINE:-1}"
cd "$here/.."
case "${1:-}" in
  explain) python3 -m gpu.qwen explain ;;
  critic)  python3 -m gpu.qwen critic ;;
  salvage) python3 -m gpu.qwen salvage ;;
  nli)     python3 -m gpu.nli_check ;;
  *) echo "uso: bash gpu/run.sh explain|critic|salvage|nli" >&2; exit 1 ;;
esac
