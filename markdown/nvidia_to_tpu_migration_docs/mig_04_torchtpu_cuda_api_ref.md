---
id: "mig_04_torchtpu_cuda_api_ref"
title: "TorchTPU CUDA-to-TPU API reference"
url: "https://torchtpu.readthedocs.io/en/latest/api_reference/"
category: "Nvidia to tpu migration docs"
description: "Mappings from torch.cuda to device-agnostic APIs, plus TPU runtime, precision, distributed, and profiling APIs."
crawled_at: "2026-10-26T12:47:59.741803+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/api_reference/#torchtpu-api-reference)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
TorchTPU API Reference 
[ ](https://torchtpu.readthedocs.io/en/latest/api_reference/?q= "Share")
Type to start searching
[ GitHub 
  * 741
  * 60

](https://github.com/google-pytorch/torch_tpu "Go to repository")
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation") TorchTPU Documentation 
[ GitHub 
  * 741
  * 60

](https://github.com/google-pytorch/torch_tpu "Go to repository")
  * [ Home  ](https://torchtpu.readthedocs.io/en/latest/)
  * Get started with TorchTPU  Get started with TorchTPU 
    * [ Introduction to TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/)
    * [ Get started with TorchTPU on a TPU VM  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/)
    * [ Get started with TorchTPU on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/)
    * [ TorchTPU supported feature set and future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/)
    * TorchTPU API Reference  [ TorchTPU API Reference  ](https://torchtpu.readthedocs.io/en/latest/api_reference/) Table of contents 
      * [ Core Device Queries  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#core-device-queries)
      * [ Random Number Generation (RNG)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#random-number-generation-rng)
      * [ Automatic Mixed Precision (AMP)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#automatic-mixed-precision-amp)
      * [ Streams and Events  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#streams-and-events)
      * [ TPU-Specific APIs  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#tpu-specific-apis)
        * [ Execution Modes and Compiler Options  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#execution-modes-and-compiler-options)
        * [ Numerical Precision  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#numerical-precision)
        * [ Distributed Training and Topology  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#distributed-training-and-topology)
        * [ TPU Custom Operators (torch.tpu.ops) and Pallas (torch.tpu.pallas)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#tpu-custom-operators-torchtpuops-and-pallas-torchtpupallas)
          * [ General, Attention, MoE, and Collective Operators  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#general-attention-moe-and-collective-operators)
          * [ SparseCore Embedding Operators  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#sparsecore-embedding-operators)
        * [ Fused Training Step and Optimizers (torch.tpu.optimizers)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#fused-training-step-and-optimizers-torchtpuoptimizers)
        * [ Profiling (torch.tpu.profiler)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#profiling-torchtpuprofiler)
      * [ Environment Variables  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#environment-variables)
        * [ Device Visibility, Runtime, and Distributed Launch  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#device-visibility-runtime-and-distributed-launch)
        * [ Hardware Topology and Multi-Host Coordination  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#hardware-topology-and-multi-host-coordination)
        * [ Execution Mode, Compilation, and Caching  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#execution-mode-compilation-and-caching)
        * [ Debugging, Safety, Profiling, and Tracing  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#debugging-safety-profiling-and-tracing)
        * [ Environment Variable Configuration Snippets  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#environment-variable-configuration-snippets)
          * [ 1. C++ Stacktraces (TORCH_SHOW_CPP_STACKTRACES)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#1-c-stacktraces-torch_show_cpp_stacktraces)
          * [ 2. Internal Debug Checks & Boundary Validation (TORCH_TPU_ENABLE_DEBUG_CHECKS)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#2-internal-debug-checks-boundary-validation-torch_tpu_enable_debug_checks)
          * [ 3. Dumping XLA IR / HLO (XLA_FLAGS)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#3-dumping-xla-ir-hlo-xla_flags)
          * [ 4. Multi-Tiered Compilation Caching (TORCH_TPU_TIER2_COMPILATION_CACHE & TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#4-multi-tiered-compilation-caching-torch_tpu_tier2_compilation_cache-torch_tpu_tier3_compilation_cache_root)
    * [ TorchTPU FAQ  ](https://torchtpu.readthedocs.io/en/latest/faq/)
  * In-depth  In-depth 
    * [ How TorchTPU works  ](https://torchtpu.readthedocs.io/en/latest/how_torchtpu_works/)
    * [ TorchTPU execution model  ](https://torchtpu.readthedocs.io/en/latest/torchtpu_execution_model/)
    * [ TorchTPU and the TPU memory model  ](https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/)
    * [ TorchTPU distributed support  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/)
    * [ TorchTPU custom kernels  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/)
    * [ Dynamic shapes  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/)
  * Case studies  Case studies 
    * [ FLUX optimization  ](https://torchtpu.readthedocs.io/en/latest/case_studies_flux/)
    * [ Muse Glimmer 30B: autoregressive decoding  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_inference/)
    * [ Muse Glimmer 30B: training  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_training/)
    * [ FSDP best practices  ](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/)
  * Analyze your workload  Analyze your workload 
    * [ Manage numerical precision in TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/)
    * [ Performance profiling with XProf  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/)


Table of contents 
  * [ Core Device Queries  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#core-device-queries)
  * [ Random Number Generation (RNG)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#random-number-generation-rng)
  * [ Automatic Mixed Precision (AMP)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#automatic-mixed-precision-amp)
  * [ Streams and Events  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#streams-and-events)
  * [ TPU-Specific APIs  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#tpu-specific-apis)
    * [ Execution Modes and Compiler Options  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#execution-modes-and-compiler-options)
    * [ Numerical Precision  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#numerical-precision)
    * [ Distributed Training and Topology  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#distributed-training-and-topology)
    * [ TPU Custom Operators (torch.tpu.ops) and Pallas (torch.tpu.pallas)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#tpu-custom-operators-torchtpuops-and-pallas-torchtpupallas)
      * [ General, Attention, MoE, and Collective Operators  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#general-attention-moe-and-collective-operators)
      * [ SparseCore Embedding Operators  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#sparsecore-embedding-operators)
    * [ Fused Training Step and Optimizers (torch.tpu.optimizers)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#fused-training-step-and-optimizers-torchtpuoptimizers)
    * [ Profiling (torch.tpu.profiler)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#profiling-torchtpuprofiler)
  * [ Environment Variables  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#environment-variables)
    * [ Device Visibility, Runtime, and Distributed Launch  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#device-visibility-runtime-and-distributed-launch)
    * [ Hardware Topology and Multi-Host Coordination  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#hardware-topology-and-multi-host-coordination)
    * [ Execution Mode, Compilation, and Caching  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#execution-mode-compilation-and-caching)
    * [ Debugging, Safety, Profiling, and Tracing  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#debugging-safety-profiling-and-tracing)
    * [ Environment Variable Configuration Snippets  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#environment-variable-configuration-snippets)
      * [ 1. C++ Stacktraces (TORCH_SHOW_CPP_STACKTRACES)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#1-c-stacktraces-torch_show_cpp_stacktraces)
      * [ 2. Internal Debug Checks & Boundary Validation (TORCH_TPU_ENABLE_DEBUG_CHECKS)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#2-internal-debug-checks-boundary-validation-torch_tpu_enable_debug_checks)
      * [ 3. Dumping XLA IR / HLO (XLA_FLAGS)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#3-dumping-xla-ir-hlo-xla_flags)
      * [ 4. Multi-Tiered Compilation Caching (TORCH_TPU_TIER2_COMPILATION_CACHE & TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT)  ](https://torchtpu.readthedocs.io/en/latest/api_reference/#4-multi-tiered-compilation-caching-torch_tpu_tier2_compilation_cache-torch_tpu_tier3_compilation_cache_root)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/api_reference.md "Edit this page")
# TorchTPU API Reference[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#torchtpu-api-reference "Permanent link")
This document is the reference guide for TorchTPU's public Python APIs and environment variables. It is designed to help you:
  * **Migrate from CUDA to TPU** : Map common `torch.cuda` calls to PyTorch's device-agnostic [`torch.accelerator`](https://docs.pytorch.org/docs/stable/accelerator.html) APIs.
  * **Use TPU-specific features** : Configure execution modes, MXU numerical precision, distributed topology, custom Pallas/TPU operators, traceable optimizers, and XProf profiling via the **`torch.tpu`**module.
  * **Configure the runtime** : Tune compilation caching, debugging checks, and multi-host launch settings through environment variables.


Note
For the exhaustive, automatically generated source-of-truth list of all public Python APIs and environment variables, see [TorchTPU Public APIs (`public_apis.md`)](https://github.com/google-pytorch/torch_tpu/blob/0.2.0-docs/docs/public_apis.md).
##  **Core Device Queries**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#core-device-queries "Permanent link")
When `torch` is imported with TorchTPU installed, the backend automatically registers the `"tpu"` device and the `torch.tpu` module. Where PyTorch provides a device-agnostic [`torch.accelerator`](https://docs.pytorch.org/docs/stable/accelerator.html) API, use it instead of a backend-specific API so your code stays portable across accelerators. Use `torch.tpu` for TPU-specific hardware properties that have no generic equivalent.  
| CUDA API  | TPU / Accelerator API  | Description  |  
| --- | --- | --- |  
| `torch.device("cuda")`  | `torch.accelerator.current_accelerator()`  | Returns `torch.device("tpu")` when TPU is the active accelerator.  |  
| `torch.cuda.is_available()`  | `torch.accelerator.is_available()`  | Checks if the TPU backend is available.  |  
| `torch.cuda.is_initialized()`  | `torch.tpu.is_initialized()`  | Checks if TorchTPU's runtime state has been initialized.  |  
| `torch.cuda.device_count()`  | `torch.accelerator.device_count()`  | Number of devices visible to the current process.  |  
| `torch.cuda.current_device()`  | `torch.accelerator.current_device_index()`  | Returns the active TPU device index.  |  
| `torch.cuda.set_device(rank)`  | `torch.accelerator.set_device_index(rank)`  | Sets the active TPU device index for the current process.  |  
| `torch.cuda.device(rank)`  | `torch.accelerator.device_index(rank)`  | Context manager that temporarily sets the active device index.  |  
| `torch.cuda.get_device_name(device=None)`  | `torch.tpu.get_device_properties(device=None).name`  | Returns the human-readable model name of the attached TPU (e.g., `"TPU v6e"`).  |  
| `torch.cuda.get_device_properties(device=None)`  | `torch.tpu.get_device_properties(device=None)`  | Returns static TPU device properties (including `name`, `devices_per_chip`, `hbm_bytes_per_chip`, `hbm_bytes_per_device`, `bf16_flops_per_chip`, `bf16_flops_per_device`, `sparse_cores_per_device`, and `sparse_core_simd_width`).  |  
The `torch.accelerator` APIs in this table require PyTorch 2.11 or later. In the rare case that you use an older PyTorch version, use the corresponding `torch.tpu` API instead (for example `torch.tpu.device_count()` or `torch.tpu.current_device()`). In PyTorch 2.11 and later, those redundant `torch.tpu` APIs are internal to TorchTPU, and calling them directly from user code raises an error.

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-2)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-3)# Initialize hardware
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-4)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-5)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-6)print(f"torch.accelerator.is_available(): {torch.accelerator.is_available()}")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-7)print(f"torch.accelerator.device_count(): {torch.accelerator.device_count()}")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-8)print(
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-9)    "torch.accelerator.current_device_index():"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-10)    f" {torch.accelerator.current_device_index()}"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-11))
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-12)print(
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-13)    "torch.tpu.get_device_properties().name:"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-14)    f" {torch.tpu.get_device_properties().name}"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-0-15))

```

##  **Random Number Generation (RNG)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#random-number-generation-rng "Permanent link")  
| CUDA API  | TPU / Accelerator API  | Description  |  
| --- | --- | --- |  
| `torch.cuda.manual_seed(seed)`  | `torch.tpu.manual_seed(seed)`  | Seeds the active TPU device's random number generator.  |  
| `torch.cuda.manual_seed_all(seed)`  | `torch.tpu.manual_seed_all(seed)`  | Seeds the RNG across all local TPU devices.  |  
| `torch.cuda.initial_seed()`  | `torch.accelerator.random.initial_seed()`  | Returns the initial random seed of the current TPU device.  |  
| `torch.cuda.get_rng_state()`  | `torch.accelerator.random.get_rng_state()`  | Returns the RNG state tensor for the current device.  |  
| `torch.cuda.set_rng_state(new_state, device=...)`  | `torch.tpu.set_rng_state(new_state, device=...)`  | Sets the RNG state tensor for the current process's active TPU device.  |  
| `torch.cuda.default_generators`  | `torch.tpu.default_generators`  | Lazily initialized tuple of default `torch.Generator` instances indexed by local device ordinal.  |  
The `torch.accelerator.random` APIs in this table require PyTorch 2.13 or later. In the rare case that you use an older PyTorch version, use `torch.tpu.initial_seed()` or `torch.tpu.get_rng_state()` instead. In PyTorch 2.13 and later, these `torch.tpu` APIs are internal to TorchTPU, and calling them from your code raises an error.

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-1-1)# Set the seed across all cores
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-1-2)torch.tpu.manual_seed_all(42)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-1-3)print("Seeded all TPU cores with value 42.")

```

##  **Automatic Mixed Precision (AMP)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#automatic-mixed-precision-amp "Permanent link")
TorchTPU integrates with PyTorch's standard [`torch.amp.autocast`](https://docs.pytorch.org/docs/stable/amp.html) framework using the `"tpu"` device type string.  
| CUDA API  | TPU API  | Description  |  
| --- | --- | --- |  
| `torch.amp.autocast("cuda", ...)`  | `torch.amp.autocast("tpu", ...)`  | Context manager / decorator that enables automatic mixed precision (`bfloat16` by default on TPU).  |  
| `torch.cuda.get_amp_supported_dtype()`  | `torch.tpu.get_amp_supported_dtype()`  | Lists supported dtypes on TPU (`bfloat16`, `float16`, `float32`, `float64`, `float8_*`, integer, boolean, and complex types).  |  

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-2-1)supported_dtypes = torch.tpu.get_amp_supported_dtype()
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-2-2)print(f"AMP supported dtypes: {supported_dtypes}")

```

##  **Streams and Events**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#streams-and-events "Permanent link")
For stream management and device synchronization, use standard [`torch.accelerator`](https://docs.pytorch.org/docs/stable/accelerator.html) APIs instead of backend-specific APIs. Use `torch.tpu` only when constructing TPU `Stream` or `Event` objects directly or configuring TPU core pinning.  
| CUDA API  | TPU / Accelerator API  | Description  |  
| --- | --- | --- |  
| `torch.cuda.current_stream()`  | `torch.accelerator.current_stream()`  | Returns the active stream for a device.  |  
| `torch.cuda.set_stream(stream)`  | `torch.accelerator.set_stream(stream)`  | Sets the active stream.  |  
| `torch.cuda.default_stream(device=None)`  | `torch.tpu.default_stream(device=None)`  | Returns the default `TpuStream` for the device.  |  
| `torch.cuda.stream(stream)`  | `torch.tpu.stream(stream)`  | Context manager that selects a given `TpuStream`.  |  
| `torch.cuda.synchronize()`  | `torch.accelerator.synchronize()`  | Waits for all pending work on the TPU device to complete.  |  
| `torch.cuda.Stream`  | `torch.tpu.Stream(device=None, priority=0, *, pinned=None)`  | Subclasses `torch.Stream`. Supports `synchronize()`, `record_event()`, `wait_event()`, `wait_stream()`, and core pinning (`pinned="dense"` or `"sparse"`, queried via `is_dense` / `is_sparse`).  |  
| `torch.cuda.Event`  | `torch.tpu.Event(enable_timing=False)`  | Subclasses `torch.Event`. Supports `record()`, `synchronize()`, `query()`, and `elapsed_time(end_event)`.  |  
The `torch.accelerator` APIs in this table require PyTorch 2.11 or later. In the rare case that you use an older PyTorch version, use `torch.tpu.current_stream()`, `torch.tpu.set_stream()`, or `torch.tpu.synchronize()` instead.
Note
Streams are a CUDA concept with no direct analogy in TPU. In TorchTPU's deferred execution model, the XLA compiler and PjRt runtime schedule and overlap operations automatically based on data dependencies, so manual multi-stream management is not needed.
##  **TPU-Specific APIs**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#tpu-specific-apis "Permanent link")
Beyond standard CUDA equivalents, `torch.tpu` exposes APIs designed specifically for TPU execution modes, MXU precision, XLA compilation, distributed topology, custom Pallas kernels, traceable optimizers, and profiling.
###  **Execution Modes and Compiler Options**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#execution-modes-and-compiler-options "Permanent link")
Control how eager operations are queued, fused, and compiled by XLA. For an architectural walkthrough, see [TorchTPU Execution modes](https://torchtpu.readthedocs.io/en/latest/torchtpu_execution_model/).  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.EagerMode`  | Enum controlling eager execution: `DEFER_AND_FUSE`, `DEFER_NEVER`, and `DEFER_NEVER_AND_LAUNCH_BLOCKING`.  |  
| `torch.tpu.eager_mode`  | Gets or sets the active `EagerMode` globally.  |  
| `torch.tpu.set_eager_mode(mode)`  | Context manager that temporarily sets the active `EagerMode`.  |  
| `torch.tpu.compiler.custom_compiler_options(options)`  | Context manager that passes custom XLA compiler flags to eager operations materialized inside the block.  |  

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-3-1)print(f"Default eager_mode: {torch.tpu.eager_mode}")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-3-2)with torch.tpu.set_eager_mode(torch.tpu.EagerMode.DEFER_AND_FUSE):
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-3-3)  x = torch.ones((4, 4), device="tpu") + 1
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-3-4)  print(
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-3-5)      f"Inside context manager: {torch.tpu.eager_mode}, sum={x.sum().item()}"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-3-6)  )

```

###  **Numerical Precision**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#numerical-precision "Permanent link")
Control Matrix Multiply Unit (MXU) precision and intermediate `float32` accumulation. For detailed guidance, see [Numerical precision](https://torchtpu.readthedocs.io/en/latest/numerical_precision/).  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.Precision`  | Enum controlling MXU precision for `float32` matmuls and convolutions: `Precision.DEFAULT`, `Precision.HIGH`, and `Precision.HIGHEST`.  |  
| `torch.tpu.precision(level)`  | Context manager that sets the `Precision` level for matmul and convolution operations within the block.  |  
| `torch.tpu.allow_excess_precision`  | Gets or sets XLA's `--xla_allow_excess_precision` flag globally to keep intermediate fused values in `float32`.  |  

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-4-1)a = torch.randn(64, 64, device="tpu", dtype=torch.float32)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-4-2)b = torch.randn(64, 64, device="tpu", dtype=torch.float32)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-4-3)with torch.tpu.precision(torch.tpu.Precision.HIGH):
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-4-4)  c = torch.matmul(a, b)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-4-5)print(f"Computed HIGH-precision matmul with output shape: {tuple(c.shape)}")

```

###  **Distributed Training and Topology**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#distributed-training-and-topology "Permanent link")
TorchTPU registers `"tpu_dist"` (also aliased as `"tpu"`) as the default `torch.distributed` backend for `"tpu"` devices. See [Get started with TorchTPU on GKE](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/) and [FSDP best practices](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/).  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.topology_aware_mesh(mesh_shape, ...)`  | Computes a topology-aware rank layout tensor of shape `mesh_shape` for `DeviceMesh("tpu", mesh=...)`.  |  
| `torch.tpu.distributed.set_tpu_launch_env(...)`  | Populates TPU topology and multi-host launch environment variables before spawning workers.  |  
| `torch.tpu.distributed.spmd_safe(func)`  | Decorator declaring that all ranks execute identical TPU operations in `func`, enabling eager collective fusion.  |  
| `torch.tpu.window_num_stripes`  | Gets or sets the maximum number of concurrent DMA stripes for peer-to-peer transfers.  |  
| `torch.tpu.window_stripe_chunk_mb`  | Gets or sets the minimum payload size (in MB) per DMA stripe for peer-to-peer transfers.  |  
###  **TPU Custom Operators (`torch.tpu.ops`) and Pallas (`torch.tpu.pallas`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#tpu-custom-operators-torchtpuops-and-pallas-torchtpupallas "Permanent link")
TorchTPU exposes hardware-specialized operators under `torch.tpu.ops` and a custom JAX/Pallas kernel wrapper under `torch.tpu.pallas`. See [Adding custom kernels using Pallas](https://torchtpu.readthedocs.io/en/latest/custom_kernels/).
####  **General, Attention, MoE, and Collective Operators**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#general-attention-moe-and-collective-operators "Permanent link")  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.ops.max_pool{1,2,3}d(...)`  | Applies 1D, 2D, or 3D max pooling on TPU without materializing an index tensor.  |  
| `torch.tpu.ops.max_pool{1,2,3}d_backward(...)`  | Computes the backward pass for `max_pool{1,2,3}d` without an index tensor.  |  
| `torch.tpu.ops.optimization_barrier(inputs)`  | Prevents XLA from moving, fusing, or deduplicating computations across the barrier.  |  
| `torch.tpu.ops.splash_sdpa(q, k, v, ...)`  | Scaled dot-product attention backed by the TPU Pallas Splash Attention kernel.  |  
| `torch.tpu.ops.ragged_dot(lhs, rhs, group_sizes, ...)`  | Grouped matrix multiplication for Mixture-of-Experts (MoE) workloads.  |  
| `torch.tpu.ops.ragged_dot_weight_grad(lhs, grad_output, group_sizes)`  | Computes the weight gradient for `ragged_dot`.  |  
| `torch.tpu.ops.align_jagged_to_multiple(nt, ...)`  | Pads a `torch.jagged` `NestedTensor` buffer to a specified multiple for TPU alignment.  |  
| `torch.tpu.ops.strip_jagged_padding(nt, ...)`  | Removes trailing padding added by `align_jagged_to_multiple`.  |  
| `torch.tpu.ops.all_gather_dim(input, dim, group=None)`  | All-gathers `input` across `group` and concatenates along dimension `dim`.  |  
| `torch.tpu.ops.reduce_scatter_dim(input, dim, group=None, ...)`  | Reduces `input` across `group` and scatters chunks along dimension `dim`.  |  
| `torch.tpu.ops.ragged_all_to_all(...)`  | Exchanges variable-length tensor slices across ranks in a process group.  |  
|  `torch.tpu.ops.send(tensors, dst, tag)` / `torch.tpu.ops.recv(tensors, src, tag)`  | Point-to-point tensor send and receive on the default TPU process group.  |  
| `torch.tpu.pallas.jax_op(name, fn=None, ...)`  | Registers a JAX/Pallas function as a traceable PyTorch custom operator.  |  
####  **SparseCore Embedding Operators**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#sparsecore-embedding-operators "Permanent link")
These operators require a TPU with SparseCores. The `sparse_cores_per_device` property of `torch.tpu.get_device_properties()` is the number of SparseCores per device (0 on TPUs without SparseCores), and `sparse_core_simd_width` is their SIMD width.  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.ops.sparse_dense_matmul(...)`  | Performs CSR embedding lookup and aggregation on TPU SparseCore.  |  
|  `torch.tpu.ops.sparse_dense_matmul_grad_with_sgd(...)` / `_with_adagrad(...)` / `_with_adam(...)`  | Computes backward gradients for `sparse_dense_matmul` and applies a fused in-place SGD, Adagrad, or Adam table update on SparseCore.  |  
| `torch.tpu.ops.sparse_dense_matmul_activation_unstack(...)`  | Splits stacked SparseCore embedding activations into per-feature tensors.  |  
| `torch.tpu.ops.sparse_dense_matmul_gradient_stack(...)`  | Stacks per-feature activation gradients into a single tensor for SparseCore.  |  
| `torch.tpu.ops.sparse_gather(...)`  | Gathers rows from a 2D tensor using CSR indices on TPU SparseCore.  |  
| `torch.tpu.ops.sparse_gather_backward(...)`  | Scatter-adds gradients for `sparse_gather` on TPU SparseCore.  |  
| `torch.tpu.ops.sparse_iota(...)`  | Generates within-row position indices for non-zero elements in a CSR matrix on SparseCore.  |  
| `torch.tpu.ops.sparse_map_row(...)`  | Maps a custom MLIR row-wise computation over sparse CSR matrices on SparseCore.  |  
###  **Fused Training Step and Optimizers (`torch.tpu.optimizers`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#fused-training-step-and-optimizers-torchtpuoptimizers "Permanent link")
`torch.tpu.optimizers` traces the forward pass, loss computation, backward pass, and functional optimizer step into a single compiled TPU graph.  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.optimizers.SingleTraceTrainer(model, optimizer=None, ...)`  | Manages functional parameters (`params`), optimizer state (`param_group`), and compiles the full training step via `make_compiled_train_step(...)`.  |  
| `torch.tpu.optimizers.Optimizer(lr=..., weight_decay=...)`  | Base class for stateless functional optimizers (exposes `defaults`, `init_param_group`, and `step`).  |  
| `torch.tpu.optimizers.AdamW(...)`  | Traceable functional AdamW optimizer (`AdamW.ParamGroup`).  |  
| `torch.tpu.optimizers.Muon(...)`  | Traceable functional Muon optimizer (`Muon.ParamGroup`).  |  
| `torch.tpu.optimizers.Sgd(...)`  | Traceable functional SGD optimizer (`Sgd.ParamGroup`).  |  
###  **Profiling (`torch.tpu.profiler`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#profiling-torchtpuprofiler "Permanent link")
Configure TPU hardware and Python tracing for XProf and TensorBoard. See [XProf for TorchTPU](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/).  
| API  | Description  |  
| --- | --- |  
| `torch.tpu.profiler.TpuProfilerConfig(...)`  | Experimental config passed to `torch.profiler.profile(..., experimental_config=...)` to configure host, TPU device, and Python tracing for XProf.  |  
##  **Environment Variables**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#environment-variables "Permanent link")
TorchTPU's behavior is controlled through several environment variables that configure the XLA compiler, the TPU driver (`libtpu`), and PyTorch's own debug subsystem.
> **CRITICAL: Process-Global Initialization** TorchTPU environment variables are **locked** the moment the backend initializes (usually during `import torch` or `torch.device("tpu")`).
###  **Device Visibility, Runtime, and Distributed Launch**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#device-visibility-runtime-and-distributed-launch "Permanent link")  
| Environment Variable  | Description  |  
| --- | --- |  
| `TPU_VISIBLE_DEVICES`  | Comma-separated TPU chip indices visible to the current process (analogous to `CUDA_VISIBLE_DEVICES`).  |  
| `RANK`  | Global rank of the current process in a distributed job.  |  
| `LOCAL_RANK`  | Host-local rank of the current process.  |  
| `WORLD_SIZE`  | Total number of processes in the distributed job.  |  
| `NNODES`  | Total number of host nodes in a multi-host job.  |  
| `NODE_RANK`  | Rank of the current host node in a multi-host job.  |  
| `MASTER_ADDR`  | Address of the rank-0 coordinator node for `torch.distributed`.  |  
| `MASTER_PORT`  | Port on `MASTER_ADDR` used for `torch.distributed` rendezvous.  |  
| `TORCH_DEVICE_BACKEND_AUTOLOAD`  | Set to `"0"` to disable automatic registration of the `torch_tpu` backend.  |  
| `TORCH_TPU_ALLOW_LEGACY_DEVICE_APIS`  | When enabled, allows calling internal `torch.tpu` device APIs (those with a `torch.accelerator` equivalent) from outside PyTorch core with a one-time warning instead of raising a `RuntimeError`. Use this only as a temporary fix; migrating to `torch.accelerator.*` is preferred, and this variable will likely be removed in a future release.  |  
| `LIBTPU_INIT_ARGS`  | Space-separated initialization flags passed to `libtpu` and the PJRT runtime.  |  
| `TPU_PREMAPPED_BUFFER_SIZE`  | Premapped host-to-device memory buffer size in bytes for the PJRT client.  |  
| `TMPDIR`  | Temporary directory used by the runtime and compiler.  |  
###  **Hardware Topology and Multi-Host Coordination**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#hardware-topology-and-multi-host-coordination "Permanent link")
These variables specify the TPU hardware topology and process networking. In most cases, they are set automatically by `torch.tpu.distributed.set_tpu_launch_env()`, the TorchTPU launcher, or the Google Cloud environment.  
| Environment Variable  | Description  |  
| --- | --- |  
| `TORCH_TPU_TOPOLOGY`  | Physical topology of the TPU slice (e.g., `2x2x1`, `2x2x4`).  |  
| `TORCH_TPU_SLICEBUILDER_ADDRESSES`  | Comma-separated `host:port` worker addresses for the TPU slice builder service.  |  
| `TORCH_TPU_DEVICES_PER_HOST`  | Number of TPU chips per host when deriving slice builder addresses.  |  
| `TORCH_TPU_BASE_PORT`  | Starting port number when deriving slice builder addresses.  |  
| `TORCH_TPU_SPMD_HANDSHAKE_STAGE`  | Stage at which ranks verify that collective graphs match across ranks.  |  
| `TORCHCOMM_RANK`  | Process rank for `torchcomm` (takes precedence over `RANK`).  |  
| `TORCHCOMM_SIZE`  | World size for `torchcomm` (takes precedence over `WORLD_SIZE`).  |  
###  **Execution Mode, Compilation, and Caching**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#execution-mode-compilation-and-caching "Permanent link")
These variables control how PyTorch operations and graphs are dispatched, lowered, optimized by XLA, and cached across runs and ranks.  
| Environment Variable  | Description  |  
| --- | --- |  
| `TORCH_TPU_DEFER_AND_FUSE`  | When enabled (`"1"`/`"true"`), sets the default eager mode to `EagerMode.DEFER_AND_FUSE`.  |  
| `TORCH_TPU_LAUNCH_BLOCKING`  | When enabled (`"1"`/`"true"`), sets the default eager mode to `EagerMode.DEFER_NEVER_AND_LAUNCH_BLOCKING`.  |  
| `TORCH_TPU_TIER2_COMPILATION_CACHE`  | Directory name under `/dev/shm/torch_tpu_cache/` for the host-local compilation cache (or `"disabled"`).  |  
| `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`  | Path (e.g., `gs://...` or local path) to the persistent Tier-3 compilation cache shared across hosts and runs.  |  
| `XLA_FLAGS`  | Space-separated XLA compiler flags (e.g., `--xla_dump_hlo_as_text --xla_dump_to=...`).  |  
###  **Debugging, Safety, Profiling, and Tracing**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#debugging-safety-profiling-and-tracing "Permanent link")
These variables control debugging context, runtime safety checks, and profiler output for TorchTPU.  
| Environment Variable  | Description  |  
| --- | --- |  
| `TORCH_SHOW_CPP_STACKTRACES`  | When set to `"1"`, enriches Python `RuntimeError` exceptions with C++ backtraces.  |  
| `TORCH_TPU_ENABLE_DEBUG_CHECKS`  | When set to `"1"`, enables runtime debug and bounds checks on TPU.  |  
| `TORCH_TPU_PROFILER_OUTPUT_DIR`  | Fallback output directory for XProf trace files when `TpuProfilerConfig.run_dir` is unset.  |  
| `TORCH_TPU_XPROF_SESSION_ID`  | Shared XProf profiling session ID across multi-host workers.  |  
| `TORCH_TRACE`  | Output directory for structured compiler and dispatcher trace logs (`tlparse`).  |  
###  **Environment Variable Configuration Snippets**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#environment-variable-configuration-snippets "Permanent link")
####  **1. C++ Stacktraces (`TORCH_SHOW_CPP_STACKTRACES`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#1-c-stacktraces-torch_show_cpp_stacktraces "Permanent link")
Setting `TORCH_SHOW_CPP_STACKTRACES=1` before importing `torch` makes it much easier to diagnose errors that occur deep within the C++ backend or XLA. Instead of a simple Python `RuntimeError`, you receive a detailed `C++ CapturedTraceback` showing exact execution frames.

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-1)import os
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-2)os.environ["TORCH_SHOW_CPP_STACKTRACES"] = "1"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-3)import torch
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-4)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-5)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-6)a = torch.randn(10, device=device)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-7)b = torch.randn(20, device=device)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-8)# Raises RuntimeError enriched with C++ Error Trace and Captured Traceback:
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-5-9)c = a + b

```

####  **2. Internal Debug Checks & Boundary Validation (`TORCH_TPU_ENABLE_DEBUG_CHECKS`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#2-internal-debug-checks-boundary-validation-torch_tpu_enable_debug_checks "Permanent link")
By default, the TPU skips bounds checks for speed. Enabling `TORCH_TPU_ENABLE_DEBUG_CHECKS=1` catches subtle bugs related to out-of-bounds indices (such as in `torch.take`), though it slows down execution due to extra CPU/TPU synchronization. Operations that would otherwise fail silently or cause data corruption raise an explicit exception like `take(): expected indices to be in range`:

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-1)import os
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-2)os.environ["TORCH_TPU_ENABLE_DEBUG_CHECKS"] = "1"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-3)import torch
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-4)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-5)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-6)x = torch.tensor([1.0, 2.0, 3.0], device=device)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-7)indices = torch.tensor([5], device=device)  # Out of bounds
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-8)# Raises an explicit out-of-bounds exception when materialized:
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-6-9)y = torch.take(x, indices).cpu()

```

####  **3. Dumping XLA IR / HLO (`XLA_FLAGS`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#3-dumping-xla-ir-hlo-xla_flags "Permanent link")
By setting `XLA_FLAGS`, you can force the compiler to dump the High-Level Optimizer (HLO) text to a directory. The dump directory (e.g., `/tmp/hlo_dump`) will contain:
  * **`*.after_optimizations.txt`**: The final HLO graph showing hardware-level operations.
  * **`*.flagfile`**: A full list of active XLA compiler flags (verifies`xla_optimization_level`).
  * **`*tpu_comp_env.txt`**: Internal TPU environment settings used during compilation.

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-1)import os
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-2)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-3)dump_dir = "/tmp/hlo_dump"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-4)os.makedirs(dump_dir, exist_ok=True)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-5)os.environ["XLA_FLAGS"] = f"--xla_dump_hlo_as_text --xla_dump_to={dump_dir}"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-6)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-7)import torch
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-8)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-9)x = torch.randn(10, device=device)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-7-10)y = (x + 1).to("cpu")

```

####  **4. Multi-Tiered Compilation Caching (`TORCH_TPU_TIER2_COMPILATION_CACHE` & `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`)**[¶](https://torchtpu.readthedocs.io/en/latest/api_reference/#4-multi-tiered-compilation-caching-torch_tpu_tier2_compilation_cache-torch_tpu_tier3_compilation_cache_root "Permanent link")
TorchTPU uses multi-tiered caching to avoid redundant compilation across runs and ranks:
  * **Tier 2 (`TORCH_TPU_TIER2_COMPILATION_CACHE`)** is stored locally in shared memory within the host. It expects a directory **name** (e.g., `"tpu_tier2_cache"`), which the backend automatically places inside `/dev/shm/torch_tpu_cache/<name>`.
  * **Tier 3 (`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`)** is a persistent compilation cache shared across hosts and sessions (typically a `gs://` bucket URI or a shared filesystem path).


Compiled binary artifacts (`*.bin` executables) are saved to the cache directories asynchronously and reused in subsequent runs, dramatically reducing JIT compilation latency:

```
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-1)import os
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-2)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-3)tier2_name = "tpu_tier2_cache"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-4)tier2_path = os.path.join("/dev/shm/torch_tpu_cache", tier2_name)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-5)tier3_path = "/tmp/tpu_tier3_cache"  # Or "gs://<bucket_name>/<path_to_cache>"
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-6)os.makedirs(tier2_path, exist_ok=True)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-7)os.makedirs(tier3_path, exist_ok=True)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-8)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-9)# TORCH_TPU_TIER2_COMPILATION_CACHE expects just the directory NAME inside /dev/shm/torch_tpu_cache/
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-10)os.environ["TORCH_TPU_TIER2_COMPILATION_CACHE"] = tier2_name
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-11)os.environ["TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT"] = tier3_path
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-12)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-13)import torch
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-14)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-15)a = torch.randn(1024, 1024, device=device)
[](https://torchtpu.readthedocs.io/en/latest/api_reference/#__codelineno-8-16)_ = (a @ a).to("cpu")

```

Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)