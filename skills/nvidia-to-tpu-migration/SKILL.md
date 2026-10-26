---
name: nvidia-to-tpu-migration
description: Expert AI Agent Skill for migrating NVIDIA CUDA PyTorch workloads to Cloud TPUs using TorchTPU, Pallas, Tokamax, and tpu_dist.
---

# NVIDIA CUDA to Cloud TPU Migration Skill

This skill guides engineers through porting PyTorch codebases written for NVIDIA GPUs (CUDA) to native Cloud TPUs using Google's **TorchTPU** stack.

---

## 1. Migration Overview

Google now labels **PyTorch/XLA deprecated** in favor of **TorchTPU**. TorchTPU provides native PyTorch device support (`device="tpu"`), eliminates lazy tensor graph capture overhead, and brings direct parity with CUDA programming models.

### Golden Rules of TPU Migration
1. **Never Just String-Replace `cuda` with `tpu`**: Look out for custom CUDA kernels (`.cu`), unsupported Triton kernels, in-place view operations, and NCCL primitives.
2. **Eager Mode First, Compile Second**: Ensure the forward and backward passes execute with correct numerical outputs in eager mode before invoking `torch.compile(..., backend="openxla")`.
3. **Use Bounded Dynamic Shapes**: Avoid excessive dynamic shapes that trigger continuous recompilation loops. Pad input tokens to fixed bucket lengths (e.g., 512, 1024, 2048, 4096).
4. **Use `bfloat16` Everywhere**: TPU Matrix Units (MXUs) natively perform systolic matrix multiplication in `bfloat16`. FP16 requires dynamic loss scaling and is prone to underflow.

---

## 2. Step-by-Step Code Transformation

### Step 1: Device Assignment & Model Transfer
```python
# Before (NVIDIA CUDA):
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MyModel().to(device)
inputs = inputs.cuda()

# After (Native TorchTPU):
import torch
import torch_tpu
device = torch.device("tpu" if torch.tpu.is_available() else "cpu")
model = MyModel().to(device)
inputs = inputs.to("tpu")
```

### Step 2: Distributed Backend Replacement
```python
# Before (NCCL for CUDA):
import torch.distributed as dist
dist.init_process_group(backend="nccl")

# After (tpu_dist for TPU):
import torch.distributed as dist
import torch_tpu
dist.init_process_group(backend="tpu_dist")
```

### Step 3: Numerical Precision
```python
# Configure float32 matmul precision to leverage MXU hardware:
import torch
torch.tpu.set_float32_matmul_precision("high")

# Prefer bfloat16 autocast or model conversion:
model = model.to(torch.bfloat16)
```

---

## 3. Handling Custom Kernels

If your codebase relies on custom CUDA C++ or Triton kernels:

1. **Prebuilt Optimized Kernels**: Check [Tokamax](https://github.com/openxla/tokamax) for drop-in TPU implementations of FlashAttention, RMSNorm, RoPE, and SwiGLU.
2. **Pallas Kernels**: For custom operators, implement kernels using JAX Pallas (`jax.experimental.pallas.tpu`). Pallas allows low-level control over TPU Vector and Matrix Units.
3. **Helion**: For experimental kernel synthesis on Ironwood (TPU7x).

---

## 4. Compilation Cache Configuration

Prevent recompilation on node restarts by setting persistent cache paths:

```bash
export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/mnt/persistent_disk/tpu_cache/tier3"
```
