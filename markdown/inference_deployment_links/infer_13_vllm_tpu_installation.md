---
id: "infer_13_vllm_tpu_installation"
title: "vLLM TPU Installation and container guide"
url: "https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/"
category: "Inference deployment links"
description: "Official installation reference for the JAX-native vLLM TPU stack, including pip/uv and Docker options."
crawled_at: "2026-10-26T12:47:44.364745+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#installation)
[ ![vLLM logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/vllm-logo-only-light.png) + ![JAX logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/jax-logo.svg) ](https://docs.vllm.ai/projects/tpu/en/latest/ "vLLM JAX")
vLLM JAX 
Installation 
[ ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/?q= "Share")
Type to start searching
[ GitHub 
  * v0.32.0
  * 467
  * 349

](https://github.com/vllm-project/tpu-inference "Go to repository")
[ ![vLLM logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/vllm-logo-only-light.png) + ![JAX logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/jax-logo.svg) ](https://docs.vllm.ai/projects/tpu/en/latest/ "vLLM JAX") vLLM JAX 
[ GitHub 
  * v0.32.0
  * 467
  * 349

](https://github.com/vllm-project/tpu-inference "Go to repository")
  * [ Home  ](https://docs.vllm.ai/projects/tpu/en/latest/)
  * Getting Started  Getting Started 
    * [ TPU Setup  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/tpu_setup/)
    * Installation  [ Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/) Table of contents 
      * [ Installation Commands  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#installation-commands)
      * [ Verify Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#verify-installation)
    * [ Quickstart  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/)
  * Features & Usage  Features & Usage 
    * [ Recommended Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/)
    * [ Feature Matrix  ](https://docs.vllm.ai/projects/tpu/en/latest/features/)
    * Deployment Recipes  Deployment Recipes 
      * [ v7x Recipes (Ironwood)  ](https://docs.vllm.ai/projects/tpu/en/latest/deployment_guides/ironwood/)
      * [ v6e Recipes (Trillium)  ](https://docs.vllm.ai/projects/tpu/en/latest/deployment_guides/trillium/)
    * Code Examples  Code Examples 
      * [ Multi Modal Inference  ](https://docs.vllm.ai/projects/tpu/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://docs.vllm.ai/projects/tpu/en/latest/api_and_code_examples/offline_lora_inference/)
    * [ Out-of-Tree Usage  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/out-of-tree/)
  * Developers Guides  Developers Guides 
    * [ Contributing to vLLM JAX  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/contributing/)
    * [ Adding a New Model to CI  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/buildkite/)
    * [ JAX Model Development  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/jax_model_development/)
    * [ Torchax Model Development  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/torchax_model_development/)
    * [ Profiling  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/profiling/)


Table of contents 
  * [ Installation Commands  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#installation-commands)
  * [ Verify Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#verify-installation)


[ ](https://github.com/vllm-project/tpu-inference/edit/main/docs/getting_started/installation.md "Edit this page")
# Installation[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#installation "Permanent link")
This guide provides instructions for installing and running `vllm-jax`.
There are three ways to install `vllm-jax`:
  * **uv pip** (Recommended): Fast installation of official stable releases into a Python virtual environment. Best for standard inference and serving.
  * **Docker** : Pre-built containers with shared memory configured. Best for reproducible environments and Kubernetes (GKE).
  * **Source** : Build directly from the repository. Best for debugging, contributors, and custom kernel development.


## Installation Commands[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#installation-commands "Permanent link")
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

## Verify Installation[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#verify-installation "Permanent link")
To quickly verify that the installation was successful under any of the above methods and `vllm-tpu` is correctly configured:

```
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-1)python -c '
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-2)import jax
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-3)import vllm
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-4)import importlib.metadata
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-5)from vllm.platforms import current_platform
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-6)
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-7)tpu_version = importlib.metadata.version("tpu_inference")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-8)print(f"vllm version: {vllm.__version__}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-9)print(f"tpu_inference version: {tpu_version}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-10)print(f"vllm platform: {current_platform.get_device_name()}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-11)print(f"jax backends: {jax.devices()}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-12)'
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-13)# Expected output:
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-14)# vllm version: 0.x.x
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-15)# tpu_inference version: 0.x.x
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-16)# vllm platform: TPU V6E (or your specific TPU architecture)
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#__codelineno-0-17)# jax backends: [TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), ...]

```

Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)