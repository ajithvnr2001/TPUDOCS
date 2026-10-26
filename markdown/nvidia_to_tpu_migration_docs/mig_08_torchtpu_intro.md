---
id: "mig_08_torchtpu_intro"
title: "TorchTPU documentation: introduction and feature set"
url: "https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/"
category: "Nvidia to tpu migration docs"
description: "Native PyTorch TPU concepts, migration changes, execution modes, and compilation."
crawled_at: "2026-10-26T12:48:03.803956+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#introduction-to-torchtpu)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
Introduction to TorchTPU 
[ ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/?q= "Share")
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
    * Introduction to TorchTPU  [ Introduction to TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/) Table of contents 
      * [ Why use TorchTPU?  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#why-use-torchtpu)
      * [ Quickstart: Running on TPU  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#quickstart-running-on-tpu)
      * [ Key features  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#key-features)
      * [ Limitations and future work  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#limitations-and-future-work)
      * [ Getting started  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#getting-started)
    * [ Get started with TorchTPU on a TPU VM  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/)
    * [ Get started with TorchTPU on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/)
    * [ TorchTPU supported feature set and future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/)
    * [ TorchTPU API Reference  ](https://torchtpu.readthedocs.io/en/latest/api_reference/)
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
  * [ Why use TorchTPU?  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#why-use-torchtpu)
  * [ Quickstart: Running on TPU  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#quickstart-running-on-tpu)
  * [ Key features  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#key-features)
  * [ Limitations and future work  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#limitations-and-future-work)
  * [ Getting started  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#getting-started)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/intro_to_torchtpu.md "Edit this page")
# Introduction to TorchTPU[¶](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#introduction-to-torchtpu "Permanent link")
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-pytorch/torch_tpu/blob/0.2.0-docs/docs/notebooks/intro_to_torchtpu.ipynb)
TorchTPU is an open-source, native PyTorch backend for [Google Cloud TPUs](https://cloud.google.com/tpu), developed in collaboration between Google and the PyTorch team at Meta. With TorchTPU, developers can run existing PyTorch workloads on TPU hardware with minimal code changes and scale training and inference workloads from a single chip to multi-slice TPU pods.
## Why use TorchTPU?[¶](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#why-use-torchtpu "Permanent link")
Google TPUs are application-specific integrated circuits (ASICs) purpose-built for the matrix and vector operations that power deep learning, offering high throughput, energy efficiency, and performance per dollar at scale. While TPUs have historically been paired with the JAX and TensorFlow ecosystems, TorchTPU brings native TPU support directly to the [PyTorch ecosystem](https://github.com/google-pytorch/torch_tpu) designed intentionally around the following three guiding principles:
  * **Native PyTorch citizenship:** TorchTPU integrates directly with PyTorch with no JAX runtime dependencies. It preserves standard PyTorch tensor view and in-place mutation semantics, adopts PyTorch's one-process-per-device execution model, and supports `torch.compile` through Dynamo.
  * **Out-of-the-box usability:** Porting a workload from a GPU to a TPU starts with changing `device="cuda"` to `device="tpu"` and `backend="nccl"` to `backend="tpu_dist"`. Your unmodified PyTorch model runs immediately in eager mode, with clear error messages when diagnosing runtime or compiler issues.
  * **Production-scale performance:** Beyond op-by-op eager execution, TorchTPU introduces a deferred-fusion eager mode, a Dynamo-to-XLA compiler pipeline, bounded dynamism to avoid shape-driven recompilations, and custom kernel APIs to help you reach peak hardware utilization.


## Quickstart: Running on TPU[¶](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#quickstart-running-on-tpu "Permanent link")
In the following cell, you can see a simple example of a PyTorch program running on TPU. You can run [this example on Colab](https://colab.research.google.com/github/google-pytorch/torch_tpu/blob/0.2.0-docs/docs/notebooks/intro_to_torchtpu.ipynb) by enabling the TPU runtime.

```
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-2)
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-3)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-4)x = torch.randn((4, 4), device=device)
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-5)y = torch.ones((4, 4), device=device)
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-6)
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-7)result = torch.matmul(x, y).cpu()
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-8)print(f"Executed on device: {x.device}")
[](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#__codelineno-0-9)print(f"Result shape on CPU: {result.shape}, sum: {result.sum():.4f}")

```

## Key features[¶](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#key-features "Permanent link")
  * **Comprehensive operator and model coverage:** Supports 450 core ATen operators (both forward and backward passes) and is continuously validated across 5,000 popular HuggingFace models spanning LLMs (Llama, Qwen, Gemma, DeepSeek, Mistral), vision models (ViT, ResNet, ConvNeXt, DINOv2), audio models (Whisper, Wav2Vec2), and diffusion pipelines (FLUX, Stable Diffusion).
  * **Three eager execution modes:**
    * **Strict (default):** Dispatches one ATen operator at a time asynchronously to the TPU, matching standard PyTorch eager behavior on GPUs.
    * **Debug (`TORCH_TPU_LAUNCH_BLOCKING=1`):** Runs each operator synchronously with the CPU and enables runtime bounds checking to simplify debugging.
    * **DeferAndFuse (`TORCH_TPU_DEFER_AND_FUSE=1`):** Defers and fuses sequences of ATen operators into optimized computation blocks up to a materialization point (such as `.cpu()` or `.item()`), significantly reducing High Bandwidth Memory (HBM) traffic and accelerating eager execution.
  * **Graph compilation with`torch.compile` :** Registers the `"tpu"` Dynamo backend (`torch.compile(model)`) to lower entire PyTorch FX graphs into [StableHLO](https://openxla.org/stablehlo/spec) and compile them with the [OpenXLA compiler](https://openxla.org/xla). Active support for dynamic shapes (`torch._dynamo.mark_dynamic`) lets compiled graphs handle varying batch sizes or sequence lengths up to a specified bound without recompiling.
  * **Bounded dynamism:** Natively mitigates recompilations caused by variable batch sizes and sequence lengths by compiling against dynamic upper bounds.
  * **Multi-tier compilation cache:** Eliminates redundant XLA compilations across three cache tiers:
    * **Tier 1:** Process-local in-memory cache (always enabled).
    * **Tier 2:** Host-local shared memory for cross-process reuse in multi-device jobs.
    * **Tier 3:** Persistent remote cache (such as Cloud Storage) for reuse across hosts and job restarts.
  * **Native distributed primitives:** Implements TPU collectives at the `torch.distributed` Process Group (`c10d::Backend`) level via `backend="tpu_dist"`, supporting `DistributedDataParallel` (DDP), `FullyShardedDataParallel` (FSDP2 and SimpleFSDP), and `DTensor`. You can also use `torch.tpu.distributed.topology_aware_mesh` to align parallelism dimensions with physical TPU interconnects.
  * **Custom TPU kernels:** Author custom kernels in [Pallas](https://docs.jax.dev/en/latest/pallas/index.html) (callable via `torch.tpu.pallas.jax_op` with direct inter-chip RDMA collectives support), write tile-based kernels using the experimental [Helion](https://pytorch.org/blog/helion/) DSL, or import optimized pre-built TPU kernels from Tokamax.
  * **Ecosystem integrations:** Works out of the box with standard PyTorch serving and training frameworks and profiling suites, including `torch.profiler` (TensorBoard/XProf), vLLM, SGLang, TorchTitan, Ray, and TorchRec.


## Limitations and future work[¶](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#limitations-and-future-work "Permanent link")
As any product, TorchTPU does have known limitations, which will be addressed over time. While our initial release delivers robust, out-of-the-box coverage for major workloads, TorchTPU is a collaborative, community-driven effort. Please review our [feature set and roadmap](https://torchtpu.readthedocs.io/en/latest/feature_set/) to see what is on the horizon, or jump right in by [submitting PRs](https://github.com/google-pytorch/torch_tpu) on GitHub to help us resolve these limitations. This is a community project, and we'd love to hear from you and invite you to collaborate with us via [GitHub](https://github.com/google-pytorch/torch_tpu), <https://discuss.pytorch.org/c/tpu>, <https://dev-discuss.pytorch.org/c/tpu/> and torchtpu-feedback@google.com.
  * Dynamic Shapes cause recompilations
    * `torch.compile` sets `dynamic=False` by default on TorchTPU. `dynamic=None` or `dynamic=True` are not yet supported for production. [See discussion on dynamic shapes](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/)
    * As example, running decode/generate step on Hugging Face LLMs will involve recompilations at each step unless bounded dynamism is enabled.
  * View ops may be expensive on TPU (see [TorchTPU memory model](https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/)).
  * MPMD with collectives is supported for functionality, but it will not reach peak performance yet. Collective overlap with compute has [some constraints](https://torchtpu.readthedocs.io/en/latest/distributed_support/):
    * Full stream support with SparseCore offload will come in the near future.
    * Use SimpleFSDP with `torch.compile()` as opposed to FSDPv2 with eager or `torch.compile` see [FSDP best practices](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/)
    * Use the `spmd_safe` decorator on regions **users guarantee** to be exactly the same is the recommended way to get peak performance from XLA optimizations on communicating modules (i.e., to enable compute/communication overlap)
  * TorchTPU does not currently have native FlexAttention support
  * Current generation TPUs do not support matmul accumulation in lower precision than fp32 (e.g., tf32).
  * Only one process can access a TPU device, limiting support for co-located RL (note a TPU chip can have one or more devices associated with it, and they can be accessed by separate OS processes).


**Other recommendations:**  
| Limitation  | Recommendation  |  
| --- | --- |  
| Eager modes have a non-zero warmup time  | Enable persistent compilation cache  |  
| Torch.compile takes a long time  | Enable persistent compilation cache  |  
| CNN in PyTorch default using channel-first layout is very inefficient on TPU  | Use this [PyTorch option](https://docs.pytorch.org/tutorials/intermediate/memory_format_tutorial.html) to set a channel last layout for better performance.  |  
| Device mesh mapping may be suboptimal by default due to differences in topology between TPUs and other architectures  | Use `topology_aware_mesh` for optimal device mesh mapping, and ability to customize device mesh mapping  |  
## Getting started[¶](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/#getting-started "Permanent link")
This documentation suite is organized into four structured sections to help you move from first setup to distributed production deployment:
  * **Get Started:** Step-by-step walkthroughs to configure your environment and deploy workloads on [a VM](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/) or [through GKE](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/).
  * **In-Depth:** Deep dives into the [TPU memory model](https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/), [distributed execution](https://torchtpu.readthedocs.io/en/latest/distributed_support/), and the different [execution modes](https://torchtpu.readthedocs.io/en/latest/torchtpu_execution_model/).
  * **Case studies:** End-to-end recipes covering optimizations for the [Flux model](https://torchtpu.readthedocs.io/en/latest/case_studies_flux/), training [Muse Glimmer](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_training/), [End-to-end LLM inference](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_inference/) and the effective application of [FSDP](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/).
  * **Analyze your workload:** [Profiling](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/), managing [numerical precision](https://torchtpu.readthedocs.io/en/latest/numerical_precision/)


Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)