---
id: "infer_12_vllm_tpu_quickstart"
title: "vLLM TPU quickstart"
url: "https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/"
category: "Inference deployment links"
description: "Install the TPU-compatible vLLM stack and start an inference API server."
crawled_at: "2026-10-26T12:47:44.623882+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#get-started-with-vllm-jax)
[ ![vLLM logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/vllm-logo-only-light.png) + ![JAX logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/jax-logo.svg) ](https://docs.vllm.ai/projects/tpu/en/latest/ "vLLM JAX")
vLLM JAX 
Quickstart 
[ ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/?q= "Share")
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
    * [ Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/)
    * Quickstart  [ Quickstart  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/) Table of contents 
      * [ Requirements  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#requirements)
      * [ Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#installation)
      * [ Verify Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#verify-installation)
      * [ Run the vLLM Server  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#run-the-vllm-server)
      * [ Next steps:  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#next-steps)
      * [ For further reading  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#for-further-reading)
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
  * [ Requirements  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#requirements)
  * [ Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#installation)
  * [ Verify Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#verify-installation)
  * [ Run the vLLM Server  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#run-the-vllm-server)
  * [ Next steps:  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#next-steps)
  * [ For further reading  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#for-further-reading)


[ ](https://github.com/vllm-project/tpu-inference/edit/main/docs/getting_started/quickstart.md "Edit this page")
# Get started with vLLM JAX[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#get-started-with-vllm-jax "Permanent link")
Google Cloud TPUs (Tensor Processing Units) accelerate machine learning workloads. vLLM supports TPU v6e and v5e. For architecture, supported topologies, and more, see [TPU System Architecture](https://cloud.google.com/tpu/docs/system-architecture) and specific TPU version pages ([v5e](https://cloud.google.com/tpu/docs/v5e) and [v6e](https://cloud.google.com/tpu/docs/v6e)).
* * *
## Requirements[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#requirements "Permanent link")
  * **Google Cloud TPU VM:** Access to a TPU VM. For setup instructions, see the [Cloud TPU Setup guide](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/tpu_setup/).
  * **TPU versions:** v7x, v6e, v5e
  * **Python:** 3.11 or newer (3.12 used in examples).


* * *
## Installation[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#installation "Permanent link")
For detailed steps on installing `vllm-tpu` with `pip` or running it as a Docker image, please see the [**Installation Guide**](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/).
We recommend using [uv](https://docs.astral.sh/uv/) (`uv pip install`) instead of standard `pip` as it improves installation speed.

```
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-0-1)uv pip install vllm-tpu

```

## Verify Installation[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#verify-installation "Permanent link")
To quickly verify that the installation was successful and `vllm-tpu` is correctly configured:

```
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-1)python -c '
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-2)import jax
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-3)import vllm
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-4)import importlib.metadata
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-5)from vllm.platforms import current_platform
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-6)
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-7)tpu_version = importlib.metadata.version("tpu_inference")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-8)print(f"vllm version: {vllm.__version__}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-9)print(f"tpu_inference version: {tpu_version}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-10)print(f"vllm platform: {current_platform.get_device_name()}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-11)print(f"jax backends: {jax.devices()}")
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-12)'
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-13)# Expected output:
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-14)# vllm version: 0.x.x
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-15)# tpu_inference version: 0.x.x
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-16)# vllm platform: TPU V6E (or your specific TPU architecture)
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-1-17)# jax backends: [TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), ...]

```

## Run the vLLM Server[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#run-the-vllm-server "Permanent link")
After installing `vllm-tpu`, you can start the API server.
  1. **Log in to Hugging Face:** You'll need a Hugging Face token to download models.

```
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-2-1)export TOKEN=YOUR_TOKEN
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-2-2)git config --global credential.helper store
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-2-3)huggingface-cli login --token $TOKEN

```

  1. **Launch the Server:** The following command starts the server with the Llama-3.1-8B model.

```
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-3-1)vllm serve "meta-llama/Llama-3.1-8B" \
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-3-2)    --download_dir /tmp \
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-3-3)    --tensor_parallel_size=1 \
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-3-4)    --max-model-len=2048

```

  1. **Send a Request:**


Once the server is running, you can send it a request using `curl`:

```
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-1)curl http://localhost:8000/v1/completions \
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-2)    -H "Content-Type: application/json" \
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-3)    -d '{
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-4)        "model": "meta-llama/Llama-3.1-8B",
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-5)        "prompt": "Hello, my name is",
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-6)        "max_tokens": 20,
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-7)        "temperature": 0.7
[](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#__codelineno-4-8)    }'

```

## Next steps:[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#next-steps "Permanent link")
Check out complete, end-to-end example recipes in the [tpu-recipes repository](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/trillium/vLLM)
## For further reading[¶](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/#for-further-reading "Permanent link")
  * [Examples](https://github.com/vllm-project/tpu-inference/tree/main/examples)
  * [v7x (Ironwood) Recipes](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/ironwood/vLLM)
  * [v6e (Trillium) Recipes](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/trillium/vLLM)
  * [GKE serving with vLLM TPU](https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu)


Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)