---
name: infer-13-vllm-tpu-installation
description: "vLLM TPU Installation and container guide \u2014 Official installation reference for the JAX-native vLLM TPU stack, including pip/uv and Docker options."
source_url: "https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/"
category: "inference_deployment_links"
---

# Agent Skill: vLLM TPU Installation and container guide

- **Official Source**: [https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/)
- **Category**: `inference_deployment_links`
- **Resource ID**: `infer_13_vllm_tpu_installation`
- **When to Activate**: Official installation reference for the JAX-native vLLM TPU stack, including pip/uv and Docker options.

## Document Sections

- **Installation**
  - **Installation Commands**
- **1. Create a working directory:**
- **2. Install uv and set up a Python virtual environment:**
- **If you prefer standard pip, simply use `python3.12 -m venv vllm_env`**
- **3. Use the following command to install vllm-tpu using uv or pip:**
- **Or instead: pip install vllm-tpu**
  - **Verify Installation**
- **Expected output:**
- **vllm version: 0.x.x**
- **tpu_inference version: 0.x.x**
- **vllm platform: TPU V6E (or your specific TPU architecture)**
- **jax backends: [TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), ...]**

## Key CLI Commands & Invocations

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv vllm_env --python 3.12
uv pip install vllm-tpu
python -c '
```

## Complete Technical Reference

# Installation
This guide provides instructions for installing and running `vllm-jax`.
There are three ways to install `vllm-jax`:
  * **uv pip** (Recommended): Fast installation of official stable releases into a Python virtual environment. Best for standard inference and serving.
  * **Docker** : Pre-built containers with shared memory configured. Best for reproducible environments and Kubernetes (GKE).
  * **Source** : Build directly from the repository. Best for debugging, contributors, and custom kernel development.


## Installation Commands
Select your preferred installation method to generate the exact setup command.
Method uv pip Docker Source
Image Release (latest) Nightly
Install the latest official release using uv pip for any supported TPU.

```
# 1. Create a working directory:
mkdir ~/work-dir
cd ~/work-dir

# 2. Install uv and set up a Python virtual environment:
# If you prefer standard pip, simply use `python3.12 -m venv vllm_env`
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv venv vllm_env --python 3.12
source vllm_env/bin/activate

# 3. Use the following command to install vllm-tpu using uv or pip:
uv pip install vllm-tpu
# Or instead: pip install vllm-tpu
```

## Verify Installation
To quickly verify that the installation was successful under any of the above methods and `vllm-tpu` is correctly configured:

```
python -c '
import jax
import vllm
import importlib.metadata
from vllm.platforms import current_platform

tpu_version = importlib.metadata.version("tpu_inference")
print(f"vllm version: {vllm.__version__}")
print(f"tpu_inference version: {tpu_version}")
print(f"vllm platform: {current_platform.get_device_name()}")
print(f"jax backends: {jax.devices()}")
'
# Expected output:
# vllm version: 0.x.x
# tpu_inference version: 0.x.x
# vllm platform: TPU V6E (or your specific TPU architecture)
# jax backends: [TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), ...]

```
