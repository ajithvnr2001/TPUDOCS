---
id: "mig_18_torchtpu_engineering_overview"
title: "TorchTPU engineering overview"
url: "https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/"
category: "nvidia_to_tpu_migration_docs"
description: "Explains native PyTorch TPU execution and the engineering choices behind workload portability."
crawled_at: "2026-10-26T14:44:05.047697+00:00"
crawler_engine: "Crawl4AI+BlogArticleCleaner"
---

# TorchTPU: Running PyTorch Natively on TPUs at Google Scale
APRIL 7, 2026
[Claudio Basile](https://developers.googleblog.com/search/?author=Claudio+Basile) Technical Lead Torch TPU
[Kat Ko](https://developers.googleblog.com/search/?author=Kat+Ko) Engineering Lead TorchTPU
[Ben Wilson](https://developers.googleblog.com/search/?author=Ben+Wilson) Software Engineer Torch TPU
[Lee Howes](https://developers.googleblog.com/search/?author=Lee+Howes) Engineering Lead Torch TPU
[Bill Jia](https://developers.googleblog.com/search/?author=Bill+Jia) VP, Engineering Core ML
[Joe Pamer](https://developers.googleblog.com/search/?author=Joe+Pamer) Senior Director Engineering Core ML
[Michael Voznesensky](https://developers.googleblog.com/search/?author=Michael+Voznesensky) Engineer Lead Torch TPU
[Robert Hundt](https://developers.googleblog.com/search/?author=Robert+Hundt) Distinguished Engineer Core ML
Share
  * [ Facebook ](https://www.facebook.com/sharer/sharer.php?u={url} "Share on Facebook")
  * [ Twitter ](https://twitter.com/intent/tweet?text={url} "Share on Twitter")
  * [ LinkedIn ](https://www.linkedin.com/shareArticle?url={url}&mini=true "Share on LinkedIn")
  * Mail
  * [ ](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/ "Get shareable link")


![Blog-A](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Blog-A.original.png)
The challenges of building for modern AI infrastructure have fundamentally shifted. The modern frontier of machine learning now requires leveraging distributed systems, spanning thousands of accelerators. As models scale to run on clusters of O(100,000) chips, the software that powers these models must meet new demands for performance, hardware portability, and reliability.
At Google, our Tensor Processing Units (TPUs) are foundational to our supercomputing infrastructure. These custom ASICs power training and serving for both Google’s own AI platforms, like Gemini and Veo, and the massive workloads of our Cloud customers. The entire AI community should be able to easily access the full capabilities of TPUs, and because many of these potential users build models in PyTorch, an integration that allows PyTorch to work natively and efficiently on the TPU is crucial.
**Enter TorchTPU.** As an engineering team, our mandate was to build a stack that leads with usability, portability, and excellent performance. We wanted to enable developers to migrate existing PyTorch workloads with minimal code changes while giving them the APIs and the tools to extract every ounce of compute from our hardware. Here is a look under the hood at the engineering principles driving TorchTPU, the technical architecture we’ve built, and our roadmap for 2026.
## **Architecting for Usability, Portability, and Performance**
To understand TorchTPU, you first have to understand the hardware it targets.
A TPU system is not just a chip; it is [an integrated network](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/). A host is attached to multiple chips, and each chip connects to the host and to other chips via our Inter-Chip Interconnect (ICI). This ICI links the chips into a highly efficient 2D or 3D Torus topology, allowing for massive scale-up without traditional networking bottlenecks. Within each chip, execution is divided between TensorCores and SparseCores. TensorCores are single-threaded units dedicated to dense matrix math, while SparseCores handle irregular memory access patterns like embeddings, gather/scatter operations, and offloading collectives.
These features mean TPUs are a powerful tool for machine learning; and our goal is to provide the specialized support needed to fully leverage these unique capabilities. This is where PyTorch comes in: the PyTorch toolchain already creates a consistent, widely-used interface over other device types.
Our core principle for usability is simple:**it should feel like PyTorch**. A developer should be able to take an existing PyTorch script, change their initialization to “tpu”, and run their training loop without modifying a single line of core logic.
Achieving this required an entirely new approach to how PyTorch interacts with the TPU compiler and runtime stack.
## **Engineering the TorchTPU Stack: The Technical Reality**
### **Eager First: Flexibility Without Compromise**
Moving from concept to a native PyTorch experience on TPU meant rethinking the execution stack. We established an "Eager First" philosophy. Instead of requiring developers into static graph compilation immediately, we implemented TorchTPU using PyTorch’s “PrivateUse1” interface. No subclasses, no wrappers; just ordinary, familiar PyTorch Tensors on a TPU. By integrating at this deep level, we are able to fully prioritize the eager execution experience developers expect from PyTorch.
We engineered three distinct eager modes to support the development lifecycle.
The first eager mode is Debug Eager, which dispatches one operation at a time and synchronizes with the CPU after every execution. It is inherently slow, but invaluable for tracking down shape mismatches, NaN values, and out-of-memory crashes.
The second is Strict Eager, which maintains single-op dispatch, but executes asynchronously, with the intent of mirroring the default PyTorch experience. This allows both the CPU and TPU to execute simultaneously, until a synchronization point is reached in the user’s script.
The breakthrough, however, is our Fused Eager mode. Using automated reflection on the stream of operations, TorchTPU fuses steps on the fly into larger, computationally dense chunks before handing them to the TPU. By maximizing TensorCore utilization and minimizing memory bandwidth overhead, Fused Eager consistently delivers a 50% to 100+% performance increase over Strict Eager, with no setup required by the user.
All three modes are backed by a shared Compilation Cache that can operate on a single host, or be configured as persistent across multi-host setups. This means that as TorchTPU learns your workload, you spend less time compiling, and more time running.
### **Static Compilation: Dynamo, XLA, and StableHLO**
For users who want to unlock peak performance on the TPU, TorchTPU integrates natively with the torch.compile interface for full-graph compilation. We start by capturing the FX graph using Torch Dynamo. However, rather than routing through Torch Inductor, we utilize XLA as our primary backend compiler.
This was a highly deliberate architectural decision. XLA is rigorously battle-tested for TPU topologies. More importantly, it natively understands how to optimize the critical overlap between dense computation and collective communications across the ICI. Our translation layer maps PyTorch's operators directly into [StableHLO](https://openxla.org/stablehlo), XLA’s primary Intermediate Representation (IR) for tensor math. This creates a direct connection from PyTorch into XLA’s core lowering path, allowing us to generate highly optimized TPU binaries while reusing the execution paths established by our eager modes.
For developers writing custom operators, we ensure extensibility doesn't break performance. TorchTPU natively supports custom kernels written in [Pallas](https://docs.jax.dev/en/latest/jax.experimental.pallas.tpu.html) and JAX. By decorating a JAX function with @torch_tpu.pallas.custom_jax_kernel, engineers can write low-level hardware instructions that interface directly with our lowering path. Work is ongoing to also support [Helion](https://github.com/pytorch/helion) kernels.
### **Distributed Training and the MPMD Challenge**
To preserve the flexibility and usability of eager and compiled modes at scale, we focused heavily on PyTorch's distributed APIs. Today, TorchTPU supports Distributed Data Parallel (DDP), Fully Sharded Data Parallel v2 (FSDPv2), and PyTorch’s DTensor out of the box. We've validated that many third-party libraries that build on PyTorch's distributed APIs work unchanged on TorchTPU.
One major limitation of PyTorch/XLA (a predecessor to TorchTPU) was that it only supported pure SPMD code. The reality of PyTorch inputs is that there is frequently slight divergence in the code running on different ranks: for instance, it is common for the “rank 0” process to do a little extra work for logging or analytics. This kind of input represents a challenge for the TPU stack, which is heavily optimized for SPMD optimization. XLA works best with a global view of code running on the system, but working around it adds overhead to the developer who has to carefully remove impure behavior.
TorchTPU is architected to carefully support divergent executions (MPMD), and will isolate communication primitives where necessary to preserve correctness, at minimal cost. This approach helps ensure that the experience of using PyTorch on the TPU is as natural as possible to existing PyTorch developers, while preserving XLA’s ability to overlap communication and computation with a global view of a distributed TPU deployment wherever possible.
### **TPU Hardware Awareness**
The TPU can achieve very high performance and efficiency, but optimal model design may differ slightly from other hardware. For example, we frequently see models hardcoding attention head dimensions to 64, while current-generation TPUs achieve peak matrix multiplication efficiency at dimensions of 128 or 256. Modifying the model to target 128 or 256 dimensions better utilizes the large, dense and efficient tensor cores on the TPU chip.
Portability doesn't eliminate hardware realities, so TorchTPU facilitates a tiered workflow: establish correct execution first, then use our upcoming deep-dive guidelines to identify and refactor suboptimal architectures, or to inject custom kernels, for optimal hardware utilization.
## **The Road Ahead: 2026 and Beyond**
We have laid a rock-solid foundation across training and serving support today, and we are actively tackling several open challenges to make TorchTPU a frictionless backend in the PyTorch ecosystem.
A primary focus for our compiler team is reducing recompilations triggered by dynamic sequence lengths and batch sizes. By implementing advanced bounded dynamism within XLA, we aim to handle shape changes without incurring compilation overhead. This can be an important feature for certain workloads, such as iterative next-token prediction.
We are also building out a comprehensive library of precompiled TPU kernels for standard operations to drastically reduce the latency of the first execution iteration.
Looking through the rest of 2026, we are working on:
  * The launch of our public GitHub repository, complete with extensive documentation and reproducible architectural tutorials.
  * Integration with PyTorch’s Helion DSL to further expand our custom kernel capabilities.
  * First-class support for dynamic shapes directly through torch.compile.
  * Native multi-queue support to ease migration of heavily asynchronous codebases with decoupled memory and compute streams.
  * Deep integrations with ecosystem pillars like vLLM and TorchTitan, alongside validated linear scaling up to full Pod-size infrastructure.


TorchTPU represents our dedicated engineering effort to provide a seamless, high-performance PyTorch experience on TPU hardware. We are breaking down obstacles and removing friction between the framework you love and the TPU supercomputing hardware required for the next generation of AI.
_To stay informed on the latest TorchTPU updates, please visit the_ [_TPU Developer Hub_](https://cloud.google.com/products/tpu/tpu-developer) _._
posted in: 
  * [AI](https://developers.googleblog.com/search/?technology_categories=AI)
  * [Cloud](https://developers.googleblog.com/search/?technology_categories=Cloud)
  * [Announcements](https://developers.googleblog.com/search/?content_type_categories=Announcements)
  * [Influence](https://developers.googleblog.com/search/?tag=Influence)
  * [Learn](https://developers.googleblog.com/search/?tag=Learn)


[ ](https://developers.googleblog.com/a2ui-v0-9-generative-ui/) Previous
Next [ ](https://developers.googleblog.com/speeding-up-ai-bringing-google-colossus-to-pytorch-via-gcsfs-and-rapid-bucket/)
Related Posts
[ ![Architecting Governed, Self-Evolving AI Agents on Google Cloud](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Gemini_Generated_Image_g9d0nag9d0n.2e16d0ba.fill-800x400.jpg) AI Cloud Tutorials Industry Trends Architecting Governed, Self-Evolving AI Agents on Google Cloud OCT. 22, 2026 ](https://developers.googleblog.com/architecting-governed-self-evolving-ai-agents-on-gemini-agent-platform/) [ ![Integrating TorchTPU into TorchTitan and Optimizing Models for TPU](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Torch_Titan_Header_Image.2e16d0ba.fill-800x400.jpg) AI Cloud Announcements Best Practices Integrating TorchTPU into TorchTitan and Optimizing Models for TPU OCT. 20, 2026 ](https://developers.googleblog.com/integrating-torchtpu-into-torchtitan-and-optimizing-models-for-tpu/) [ ![Streaming comes to API Gateway: real-time and AI-ready APIs, without changing your spec](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Streaming_feature_in__API_Gateway_.2e16d0ba.fill-800x400.jpg) Cloud Announcements Events Streaming comes to API Gateway: real-time and AI-ready APIs, without changing your spec OCT. 22, 2026 ](https://developers.googleblog.com/streaming-comes-to-api-gateway-real-time-and-ai-ready-apis-without-changing-your-spec/) [ ![Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/1_2.2e16d0ba.fill-800x400.png) AI Cloud Tutorials Influence Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond OCT. 21, 2026 ](https://developers.googleblog.com/powering-the-agent-development-lifecycle-with-any-framework-from-adk-to-langchain-and-beyond/)
  * Connect
