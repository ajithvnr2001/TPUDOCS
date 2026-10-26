#!/usr/bin/env bash
# Deploy LLM serving using native vLLM-TorchTPU on Cloud TPU VM
set -euo pipefail

MODEL_ID="${1:-meta-llama/Llama-3.2-1B-Instruct}"
TP_SIZE="${2:-1}"
MAX_MODEL_LEN="${3:-4096}"
PORT="${4:-8000}"

ENV_DIR="${HOME}/.venv-vllm-tpu"
CACHE_DIR="${HOME}/.tpu_cache"

mkdir -p "${CACHE_DIR}/tier3" "${CACHE_DIR}/vllm"

export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="${CACHE_DIR}/tier3"
export VLLM_CACHE_ROOT="${CACHE_DIR}/vllm"
export HF_HUB_ENABLE_HF_TRANSFER=1

echo ">>> Setting up Python 3.12 environment at ${ENV_DIR}..."
python3.12 -m venv "${ENV_DIR}"
# shellcheck disable=SC1091
source "${ENV_DIR}/bin/activate"

echo ">>> Installing vLLM-TorchTPU..."
pip install --upgrade pip
pip install --extra-index-url https://download.pytorch.org/whl/cpu vllm-torchtpu

echo ">>> Checking Hugging Face login (required for gated models)..."
if ! hf auth whoami > /dev/null 2>&1; then
  echo ">>> Logging into Hugging Face CLI..."
  hf auth login
fi

echo ">>> Starting vLLM-TorchTPU server on port ${PORT}..."
echo ">>> Model: ${MODEL_ID}, Tensor Parallel: ${TP_SIZE}, Max Seq Len: ${MAX_MODEL_LEN}"
vllm serve "${MODEL_ID}" \
  --tensor-parallel-size "${TP_SIZE}" \
  --max-model-len "${MAX_MODEL_LEN}" \
  --port "${PORT}"
