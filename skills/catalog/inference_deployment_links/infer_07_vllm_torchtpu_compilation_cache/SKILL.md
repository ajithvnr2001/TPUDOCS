---
name: infer-07-vllm-torchtpu-compilation-cache
description: "vLLM-TorchTPU compilation cache \u2014 Persist compiled artifacts and reduce repeated startup compilation."
source_url: "https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/"
category: "inference_deployment_links"
---

# Agent Skill: vLLM-TorchTPU compilation cache

- **Official Source**: [https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/)
- **Category**: `inference_deployment_links`
- **Resource ID**: `infer_07_vllm_torchtpu_compilation_cache`
- **When to Activate**: Persist compiled artifacts and reduce repeated startup compilation.

## Document Sections

- **TorchTPU Compilation Cache**
  - **Cache Architecture & Environment Variables**
  - **Compilation Debugging & Telemetry**
    - **`VLLM_XLA_CHECK_RECOMPILATION` (Runtime Recompilation Detector)**

## Key CLI Commands & Invocations

```bash
export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/path/to/persistent_cache"
```

## Key Environment Variables

- `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`

## Complete Technical Reference

# TorchTPU Compilation Cache
To enable persistent native C++ compilation caching in `vllm-torchtpu`, set `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` to a persistent directory path:

```
export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/path/to/persistent_cache"

```

## Cache Architecture & Environment Variables
`vllm-torchtpu` separates Python-level framework tracing cache from native C++ compiled binary executables:
  1. **`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`**(C++ Native PJRT Binaries):
     * **Purpose** : Controls the persistent root directory for native C++ PJRT compiled binary executables (`.bin` files).
     * **Scope** : Native `torch_tpu` C++ backend. This is the primary driver variable required to enable persistent executable binary caching on TPU.
  2. **`VLLM_CACHE_ROOT`**(vLLM Python-Level Framework Artifacts):
     * **Purpose** : Controls the root directory for vLLM Python-level framework tracing artifacts.
     * **Scope** : Stores PyTorch Dynamo FX graph bytecode, Guard expressions, AOTAutograd tracing artifacts (`torch_compile_cache/torch_aot_compile`), and `TpuCompilerAdaptor` metadata pickle handles (`artifact_compile_range_*`).
     * **Note** : `VLLM_CACHE_ROOT` manages Python framework artifacts and is completely independent of the C++ PJRT compiled binary executables managed by `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`.


## Compilation Debugging & Telemetry
###  `VLLM_XLA_CHECK_RECOMPILATION` (Runtime Recompilation Detector)
  * **Default** : `0` (Disabled)
  * **Purpose** : Detects unexpected compilation during serving — such as an input shape, dtype, or code path that AOT warmup never precompiled and that stalls the engine loop on a cache miss.
  * **How It Works** : Queries `torch.tpu._get_cache_stats()` and advances the cached graph count watermark at each checkpoint (including every AOT precompile bucket and runtime forward step), logging newly compiled graphs whenever a cache miss occurs.
  * **Overhead** : `0` (zero runtime overhead) vs `1` (queries cache stats and logs per step).
  * **Recommendation** :
    * `1`: Enable in CI and test pipelines to catch compilation leaks and un-warmed code paths.
    * `0`: Keep disabled in production and benchmarking for maximum throughput.
