# Complete Reference Compendium: `training_framework_links` (22 Resources)

## `train_01_torchtpu_gke_quickstart` — TorchTPU GKE quickstart
- **URL**: https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/
- **Description**: Deploy TorchTPU containers on GKE for single-device, single-host, or multi-host workloads.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_01_torchtpu_gke_quickstart/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_01_torchtpu_gke_quickstart.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_01_torchtpu_gke_quickstart.md`

### Sections (19) & Code Examples (19)
- Get started with TorchTPU on GKE
- Before you begin
- Prerequisites
- Set environment variables
- Authenticate and get cluster credentials
- Submit workloads with kubectl
- Run a single-device workload (one TensorCore of a 4-chip host)
- 1. Create a tensor on the CPU
- 2. Move it to the TPU
- OR
- 3. Create a tensor directly on the TPU
- Run distributed workloads on GKE
- Single host, multiple chips (4 chips / 8 devices on one host)
- Detect and export TPU configuration dynamically.
- Multiple hosts (64 chips / 128 devices across 16 hosts)

## `train_02_tf_distribute_tpustrategy` — TensorFlow TPUStrategy API
- **URL**: https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy
- **Description**: API reference for synchronous TensorFlow training on TPUs and TPU Pods.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_02_tf_distribute_tpustrategy/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_02_tf_distribute_tpustrategy.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_02_tf_distribute_tpustrategy.md`

### Sections (40) & Code Examples (35)
- tf.distribute.TPUStrategy
- Used in the notebooks
- Args
- Attributes
- Methods
- `distribute_datasets_from_function`
- `experimental_assign_to_logical_device`
- Initializing TPU system with 2 logical devices and 4 replicas.
- `experimental_distribute_dataset`
- Passing the devices is optional.
- Create a dataset
- Distribute that dataset
- Iterate over the `tf.distribute.DistributedDataset`
- `experimental_distribute_values_from_function`
- Example usage:

## `train_03_tpu7x_training` — Train a model on TPU7x with MaxText or TorchTitan
- **URL**: https://docs.cloud.google.com/tpu/docs/tpu7x-training
- **Description**: Provision Ironwood training infrastructure and use JAX or PyTorch training recipes.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_03_tpu7x_training/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_03_tpu7x_training.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_03_tpu7x_training.md`

### Sections (11) & Code Examples (5)
- Train a model using TPU7x (Ironwood)
- Before you begin
- Deploy the TPU7x (Ironwood) cluster
- Deploy a training workload with MaxText
- Build and upload the MaxText Docker image
- Clone MaxText
- Build the Docker image
- Define the MaxText training command
- Submit the MaxText training job
- Deploy a training workload with TorchTitan
- What's next

## `train_04_gke_ray_torchtpu_finetune` — Fine-tune models with Ray and TorchTPU on GKE
- **URL**: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-models-tpu-ray-torchtpu
- **Description**: Distributed PyTorch fine-tuning across TPU hosts using Ray and FSDP2.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_04_gke_ray_torchtpu_finetune/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_04_gke_ray_torchtpu_finetune.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_04_gke_ray_torchtpu_finetune.md`

### Sections (41) & Code Examples (41)
- Fine-tune models on multi-host TPUs with Ray and TorchTPU
- Background
- TPUs
- TorchTPU
- KubeRay and Ray on TPUs
- Objectives
- Costs
- Before you begin
- Prepare your environment
- Create a GKE cluster
- Autopilot
- Standard
- Trillium (v6e)
- Ironwood (TPU7x)
- Build the container image

## `train_05_jax_installation` — JAX installation
- **URL**: https://docs.jax.dev/en/latest/installation.html
- **Description**: Official accelerator-specific installation, including jax[tpu] for Cloud TPU VMs.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_05_jax_installation/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_05_jax_installation.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_05_jax_installation.md`

### Sections (39) & Code Examples (27)
- Installation
- Supported platforms
- CPU
- pip installation: CPU
- NVIDIA GPU
- pip installation: NVIDIA GPU (CUDA, installed via pip, easier)
- NVIDIA CUDA 13 installation
- Note: wheels only available on linux.
- Alternatively, for CUDA 12, use
- pip install --upgrade "jax[cuda12]"
- pip installation: NVIDIA GPU (CUDA, installed locally, harder)
- Installs the wheel compatible with NVIDIA CUDA 13 and cuDNN 9.12 or newer.
- Note: wheels only available on linux.
- Installs the wheel compatible with NVIDIA CUDA 12 and cuDNN 9.10 or newer.
- Note: wheels only available on linux.

## `train_06_thinking_in_jax` — Thinking in JAX
- **URL**: https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html
- **Description**: JAX programming concepts for portable CPU, GPU, and TPU computation.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_06_thinking_in_jax/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_06_thinking_in_jax.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_06_thinking_in_jax.md`

### Sections (15) & Code Examples (60)
- Quickstart: How to think in JAX
- Installation
- JAX vs. NumPy
- NumPy: mutable arrays
- JAX: immutable arrays
- JAX arrays (`jax.Array`)
- Array creation
- Array devices and sharding
- Just-in-time compilation with `jax.jit`
- Taking derivatives with `jax.grad`
- Auto-vectorization with `jax.vmap`
- Pseudorandom numbers
- Debugging
- `jax.debug.print`
- Debugging flags

## `train_07_jax_ai_stack` — Building production AI on Cloud TPUs with JAX
- **URL**: https://docs.cloud.google.com/tpu/docs/jax-ai-stack
- **Description**: Overview of the JAX AI stack and production-oriented choices; identifies MaxText for LLMs and MaxDiffusion for diffusion, alongside Flax, Optax, Orbax, Grain, Qwix, and Tunix.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_07_jax_ai_stack/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_07_jax_ai_stack.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_07_jax_ai_stack.md`

### Sections (37) & Code Examples (2)
- Building production AI on Cloud TPUs with JAX
- The architectural imperative: performance beyond frameworks
- The core JAX AI stack
- JAX: A foundation for composable, high performance program transformation
- Flax: Flexible neural network authoring
- Key strengths:
- Optax: Composable gradient processing and optimization strategies
- Motivation
- Design
- Optax implementation of a RMSProp optimizer with a custom learning rate
- schedule, gradient clipping and gradient accumulation.
- The same thing, in PyTorch
- Key strengths
- Orbax / TensorStore - Large scale distributed checkpointing
- Key strengths:

## `train_08_tensorflow_tpu_guide` — TensorFlow TPU guide
- **URL**: https://www.tensorflow.org/guide/tpu
- **Description**: Initialize TPU hardware and use tf.distribute.TPUStrategy for TensorFlow/Keras workloads.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_08_tensorflow_tpu_guide/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_08_tensorflow_tpu_guide.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_08_tensorflow_tpu_guide.md`

### Sections (19) & Code Examples (22)
- Use TPUs
- Setup
- TPU initialization
- This is the TPU initialization code that has to be at the beginning.
- Manual device placement
- Distribution strategies
- Classification on TPUs
- Define a Keras model
- Load the dataset
- Train the model using Keras high-level APIs
- Train the model using a custom training loop
- Create the model, optimizer and metrics inside the `tf.distribute.Strategy`
- scope, so that the variables can be mirrored on each device.
- Calculate per replica batch size, and distribute the `tf.data.Dataset`s
- on each TPU worker.

## `train_09_torchtitan_tpu_getting_started` — TorchTitan on TPU getting started
- **URL**: https://github.com/google-pytorch/torchtitan/blob/main/torchtitan/experiments/tpu/README.md
- **Description**: TPU-specific setup and training recipes for TorchTitan.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_09_torchtitan_tpu_getting_started/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_09_torchtitan_tpu_getting_started.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_09_torchtitan_tpu_getting_started.md`

### Sections (50) & Code Examples (33)
- TorchTitan on TPU Getting Started
- TorchTPU Support for TorchTitan
- Before you begin
- Single-host model training on a TPU VM
- Prerequisites
- Create a TPU VM
- Install TorchTitan and TorchTPU
- Option A: TorchTPU release with PyTorch 2.15 (recommended)
- Option B: Build TorchTPU from source for the PyTorch nightly (for development)
- Run a TorchTitan training job
- Multi-host model training on GKE
- Provision Cloud TPU resources
- Install Cluster Toolkit and its dependencies
- Restart the terminal and reactivate the virtual environment after running this command.
- Create a single-slice cluster

## `train_10_hf_keras_tf_tpu_guide` — Hugging Face Keras/TF TPU guide
- **URL**: https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf
- **Description**: Usable Keras sequence-classification example: initialize TPUClusterResolver, TPUStrategy, load/tokenize data, create the model inside strategy.scope(), and call model.fit().
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_10_hf_keras_tf_tpu_guide/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_10_hf_keras_tf_tpu_guide.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_10_hf_keras_tf_tpu_guide.md`

### Sections (11) & Code Examples (4)
- Training on TPU with TensorFlow
- What is a TPU?
- What kinds of TPU are available?
- What sizes of TPU are available?
- I keep hearing about this XLA thing. What’s XLA, and how does it relate to TPUs?
- How do I make my model XLA compatible?
- XLA Rule #1: Your code cannot have “data-dependent conditionals”
- XLA Rule #2: Your code cannot have “data-dependent shapes”
- XLA Rule #3: XLA will need to recompile your model for every different input shape it sees
- How do I actually train my model on TPU?
- Summary

## `train_11_mnist_tf2_keras` — Cloud TPU MNIST with TensorFlow 2.x/Keras
- **URL**: https://cloud.google.com/tpu/docs/tutorials/mnist-2.x
- **Description**: Official end-to-end TensorFlow/Keras training recipe using TPU distribution; useful as a small migration smoke test before a larger workload.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_11_mnist_tf2_keras/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_11_mnist_tf2_keras.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_11_mnist_tf2_keras.md`

### Sections (41) & Code Examples (4)
- Cloud TPU MNIST with TensorFlow 2.x and Keras (`mnist-2.x`)
- 1. Overview & Architecture
- 2. Provision a Cloud TPU VM & Install TensorFlow
- Create a TPU VM using Compute Engine
- SSH into the TPU VM
- 3. Initialize `TPUClusterResolver` and `TPUStrategy`
- 4. Official `tensorflow/tpu` Keras MNIST Script (`models/experimental/mnist_keras/mnist.py`)
- Copyright 2018 The TensorFlow Authors. All Rights Reserved.
- Licensed under the Apache License, Version 2.0 (the "License");
- you may not use this file except in compliance with the License.
- You may obtain a copy of the License at
- http://www.apache.org/licenses/LICENSE-2.0
- Unless required by applicable law or agreed to in writing, software
- distributed under the License is distributed on an "AS IS" BASIS,
- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

## `train_12_keras_distributed_jax` — Keras distributed training with JAX
- **URL**: https://keras.io/guides/distributed_training_with_jax/
- **Description**: Use JAX sharding to train Keras models across multiple GPUs or TPUs.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_12_keras_distributed_jax/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_12_keras_distributed_jax.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_12_keras_distributed_jax.md`

### Sections (15) & Code Examples (4)
- Multi-GPU distributed training with JAX
- Introduction
- Setup
- Single-host, multi-device synchronous training
- Config
- Initialize all state with .build()
- This is the loss function that will be differentiated.
- Keras provides a pure functional forward pass: model.stateless_call
- Function to compute gradients
- Training step, Keras provides a pure functional optimizer.stateless_apply
- Replicate the model and optimizer variable on all devices
- Data will be split along the batch axis
- Display data sharding
- Custom training loop
- Post-processing model state update to write them back into the model

## `train_13_keras_distribution_guide` — Keras 3 distribution guide
- **URL**: https://keras.io/guides/distribution/
- **Description**: Data and model distribution concepts for multi-device Keras workflows.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_13_keras_distribution_guide/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_13_keras_distribution_guide.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_13_keras_distribution_guide.md`

### Sections (35) & Code Examples (7)
- Distributed training with Keras 3
- Introduction
- How it works
- Setup
- The distribution API is only implemented for the JAX backend for now.
- `DeviceMesh` and `TensorLayout`
- Retrieve the local available gpu devices.
- Define a 2x4 device mesh with data and model parallel axes
- A 2D layout, which describes how a tensor is distributed across the
- mesh. The layout can be visualized as a 2D grid with "model" as rows and
- "data" as columns, and it is a [4, 2] grid when it mapped to the physical
- devices on the mesh.
- A 4D layout which could be used for data parallel of a image input.
- Distribution
- DataParallel

## `train_14_keras_sparsecore_embedding` — Keras SparseCore embedding example
- **URL**: https://keras.io/keras_rs/examples/distributed_embedding_jax/
- **Description**: Distributed recommendation-model embeddings using JAX and TPU SparseCore.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_14_keras_sparsecore_embedding/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_14_keras_sparsecore_embedding.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_14_keras_sparsecore_embedding.md`

### Sections (11) & Code Examples (16)
- DistributedEmbedding using TPU SparseCore and JAX
- Introduction
- Dataset distribution
- Preparing the dataset
- Ratings data.
- Features of all the available movies.
- Configuring DistributedEmbedding
- Configuring tables
- Configuring features
- Defining the Model
- Fitting and evaluating

## `train_15_hf_training_guide` — Hugging Face fine-tuning guide
- **URL**: https://huggingface.co/docs/transformers/training
- **Description**: General model, dataset, Trainer, and checkpoint workflow; not a TPU runtime setup guide.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_15_hf_training_guide/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_15_hf_training_guide.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_15_hf_training_guide.md`

### Sections (7) & Code Examples (6)
- Fine-tune a Pretrained Model (Hugging Face Transformers)
- Fine-tuning
- Tokenization
- Loading a model
- Training configuration
- Training
- Next steps

## `train_16_maxtext` — MaxText
- **URL**: https://github.com/google/maxtext
- **Description**: Google AI-Hypercomputer JAX/XLA LLM training and post-training codebase for Cloud TPUs and GPUs; supports models such as Gemma, Llama, DeepSeek, Qwen, and Mistral plus SFT/GRPO/GSPO.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_16_maxtext/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_16_maxtext.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_16_maxtext.md`

### Sections (10) & Code Examples (0)
- MaxText
- Installation
- Decoupled mode
- 🔥 Latest news 🔥
- Use cases
- Pre-training
- Post-training
- Model library
- Get involved
- License

## `train_17_maxtext_setup_sh` — MaxText TPU setup script
- **URL**: https://github.com/google/maxtext/blob/main/src/dependencies/scripts/setup.sh
- **Description**: Concrete MaxText dependency setup for TPU, including stable/nightly JAX, jaxlib, and libtpu selection.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_17_maxtext_setup_sh/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_17_maxtext_setup_sh.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_17_maxtext_setup_sh.md`

### Sections (62) & Code Examples (1)
- MaxText TPU Setup Script (`src/dependencies/scripts/setup.sh`)
- Copyright 2023–2025 Google LLC
- Licensed under the Apache License, Version 2.0 (the "License");
- you may not use this file except in compliance with the License.
- You may obtain a copy of the License at
- https://www.apache.org/licenses/LICENSE-2.0
- Unless required by applicable law or agreed to in writing, software
- distributed under the License is distributed on an "AS IS" BASIS,
- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- See the License for the specific language governing permissions and
- limitations under the License.
- ==================================
- TPU EXAMPLES
- ==================================
- Install dependencies in dependencies/generated_requirements/tpu-requirements.txt

## `train_18_maxtext_gemma_sft_single_host` — MaxText single-host Gemma supervised fine-tuning
- **URL**: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext
- **Description**: Fine-tune Gemma on a v6e-8 TPU VM and convert checkpoints between Hugging Face and MaxText.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_18_maxtext_gemma_sft_single_host/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_18_maxtext_gemma_sft_single_host.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_18_maxtext_gemma_sft_single_host.md`

### Sections (18) & Code Examples (17)
- Run supervised fine-tuning on a TPU VM by using MaxText
- Workload summary
- Objectives
- Costs
- Before you begin
- Set up the environment
- Create your Cloud TPU VM
- Install MaxText
- Convert the model to MaxText format
- Start the training workload
- -- MaxText configuration --
- -- Dataset configuration --
- Convert the trained model back into Hugging Face format
- Clean up
- Delete your TPU VM instance

## `train_19_maxtext_gemma_sft_multihost` — MaxText multi-host Gemma SFT
- **URL**: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext
- **Description**: Multi-host v6e/GKE recipe for Gemma 4 31B SFT with MaxText, Cluster Toolkit, UltraChat, and export back to Hugging Face format.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_19_maxtext_gemma_sft_multihost/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_19_maxtext_gemma_sft_multihost.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_19_maxtext_gemma_sft_multihost.md`

### Sections (27) & Code Examples (18)
- Run SFT for Gemma 4 31B on multi-host TPU v6e
- Workload summary
- Objectives
- Costs
- Before you begin
- Set up your environment variables
- Install Cluster Toolkit dependencies
- Install Cluster Toolkit
- Authenticate your environment
- Create your Cluster Toolkit cluster
- Grant the GKE Node Pool Service Account storage.admin access for checkpoint writes
- Change n2-standard-8 to e2-standard-8 to avoid GCE_STOCKOUT in some regions
- Pin system node pool to a single zone to avoid cross-zone stockouts
- Convert the model to MaxText format
- Configure gcluster Defaults

## `train_20_gke_train_llm_jax` — Fine-tune an LLM on GKE with JAX
- **URL**: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-llm-tpus-gke-jax
- **Description**: Introductory distributed Gemma fine-tuning tutorial on TPUs using JAX; points production LLM fine-tuning to MaxText and diffusion work to MaxDiffusion.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_20_gke_train_llm_jax/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_20_gke_train_llm_jax.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_20_gke_train_llm_jax.md`

### Sections (109) & Code Examples (41)
- Fine-tune a LLM using TPUs on GKE with JAX
- Background
- Gemma
- TPUs
- JAX
- Objectives
- Before you begin
- Check for the roles
- Grant the roles
- Prepare the environment
- Create and configure Google Cloud resources
- Create a GKE cluster
- Autopilot
- Standard
- Install JobSet

## `train_21_gke_ray_train_trillium` — Train with JAX, Ray Train, and TPU Trillium on GKE
- **URL**: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu
- **Description**: Distributed training across TPU hosts using Ray Train and JAX.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_21_gke_ray_train_trillium/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_21_gke_ray_train_trillium.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_21_gke_ray_train_trillium.md`

### Sections (21) & Code Examples (37)
- Train an LLM using JAX, Ray Train, and TPU Trillium on GKE
- Background
- JAX
- MaxText
- TPUs
- KubeRay
- Objectives
- Before you begin
- Prepare your environment
- Create a GKE cluster
- Autopilot
- Standard
- Configure a Cloud Storage bucket and a service account
- Create the training script
- Start from a Ray base image which includes JaxTrainer API.

## `train_22_maxdiffusion` — MaxDiffusion
- **URL**: https://github.com/google/maxdiffusion
- **Description**: JAX/XLA diffusion reference implementations for Cloud TPUs (and GPUs), covering Stable Diffusion, SDXL, Flux, DreamBooth, Wan and other training/inference workloads.
- **Dedicated Skill**: `skills/catalog/training_framework_links/train_22_maxdiffusion/SKILL.md`
- **OKF Entity**: `okf/entities/training_framework_links/train_22_maxdiffusion.okf.json`
- **Markdown Source**: `markdown/training_framework_links/train_22_maxdiffusion.md`

### Sections (23) & Code Examples (61)
- MaxDiffusion (Google AI-Hypercomputer)
- What's new?
- Overview
- Table of Contents
- Getting Started
- Getting Started:
- NVIDIA DGX Spark
- Training
- Inference
- Example: enable MagCache for Wan 2.2 T2V
- Example: enable MagCache for Wan 2.2 I2V
- Ring Attention
- Automatic Tile-Size Search
- Getting Started: Multihost development
- Comparison to Alternatives
