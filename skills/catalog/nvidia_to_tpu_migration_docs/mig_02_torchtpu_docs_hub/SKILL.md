---
name: mig-02-torchtpu-docs-hub
description: "TorchTPU documentation hub \u2014 Index of native PyTorch TPU quickstarts, migration APIs, examples, and performance documentation."
source_url: "https://torchtpu.readthedocs.io/"
category: "nvidia_to_tpu_migration_docs"
---

# Agent Skill: TorchTPU documentation hub

- **Official Source**: [https://torchtpu.readthedocs.io/](https://torchtpu.readthedocs.io/)
- **Category**: `nvidia_to_tpu_migration_docs`
- **Resource ID**: `mig_02_torchtpu_docs_hub`
- **When to Activate**: Index of native PyTorch TPU quickstarts, migration APIs, examples, and performance documentation.

## Document Sections

- **Home**
  - **About**
  - **What are you trying to do today?**

## Complete Technical Reference

# Home
[![TorchTPU](https://torchtpu.readthedocs.io/en/0.2.0/images/torchtpu_banner.png)](https://torchtpu.readthedocs.io/en/0.2.0/images/torchtpu_banner.png)
[**GitHub**](https://github.com/google-pytorch/torch_tpu) | [**Discussion Forum**](https://discuss.pytorch.org/c/tpu/45) | [**PyTorch on TPU**](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)
## About
TorchTPU is an open-source, native PyTorch backend for Google Cloud TPUs, developed in collaboration between Google and Meta. With TorchTPU, you can run existing PyTorch models on TPU hardware with minimal code changes and scale training and inference workloads from a single chip to multi-slice TPU pods.
## What are you trying to do today?
  * **Get started**
Provision environments, understand fundamental architectures, and run your first workloads.
    * [ Introduction to TorchTPU](https://torchtpu.readthedocs.io/en/0.2.0/intro_to_torchtpu/): Why TorchTPU was created, what it provides, and how it can help you.
    * [ Get started with TorchTPU on a VM](https://torchtpu.readthedocs.io/en/0.2.0/get_started_on_a_vm/): Setup TorchTPU on a TPU VM.
    * [ Get started with TorchTPU on GKE](https://torchtpu.readthedocs.io/en/0.2.0/get_started_on_gke/): Use TorchTPU through GKE.
    * [ Supported feature set and roadmap](https://torchtpu.readthedocs.io/en/0.2.0/feature_set/): Currently supported features and plans for future releases.
    * [ API reference](https://torchtpu.readthedocs.io/en/0.2.0/api_reference/): The TorchTPU API and environment variables for the current release.
    * [ TorchTPU FAQ](https://torchtpu.readthedocs.io/en/0.2.0/faq/): Frequently asked questions about TorchTPU.
  * **In-depth architecture & core concepts**
Deep-dive into the mechanics of memory layouts, execution engines, and distributed execution.
    * [ How TorchTPU works](https://torchtpu.readthedocs.io/en/0.2.0/how_torchtpu_works/): How TorchTPU integrates with PyTorch and the TPU hardware from top to bottom.
    * [ The TorchTPU execution model](https://torchtpu.readthedocs.io/en/0.2.0/torchtpu_execution_model/): In depth detail of how TorchTPU executes PyTorch code and the different execution modes it supports.
    * [ The TorchTPU memory model](https://torchtpu.readthedocs.io/en/0.2.0/torchtpu_memory_model/): How TorchTPU handles the way the TPU and XLA compiler deal with memory.
    * [ Distributed support](https://torchtpu.readthedocs.io/en/0.2.0/distributed_support/): How TorchTPU supports distributed workloads.
    * [ Custom kernel support](https://torchtpu.readthedocs.io/en/0.2.0/custom_kernels/): How to write custom kernels for TorchTPU.
    * [ Dynamic shapes](https://torchtpu.readthedocs.io/en/0.2.0/dynamic_shapes/): Support for dynamic tensor shapes.
  * **Case studies**
Explore practical examples of how to use TorchTPU to solve real-world problems.
    * [ FLUX Optimization](https://torchtpu.readthedocs.io/en/0.2.0/case_studies_flux/): Example demonstrating how to identify and apply multiple optimizations on FLUX.
    * [ Muse Glimmer 30B inference](https://torchtpu.readthedocs.io/en/0.2.0/case_studies_muse_glimmer_30b_inference/): Example of iterative decoding using real weights with static/dynamic KV cache.
    * [ Muse Glimmer 30B training](https://torchtpu.readthedocs.io/en/0.2.0/case_studies_muse_glimmer_30b_training/): A training loop on a standalone implementation of Muse Glimmer 30B.
    * [ Using FSDP](https://torchtpu.readthedocs.io/en/0.2.0/case_studies_fsdp/): The recommended approach to using FSDP for TorchTPU.
  * **Analyze your workload**
    * [ Numerical precision and parity](https://torchtpu.readthedocs.io/en/0.2.0/numerical_precision/): Controlling precision in TorchTPU.
    * [ Profile performance with XProf](https://torchtpu.readthedocs.io/en/0.2.0/performance_profiling_with_xprof/): How to use XProf as a TorchTPU profiler.
