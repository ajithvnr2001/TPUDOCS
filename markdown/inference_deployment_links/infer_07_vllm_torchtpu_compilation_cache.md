---
id: "infer_07_vllm_torchtpu_compilation_cache"
title: "vLLM-TorchTPU compilation cache"
url: "https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/"
category: "Inference deployment links"
description: "Persist compiled artifacts and reduce repeated startup compilation."
crawled_at: "2026-10-26T12:47:33.096242+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#torchtpu-compilation-cache)
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU")
vLLM TorchTPU 
Compilation & Warmup Cache 
[ ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/?q= "Share")
Initializing search 
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU") vLLM TorchTPU 
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
  * [ Home  ](https://vllm-torchtpu.readthedocs.io/en/latest/)
  * Getting Started  Getting Started 
    * [ Cloud TPU Setup  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/)
    * [ Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/)
    * [ Quickstart  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/)
    * [ Docker Guide  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/)
  * User Guide  User Guide 
    * [ Supported Models & Features  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/)
    * [ Parallelism & Scaling  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)
    * [ Multi-Host Serving  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)
    * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/disaggregated_serving/)
    * [ Quantization  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/quantization/)
    * [ Speculative Decoding  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/speculative_decoding/)
    * Compilation & Warmup Cache  [ Compilation & Warmup Cache  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/) Table of contents 
      * [ Cache Architecture & Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#cache-architecture-environment-variables)
      * [ Compilation Debugging & Telemetry  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#compilation-debugging-telemetry)
        * [ VLLM_XLA_CHECK_RECOMPILATION (Runtime Recompilation Detector)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#vllm_xla_check_recompilation-runtime-recompilation-detector)
    * Code Examples  Code Examples 
      * [ Offline Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_inference/)
      * [ Multi Modal Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_lora_inference/)
  * Deployment & Recipes  Deployment & Recipes 
    * [ TPU v7x (Ironwood) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/)
    * [ TPU v6e (Trillium) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v6e_recipes/)
    * [ Kubernetes & GKE  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/kubernetes/)
  * Developer Guide  Developer Guide 
    * [ Contributing  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/contributing/)
    * [ Coding Guidance  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/coding_guidance/)
    * [ Optimization Best Practices  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/optimization_best_practices/)
    * [ TPU Patch Mechanism  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/tpu_patch_mechanism/)
    * [ Type Checking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/type_checking/)
    * [ Testing & CI  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/testing_and_ci/)
    * [ Benchmarking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/benchmarking/)
    * [ Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/)
Profiling 
      * [ Offline (tpu_profiling.py)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/offline/)
      * [ Server-side Capture  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/server/)
      * [ Phased Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/phased/)
      * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/disaggregated/)
      * [ Output Layout  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/output/)
      * [ Viewing Traces  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/viewing/)
      * [ Troubleshooting  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/troubleshooting/)
  * Reference  Reference 
    * [ Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/)
  * [ Roadmap  ](https://vllm-torchtpu.readthedocs.io/en/latest/roadmap/)


Table of contents 
  * [ Cache Architecture & Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#cache-architecture-environment-variables)
  * [ Compilation Debugging & Telemetry  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#compilation-debugging-telemetry)
    * [ VLLM_XLA_CHECK_RECOMPILATION (Runtime Recompilation Detector)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#vllm_xla_check_recompilation-runtime-recompilation-detector "VLLM_XLA_CHECK_RECOMPILATION \(Runtime Recompilation Detector\)")


[ ](https://github.com/vllm-project/vllm-torchtpu/edit/main/docs/user_guide/compilation_cache.md "Edit this page")
# TorchTPU Compilation Cache[¶](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#torchtpu-compilation-cache "Permanent link")
To enable persistent native C++ compilation caching in `vllm-torchtpu`, set `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` to a persistent directory path:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#__codelineno-0-1)export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/path/to/persistent_cache"

```

## Cache Architecture & Environment Variables[¶](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#cache-architecture-environment-variables "Permanent link")
`vllm-torchtpu` separates Python-level framework tracing cache from native C++ compiled binary executables:
  1. **`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`**(C++ Native PJRT Binaries):
     * **Purpose** : Controls the persistent root directory for native C++ PJRT compiled binary executables (`.bin` files).
     * **Scope** : Native `torch_tpu` C++ backend. This is the primary driver variable required to enable persistent executable binary caching on TPU.
  2. **`VLLM_CACHE_ROOT`**(vLLM Python-Level Framework Artifacts):
     * **Purpose** : Controls the root directory for vLLM Python-level framework tracing artifacts.
     * **Scope** : Stores PyTorch Dynamo FX graph bytecode, Guard expressions, AOTAutograd tracing artifacts (`torch_compile_cache/torch_aot_compile`), and `TpuCompilerAdaptor` metadata pickle handles (`artifact_compile_range_*`).
     * **Note** : `VLLM_CACHE_ROOT` manages Python framework artifacts and is completely independent of the C++ PJRT compiled binary executables managed by `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`.


## Compilation Debugging & Telemetry[¶](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#compilation-debugging-telemetry "Permanent link")
###  `VLLM_XLA_CHECK_RECOMPILATION` (Runtime Recompilation Detector)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/#vllm_xla_check_recompilation-runtime-recompilation-detector "Permanent link")
  * **Default** : `0` (Disabled)
  * **Purpose** : Detects unexpected compilation during serving — such as an input shape, dtype, or code path that AOT warmup never precompiled and that stalls the engine loop on a cache miss.
  * **How It Works** : Queries `torch.tpu._get_cache_stats()` and advances the cached graph count watermark at each checkpoint (including every AOT precompile bucket and runtime forward step), logging newly compiled graphs whenever a cache miss occurs.
  * **Overhead** : `0` (zero runtime overhead) vs `1` (queries cache stats and logs per step).
  * **Recommendation** :
    * `1`: Enable in CI and test pipelines to catch compilation leaks and un-warmed code paths.
    * `0`: Keep disabled in production and benchmarking for maximum throughput.


Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)