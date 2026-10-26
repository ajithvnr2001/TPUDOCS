---
id: "mig_06_torchtpu_feature_set"
title: "TorchTPU supported features and roadmap"
url: "https://torchtpu.readthedocs.io/en/latest/feature_set/"
category: "Nvidia to tpu migration docs"
description: "Check validated versus experimental hardware, operators, models, kernels, and distributed features."
crawled_at: "2026-10-26T12:48:03.381642+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/feature_set/#torchtpu-supported-feature-set-and-future-work)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
TorchTPU supported feature set and future work 
[ ](https://torchtpu.readthedocs.io/en/latest/feature_set/?q= "Share")
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
    * TorchTPU supported feature set and future work  [ TorchTPU supported feature set and future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/) Table of contents 
      * [ Current supported feature set  ](https://torchtpu.readthedocs.io/en/latest/feature_set/#current-supported-feature-set)
      * [ Future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/#future-work)
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
  * [ Current supported feature set  ](https://torchtpu.readthedocs.io/en/latest/feature_set/#current-supported-feature-set)
  * [ Future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/#future-work)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/feature_set.md "Edit this page")
# TorchTPU supported feature set and future work[¶](https://torchtpu.readthedocs.io/en/latest/feature_set/#torchtpu-supported-feature-set-and-future-work "Permanent link")
## Current supported feature set[¶](https://torchtpu.readthedocs.io/en/latest/feature_set/#current-supported-feature-set "Permanent link")
The table below reflects our current feature coverage as of the initial open-source release.
To help you evaluate TorchTPU for your workloads, we categorize features into two tiers:
  * **Validated:** Capabilities that have end-to-end continuous testing, automated CI/CD coverage, and benchmark verification across standard model architectures.
  * **Experimental:** Early-stage implementations, emerging APIs, or prototype features. These are functional and available for early feedback, but may undergo behavioral refinement or API changes based on community input.


Note
TorchTPU is evolving rapidly in the open. For the most up-to-date status or to request specific features, visit our [GitHub](https://github.com/google-pytorch/torch_tpu).  
|   | **Validated**  | **Experimental**  |  
| --- | --- | --- |  
| **PyTorch Community Engagement**  | 
  * OSS release for TorchTPU, vLLM, SGLang, TorchTitan, TorchRec
  * Accepting external PRs
  * Documentation / Tutorials
  * CI/CD
  * Colab

 | 
  * TPU Agent for ATEN migration

 |  
| **TPU Support**  | 
  * v5e, v5p, v6e, v7

 |   |  
| **Basic functionality**  | 
  * Ease of migration
  * Mixed eager + compiled
  * FW + BW
  * Torch.profile
  * Dynamic ops (recompilation)

 | 
  * SymInts
  * Jagged tensors

 |  
| **Model Architectures**  | 
  * Transformer (Dense + MoE): Qwen, Llama, Muse Glimmer, Gemma
  * Diffusion: WAN, FLUX
  * CNN

 | 
  * GLM, Kimi, DeepSeek, GPT OSS, many more (hill climb)
  * Mamba
  * LSTM/GRU
  * DLRM

 |  
| **Kernel Support**  | 
  * Pallas
  * Tokamax

 | 
  * Helion

 |  
| **Quantization**  | 
  * Full tensor FP8/FP4
  * Per-channel FP8

 |   |  
| **Distributed**  | 
  * Optimal mesh
  * SimpleFSDP
  * Checkpointing
  * Activation offloading
  * Multi-slice up to 8K chip

 | 
  * FSDPv2 (low perf)
  * MPMD (low perf)
  * TorchComm

 |  
| **Ecosystem Integrations**  | 
  * Hugging Face
  * Ray
  * vLLM / SGLang
  * TorchTitan
  * TorchRec

 |   |  
| **Production-ready Solutions**  | 
  * Inference (multi-host, P/D disagg)
  * Fine-tuning (up to \~8K chips)

 |   |  
## Future work[¶](https://torchtpu.readthedocs.io/en/latest/feature_set/#future-work "Permanent link")
This section outlines our future development horizons and explorations, not a committed release schedule.
As a community-first open-source project, our development priorities are intentionally responsive to community feedback and developer adoption. Features, timelines, and architectural approaches may evolve as we learn what workloads matter most to you.
We organize our upcoming work into two broad horizons:
  * **Near-Term Focus:** Areas of active design, ongoing prototyping, and performance hardening that the core team is currently prioritizing.
  * **Future Exploration:** Long-term architectural explorations, prospective ecosystem integrations, and community-requested backlog items that we are actively investigating.

  
|   | **Near-term focus**  | **Future exploration**  |  
| --- | --- | --- |  
| **PyTorch Community Engagement**  | 
  * More docs / tutorial / blogs

 | 
  * TPU Agent for Kernel migration

 |  
| **TPU Support**  | 
  * v8i, v8t

 |   |  
| **Basic functionality**  | 
  * Streams
  * Graph capture
  * Eager mode with fast startup time
  * Dynamic ops (no recompilation)

 |   |  
| **Model Architectures**  | 
  * Day 1 model support

 |   |  
| **Quantization**  | 
  * Block-wise FP8/FP4 w/ torchao (peak perf on TPUv8t)

 |   |  
| **Distributed**  | 
  * FSDPv2 (w/ perf)
  * MPMD (w/ perf)
  * Training > 8K chips
  * Multi-tier checkpointing
  * Goodput

 | 
  * Training >> 8K chips

 |  
| **Ecosystem Integrations**  | 
  * VeRL

 |   |  
| **Production-ready Solutions**  | 
  * RL

 | 
  * Pre-training

 |  
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)