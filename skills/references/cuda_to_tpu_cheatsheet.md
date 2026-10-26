# CUDA to TPU API & Workflow Cheatsheet

This reference provides a side-by-side mapping for engineers migrating NVIDIA CUDA PyTorch workloads to Cloud TPUs using **TorchTPU**.

## 1. Device Placement & Initialization

| Feature / Operation | NVIDIA CUDA (`torch.cuda`) | Native TPU (`torch_tpu`) | Notes |
| :--- | :--- | :--- | :--- |
| **Import / Registration** | Default in standard PyTorch | `import torch_tpu` | Registers the `tpu` device in PyTorch runtime |
| **Tensor Placement** | `tensor.cuda()` or `tensor.to("cuda")` | `tensor.to("tpu")` | Allocates tensor directly in HBM on the TPU chip |
| **Device String** | `"cuda:0"` | `"tpu:0"` (or `"tpu"`) | Index targets the local device |
| **Device Count** | `torch.cuda.device_count()` | `torch.tpu.device_count()` | Returns number of TPU chips on the VM (e.g., 4 on v6e-4, 8 on v6e-8) |
| **Current Device** | `torch.cuda.current_device()` | `torch.tpu.current_device()` | Returns index of active device |
| **Set Active Device** | `torch.cuda.set_device(id)` | `torch.tpu.set_device(id)` | Sets current active TPU device |
| **Device Synchronization** | `torch.cuda.synchronize()` | `torch.tpu.synchronize()` | Blocks host until all pending TPU ops complete |
| **Memory Allocated** | `torch.cuda.memory_allocated()` | `torch.tpu.memory_allocated()` | Returns current HBM allocation in bytes |
| **Empty Cache** | `torch.cuda.empty_cache()` | `torch.tpu.empty_cache()` | Clears unused cached allocations |

---

## 2. Distributed Training & Communications

| Component | NVIDIA CUDA Stack | TPU Stack | Notes |
| :--- | :--- | :--- | :--- |
| **Distributed Backend** | `nccl` | `tpu_dist` | Initialize with `torch.distributed.init_process_group("tpu_dist")` |
| **DDP** | `torch.nn.parallel.DistributedDataParallel` | Supported via `tpu_dist` | Fully compatible |
| **FSDP / FSDP2** | PyTorch FSDP2 with NCCL | PyTorch FSDP2 with `tpu_dist` | Recommended for multi-host LLM fine-tuning |
| **Tensor Parallelism** | Megatron-LM / NCCL collectives | Tokamax / DTensor / `tpu_dist` | Low latency ICI interconnect handles cross-chip communication |
| **Host Interconnect** | InfiniBand / RoCE | ICI (Inter-Chip Interconnect) within slice; DCN for multi-host | TPU Pod slices have 2D/3D torus ICI networks |

---

## 3. Compilation & Acceleration

| Feature | NVIDIA CUDA | TPU (TorchTPU / XLA) | Recommendations |
| :--- | :--- | :--- | :--- |
| **`torch.compile` Backend** | `inductor` | `openxla` / `tpu` | Eager mode first for verification, then compile |
| **Compilation Cache** | `TORCHINDUCTOR_CACHE_DIR` | `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` | Essential for avoiding repeated compilation overhead on startup |
| **Dynamic Shapes** | Handled natively by Inductor | Use bounded dynamic shapes; pad sequences where possible | Excessive dynamic shapes trigger repeated compilation |
| **Custom Kernels** | CUDA C++, Triton (`@triton.jit`) | **Pallas** (`jax.experimental.pallas`) or **Tokamax** | Tokamax provides drop-in optimized kernels for PyTorch |

---

## 4. Precision & Numerical Behavior

| Precision | CUDA Usage | TPU Usage | Notes |
| :--- | :--- | :--- | :--- |
| **bfloat16** | `torch.bfloat16` (Ampere+) | `torch.bfloat16` (Native!) | TPU Matrix Units (MXUs) natively execute bfloat16 matrix multiplication |
| **fp16** | Common on NVIDIA V100/T4 | Supported, but `bfloat16` strongly preferred | bfloat16 avoids dynamic loss scaling and underflow |
| **fp32** | Standard single precision | Executed via internal bfloat16 expansions on MXU or Float32 precision flags | Set `torch.tpu.set_float32_matmul_precision("high" | "highest")` |
| **fp8** | Ada / Hopper FP8 (E4M3, E5M2) | Supported on TPU v6e and TPU7x | Use for quantized inference in vLLM-TorchTPU |
