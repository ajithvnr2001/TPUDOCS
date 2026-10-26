---
name: tpu-training-workflows
description: Expert AI Agent Skill for training, post-training, and fine-tuning LLMs and diffusion models on Cloud TPUs with MaxText, TorchTitan, Ray Train, JAX sharding, and Keras 3.
---

# TPU Distributed Training Workflows Skill

This skill provides production training blueprints for distributed training on Google Cloud TPUs, covering both JAX-native stacks (MaxText, MaxDiffusion) and PyTorch-native stacks (TorchTitan, Ray + TorchTPU + FSDP2).

---

## 1. Choosing Your Training Stack

| Framework | Primary Framework | Key Codebases | Scale / Best Use Case |
| :--- | :--- | :--- | :--- |
| **MaxText** | JAX / XLA | [google/maxtext](https://github.com/google/maxtext) | Google AI Hypercomputer flagship LLM training (Gemma 4, Llama, DeepSeek, Qwen) with SFT, GRPO, and GSPO. |
| **TorchTitan** | Native PyTorch (`torch_tpu`) | [google-pytorch/torchtitan](https://github.com/google-pytorch/torchtitan) | Native PyTorch 1D/2D/3D parallelism (FSDP2, Tensor Parallel, Pipeline Parallel) on TPU v6e and TPU7x. |
| **Ray Train + TorchTPU** | PyTorch + Ray Operator | GKE Ray Operator | Distributed SFT and full fine-tuning across Kubernetes-managed multi-host slices with FSDP2. |
| **MaxDiffusion** | JAX / XLA | [google/maxdiffusion](https://github.com/google/maxdiffusion) | Stable Diffusion, SDXL, Flux, DreamBooth, and Wan video generation on TPUs. |
| **Keras 3 with JAX** | Keras / JAX | `keras.distribution` | High-level data and model parallel distribution across TPU Pod slices. |

---

## 2. JAX / MaxText LLM Supervised Fine-Tuning (SFT)

### Single-Host Recipe (e.g. TPU v6e-8)
```bash
# Clone MaxText
git clone https://github.com/google/maxtext.git
cd maxtext

# Run setup script for TPU dependencies (JAX, jaxlib, libtpu)
bash src/dependencies/scripts/setup.sh

# Run Gemma SFT with synthetic or UltraChat dataset
python3 -m MaxText.train MaxText/configs/base.yml \
  model_name=gemma-7b \
  steps=100 \
  per_device_batch_size=2 \
  max_target_length=2048 \
  base_output_directory=gs://my-tpu-checkpoints/maxtext/
```

### Multi-Host Scaling with Cluster Toolkit
For multi-host TPU slices (e.g. v6e-256):
- Deploy via GKE using the AI Hypercomputer recipe:
  `ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext`
- Automatic checkpoint export back to Hugging Face format for downstream serving.

---

## 3. PyTorch-Native Training with TorchTitan

TorchTitan is PyTorch's clean, minimal pre-training repository, officially adapted for Cloud TPUs via `torch_tpu`:

```bash
# Install TorchTitan and dependencies
git clone https://github.com/google-pytorch/torchtitan.git
cd torchtitan

# Configure environment
export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/data/tpu_cache/tier3"

# Launch 8-device training run
torchrun --nproc_per_node=8 train.py --job.config_file experiments/tpu/llama3_8b.toml
```

---

## 4. Distributed PyTorch on GKE with Ray & FSDP2

For teams orchestrating jobs on Kubernetes:
1. Spin up a GKE cluster with TPU node pools (`--accelerator=type=tpu-v6e-slice,count=16`).
2. Deploy the KubeRay Operator.
3. Submit Ray jobs configuring:
   ```python
   import ray
   import torch.distributed as dist
   
   @ray.remote(resources={"TPU": 4})
   def train_worker(rank, world_size):
       dist.init_process_group(
           backend="tpu_dist",
           init_method="env://",
           world_size=world_size,
           rank=rank
       )
       # Execute training loop with PyTorch FSDP2
   ```
