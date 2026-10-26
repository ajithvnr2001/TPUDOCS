---
id: "mig_05_torchtpu_faq"
title: "TorchTPU FAQ"
url: "https://torchtpu.readthedocs.io/en/latest/faq/"
category: "Nvidia to tpu migration docs"
description: "Migration questions, CUDA versus TPU execution, and the replacement of PyTorch/XLA."
crawled_at: "2026-10-26T12:47:59.023574+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/faq/#torchtpu-faq)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
TorchTPU FAQ 
[ ](https://torchtpu.readthedocs.io/en/latest/faq/?q= "Share")
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
    * [ TorchTPU API Reference  ](https://torchtpu.readthedocs.io/en/latest/api_reference/)
    * TorchTPU FAQ  [ TorchTPU FAQ  ](https://torchtpu.readthedocs.io/en/latest/faq/) Table of contents 
      * [ What is the difference between PyTorch/XLA and TorchTPU?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-difference-between-pytorchxla-and-torchtpu)
      * [ What is the difference between TorchAX and TorchTPU?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-difference-between-torchax-and-torchtpu)
      * [ What is happening to PyTorch/XLA?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-happening-to-pytorchxla)
      * [ Is TorchTPU replacing JAX?  ](https://torchtpu.readthedocs.io/en/latest/faq/#is-torchtpu-replacing-jax)
      * [ What is the best way for me to connect with TorchTPU developers?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-best-way-for-me-to-connect-with-torchtpu-developers)
      * [ Will there be any community engagement forums?  ](https://torchtpu.readthedocs.io/en/latest/faq/#will-there-be-any-community-engagement-forums)
      * [ What support does TorchTPU provide for kernel development?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-support-does-torchtpu-provide-for-kernel-development)
      * [ Which TPU generations are actively supported? What's the plan for future hardware support?  ](https://torchtpu.readthedocs.io/en/latest/faq/#which-tpu-generations-are-actively-supported-whats-the-plan-for-future-hardware-support)
      * [ Where can we find TorchTPU's supported features & future roadmap?  ](https://torchtpu.readthedocs.io/en/latest/faq/#where-can-we-find-torchtpus-supported-features-future-roadmap)
      * [ Is there an agent to make my onboarding easier?  ](https://torchtpu.readthedocs.io/en/latest/faq/#is-there-an-agent-to-make-my-onboarding-easier)
      * [ Can I use TorchTPU with our custom serving solution?  ](https://torchtpu.readthedocs.io/en/latest/faq/#can-i-use-torchtpu-with-our-custom-serving-solution)
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
  * [ What is the difference between PyTorch/XLA and TorchTPU?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-difference-between-pytorchxla-and-torchtpu)
  * [ What is the difference between TorchAX and TorchTPU?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-difference-between-torchax-and-torchtpu)
  * [ What is happening to PyTorch/XLA?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-happening-to-pytorchxla)
  * [ Is TorchTPU replacing JAX?  ](https://torchtpu.readthedocs.io/en/latest/faq/#is-torchtpu-replacing-jax)
  * [ What is the best way for me to connect with TorchTPU developers?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-best-way-for-me-to-connect-with-torchtpu-developers)
  * [ Will there be any community engagement forums?  ](https://torchtpu.readthedocs.io/en/latest/faq/#will-there-be-any-community-engagement-forums)
  * [ What support does TorchTPU provide for kernel development?  ](https://torchtpu.readthedocs.io/en/latest/faq/#what-support-does-torchtpu-provide-for-kernel-development)
  * [ Which TPU generations are actively supported? What's the plan for future hardware support?  ](https://torchtpu.readthedocs.io/en/latest/faq/#which-tpu-generations-are-actively-supported-whats-the-plan-for-future-hardware-support)
  * [ Where can we find TorchTPU's supported features & future roadmap?  ](https://torchtpu.readthedocs.io/en/latest/faq/#where-can-we-find-torchtpus-supported-features-future-roadmap)
  * [ Is there an agent to make my onboarding easier?  ](https://torchtpu.readthedocs.io/en/latest/faq/#is-there-an-agent-to-make-my-onboarding-easier)
  * [ Can I use TorchTPU with our custom serving solution?  ](https://torchtpu.readthedocs.io/en/latest/faq/#can-i-use-torchtpu-with-our-custom-serving-solution)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/faq.md "Edit this page")
# TorchTPU FAQ[¶](https://torchtpu.readthedocs.io/en/latest/faq/#torchtpu-faq "Permanent link")
## What is the difference between PyTorch/XLA and TorchTPU?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-difference-between-pytorchxla-and-torchtpu "Permanent link")
Pytorch/XLA historically served as a bridging framework, heavily dependent on JAX runtime components and specialized APIs. TorchTPU offers a native Pytorch backend for [Google Cloud TPUs](https://cloud.google.com/tpu) and zero JAX runtime dependencies, and existing PyTorch workloads run out of the box with trivial code changes (e.g., `.to("cuda")` → `.to("tpu")`)
## What is the difference between TorchAX and TorchTPU?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-difference-between-torchax-and-torchtpu "Permanent link")
TorchAX (also known as torch_xla2) is an implementation that intercepts PyTorch operations at the Python level and lowers them into XLA (often via JAX). While TorchAX has been used heavily for inference benchmarking and prototyping, TorchTPU is the new official standard for a drop-in, PyTorch-native experience on TPUs.
## What is happening to PyTorch/XLA?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-happening-to-pytorchxla "Permanent link")
PyTorch/XLA is deprecated and replaced by [TorchTPU](https://github.com/google-pytorch/torch_tpu), which is now public.
## Is TorchTPU replacing JAX?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#is-torchtpu-replacing-jax "Permanent link")
No. TorchTPU is designed to complement the TPU ecosystem by providing a native PyTorch entry point to Cloud TPUs. It allows developers with existing PyTorch codebases to run directly on TPUs with zero or minimal rewrites, eliminating the need to rewrite models in JAX or manage separate codebases for GPU and TPU infrastructure.
  * **When to think of TorchTPU?** If you have existing PyTorch codebase, want multi-hardware portability (GPU/TPU) without refactoring, using PyTorch-native frameworks (e.g., TorchTitan, vLLM, SGLang, Hugging Face), or wants rapid GPU-to-TPU migration.


## What is the best way for me to connect with TorchTPU developers?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#what-is-the-best-way-for-me-to-connect-with-torchtpu-developers "Permanent link")
You can share feedback by emailing torchtpu-feedback@google.com and we welcome contributions directly to the repo: <https://github.com/google-pytorch/torch_tpu>. You can also use the tag "TPU" at [discuss.pytorch.org](https://discuss.pytorch.org/).
## Will there be any community engagement forums?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#will-there-be-any-community-engagement-forums "Permanent link")
Yes, community engagement is extremely important for us, and we'll be sharing details for such forums. Additionally, we plan to host monthly office hours.
## What support does TorchTPU provide for kernel development?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#what-support-does-torchtpu-provide-for-kernel-development "Permanent link")
Refer to [TorchTPU Custom Kernel support](https://torchtpu.readthedocs.io/en/latest/custom_kernels/).
## Which TPU generations are actively supported? What's the plan for future hardware support?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#which-tpu-generations-are-actively-supported-whats-the-plan-for-future-hardware-support "Permanent link")
TorchTPU actively supports v5e, v5p, Trillium (TPU v6e) and Ironwood (TPU v7x). Validation and optimization for TPU v8 and future chips is ongoing as part of our roadmap.
## Where can we find TorchTPU's supported features & future roadmap?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#where-can-we-find-torchtpus-supported-features-future-roadmap "Permanent link")
See [Supported features](https://torchtpu.readthedocs.io/en/latest/feature_set/) for the current feature set and planned upcoming feature set.
## Is there an agent to make my onboarding easier?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#is-there-an-agent-to-make-my-onboarding-easier "Permanent link")
Check out the TPU agent suite (Experimental): <https://github.com/google-pytorch/tpu-agent-suite>
The TPU Agent Suite is an open-source plugin delivering specialized sub-agents to automate onboarding, diagnostics, and inference performance tuning for PyTorch models on Cloud TPU v6e and v7x.
## Can I use TorchTPU with our custom serving solution?[¶](https://torchtpu.readthedocs.io/en/latest/faq/#can-i-use-torchtpu-with-our-custom-serving-solution "Permanent link")
Yes. While TorchTPU offers out-of-the-box integration with industry-standard serving engines like vLLM and SGLang, custom or in-house serving solutions can integrate with TorchTPU via native PyTorch execution APIs and lower-level compiler backends. For advanced orchestration, customers can also deploy custom serving setups on GKE with llm-d.
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)