---
name: infer-03-vllm-torchtpu-installation
description: "vLLM-TorchTPU installation \u2014 Install the PyTorch-native vLLM TPU plugin; distinct from the vllm-tpu JAX backend."
source_url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/"
category: "inference_deployment_links"
---

# Agent Skill: vLLM-TorchTPU installation

- **Official Source**: [https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/)
- **Category**: `inference_deployment_links`
- **Resource ID**: `infer_03_vllm_torchtpu_installation`
- **When to Activate**: Install the PyTorch-native vLLM TPU plugin; distinct from the vllm-tpu JAX backend.

## Document Sections

- **Installation**
  - **Interactive Installation Generator**
- **Install vllm-torchtpu from PyPI (https://pypi.org/project/vllm-torchtpu/):**
  - **Prerequisites**
  - **Package Architecture (`vllm-torchtpu` vs. `vllm-torchtpu-core`)**
  - **Option 1: Install from PyPI ([`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/))**
    - **Using `uv` (Recommended)**
- **Route torch and torchvision to the PyTorch CPU index**
    - **Using `pip`**
  - **Option 2: Install from `vllm-torchtpu` Repository (`--group vllm`)**
    - **Using `uv` (Recommended)**
- **1. Install uv (if not already installed)**
- **2. Clone vllm-torchtpu and sync the environment (including the vllm group)**
- **3. Activate the virtual environment**
    - **Using `pip`**
  - **Option 3: Install `vllm` and `vllm-torchtpu-core` Separately (Cross-Repo Development)**
    - **Using `uv` (Recommended)**
- **1. Clone and install vLLM in editable mode (with common dependencies)**
- **2. Clone and install vllm-torchtpu-core only (without --group vllm)**
    - **Using `pip`**
- **1. Clone and install vLLM in editable mode (with common dependencies)**
- **2. Clone and install vllm-torchtpu-core only (without --group vllm)**
  - **Optional Dependency Groups & Extras**
  - **Verify Installation**

## Key CLI Commands & Invocations

```bash
uv venv --python 3.12 ~/uv_venv
export UV_TORCH_BACKEND=cpu
uv pip install vllm-torchtpu
python3.12 -m venv ~/pip_venv --symlinks
pip install --upgrade pip
pip install \
vllm-torchtpu
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/vllm-project/vllm-torchtpu.git
uv venv --python 3.12 --seed
python3.12 -m venv .venv
git clone --depth 1 --branch v0.31.0 https://github.com/vllm-project/vllm.git ~/vllm
git clone https://github.com/vllm-project/vllm-torchtpu.git ~/vllm-torchtpu && cd ~/vllm-torchtpu
uv pip install -e .
python -c "from vllm.platforms import current_platform; print(current_platform.device_name)"
```

## Key Environment Variables

- `UV_TORCH_BACKEND`
- `VLLM_TARGET_DEVICE`

## Complete Technical Reference

# Installation
`vllm-torchtpu` is a platform plugin for [vLLM](https://docs.vllm.ai/) that enables PyTorch-native LLM and multimodal serving on Google Cloud TPUs via `torch_tpu` and custom JAX/Pallas kernels.
* * *
## Interactive Installation Generator
Choose your preferred installation method below:
1. Installation Method
PyPI Wheel (Recommended) Editable Source Install Docker Container
2. Container Type
Release Image (:latest) Nightly Image (:nightly)
Install the pre-built [`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/) package and its dependencies from PyPI into a Python 3.12 virtual environment.

```
# Install vllm-torchtpu from PyPI (https://pypi.org/project/vllm-torchtpu/):
uv venv --python 3.12 ~/uv_venv
source ~/uv_venv/bin/activate
export UV_TORCH_BACKEND=cpu
uv pip install vllm-torchtpu
```

* * *
## Prerequisites
  * **Python 3.12** (`>=3.12,<3.13`). Pre-built `tpu-sync-torch` and `torch_tpu` wheels target CPython 3.12.
  * We recommend using `uv` for installing dependencies as it is significantly faster than standard `pip`.


* * *
## Package Architecture (`vllm-torchtpu` vs. `vllm-torchtpu-core`)
  * **`pip install vllm-torchtpu`**(Combined PyPI package): Installs`site-packages/vllm/` (provides `import vllm` and the `vllm` CLI, built with `VLLM_TARGET_DEVICE="empty"`), and automatically pulls `vllm-torchtpu-core` as a dependency.
  * **`pip install vllm-torchtpu-core`**(OOT Plugin package built from this repo): Installs`site-packages/vllm_torchtpu/` (`import vllm_torchtpu`), which is automatically discovered and loaded by `vllm` via the `vllm.platform_plugins` entry point—you still run `vllm serve` or `import vllm` in user code. `vllm` is **not** a core dependency of `vllm-torchtpu-core`; for source installs, `--group vllm` builds `vllm` from source.

```
+----------------------------------------------------------------------------+
|  PyPI Package: vllm-torchtpu  (Combined Wrapper Wheel)                     |
|  * Installs: `site-packages/vllm/`  -->  `import vllm` / `vllm serve`      |
|  * Upstream vLLM built with VLLM_TARGET_DEVICE="empty"                     |
|  * Discovers OOT plugin via `vllm.platform_plugins` entry point            |
|                                                                            |
|  +----------------------------------------------------------------------+  |
|  |  PyPI Package: vllm-torchtpu-core  (OOT Plugin Wheel — This Repo)    |  |
|  |  * Installs: `site-packages/vllm_torchtpu/`  (auto-loaded by vLLM)   |  |
|  |  * Entry point: `torchtpu = "vllm_torchtpu.platforms:..."`           |  |
|  |  * Requires TPU runtime dependencies:                                |  |
|  |    torch (CPU), torchvision (CPU), torch-tpu, libtpu,                |  |
|  |    tpu-sync-torch                                                    |  |
|  +----------------------------------------------------------------------+  |
+----------------------------------------------------------------------------+
  ^
  +-- Repo source install (`-e . --group vllm`):
      Installs `vllm-torchtpu-core` from source + builds pinned upstream
      `vllm` from Git via PEP 735 `[dependency-groups]`.

```

Why the PyTorch CPU index (`https://download.pytorch.org/whl/cpu`) is required
On Linux `x86_64`, default PyPI (`pypi.org`) serves `torch` and `torchvision` wheels compiled with CUDA, which pulls gigabytes of unnecessary `nvidia-*` runtime dependencies onto TPU hosts. Setting `UV_TORCH_BACKEND=cpu` (or `pyproject.toml`'s `[tool.uv.sources]` for `uv`) or passing `--extra-index-url https://download.pytorch.org/whl/cpu` (for `pip`) routes `torch` and `torchvision` to the official PyTorch CPU wheel index while resolving all other dependencies (including `torch-tpu`, `libtpu`, and `tpu-sync-torch`) from public PyPI.
* * *
## Option 1: Install from PyPI ([`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/))
For standard usage without modifying source code, install the pre-built [`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/) package directly from PyPI (this automatically installs both `vllm` and [`vllm-torchtpu-core`](https://pypi.org/project/vllm-torchtpu-core/)):
### Using `uv` (Recommended)

```
uv venv --python 3.12 ~/uv_venv
source ~/uv_venv/bin/activate

# Route torch and torchvision to the PyTorch CPU index
export UV_TORCH_BACKEND=cpu

uv pip install vllm-torchtpu

```

### Using `pip`

```
python3.12 -m venv ~/pip_venv --symlinks
source ~/pip_venv/bin/activate
pip install --upgrade pip

pip install \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  vllm-torchtpu

```

* * *
## Option 2: Install from `vllm-torchtpu` Repository (`--group vllm`)
To install `vllm-torchtpu-core` from a local clone of this repository and automatically build the pinned `vllm` commit from source via `--group vllm`:
### Using `uv` (Recommended)
`pyproject.toml` configures the `pytorch-cpu` index (`https://download.pytorch.org/whl/cpu`) for `torch` and `torchvision`, and pins compatible `torch-tpu`, `jax`, `libtpu`, and `vllm` versions automatically.

```
# 1. Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# 2. Clone vllm-torchtpu and sync the environment (including the vllm group)
git clone https://github.com/vllm-project/vllm-torchtpu.git
cd vllm-torchtpu
VLLM_TARGET_DEVICE=empty uv sync --group vllm

# 3. Activate the virtual environment
source .venv/bin/activate

```

To install in editable mode with test and development dependencies:

```
uv venv --python 3.12 --seed
source .venv/bin/activate
export UV_TORCH_BACKEND=cpu
VLLM_TARGET_DEVICE=empty uv pip install -e . --group vllm --group test

```

### Using `pip`
If using standard `pip` (`pip >= 25.1` for `--group` support), pass `--extra-index-url https://download.pytorch.org/whl/cpu` so `torch` and `torchvision` resolve to CPU wheels rather than default PyPI's CUDA wheels:

```
python3.12 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip

git clone https://github.com/vllm-project/vllm-torchtpu.git
cd vllm-torchtpu

VLLM_TARGET_DEVICE=empty pip install -e . --group vllm \
  --extra-index-url https://download.pytorch.org/whl/cpu

```

* * *
## Option 3: Install `vllm` and `vllm-torchtpu-core` Separately (Cross-Repo Development)
Follow these steps when developing or debugging both `vllm` and `vllm-torchtpu-core` in separate local checkouts (or installing `vllm-torchtpu-core` without `--group vllm`). Currently, `vllm==0.31.0` is supported.
### Using `uv` (Recommended)

```
uv venv --python 3.12 ~/uv_venv
source ~/uv_venv/bin/activate
export UV_TORCH_BACKEND=cpu

# 1. Clone and install vLLM in editable mode (with common dependencies)
git clone --depth 1 --branch v0.31.0 https://github.com/vllm-project/vllm.git ~/vllm
VLLM_TARGET_DEVICE="empty" uv pip install -e ~/vllm

# 2. Clone and install vllm-torchtpu-core only (without --group vllm)
git clone https://github.com/vllm-project/vllm-torchtpu.git ~/vllm-torchtpu && cd ~/vllm-torchtpu
uv pip install -e .

```

_(Or install`vllm-torchtpu-core` from PyPI instead of step 2: `uv pip install vllm-torchtpu-core`)_
### Using `pip`

```
python3.12 -m venv ~/pip_venv --symlinks
source ~/pip_venv/bin/activate
pip install --upgrade pip

# 1. Clone and install vLLM in editable mode (with common dependencies)
git clone --depth 1 --branch v0.31.0 https://github.com/vllm-project/vllm.git ~/vllm
VLLM_TARGET_DEVICE="empty" pip install \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  -e ~/vllm

# 2. Clone and install vllm-torchtpu-core only (without --group vllm)
git clone https://github.com/vllm-project/vllm-torchtpu.git ~/vllm-torchtpu && cd ~/vllm-torchtpu
pip install \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  -e .

```

_(Or install`vllm-torchtpu-core` from PyPI instead of step 2: `pip install --extra-index-url https://download.pytorch.org/whl/cpu vllm-torchtpu-core`)_
Why `VLLM_TARGET_DEVICE=empty`?
`vllm-torchtpu-core` registers itself through vLLM's out-of-tree platform plugin entry points (`vllm.platform_plugins` and `vllm.general_plugins`). Installing `vllm` with `VLLM_TARGET_DEVICE=empty` skips CUDA C++ extension compilation while keeping all Python server and engine entrypoints editable.
* * *
## Optional Dependency Groups & Extras
| Flag  | Purpose  |  
| --- | --- |  
| `--group vllm`  | Installs pinned upstream `vllm` (`v0.31.0`) from source.  |  
| `--group test`  | Installs `pytest`, `pytest-mock`, `pytest-cov`, `parameterized`, and `vllm_test_utils`.  |  
| `--extra benchmarking`  | Installs `lm-eval`, `evalscope`, `datasets`, and `runai-model-streamer[gcs]`.  |  
| `--extra omni`  | Installs `vllm-omni` for multimodal diffusion models (e.g., FLUX, Wan2.2).  |  
* * *
## Verify Installation
Verify that vLLM detects the `vllm-torchtpu` platform plugin:

```
python -c "from vllm.platforms import current_platform; print(current_platform.device_name)"

```
