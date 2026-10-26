#!/usr/bin/env bash
# Setup native PyTorch environment with TorchTPU on Cloud TPU VM
set -euo pipefail

ENV_DIR="${HOME}/.venv-tpu"

echo ">>> Initializing Python 3.12 virtual environment at ${ENV_DIR}..."
python3.12 -m venv "${ENV_DIR}"
# shellcheck disable=SC1091
source "${ENV_DIR}/bin/activate"

echo ">>> Upgrading pip and installing TorchTPU..."
pip install --upgrade pip
pip install torch_tpu==0.2.0 --extra-index-url https://download.pytorch.org/whl/cpu

echo ">>> Running hardware smoke test..."
python -c 'import torch; import torch_tpu; x = torch.ones((4, 4), device="tpu"); print("TPU Matrix Multiplication Result:\n", (x @ x).cpu()); print("Hardware smoke test passed!")'
