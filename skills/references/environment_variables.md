# Cloud TPU Environment Variables & Optimization Settings

This guide documents the critical runtime environment variables used across **TorchTPU**, **vLLM-TorchTPU**, **JAX**, and **Cloud TPU VM**.

## 1. TorchTPU & PyTorch Native

| Variable | Description | Recommended Setting |
| :--- | :--- | :--- |
| `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` | Path to persistent disk directory storing compiled AOT/Tier-3 kernels. Eliminates repeated compilation on restart. | `/data/tpu_cache/tier3` or persistent SSD |
| `PJRT_DEVICE` | Hardware device target for PJRT runtime. | `TPU` |
| `TPU_VISIBLE_DEVICES` | Comma-separated list of local device indices visible to the process. | `0` or `0,1,2,3` |
| `LIBTPU_INIT_ARGS` | Low-level compiler and runtime flags passed directly to `libtpu.so`. | `--xla_tpu_enable_data_parallel_all_reduce_opt=true` |
| `TORCH_SHOW_CPP_STACKTRACES` | Print native C++ stacktraces during debugging. | `1` (debug only) |

---

## 2. vLLM-TorchTPU Serving

| Variable | Description | Recommended Setting |
| :--- | :--- | :--- |
| `VLLM_CACHE_ROOT` | Root directory for caching downloaded model weights, tokenizers, and configs. | `/data/vllm_cache` |
| `VLLM_ENGINE_ITERATION_TIMEOUT_S` | Watchdog timeout for step execution in vLLM engine. | `60` |
| `HF_HUB_ENABLE_HF_TRANSFER` | Accelerates Hugging Face weight downloads using Rust-based `hf_transfer`. | `1` |
| `HF_TOKEN` | Hugging Face user access token for gated models (e.g. Llama-3.2). | Set before launch |

---

## 3. JAX & XLA Engine

| Variable | Description | Recommended Setting |
| :--- | :--- | :--- |
| `JAX_PLATFORMS` | Explicit platform list for JAX device discovery. | `tpu,cpu` |
| `XLA_FLAGS` | Global XLA compiler flags. | `--xla_gpu_cuda_data_dir=...` (not used on TPU) |
| `JAX_TRACEBACK_FILTERING` | Formatting for JAX compile-time error tracebacks. | `off` |
