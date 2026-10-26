---
id: "infer_03_vllm_torchtpu_installation"
title: "vLLM-TorchTPU installation"
url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/"
category: "Inference deployment links"
description: "Install the PyTorch-native vLLM TPU plugin; distinct from the vllm-tpu JAX backend."
crawled_at: "2026-10-26T12:47:29.086272+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#installation)
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU")
vLLM TorchTPU 
Installation 
[ ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/?q= "Share")
Type to start searching
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU") vLLM TorchTPU 
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
  * [ Home  ](https://vllm-torchtpu.readthedocs.io/en/latest/)
  * Getting Started  Getting Started 
    * [ Cloud TPU Setup  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/)
    * Installation  [ Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/) Table of contents 
      * [ Interactive Installation Generator  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#interactive-installation-generator)
      * [ Prerequisites  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#prerequisites)
      * [ Package Architecture (vllm-torchtpu vs. vllm-torchtpu-core)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#package-architecture-vllm-torchtpu-vs-vllm-torchtpu-core)
      * [ Option 1: Install from PyPI (vllm-torchtpu)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-1-install-from-pypi-vllm-torchtpu)
        * [ Using uv (Recommended)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended)
        * [ Using pip  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip)
      * [ Option 2: Install from vllm-torchtpu Repository (--group vllm)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-2-install-from-vllm-torchtpu-repository-group-vllm)
        * [ Using uv (Recommended)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended_1)
        * [ Using pip  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip_1)
      * [ Option 3: Install vllm and vllm-torchtpu-core Separately (Cross-Repo Development)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-3-install-vllm-and-vllm-torchtpu-core-separately-cross-repo-development)
        * [ Using uv (Recommended)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended_2)
        * [ Using pip  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip_2)
      * [ Optional Dependency Groups & Extras  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#optional-dependency-groups-extras)
      * [ Verify Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#verify-installation)
    * [ Quickstart  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/)
    * [ Docker Guide  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/)
  * User Guide  User Guide 
    * [ Supported Models & Features  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/)
    * [ Parallelism & Scaling  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)
    * [ Multi-Host Serving  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)
    * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/disaggregated_serving/)
    * [ Quantization  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/quantization/)
    * [ Speculative Decoding  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/speculative_decoding/)
    * [ Compilation & Warmup Cache  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/)
    * Code Examples  Code Examples 
      * [ Offline Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_inference/)
      * [ Multi Modal Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_lora_inference/)
  * Deployment & Recipes  Deployment & Recipes 
    * [ TPU v7x (Ironwood) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/)
    * [ TPU v6e (Trillium) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v6e_recipes/)
    * [ Kubernetes & GKE  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/kubernetes/)
  * Developer Guide  Developer Guide 
    * [ Contributing  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/contributing/)
    * [ Coding Guidance  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/coding_guidance/)
    * [ Optimization Best Practices  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/optimization_best_practices/)
    * [ TPU Patch Mechanism  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/tpu_patch_mechanism/)
    * [ Type Checking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/type_checking/)
    * [ Testing & CI  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/testing_and_ci/)
    * [ Benchmarking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/benchmarking/)
    * [ Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/)
Profiling 
      * [ Offline (tpu_profiling.py)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/offline/)
      * [ Server-side Capture  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/server/)
      * [ Phased Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/phased/)
      * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/disaggregated/)
      * [ Output Layout  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/output/)
      * [ Viewing Traces  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/viewing/)
      * [ Troubleshooting  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/troubleshooting/)
  * Reference  Reference 
    * [ Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/)
  * [ Roadmap  ](https://vllm-torchtpu.readthedocs.io/en/latest/roadmap/)


Table of contents 
  * [ Interactive Installation Generator  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#interactive-installation-generator)
  * [ Prerequisites  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#prerequisites)
  * [ Package Architecture (vllm-torchtpu vs. vllm-torchtpu-core)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#package-architecture-vllm-torchtpu-vs-vllm-torchtpu-core)
  * [ Option 1: Install from PyPI (vllm-torchtpu)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-1-install-from-pypi-vllm-torchtpu)
    * [ Using uv (Recommended)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended)
    * [ Using pip  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip)
  * [ Option 2: Install from vllm-torchtpu Repository (--group vllm)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-2-install-from-vllm-torchtpu-repository-group-vllm)
    * [ Using uv (Recommended)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended_1)
    * [ Using pip  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip_1)
  * [ Option 3: Install vllm and vllm-torchtpu-core Separately (Cross-Repo Development)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-3-install-vllm-and-vllm-torchtpu-core-separately-cross-repo-development)
    * [ Using uv (Recommended)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended_2)
    * [ Using pip  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip_2)
  * [ Optional Dependency Groups & Extras  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#optional-dependency-groups-extras)
  * [ Verify Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#verify-installation)


[ ](https://github.com/vllm-project/vllm-torchtpu/edit/main/docs/getting_started/installation.md "Edit this page")
# Installation[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#installation "Permanent link")
`vllm-torchtpu` is a platform plugin for [vLLM](https://docs.vllm.ai/) that enables PyTorch-native LLM and multimodal serving on Google Cloud TPUs via `torch_tpu` and custom JAX/Pallas kernels.
* * *
## Interactive Installation Generator[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#interactive-installation-generator "Permanent link")
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
## Prerequisites[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#prerequisites "Permanent link")
  * **Python 3.12** (`>=3.12,<3.13`). Pre-built `tpu-sync-torch` and `torch_tpu` wheels target CPython 3.12.
  * We recommend using `uv` for installing dependencies as it is significantly faster than standard `pip`.


* * *
## Package Architecture (`vllm-torchtpu` vs. `vllm-torchtpu-core`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#package-architecture-vllm-torchtpu-vs-vllm-torchtpu-core "Permanent link")
  * **`pip install vllm-torchtpu`**(Combined PyPI package): Installs`site-packages/vllm/` (provides `import vllm` and the `vllm` CLI, built with `VLLM_TARGET_DEVICE="empty"`), and automatically pulls `vllm-torchtpu-core` as a dependency.
  * **`pip install vllm-torchtpu-core`**(OOT Plugin package built from this repo): Installs`site-packages/vllm_torchtpu/` (`import vllm_torchtpu`), which is automatically discovered and loaded by `vllm` via the `vllm.platform_plugins` entry point—you still run `vllm serve` or `import vllm` in user code. `vllm` is **not** a core dependency of `vllm-torchtpu-core`; for source installs, `--group vllm` builds `vllm` from source.

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-1)+----------------------------------------------------------------------------+
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-2)|  PyPI Package: vllm-torchtpu  (Combined Wrapper Wheel)                     |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-3)|  * Installs: `site-packages/vllm/`  -->  `import vllm` / `vllm serve`      |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-4)|  * Upstream vLLM built with VLLM_TARGET_DEVICE="empty"                     |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-5)|  * Discovers OOT plugin via `vllm.platform_plugins` entry point            |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-6)|                                                                            |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-7)|  +----------------------------------------------------------------------+  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-8)|  |  PyPI Package: vllm-torchtpu-core  (OOT Plugin Wheel — This Repo)    |  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-9)|  |  * Installs: `site-packages/vllm_torchtpu/`  (auto-loaded by vLLM)   |  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-10)|  |  * Entry point: `torchtpu = "vllm_torchtpu.platforms:..."`           |  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-11)|  |  * Requires TPU runtime dependencies:                                |  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-12)|  |    torch (CPU), torchvision (CPU), torch-tpu, libtpu,                |  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-13)|  |    tpu-sync-torch                                                    |  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-14)|  +----------------------------------------------------------------------+  |
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-15)+----------------------------------------------------------------------------+
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-16)  ^
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-17)  +-- Repo source install (`-e . --group vllm`):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-18)      Installs `vllm-torchtpu-core` from source + builds pinned upstream
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-0-19)      `vllm` from Git via PEP 735 `[dependency-groups]`.

```

Why the PyTorch CPU index (`https://download.pytorch.org/whl/cpu`) is required
On Linux `x86_64`, default PyPI (`pypi.org`) serves `torch` and `torchvision` wheels compiled with CUDA, which pulls gigabytes of unnecessary `nvidia-*` runtime dependencies onto TPU hosts. Setting `UV_TORCH_BACKEND=cpu` (or `pyproject.toml`'s `[tool.uv.sources]` for `uv`) or passing `--extra-index-url https://download.pytorch.org/whl/cpu` (for `pip`) routes `torch` and `torchvision` to the official PyTorch CPU wheel index while resolving all other dependencies (including `torch-tpu`, `libtpu`, and `tpu-sync-torch`) from public PyPI.
* * *
## Option 1: Install from PyPI ([`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/))[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-1-install-from-pypi-vllm-torchtpu "Permanent link")
For standard usage without modifying source code, install the pre-built [`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/) package directly from PyPI (this automatically installs both `vllm` and [`vllm-torchtpu-core`](https://pypi.org/project/vllm-torchtpu-core/)):
### Using `uv` (Recommended)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-1)uv venv --python 3.12 ~/uv_venv
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-2)source ~/uv_venv/bin/activate
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-3)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-4)# Route torch and torchvision to the PyTorch CPU index
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-5)export UV_TORCH_BACKEND=cpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-6)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-1-7)uv pip install vllm-torchtpu

```

### Using `pip`[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-1)python3.12 -m venv ~/pip_venv --symlinks
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-2)source ~/pip_venv/bin/activate
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-3)pip install --upgrade pip
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-4)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-5)pip install \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-6)  --extra-index-url https://download.pytorch.org/whl/cpu \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-2-7)  vllm-torchtpu

```

* * *
## Option 2: Install from `vllm-torchtpu` Repository (`--group vllm`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-2-install-from-vllm-torchtpu-repository-group-vllm "Permanent link")
To install `vllm-torchtpu-core` from a local clone of this repository and automatically build the pinned `vllm` commit from source via `--group vllm`:
### Using `uv` (Recommended)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended_1 "Permanent link")
`pyproject.toml` configures the `pytorch-cpu` index (`https://download.pytorch.org/whl/cpu`) for `torch` and `torchvision`, and pins compatible `torch-tpu`, `jax`, `libtpu`, and `vllm` versions automatically.

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-1)# 1. Install uv (if not already installed)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-2)curl -LsSf https://astral.sh/uv/install.sh | sh
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-3)source $HOME/.local/bin/env
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-4)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-5)# 2. Clone vllm-torchtpu and sync the environment (including the vllm group)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-6)git clone https://github.com/vllm-project/vllm-torchtpu.git
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-7)cd vllm-torchtpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-8)VLLM_TARGET_DEVICE=empty uv sync --group vllm
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-9)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-10)# 3. Activate the virtual environment
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-3-11)source .venv/bin/activate

```

To install in editable mode with test and development dependencies:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-4-1)uv venv --python 3.12 --seed
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-4-2)source .venv/bin/activate
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-4-3)export UV_TORCH_BACKEND=cpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-4-4)VLLM_TARGET_DEVICE=empty uv pip install -e . --group vllm --group test

```

### Using `pip`[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip_1 "Permanent link")
If using standard `pip` (`pip >= 25.1` for `--group` support), pass `--extra-index-url https://download.pytorch.org/whl/cpu` so `torch` and `torchvision` resolve to CPU wheels rather than default PyPI's CUDA wheels:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-1)python3.12 -m venv .venv
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-2)source .venv/bin/activate
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-3)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-4)pip install --upgrade pip
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-5)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-6)git clone https://github.com/vllm-project/vllm-torchtpu.git
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-7)cd vllm-torchtpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-8)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-9)VLLM_TARGET_DEVICE=empty pip install -e . --group vllm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-5-10)  --extra-index-url https://download.pytorch.org/whl/cpu

```

* * *
## Option 3: Install `vllm` and `vllm-torchtpu-core` Separately (Cross-Repo Development)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#option-3-install-vllm-and-vllm-torchtpu-core-separately-cross-repo-development "Permanent link")
Follow these steps when developing or debugging both `vllm` and `vllm-torchtpu-core` in separate local checkouts (or installing `vllm-torchtpu-core` without `--group vllm`). Currently, `vllm==0.31.0` is supported.
### Using `uv` (Recommended)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-uv-recommended_2 "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-1)uv venv --python 3.12 ~/uv_venv
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-2)source ~/uv_venv/bin/activate
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-3)export UV_TORCH_BACKEND=cpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-4)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-5)# 1. Clone and install vLLM in editable mode (with common dependencies)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-6)git clone --depth 1 --branch v0.31.0 https://github.com/vllm-project/vllm.git ~/vllm
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-7)VLLM_TARGET_DEVICE="empty" uv pip install -e ~/vllm
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-8)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-9)# 2. Clone and install vllm-torchtpu-core only (without --group vllm)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-10)git clone https://github.com/vllm-project/vllm-torchtpu.git ~/vllm-torchtpu && cd ~/vllm-torchtpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-6-11)uv pip install -e .

```

_(Or install`vllm-torchtpu-core` from PyPI instead of step 2: `uv pip install vllm-torchtpu-core`)_
### Using `pip`[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#using-pip_2 "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-1)python3.12 -m venv ~/pip_venv --symlinks
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-2)source ~/pip_venv/bin/activate
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-3)pip install --upgrade pip
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-4)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-5)# 1. Clone and install vLLM in editable mode (with common dependencies)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-6)git clone --depth 1 --branch v0.31.0 https://github.com/vllm-project/vllm.git ~/vllm
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-7)VLLM_TARGET_DEVICE="empty" pip install \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-8)  --extra-index-url https://download.pytorch.org/whl/cpu \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-9)  -e ~/vllm
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-10)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-11)# 2. Clone and install vllm-torchtpu-core only (without --group vllm)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-12)git clone https://github.com/vllm-project/vllm-torchtpu.git ~/vllm-torchtpu && cd ~/vllm-torchtpu
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-13)pip install \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-14)  --extra-index-url https://download.pytorch.org/whl/cpu \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-7-15)  -e .

```

_(Or install`vllm-torchtpu-core` from PyPI instead of step 2: `pip install --extra-index-url https://download.pytorch.org/whl/cpu vllm-torchtpu-core`)_
Why `VLLM_TARGET_DEVICE=empty`?
`vllm-torchtpu-core` registers itself through vLLM's out-of-tree platform plugin entry points (`vllm.platform_plugins` and `vllm.general_plugins`). Installing `vllm` with `VLLM_TARGET_DEVICE=empty` skips CUDA C++ extension compilation while keeping all Python server and engine entrypoints editable.
* * *
## Optional Dependency Groups & Extras[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#optional-dependency-groups-extras "Permanent link")  
| Flag  | Purpose  |  
| --- | --- |  
| `--group vllm`  | Installs pinned upstream `vllm` (`v0.31.0`) from source.  |  
| `--group test`  | Installs `pytest`, `pytest-mock`, `pytest-cov`, `parameterized`, and `vllm_test_utils`.  |  
| `--extra benchmarking`  | Installs `lm-eval`, `evalscope`, `datasets`, and `runai-model-streamer[gcs]`.  |  
| `--extra omni`  | Installs `vllm-omni` for multimodal diffusion models (e.g., FLUX, Wan2.2).  |  
* * *
## Verify Installation[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#verify-installation "Permanent link")
Verify that vLLM detects the `vllm-torchtpu` platform plugin:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/#__codelineno-8-1)python -c "from vllm.platforms import current_platform; print(current_platform.device_name)"

```

Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)