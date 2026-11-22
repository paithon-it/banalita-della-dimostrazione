# Ambiente comune sulla macchina con la GPU: ogni cache e ogni file temporaneo stanno dentro
# $RND (di default ~/rnd/banalita), così cancellare quella cartella toglie ogni traccia delle
# prove. Le altre cartelle di ~/rnd non si toccano.
RND="${RND:-$HOME/rnd/banalita}"
export RND \
  PIP_CACHE_DIR="$RND/pip" XDG_CACHE_HOME="$RND/cache" XDG_CONFIG_HOME="$RND/config" XDG_DATA_HOME="$RND/share" \
  HF_HOME="$RND/hf" TORCH_HOME="$RND/torch" TRITON_CACHE_DIR="$RND/triton" CUDA_CACHE_PATH="$RND/nv" \
  VLLM_CACHE_ROOT="$RND/vllm" VLLM_CONFIG_ROOT="$RND/vllm-config" VLLM_NO_USAGE_STATS=1 DO_NOT_TRACK=1 \
  VLLM_USE_FLASHINFER_SAMPLER=0 TMPDIR="$RND/tmp" PYTHONDONTWRITEBYTECODE=1 PIP_DISABLE_PIP_VERSION_CHECK=1
mkdir -p "$TMPDIR" "$PIP_CACHE_DIR" "$XDG_CACHE_HOME"
