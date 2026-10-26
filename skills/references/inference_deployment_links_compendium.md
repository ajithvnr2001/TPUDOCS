# Complete Reference Compendium: `inference_deployment_links` (18 Resources)

## `infer_01_vllm_torchtpu_repo` — vLLM-TorchTPU official repository
- **URL**: https://github.com/vllm-project/vllm-torchtpu
- **Description**: Official PyTorch-native TPU backend for vLLM; separate out-of-tree plugin/package from vllm-tpu (JAX-native).
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_01_vllm_torchtpu_repo/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_01_vllm_torchtpu_repo.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_01_vllm_torchtpu_repo.md`

### Sections (10) & Code Examples (4)
- vLLM-TorchTPU Official Repository
- About
- Supported hardware
- Get started
- Install
- Serve a model
- Supported models and features
- Recipes and deployment
- 🤝 Contribute
- 💬 Contact us

## `infer_02_vllm_torchtpu_quickstart` — vLLM-TorchTPU quickstart
- **URL**: https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/
- **Description**: Ready-to-run online serving, offline inference, and multimodal examples for PyTorch-native TPU serving.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_02_vllm_torchtpu_quickstart/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_02_vllm_torchtpu_quickstart.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_02_vllm_torchtpu_quickstart.md`

### Sections (39) & Code Examples (10)
- Quickstart
- 1. Online Serving (`vllm serve`)
- Single-Chip (`TP=1`)
- 8-Device TPU Host (`TP=8` + Expert Parallelism)
- 2. Offline Batch Inference (`vllm.LLM`)
- SPDX-FileCopyrightText: Copyright contributors to the vLLM project
- Licensed under the Apache License, Version 2.0 (the "License");
- you may not use this file except in compliance with the License.
- You may obtain a copy of the License at
- http://www.apache.org/licenses/LICENSE-2.0
- Unless required by applicable law or agreed to in writing, software
- distributed under the License is distributed on an "AS IS" BASIS,
- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- See the License for the specific language governing permissions and
- limitations under the License.

## `infer_03_vllm_torchtpu_installation` — vLLM-TorchTPU installation
- **URL**: https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/
- **Description**: Install the PyTorch-native vLLM TPU plugin; distinct from the vllm-tpu JAX backend.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_03_vllm_torchtpu_installation/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_03_vllm_torchtpu_installation.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_03_vllm_torchtpu_installation.md`

### Sections (24) & Code Examples (10)
- Installation
- Interactive Installation Generator
- Install vllm-torchtpu from PyPI (https://pypi.org/project/vllm-torchtpu/):
- Prerequisites
- Package Architecture (`vllm-torchtpu` vs. `vllm-torchtpu-core`)
- Option 1: Install from PyPI ([`vllm-torchtpu`](https://pypi.org/project/vllm-torchtpu/))
- Using `uv` (Recommended)
- Route torch and torchvision to the PyTorch CPU index
- Using `pip`
- Option 2: Install from `vllm-torchtpu` Repository (`--group vllm`)
- Using `uv` (Recommended)
- 1. Install uv (if not already installed)
- 2. Clone vllm-torchtpu and sync the environment (including the vllm group)
- 3. Activate the virtual environment
- Using `pip`

## `infer_04_vllm_torchtpu_setup` — vLLM-TorchTPU Cloud TPU setup
- **URL**: https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/
- **Description**: Official provisioning and hardware guidance for the vLLM-TorchTPU stack.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_04_vllm_torchtpu_setup/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_04_vllm_torchtpu_setup.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_04_vllm_torchtpu_setup.md`

### Sections (14) & Code Examples (11)
- Cloud TPU Setup
- TPU Versions and Topologies
- Recommended
- Experimental
- Prerequisites
- Provisioning Cloud TPUs
- Connecting and Checking Status
- Compute Engine (TPU v6e, v5p)
- Queued Resources (TPU v7x, v5e, v4)
- Verify TPU Devices
- Clean Up Resources
- Compute Engine (TPU v6e, v5p)
- Queued Resources (TPU v7x, v5e, v4)
- Next Steps

## `infer_05_vllm_torchtpu_supported_models` — vLLM-TorchTPU supported models and features
- **URL**: https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/
- **Description**: Check validated checkpoints, attention backends, quantization, and serving feature support.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_05_vllm_torchtpu_supported_models/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_05_vllm_torchtpu_supported_models.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_05_vllm_torchtpu_supported_models.md`

### Sections (3) & Code Examples (0)
- Supported Models & Features
- Validated Models
- Feature Support

## `infer_06_vllm_torchtpu_docker` — vLLM-TorchTPU Docker guide
- **URL**: https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/
- **Description**: Container images and build targets for TPU inference; distinguish runtime images from CI-only images.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_06_vllm_torchtpu_docker/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_06_vllm_torchtpu_docker.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_06_vllm_torchtpu_docker.md`

### Sections (11) & Code Examples (9)
- Docker images
- Pre-built Images on Docker Hub
- Release Images (`--target prod`)
- Nightly Images (`--target dev`)
- Running the Container on a Cloud TPU VM
- Image targets
- `ci:latest`
- `dev:latest`
- `prod:latest`
- vllm-router
- Useful build arguments

## `infer_07_vllm_torchtpu_compilation_cache` — vLLM-TorchTPU compilation cache
- **URL**: https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/
- **Description**: Persist compiled artifacts and reduce repeated startup compilation.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_07_vllm_torchtpu_compilation_cache/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_07_vllm_torchtpu_compilation_cache.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_07_vllm_torchtpu_compilation_cache.md`

### Sections (4) & Code Examples (1)
- TorchTPU Compilation Cache
- Cache Architecture & Environment Variables
- Compilation Debugging & Telemetry
- `VLLM_XLA_CHECK_RECOMPILATION` (Runtime Recompilation Detector)

## `infer_08_llama_32_1b_instruct` — Llama 3.2 1B Instruct model and access
- **URL**: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- **Description**: Model card, license, and gated-access page for the documented vLLM-TorchTPU quickstart model.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_08_llama_32_1b_instruct/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_08_llama_32_1b_instruct.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_08_llama_32_1b_instruct.md`

### Sections (26) & Code Examples (0)
- Meta Llama 3.2 1B Instruct (`meta-llama/Llama-3.2-1B-Instruct`)
- Model Information
- Intended Use
- How to use
- Use with transformers
- Use with `llama`
- Hardware and Software
- Training Data
- Quantization
- Quantization Scheme
- Quantization-Aware Training and LoRA
- SpinQuant
- Benchmarks - English Text
- Base Pretrained Models
- Instruction Tuned Models

## `infer_09_hf_cli_auth` — Hugging Face CLI authentication
- **URL**: https://huggingface.co/docs/huggingface_hub/guides/cli
- **Description**: Authenticate to download private or gated model weights before starting the TPU serving example.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_09_hf_cli_auth/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_09_hf_cli_auth.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_09_hf_cli_auth.md`

### Sections (355) & Code Examples (208)
- Command Line Interface (CLI)
- Getting started
- Standalone installer (Recommended)
- Using uv
- Install with pip
- Using Homebrew
- Updating
- Output formatting
- JSON output for scripting
- IDs only, one per line
- hf auth login
- Or using an environment variable
- hf auth whoami
- hf auth logout
- hf download

## `infer_10_sglang_torchtpu_repo` — SGLang-TorchTPU official repository
- **URL**: https://github.com/sgl-project/sglang-torchtpu
- **Description**: Official SGLang PyTorch-native TPU backend, complementary to vLLM-TorchTPU and distinct from SGLang-JAX.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_10_sglang_torchtpu_repo/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_10_sglang_torchtpu_repo.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_10_sglang_torchtpu_repo.md`

### Sections (13) & Code Examples (7)
- SGLang-TorchTPU Official Repository
- Highlights
- Get started
- Docker
- pip
- From source
- Launch a server
- Supported hardware
- Models and features
- Part of the SGLang ecosystem
- Development and contributing
- Issues and feedback
- License and acknowledgments

## `infer_11_tpu_inference_cloud_docs` — Run inference on Cloud TPU
- **URL**: https://docs.cloud.google.com/tpu/docs/tpu-inference
- **Description**: Official overview of TPU inference, vLLM integration, prerequisites, and serving examples.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_11_tpu_inference_cloud_docs/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_11_tpu_inference_cloud_docs.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_11_tpu_inference_cloud_docs.md`

### Sections (10) & Code Examples (0)
- Run inference on Cloud TPU
- Set up your TPU
- Choose an inference stack
- Inference with vLLM
- vLLM with JAX
- vLLM with PyTorch
- Inference with SGLang
- SGLang with PyTorch
- SGLang with JAX
- Profile inference performance

## `infer_12_vllm_tpu_quickstart` — vLLM TPU quickstart
- **URL**: https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/
- **Description**: Install the TPU-compatible vLLM stack and start an inference API server.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_12_vllm_tpu_quickstart/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_12_vllm_tpu_quickstart.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_12_vllm_tpu_quickstart.md`

### Sections (12) & Code Examples (5)
- Get started with vLLM JAX
- Requirements
- Installation
- Verify Installation
- Expected output:
- vllm version: 0.x.x
- tpu_inference version: 0.x.x
- vllm platform: TPU V6E (or your specific TPU architecture)
- jax backends: [TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), ...]
- Run the vLLM Server
- Next steps:
- For further reading

## `infer_13_vllm_tpu_installation` — vLLM TPU Installation and container guide
- **URL**: https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/
- **Description**: Official installation reference for the JAX-native vLLM TPU stack, including pip/uv and Docker options.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_13_vllm_tpu_installation/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_13_vllm_tpu_installation.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_13_vllm_tpu_installation.md`

### Sections (13) & Code Examples (2)
- Installation
- Installation Commands
- 1. Create a working directory:
- 2. Install uv and set up a Python virtual environment:
- If you prefer standard pip, simply use `python3.12 -m venv vllm_env`
- 3. Use the following command to install vllm-tpu using uv or pip:
- Or instead: pip install vllm-tpu
- Verify Installation
- Expected output:
- vllm version: 0.x.x
- tpu_inference version: 0.x.x
- vllm platform: TPU V6E (or your specific TPU architecture)
- jax backends: [TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), ...]

## `infer_14_vllm_tpu_recommended_models` — vLLM TPU recommended models
- **URL**: https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/
- **Description**: Model and feature validation matrix; check release and nightly support before deploying.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_14_vllm_tpu_recommended_models/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_14_vllm_tpu_recommended_models.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_14_vllm_tpu_recommended_models.md`

### Sections (4) & Code Examples (0)
- Recommended Models
- Recommended Models
- Models
- Embedding Models

## `infer_15_gke_serve_vllm_trillium` — Serve an LLM on GKE with vLLM and TPU Trillium
- **URL**: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu
- **Description**: End-to-end Kubernetes deployment tutorial for vLLM on TPU v6e.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_15_gke_serve_vllm_trillium/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_15_gke_serve_vllm_trillium.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_15_gke_serve_vllm_trillium.md`

### Sections (30) & Code Examples (32)
- Serve an LLM using TPU Trillium on GKE with vLLM
- Background
- TPU Trillium
- vLLM
- Supported models and features
- Cloud Storage FUSE
- Objectives
- Before you begin
- Check for the roles
- Grant the roles
- Prepare the environment
- Get access to the model
- Generate an access token
- Launch Cloud Shell
- Create a GKE cluster

## `infer_16_gke_ray_vllm_qwen3` — Google Kubernetes Engine Ray + vLLM TPU Qwen3 sample
- **URL**: https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve
- **Description**: Official GKE production-oriented tutorial/sample using Ray Serve and vLLM-TPU to deploy an ungated small model on a TPU v6e slice.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_16_gke_ray_vllm_qwen3/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_16_gke_ray_vllm_qwen3.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_16_gke_ray_vllm_qwen3.md`

### Sections (88) & Code Examples (13)
- Serve Qwen3 on GKE with Ray, vLLM, and TPU v6e (`ai-ml/gke-ray/tpu/get-started/serve`)
- Serve Qwen3-4B on a TPU slice with Ray Serve and vLLM
- Prerequisites
- About the base image
- Deploy
- -> Running
- Send a request
- Watch it run: Ray Dashboard + Grafana
- Ray Dashboard, Serve tab + Cluster tab (live TPU utilization / HBM)
- open http://localhost:8265
- Grafana, the Ray "Serve LLM" dashboard is auto-loaded
- open http://localhost:3000  (default login admin / prom-operator)
- How it works
- Clean up
- Next

## `infer_17_gke_online_inference_ref_arch` — GKE online inference TPU reference implementation (vLLM)
- **URL**: https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/docs/platforms/gke/base/use-cases/inference-ref-arch/online-inference-tpu/vllm-with-hf-model.md
- **Description**: Google Cloud Platform GKE inference reference architecture page for online vLLM serving on TPUs.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_17_gke_online_inference_ref_arch/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_17_gke_online_inference_ref_arch.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_17_gke_online_inference_ref_arch.md`

### Sections (6) & Code Examples (25)
- Online inference using vLLM with TPUs on Google Kubernetes Engine (GKE)
- Before you begin
- Create and configure the Google Cloud resources
- Download the model to Cloud Storage
- Deploy the inference workload
- Clean up

## `infer_18_gke_serve_kuberay_tpus` — Serve LLMs with KubeRay and TPUs on GKE
- **URL**: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray
- **Description**: Deploy vLLM-based serving using the Ray Operator and supported TPU configurations.
- **Dedicated Skill**: `skills/catalog/inference_deployment_links/infer_18_gke_serve_kuberay_tpus/SKILL.md`
- **OKF Entity**: `okf/entities/inference_deployment_links/infer_18_gke_serve_kuberay_tpus.okf.json`
- **Markdown Source**: `markdown/inference_deployment_links/infer_18_gke_serve_kuberay_tpus.md`

### Sections (50) & Code Examples (74)
- Serve an LLM using TPUs on GKE with KubeRay
- Background
- GKE managed Kubernetes service
- Ray operator
- TPUs
- vLLM
- Objectives
- Before you begin
- Prepare your environment
- Llama-3-8B-Instruct
- Mistral-7B
- Llama 3.1 70B
- Create a cluster
- Autopilot
- Standard
