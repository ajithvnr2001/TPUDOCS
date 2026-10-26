---
name: mig-06-torchtpu-feature-set
description: "TorchTPU supported features and roadmap \u2014 Check validated versus experimental hardware, operators, models, kernels, and distributed features."
source_url: "https://torchtpu.readthedocs.io/en/latest/feature_set/"
category: "nvidia_to_tpu_migration_docs"
---

# Agent Skill: TorchTPU supported features and roadmap

- **Official Source**: [https://torchtpu.readthedocs.io/en/latest/feature_set/](https://torchtpu.readthedocs.io/en/latest/feature_set/)
- **Category**: `nvidia_to_tpu_migration_docs`
- **Resource ID**: `mig_06_torchtpu_feature_set`
- **When to Activate**: Check validated versus experimental hardware, operators, models, kernels, and distributed features.

## Document Sections

  - **Current supported feature set**
  - **Future work**

## Complete Technical Reference

# TorchTPU supported feature set and future work
## Current supported feature set
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
## Future work
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
