# Cloud TPU Complete Documentation, Agent Skills & Open Knowledge Base

Comprehensive directory of **85 official Google Cloud TPU resources**, crawled end-to-end and organized into three standard formats:
1. **Separate Markdown Format (`markdown/`)**: Clean, fully formatted documentation with frontmatter metadata.
2. **AI Agent Skill Format (`skills/`)**: Operational knowledge, instructions, checklists, reference tables, and execution scripts adhering to the AI Agent Skill standard.
3. **Google Open Knowledge Format (`okf/`)**: Structured knowledge graphs, semantic triples, entity models, verified assertions, and QA banks conforming to the Google Open Knowledge Format (OKF).

Also includes the authoritative **[Practical Deployment Guide](DEPLOYMENT_GUIDE.md)** for migrating NVIDIA CUDA workloads to Cloud TPUs.

---

## Repository Structure

```text
/data/tpu/
├── README.md                                # Master documentation index and catalog
├── DEPLOYMENT_GUIDE.md                      # Practical 9-step NVIDIA to TPU deployment guide
├── resources.json                           # Structured index of all 85 target resources
├── crawler_pipeline.py                      # Crawling pipeline powered by Crawl4AI, Scrapling, ScrapeGraphAI
├── markdown/                                # Format 1: Individual Markdown files for all 85 resources
│   ├── legacy_docs/                         # (4 documents: Cloud TPU API, PyTorch/XLA legacy notice)
│   ├── tpu_setup_docs/                      # (23 documents: Setup, IAM, v6e Trillium, TPU7x Ironwood, Quotas, Pricing)
│   ├── training_framework_links/            # (22 documents: MaxText, TorchTitan, Ray on GKE, JAX, Keras 3, TF)
│   ├── inference_deployment_links/          # (18 documents: vLLM-TorchTPU, SGLang, GKE Ray Serve, Llama 3.2)
│   └── nvidia_to_tpu_migration_docs/        # (18 documents: TorchTPU API reference, Pallas, Tokamax, XProf)
├── skills/                                  # Format 2: AI Agent Skill specification
│   ├── tpu-orchestrator/SKILL.md            # Master Orchestrator Agent Skill
│   ├── tpu-setup-provisioning/SKILL.md      # Provisioning & Compute Engine management
│   ├── nvidia-to-tpu-migration/SKILL.md     # CUDA-to-TPU code migration
│   ├── tpu-inference-vllm/SKILL.md          # vLLM-TorchTPU serving operations
│   ├── tpu-training-workflows/SKILL.md      # Distributed training (MaxText, TorchTitan, Ray)
│   ├── tpu-troubleshooting-profiling/SKILL.md # Diagnostics, health monitoring, XProf
│   ├── references/                          # Cheatsheets and comparison matrices
│   │   ├── cuda_to_tpu_cheatsheet.md
│   │   ├── tpu_hardware_matrix.md
│   │   └── environment_variables.md
│   └── scripts/                             # Verified deployment bash scripts
│       ├── provision_tpu_vm.sh
│       ├── setup_torchtpu_env.sh
│       ├── serve_vllm_torchtpu.sh
│       ├── test_tpu_endpoint.sh
│       └── cleanup_tpu.sh
└── okf/                                     # Format 3: Google Open Knowledge Format (OKF)
    ├── schema.json                          # Formal JSON Schema for OKF accelerator graphs
    ├── tpu_knowledge_graph.json             # Aggregated Open Knowledge Graph (Triples, Assertions, QA)
    └── entities/                            # Individual OKF entity descriptors (85 files)
        ├── legacy_docs/
        ├── tpu_setup_docs/
        ├── training_framework_links/
        ├── inference_deployment_links/
        └── nvidia_to_tpu_migration_docs/
```

---

## Directory of 85 Official TPU Resources

### 1. Legacy Docs (4 Resources)
| ID | Resource Name | Local Markdown | Source URL | Description |
| :--- | :--- | :--- | :--- | :--- |
| `legacy_01` | Manage TPU resources (legacy Cloud TPU API) | [legacy_01.md](markdown/legacy_docs/legacy_01_manage_tpus_legacy_api.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm) | Legacy stop/delete cleanup reference; retain only for existing Cloud TPU API resources. |
| `legacy_02` | Run JAX on a Cloud TPU VM — legacy API | [legacy_02.md](markdown/legacy_docs/legacy_02_run_calculation_jax_legacy.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/run-calculation-jax) | Older Cloud TPU API quickstart; use the Compute Engine quickstart for new provisioning. |
| `legacy_03` | Hugging Face training scripts — legacy TPU instructions | [legacy_03.md](markdown/legacy_docs/legacy_03_hf_training_scripts_legacy.md) | [Hugging Face](https://huggingface.co/docs/transformers/run_scripts) | The TPU section uses PyTorch/XLA and xla_spawn.py; do not treat it as the current TorchTPU setup. |
| `legacy_04` | PyTorch/XLA documentation (legacy notice) | [legacy_04.md](markdown/legacy_docs/legacy_04_pytorch_xla_legacy_notice.md) | [PyTorch](https://docs.pytorch.org/xla/master/index.html) | Retain only for migrating existing code: labels PyTorch/XLA deprecated and replaced by TorchTPU. |

### 2. TPU Setup Docs (23 Resources)
| ID | Resource Name | Local Markdown | Source URL | Description |
| :--- | :--- | :--- | :--- | :--- |
| `setup_01` | Cloud TPU documentation hub | [setup_01.md](markdown/tpu_setup_docs/setup_01_cloud_tpu_docs_hub.md) | [Google Cloud](https://cloud.google.com/tpu/docs) | Main entry point for official TPU setup, hardware, training, serving, and operations documentation. |
| `setup_02` | Introduction to Cloud TPU | [setup_02.md](markdown/tpu_setup_docs/setup_02_intro_to_tpu.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) | Explains service choices, hardware fit, planning, provisioning; notes Cloud TPU API deprecation. |
| `setup_03` | Quickstart: Create a TPU instance | [setup_03.md](markdown/tpu_setup_docs/setup_03_quickstart_create_tpu_instance.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/quickstart-create-tpu-instance) | Fastest Compute Engine provisioning path, including required IAM roles and a v6e example. |
| `setup_04` | Set up a Google Cloud project for TPUs | [setup_04.md](markdown/tpu_setup_docs/setup_04_setup_gcp_account.md) | [Google Cloud](https://cloud.google.com/tpu/docs/setup-gcp-account) | Account/project, API enablement, IAM, and access prerequisites for TPU work. |
| `setup_05` | Create a Cloud TPU VM instance using Compute Engine | [setup_05.md](markdown/tpu_setup_docs/setup_05_create_instance_compute.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/create-instance-compute) | Detailed Compute Engine creation guide for on-demand, Spot, reservation-bound, and flex-start VMs. |
| `setup_06` | Cloud TPU resources in Compute Engine | [setup_06.md](markdown/tpu_setup_docs/setup_06_tpus_in_compute_engine.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) | Conceptual migration guide mapping TPU VMs/slices to Compute Engine instances, MIGs, and policies. |
| `setup_07` | Plan your Cloud TPU resources | [setup_07.md](markdown/tpu_setup_docs/setup_07_plan_tpus.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/plan-tpus) | Hardware/size and consumption planning across on-demand, Spot, reservations, and flex-start. |
| `setup_08` | TPU regions and zones | [setup_08.md](markdown/tpu_setup_docs/setup_08_regions_zones.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/regions-zones) | Authoritative availability matrix for TPU generations, configurations, regions, and zones. |
| `setup_09` | Cloud TPU quotas | [setup_09.md](markdown/tpu_setup_docs/setup_09_quota.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/quota) | Quota names, default per-zone limits, on-demand/preemptible distinctions, and quota requests. |
| `setup_10` | Cloud TPU pricing | [setup_10.md](markdown/tpu_setup_docs/setup_10_pricing.md) | [Google Cloud](https://cloud.google.com/tpu/pricing) | Official price reference to compare generation, zone, and consumption mode. |
| `setup_11` | TPU software versions | [setup_11.md](markdown/tpu_setup_docs/setup_11_runtimes.md) | [Google Cloud](https://cloud.google.com/tpu/docs/runtimes) | Runtime/image selection for TPU generations and PyTorch/JAX workloads. |
| `setup_12` | TPU architecture | [setup_12.md](markdown/tpu_setup_docs/setup_12_system_architecture.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm) | Explains TPU chips, matrix units, hosts, slices, topology, and distributed connectivity. |
| `setup_13` | TPU v6e hardware documentation | [setup_13.md](markdown/tpu_setup_docs/setup_13_v6e_hardware.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/v6e) | Trillium hardware specifications, memory, and supported configurations. |
| `setup_14` | TPU7x Ironwood hardware documentation | [setup_14.md](markdown/tpu_setup_docs/setup_14_tpu7x_hardware.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/tpu7x) | Hardware, topology, and configurations; supports PyTorch and JAX, **NOT TensorFlow**. |
| `setup_15` | TPU v5e hardware documentation | [setup_15.md](markdown/tpu_setup_docs/setup_15_v5e_hardware.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/v5e) | Hardware specifications and configurations for TPU v5e. |
| `setup_16` | Request TPU Spot VMs | [setup_16.md](markdown/tpu_setup_docs/setup_16_spot_compute.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/spot-compute) | Discounted/preemptible Compute Engine TPU operation, including single VMs and MIG slices. |
| `setup_17` | Connect TPU VMs to Cloud Storage | [setup_17.md](markdown/tpu_setup_docs/setup_17_storage_buckets.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute) | Access datasets and model artifacts from TPU VMs; includes Compute Engine cleanup commands. |
| `setup_18` | Cloud TPU bfloat16 guide | [setup_18.md](markdown/tpu_setup_docs/setup_18_bfloat16_guide.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/bfloat16) | Precision guidance and checkpoint portability considerations for TPU workloads. |
| `setup_19` | Cloud TPU storage best practices | [setup_19.md](markdown/tpu_setup_docs/setup_19_storage_best_practices.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/storage-best-practices) | Choose storage for data loading, model weights, and synchronous or asynchronous checkpoints. |
| `setup_20` | TPU7x performance optimizations | [setup_20.md](markdown/tpu_setup_docs/setup_20_ironwood_performance.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/ironwood-performance) | Optimize memory movement, low-precision computation, sharding, and communication on Ironwood. |
| `setup_21` | Troubleshoot your Cloud TPU workflow | [setup_21.md](markdown/tpu_setup_docs/setup_21_troubleshooting.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/troubleshooting/troubleshooting) | Operations troubleshooting using Cloud Monitoring metrics, Cloud Logging, and diagnostics. |
| `setup_22` | Monitor Cloud TPU health | [setup_22.md](markdown/tpu_setup_docs/setup_22_tpu_health.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health) | Health monitoring and unhealthy-instance detection for TPU VMs, metrics and dashboards. |
| `setup_23` | Cloud TPU samples and recipes | [setup_23.md](markdown/tpu_setup_docs/setup_23_samples_and_recipes.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/samples) | Official index of TPU recipes, including MaxText LLM training and MaxDiffusion SDXL examples. |

### 3. Training Framework Links (22 Resources)
| ID | Resource Name | Local Markdown | Source URL | Description |
| :--- | :--- | :--- | :--- | :--- |
| `train_01` | TorchTPU GKE quickstart | [train_01.md](markdown/training_framework_links/train_01_torchtpu_gke_quickstart.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/) | Deploy TorchTPU containers on GKE for single-device, single-host, or multi-host workloads. |
| `train_02` | TensorFlow TPUStrategy API | [train_02.md](markdown/training_framework_links/train_02_tf_distribute_tpustrategy.md) | [TensorFlow](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) | API reference for synchronous TensorFlow training on TPUs and TPU Pods. |
| `train_03` | Train a model on TPU7x with MaxText or TorchTitan | [train_03.md](markdown/training_framework_links/train_03_tpu7x_training.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/tpu7x-training) | Provision Ironwood training infrastructure and use JAX or PyTorch training recipes. |
| `train_04` | Fine-tune models with Ray and TorchTPU on GKE | [train_04.md](markdown/training_framework_links/train_04_gke_ray_torchtpu_finetune.md) | [Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-models-tpu-ray-torchtpu) | Distributed PyTorch fine-tuning across TPU hosts using Ray and FSDP2. |
| `train_05` | JAX installation | [train_05.md](markdown/training_framework_links/train_05_jax_installation.md) | [JAX Docs](https://docs.jax.dev/en/latest/installation.html) | Official accelerator-specific installation, including jax[tpu] for Cloud TPU VMs. |
| `train_06` | Thinking in JAX | [train_06.md](markdown/training_framework_links/train_06_thinking_in_jax.md) | [JAX Docs](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html) | JAX programming concepts for portable CPU, GPU, and TPU computation. |
| `train_07` | Building production AI on Cloud TPUs with JAX | [train_07.md](markdown/training_framework_links/train_07_jax_ai_stack.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/jax-ai-stack) | Overview of the JAX AI stack; identifies MaxText for LLMs and MaxDiffusion for diffusion. |
| `train_08` | TensorFlow TPU guide | [train_08.md](markdown/training_framework_links/train_08_tensorflow_tpu_guide.md) | [TensorFlow](https://www.tensorflow.org/guide/tpu) | Initialize TPU hardware and use tf.distribute.TPUStrategy for TensorFlow/Keras workloads. |
| `train_09` | TorchTitan on TPU getting started | [train_09.md](markdown/training_framework_links/train_09_torchtitan_tpu_getting_started.md) | [GitHub](https://github.com/google-pytorch/torchtitan/blob/main/torchtitan/experiments/tpu/README.md) | TPU-specific setup and training recipes for TorchTitan. |
| `train_10` | Hugging Face Keras/TF TPU guide | [train_10.md](markdown/training_framework_links/train_10_hf_keras_tf_tpu_guide.md) | [Hugging Face](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf) | Keras sequence-classification example: TPUClusterResolver, TPUStrategy, strategy.scope(). |
| `train_11` | Cloud TPU MNIST with TensorFlow 2.x/Keras | [train_11.md](markdown/training_framework_links/train_11_mnist_tf2_keras.md) | [Google Cloud](https://cloud.google.com/tpu/docs/tutorials/mnist-2.x) | Official end-to-end TensorFlow/Keras training recipe using TPU distribution. |
| `train_12` | Keras distributed training with JAX | [train_12.md](markdown/training_framework_links/train_12_keras_distributed_jax.md) | [Keras](https://keras.io/guides/distributed_training_with_jax/) | Use JAX sharding to train Keras models across multiple GPUs or TPUs. |
| `train_13` | Keras 3 distribution guide | [train_13.md](markdown/training_framework_links/train_13_keras_distribution_guide.md) | [Keras](https://keras.io/guides/distribution/) | Data and model distribution concepts for multi-device Keras workflows. |
| `train_14` | Keras SparseCore embedding example | [train_14.md](markdown/training_framework_links/train_14_keras_sparsecore_embedding.md) | [Keras](https://keras.io/keras_rs/examples/distributed_embedding_jax/) | Distributed recommendation-model embeddings using JAX and TPU SparseCore. |
| `train_15` | Hugging Face fine-tuning guide | [train_15.md](markdown/training_framework_links/train_15_hf_training_guide.md) | [Hugging Face](https://huggingface.co/docs/transformers/training) | General model, dataset, Trainer, and checkpoint workflow; not a TPU runtime setup guide. |
| `train_16` | MaxText | [train_16.md](markdown/training_framework_links/train_16_maxtext.md) | [GitHub](https://github.com/google/maxtext) | Google AI-Hypercomputer JAX/XLA LLM training codebase (Gemma, Llama, DeepSeek, Qwen). |
| `train_17` | MaxText TPU setup script | [train_17.md](markdown/training_framework_links/train_17_maxtext_setup_sh.md) | [GitHub](https://github.com/google/maxtext/blob/main/src/dependencies/scripts/setup.sh) | Concrete MaxText dependency setup for TPU, including stable/nightly JAX, jaxlib, and libtpu. |
| `train_18` | MaxText single-host Gemma supervised fine-tuning | [train_18.md](markdown/training_framework_links/train_18_maxtext_gemma_sft_single_host.md) | [Google Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext) | Fine-tune Gemma on a v6e-8 TPU VM and convert checkpoints between Hugging Face and MaxText. |
| `train_19` | MaxText multi-host Gemma SFT | [train_19.md](markdown/training_framework_links/train_19_maxtext_gemma_sft_multihost.md) | [Google Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext) | Multi-host v6e/GKE recipe for Gemma 4 31B SFT with MaxText, Cluster Toolkit, UltraChat. |
| `train_20` | Fine-tune an LLM on GKE with JAX | [train_20.md](markdown/training_framework_links/train_20_gke_train_llm_jax.md) | [Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-llm-tpus-gke-jax) | Introductory distributed Gemma fine-tuning tutorial on TPUs using JAX. |
| `train_21` | Train with JAX, Ray Train, and TPU Trillium on GKE | [train_21.md](markdown/training_framework_links/train_21_gke_ray_train_trillium.md) | [Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu) | Distributed training across TPU hosts using Ray Train and JAX. |
| `train_22` | MaxDiffusion | [train_22.md](markdown/training_framework_links/train_22_maxdiffusion.md) | [GitHub](https://github.com/google/maxdiffusion) | JAX/XLA diffusion reference implementations covering SD, SDXL, Flux, DreamBooth, Wan. |

### 4. Inference Deployment Links (18 Resources)
| ID | Resource Name | Local Markdown | Source URL | Description |
| :--- | :--- | :--- | :--- | :--- |
| `infer_01` | vLLM-TorchTPU official repository | [infer_01.md](markdown/inference_deployment_links/infer_01_vllm_torchtpu_repo.md) | [GitHub](https://github.com/vllm-project/vllm-torchtpu) | Official PyTorch-native TPU backend for vLLM; separate from vllm-tpu (JAX-native). |
| `infer_02` | vLLM-TorchTPU quickstart | [infer_02.md](markdown/inference_deployment_links/infer_02_vllm_torchtpu_quickstart.md) | [ReadTheDocs](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/) | Ready-to-run online serving, offline inference, and multimodal examples. |
| `infer_03` | vLLM-TorchTPU installation | [infer_03.md](markdown/inference_deployment_links/infer_03_vllm_torchtpu_installation.md) | [ReadTheDocs](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/) | Install the PyTorch-native vLLM TPU plugin; requires Python 3.12. |
| `infer_04` | vLLM-TorchTPU Cloud TPU setup | [infer_04.md](markdown/inference_deployment_links/infer_04_vllm_torchtpu_setup.md) | [ReadTheDocs](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/) | Official provisioning and hardware guidance for the vLLM-TorchTPU stack. |
| `infer_05` | vLLM-TorchTPU supported models and features | [infer_05.md](markdown/inference_deployment_links/infer_05_vllm_torchtpu_supported_models.md) | [ReadTheDocs](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/) | Check validated checkpoints, attention backends, quantization, and serving features. |
| `infer_06` | vLLM-TorchTPU Docker guide | [infer_06.md](markdown/inference_deployment_links/infer_06_vllm_torchtpu_docker.md) | [ReadTheDocs](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/) | Container images and build targets for TPU inference; runtime vs CI images. |
| `infer_07` | vLLM-TorchTPU compilation cache | [infer_07.md](markdown/inference_deployment_links/infer_07_vllm_torchtpu_compilation_cache.md) | [ReadTheDocs](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/) | Persist compiled artifacts to reduce repeated startup compilation. |
| `infer_08` | Llama 3.2 1B Instruct model and access | [infer_08.md](markdown/inference_deployment_links/infer_08_llama_32_1b_instruct.md) | [Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | Model card, license, and gated-access page for the quickstart serving model. |
| `infer_09` | Hugging Face CLI authentication | [infer_09.md](markdown/inference_deployment_links/infer_09_hf_cli_auth.md) | [Hugging Face](https://huggingface.co/docs/huggingface_hub/guides/cli) | Authenticate to download private or gated model weights before starting TPU serving. |
| `infer_10` | SGLang-TorchTPU official repository | [infer_10.md](markdown/inference_deployment_links/infer_10_sglang_torchtpu_repo.md) | [GitHub](https://github.com/sgl-project/sglang-torchtpu) | Official SGLang PyTorch-native TPU backend, complementary to vLLM-TorchTPU. |
| `infer_11` | Run inference on Cloud TPU | [infer_11.md](markdown/inference_deployment_links/infer_11_tpu_inference_cloud_docs.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/tpu-inference) | Official overview of TPU inference, vLLM integration, prerequisites, and examples. |
| `infer_12` | vLLM TPU quickstart | [infer_12.md](markdown/inference_deployment_links/infer_12_vllm_tpu_quickstart.md) | [vLLM Docs](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/) | Install the TPU-compatible vLLM stack and start an inference API server. |
| `infer_13` | vLLM TPU Installation and container guide | [infer_13.md](markdown/inference_deployment_links/infer_13_vllm_tpu_installation.md) | [vLLM Docs](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/) | Official installation reference for the JAX-native vLLM TPU stack. |
| `infer_14` | vLLM TPU recommended models | [infer_14.md](markdown/inference_deployment_links/infer_14_vllm_tpu_recommended_models.md) | [vLLM Docs](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/) | Model and feature validation matrix; check release and nightly support. |
| `infer_15` | Serve an LLM on GKE with vLLM and TPU Trillium | [infer_15.md](markdown/inference_deployment_links/infer_15_gke_serve_vllm_trillium.md) | [Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu) | End-to-end Kubernetes deployment tutorial for vLLM on TPU v6e. |
| `infer_16` | Google Kubernetes Engine Ray + vLLM TPU Qwen3 sample | [infer_16.md](markdown/inference_deployment_links/infer_16_gke_ray_vllm_qwen3.md) | [GitHub](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve) | Official GKE sample using Ray Serve and vLLM-TPU on a TPU v6e slice. |
| `infer_17` | GKE online inference TPU reference implementation | [infer_17.md](markdown/inference_deployment_links/infer_17_gke_online_inference_ref_arch.md) | [GitHub](https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/docs/platforms/gke/base/use-cases/inference-ref-arch/online-inference-tpu/vllm-with-hf-model.md) | GCP GKE inference reference architecture for online vLLM serving on TPUs. |
| `infer_18` | Serve LLMs with KubeRay and TPUs on GKE | [infer_18.md](markdown/inference_deployment_links/infer_18_gke_serve_kuberay_tpus.md) | [Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray) | Deploy vLLM-based serving using the Ray Operator and supported TPU configurations. |

### 5. NVIDIA to TPU Migration Docs (18 Resources)
| ID | Resource Name | Local Markdown | Source URL | Description |
| :--- | :--- | :--- | :--- | :--- |
| `mig_01` | PyTorch on Cloud TPU | [mig_01.md](markdown/nvidia_to_tpu_migration_docs/mig_01_pytorch_on_tpu_overview.md) | [Google Cloud](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) | Official overview of current PyTorch TPU stack, TorchTPU, and migration from PyTorch/XLA. |
| `mig_02` | TorchTPU documentation hub | [mig_02.md](markdown/nvidia_to_tpu_migration_docs/mig_02_torchtpu_docs_hub.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/) | Index of native PyTorch TPU quickstarts, migration APIs, and performance docs. |
| `mig_03` | TorchTPU VM quickstart | [mig_03.md](markdown/nvidia_to_tpu_migration_docs/mig_03_torchtpu_vm_quickstart.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/) | Create Python env on TPU VM, install TorchTPU, and run first tensor ops. |
| `mig_04` | TorchTPU CUDA-to-TPU API reference | [mig_04.md](markdown/nvidia_to_tpu_migration_docs/mig_04_torchtpu_cuda_api_ref.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/api_reference/) | Mappings from torch.cuda to device-agnostic APIs, runtime, and precision APIs. |
| `mig_05` | TorchTPU FAQ | [mig_05.md](markdown/nvidia_to_tpu_migration_docs/mig_05_torchtpu_faq.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/faq/) | Migration questions, CUDA versus TPU execution, and replacement of PyTorch/XLA. |
| `mig_06` | TorchTPU supported features and roadmap | [mig_06.md](markdown/nvidia_to_tpu_migration_docs/mig_06_torchtpu_feature_set.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/feature_set/) | Check validated vs experimental hardware, operators, models, kernels, and distributed. |
| `mig_07` | TorchTPU repository (official installation) | [mig_07.md](markdown/nvidia_to_tpu_migration_docs/mig_07_torchtpu_repo.md) | [GitHub](https://github.com/google-pytorch/torch_tpu) | Official source, supported Python versions, released packages, and installation. |
| `mig_08` | TorchTPU introduction and feature set | [mig_08.md](markdown/nvidia_to_tpu_migration_docs/mig_08_torchtpu_intro.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/) | Native PyTorch TPU concepts, migration changes, execution modes, and compilation. |
| `mig_09` | TorchTPU compilation and dynamic shapes | [mig_09.md](markdown/nvidia_to_tpu_migration_docs/mig_09_torchtpu_dynamic_shapes.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/) | Static and bounded dynamic shapes, recompilation behavior, and current limitations. |
| `mig_10` | TorchTPU distributed support | [mig_10.md](markdown/nvidia_to_tpu_migration_docs/mig_10_torchtpu_distributed_support.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/distributed_support/) | Use torch.distributed with tpu_dist, DDP, FSDP, and DTensor across TPU devices. |
| `mig_11` | TorchTPU custom kernels and API reference | [mig_11.md](markdown/nvidia_to_tpu_migration_docs/mig_11_torchtpu_custom_kernels.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/custom_kernels/) | Integrate prebuilt Tokamax kernels, custom Pallas kernels, or experimental Helion kernels. |
| `mig_12` | TorchTPU numerical precision | [mig_12.md](markdown/nvidia_to_tpu_migration_docs/mig_12_torchtpu_numerical_precision.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/numerical_precision/) | Numerical differences from CUDA and configuring TPU matrix-multiplication precision. |
| `mig_13` | TorchTPU memory model | [mig_13.md](markdown/nvidia_to_tpu_migration_docs/mig_13_torchtpu_memory_model.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/) | Tensor views, layout transformations, and view operation performance differences. |
| `mig_14` | Pallas TPU kernel quickstart | [mig_14.md](markdown/nvidia_to_tpu_migration_docs/mig_14_pallas_tpu_quickstart.md) | [JAX Docs](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html) | Write custom TPU kernels using Pallas; relevant when replacing CUDA-specific kernels. |
| `mig_15` | Tokamax TPU kernel library | [mig_15.md](markdown/nvidia_to_tpu_migration_docs/mig_15_tokamax_kernel_lib.md) | [GitHub](https://github.com/openxla/tokamax) | Prebuilt high-performance TPU kernels with PyTorch interoperability. |
| `mig_16` | TorchTPU performance profiling with XProf | [mig_16.md](markdown/nvidia_to_tpu_migration_docs/mig_16_torchtpu_xprof.md) | [TorchTPU Docs](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/) | Capture and inspect TPU execution traces; profiler prerequisites. |
| `mig_17` | TPU Agent Suite installation | [mig_17.md](markdown/nvidia_to_tpu_migration_docs/mig_17_tpu_agent_suite.md) | [GitHub](https://github.com/google-pytorch/tpu-agent-suite/blob/main/docs/install.md) | Experimental assisted onboarding and diagnostics; documents environment setup. |
| `mig_18` | TorchTPU engineering overview | [mig_18.md](markdown/nvidia_to_tpu_migration_docs/mig_18_torchtpu_engineering_overview.md) | [Google Blog](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/) | Explains native PyTorch TPU execution and engineering choices for workload portability. |

---

## Crawler & Data Pipeline Architecture

This documentation dataset was extracted and verified using modern scraping frameworks:
- **Crawl4AI**: High-performance asynchronous DOM rendering via Playwright, ensuring full client-side JavaScript execution, accurate tables, and code fences.
- **Scrapling**: Resilient HTTP extraction and DOM traversal with stealth headers.
- **ScrapeGraphAI**: Structured graph extraction, semantic triple derivation, and knowledge assertion linking.

---

## License & Attribution

All crawled documentation, code snippets, and API references are the property of their respective authors (Google Cloud, PyTorch Foundation, Hugging Face, vLLM Project, SGLang, and Keras).
