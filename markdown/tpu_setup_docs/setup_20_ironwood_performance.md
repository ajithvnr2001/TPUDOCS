---
id: "setup_20_ironwood_performance"
title: "TPU7x performance optimizations"
url: "https://docs.cloud.google.com/tpu/docs/ironwood-performance"
category: "TPU setup docs"
description: "Optimize memory movement, low-precision computation, sharding, and communication on Ironwood."
crawled_at: "2026-10-26T12:45:23.629303+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/tpu/docs/ironwood-performance#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
[ Documentation ](https://docs.cloud.google.com/docs)
close
  * Get Started


  * [ Get Started with Google Cloud  ](https://docs.cloud.google.com/docs/get-started)
  * [ Product List  ](https://docs.cloud.google.com/docs/product-list)
  * [ Cloud Customer Care  ](https://docs.cloud.google.com/support/docs)


  * Featured Products


  * [ Agent Platform  ](https://docs.cloud.google.com/products/gemini-enterprise-agent-platform)
  * [ Apigee API Management  ](https://docs.cloud.google.com/apigee)
  * [ BigQuery  ](https://docs.cloud.google.com/bigquery)
  * [ Compute Engine  ](https://docs.cloud.google.com/products/compute)
  * [ Cloud CDN  ](https://docs.cloud.google.com/cdn)
  * [ Cloud Run  ](https://docs.cloud.google.com/run)
  * [ Cloud Storage  ](https://docs.cloud.google.com/storage)
  * [ Cloud SQL  ](https://docs.cloud.google.com/sql)
  * [ Gemini Enterprise  ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Google Kubernetes Engine  ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Looker  ](https://docs.cloud.google.com/looker)


  * Cross-product Tools


  * [ Access and resources management  ](https://docs.cloud.google.com/docs/access-resources)
  * [ Costs and usage management  ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Infrastructure as code  ](https://docs.cloud.google.com/docs/iac)
  * [ SDK, languages, frameworks, and tools  ](https://docs.cloud.google.com/docs/devtools)


  * Technology Areas


  * [ AI and ML  ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Application development  ](https://docs.cloud.google.com/docs/application-development)
  * [ Application hosting  ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Compute  ](https://docs.cloud.google.com/docs/compute-area)
  * [ Data analytics and pipelines  ](https://docs.cloud.google.com/docs/data)
  * [ Databases  ](https://docs.cloud.google.com/docs/databases)
  * [ Distributed, hybrid, and multicloud  ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Industry solutions  ](https://docs.cloud.google.com/docs/industry)
  * [ Migration  ](https://docs.cloud.google.com/docs/migration)
  * [ Networking  ](https://docs.cloud.google.com/docs/networking)
  * [ Observability and monitoring  ](https://docs.cloud.google.com/docs/observability)
  * [ Security  ](https://docs.cloud.google.com/docs/security)
  * [ Storage  ](https://docs.cloud.google.com/docs/storage)


`/`
[ Console ](https://console.cloud.google.com/)
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/tpu/docs)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)


[Start free](https://console.cloud.google.com/freetrial)
[ Overview ](https://docs.cloud.google.com/tpu/docs) [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) [ Reference ](https://docs.cloud.google.com/tpu/docs/reference) [ Samples ](https://docs.cloud.google.com/tpu/docs/samples) [ Support ](https://docs.cloud.google.com/tpu/docs/support) [ Resources ](https://docs.cloud.google.com/tpu/docs/resources)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
  * [ Documentation  ](https://docs.cloud.google.com/docs)
    * More 
    * [ Overview  ](https://docs.cloud.google.com/tpu/docs)
    * [ Guides  ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
    * [ Reference  ](https://docs.cloud.google.com/tpu/docs/reference)
    * [ Samples  ](https://docs.cloud.google.com/tpu/docs/samples)
    * [ Support  ](https://docs.cloud.google.com/tpu/docs/support)
    * [ Resources  ](https://docs.cloud.google.com/tpu/docs/resources)
  * [ Console  ](https://console.cloud.google.com/)


  * Discover
  * [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
  * [TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)
  * TPU versions
    * [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)
    * [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e)
    * [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)
    * [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)
    * [TPU v4](https://docs.cloud.google.com/tpu/docs/v4)
  * [Regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones)
  * [Cloud TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine)
  * [TPU capacity modes](https://docs.cloud.google.com/tpu/docs/capacity-modes)
  * [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)
  * [JAX AI stack](https://docs.cloud.google.com/tpu/docs/jax-ai-stack)
  * Get started
  * [Set up a Google Cloud project](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute)
  * Quickstarts
    * [Create a TPU instance](https://docs.cloud.google.com/tpu/docs/quickstart-create-tpu-instance)
    * [Create a multi-host TPU slice](https://docs.cloud.google.com/tpu/docs/quickstart-create-multi-host-slice)
  * [Plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus)
  * Reserve TPUs
    * [About TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations)
    * [Request a reservation for up to 90 days (in calendar mode)](https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation)
    * [Request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation)
    * [Share a reservation](https://docs.cloud.google.com/tpu/docs/share-reservation)
    * [Consume a reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute)
  * Create TPUs
    * [TPU creation overview](https://docs.cloud.google.com/tpu/docs/create-tpu-vm-compute)
    * [Create a TPU VM instance](https://docs.cloud.google.com/tpu/docs/create-instance-compute)
    * [Create TPU Flex-start VMs](https://docs.cloud.google.com/tpu/docs/create-flex-start-compute)
    * [Create TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot-compute)
    * [TPU instances in MIGs](https://docs.cloud.google.com/tpu/docs/tpus-and-migs)
    * [Create a MIG for a multi-host TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig)
    * [Create a MIG for single-host TPU slices](https://docs.cloud.google.com/tpu/docs/create-single-host-mig)
  * Configure TPUs
  * [Configure networking and access](https://docs.cloud.google.com/tpu/docs/configure-networking-access-compute)
  * [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images)
  * [Use a custom OS image](https://docs.cloud.google.com/tpu/docs/custom-os-image)
  * [Encrypt a TPU VM boot disk with a CMEK](https://docs.cloud.google.com/tpu/docs/cmek-tpu-compute)
  * [Use a cross-project service account](https://docs.cloud.google.com/tpu/docs/cross-project-sa-compute)
  * Manage storage
    * [Storage options for TPU VMs](https://docs.cloud.google.com/tpu/docs/storage-options)
    * [Storage best practices](https://docs.cloud.google.com/tpu/docs/storage-best-practices)
    * [Attach storage disks](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute)
    * [Connect to Cloud Storage buckets](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute)
  * Manage TPUs
  * [Manage TPU resources with Compute Engine](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute)
  * [Manage maintenance events in managed capacity mode](https://docs.cloud.google.com/tpu/docs/prepare-for-maintenance)
  * [Failure recovery of TPU instances](https://docs.cloud.google.com/tpu/docs/failure-recovery)
  * Manage TPUs in All Capacity mode
    * [All Capacity mode overview](https://docs.cloud.google.com/tpu/docs/all-capacity-overview)
    * [Request an All Capacity mode reservation](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation)
    * [View the topology and health of All Capacity mode TPUs](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus)
    * [Report and repair faulty hosts in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts)
    * [Manage maintenance events in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events)
  * [Multislice training](https://docs.cloud.google.com/tpu/docs/multislice-introduction)
  * [Schedule TPU collections for inference workloads](https://docs.cloud.google.com/tpu/docs/collection-scheduling)
  * Run workloads
  * [Train a model using TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x-training)
  * [Run inference on Cloud TPU](https://docs.cloud.google.com/tpu/docs/tpu-inference)
  * [Train on Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/training-on-tpu-pods)
  * [Scale a model on TPUs](https://docs.cloud.google.com/tpu/docs/scaling-model-on-tpus)
  * Optimize performance
  * [Cloud TPU performance guide](https://docs.cloud.google.com/tpu/docs/performance-guide)
  * [Improve your model's performance with bfloat16](https://docs.cloud.google.com/tpu/docs/bfloat16)
  * [TPU7x (Ironwood) performance optimizations](https://docs.cloud.google.com/tpu/docs/ironwood-performance)
  * Monitor and troubleshoot TPUs
  * [Monitor TPU VMs](https://docs.cloud.google.com/tpu/docs/monitor-tpu)
  * [Monitor TPU health](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health)
  * [Monitor TPU capacity](https://docs.cloud.google.com/tpu/docs/monitor-capacity)
  * [Monitor TPU goodput](https://docs.cloud.google.com/tpu/docs/goodput)
  * [TPU monitoring library](https://docs.cloud.google.com/tpu/docs/tpu-monitoring-library)
  * [Monitor with tpu-info CLI](https://docs.cloud.google.com/tpu/docs/tpu-info-cli)
  * [Troubleshoot PyTorch models](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-pytorch)
  * [Troubleshoot JAX models](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-jax)
  * ML Diagnostics platform
    * [Overview](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/overview)
    * [Set up GKE](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke)
    * [Get started with the SDK](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk)
    * [Get started with the CLI](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli)
    * [Use ML Diagnostics with MaxText](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/maxtext)
    * [View machine learning runs](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/view-runs)
    * [Monitor workloads](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring)
  * Profile TPUs
  * [Profile TPU VMs](https://docs.cloud.google.com/tpu/docs/profile-tpu-vm)
  * [Profile Multislice environments](https://docs.cloud.google.com/tpu/docs/troubleshooting/troubleshoot-multislice)
  * [Profile PyTorch/XLA workloads](https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm)
  * Cloud TPU API
  * Discover
    * [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes)
    * TPU versions
      * [TPU v3](https://docs.cloud.google.com/tpu/docs/v3)
      * [TPU v2](https://docs.cloud.google.com/tpu/docs/v2)
  * Get started
    * [Set up a Google Cloud project](https://docs.cloud.google.com/tpu/docs/setup-gcp-account)
    * [Create TPUs](https://docs.cloud.google.com/tpu/docs/create-tpu-vm)
    * [Consume a reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation)
    * [Run JAX on Cloud TPU VM](https://docs.cloud.google.com/tpu/docs/run-calculation-jax)
    * [Run PyTorch on Cloud TPU VM](https://docs.cloud.google.com/tpu/docs/run-calculation-pytorch)
    * [Run JAX on Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods)
    * [Run PyTorch on Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/pytorch-pods)
  * Configure TPUs
    * [Connect a TPU to a shared VPC network](https://docs.cloud.google.com/tpu/docs/shared-vpc-networks)
    * [Connect to a TPU VM without a public IP address](https://docs.cloud.google.com/tpu/docs/tpu-iap)
    * [Configure networking and access](https://docs.cloud.google.com/tpu/docs/configure-networking-access)
    * [Encrypt a TPU VM boot disk with a CMEK](https://docs.cloud.google.com/tpu/docs/cmek-tpu)
    * [Use a cross-project service account](https://docs.cloud.google.com/tpu/docs/cross-project-sa)
    * [Attach durable block storage to a TPU VM](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage)
    * [Connect to Cloud Storage buckets](https://docs.cloud.google.com/tpu/docs/storage-buckets)
    * [Mount a Filestore instance on a TPU VM](https://docs.cloud.google.com/tpu/docs/mount-filestore)
  * Manage TPUs
    * [Manage TPU resources](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)
    * [Manage queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources)
    * [Request TPU Flex-start VMs](https://docs.cloud.google.com/tpu/docs/request-using-flex-start)
    * [Manage TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot)
    * [Prepare for maintenance events](https://docs.cloud.google.com/tpu/docs/maintenance-events)
    * [Autocheckpoint](https://docs.cloud.google.com/tpu/docs/autocheckpoint)
    * [View maintenance notifications](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications)
    * [Manually start host maintenance](https://docs.cloud.google.com/tpu/docs/manually-start-maintenance)
    * [Preemptible TPUs](https://docs.cloud.google.com/tpu/docs/preemptible)
  * Run workloads
    * [Train a model using v6e](https://docs.cloud.google.com/tpu/docs/v6e-training)
    * [Train a model using v5e](https://docs.cloud.google.com/tpu/docs/v5e-training)
    * [Run TPU applications in a Docker container](https://docs.cloud.google.com/tpu/docs/run-in-container)
  * Monitor and troubleshoot TPUs
    * [Troubleshoot TPU VMs](https://docs.cloud.google.com/tpu/docs/troubleshooting/troubleshooting)
    * [Monitor TPU VMs](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-vm-monitoring)
    * [Dashboards for monitoring and logging](https://docs.cloud.google.com/tpu/docs/troubleshooting/dashboards)
    * [Troubleshoot TensorFlow models](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-tf)
    * [Cloud TPU error glossary](https://docs.cloud.google.com/tpu/docs/troubleshooting/error_glossary)
    * [Cloud TPU audit logs](https://docs.cloud.google.com/tpu/docs/audit-logs)
  * Tutorials and notebooks
    * [MaxDiffusion inference on v6e](https://docs.cloud.google.com/tpu/docs/tutorials/LLM/maxdiffusion-inference-v6e)


  * Get Started 
  * [ Get Started with Google Cloud  ](https://docs.cloud.google.com/docs/get-started)
  * [ Product List  ](https://docs.cloud.google.com/docs/product-list)
  * [ Cloud Customer Care  ](https://docs.cloud.google.com/support/docs)
  * Featured Products 
  * [ Agent Platform  ](https://docs.cloud.google.com/products/gemini-enterprise-agent-platform)
  * [ Apigee API Management  ](https://docs.cloud.google.com/apigee)
  * [ BigQuery  ](https://docs.cloud.google.com/bigquery)
  * [ Compute Engine  ](https://docs.cloud.google.com/products/compute)
  * [ Cloud CDN  ](https://docs.cloud.google.com/cdn)
  * [ Cloud Run  ](https://docs.cloud.google.com/run)
  * [ Cloud Storage  ](https://docs.cloud.google.com/storage)
  * [ Cloud SQL  ](https://docs.cloud.google.com/sql)
  * [ Gemini Enterprise  ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Google Kubernetes Engine  ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Looker  ](https://docs.cloud.google.com/looker)
  * Cross-product Tools 
  * [ Access and resources management  ](https://docs.cloud.google.com/docs/access-resources)
  * [ Costs and usage management  ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Infrastructure as code  ](https://docs.cloud.google.com/docs/iac)
  * [ SDK, languages, frameworks, and tools  ](https://docs.cloud.google.com/docs/devtools)
  * Technology Areas 
  * [ AI and ML  ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Application development  ](https://docs.cloud.google.com/docs/application-development)
  * [ Application hosting  ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Compute  ](https://docs.cloud.google.com/docs/compute-area)
  * [ Data analytics and pipelines  ](https://docs.cloud.google.com/docs/data)
  * [ Databases  ](https://docs.cloud.google.com/docs/databases)
  * [ Distributed, hybrid, and multicloud  ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Industry solutions  ](https://docs.cloud.google.com/docs/industry)
  * [ Migration  ](https://docs.cloud.google.com/docs/migration)
  * [ Networking  ](https://docs.cloud.google.com/docs/networking)
  * [ Observability and monitoring  ](https://docs.cloud.google.com/docs/observability)
  * [ Security  ](https://docs.cloud.google.com/docs/security)
  * [ Storage  ](https://docs.cloud.google.com/docs/storage)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)


Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 
# TPU7x (Ironwood) performance optimizations
This guide describes several methods to optimize performance with TPU7x (Ironwood) by efficiently managing data movement between its multi-tiered memory system. This includes techniques like low-precision training, sharding, communication optimization, activation rematerialization, scoped vector memory (VMEM) tuning, and custom accelerator kernels.
To optimize performance with TPU7x, you must first be familiar with the Ironwood architecture, specifically the memory hierarchy and interconnect topology. For more information, see [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x).
## Low-precision training with FP8
FP8 (8-bit floating point) is an efficient numerical data format used primarily to accelerate model training and inference. By representing numbers using 8 bits – rather than the standard 16-bit formats (FP16 or BF16) and 32-bit (FP32) – TPUs can process data significantly faster and use less memory.
TPU7x supports built-in hardware acceleration for FP8 data types, offering a peak theoretical performance of 4614 TFLOPS per chip. This capability can lead to significantly faster end-to-end training times. For compatible operations, particularly dense matrix multiplications that are common for AI workloads, using FP8 can yield performance improvements of 1.3x over standard BF16 training. Compared to BF16, FP8 doubles peak FLOPs and halves memory footprint for weights and activations. FP8 should be a primary tuning lever for both compute-bound workloads and scenarios that are constrained by memory capacity or bandwidth.
Using FP8 offers the following performance benefits:
  * **Reduced high-bandwidth memory (HBM) pressure** : A smaller memory footprint allows larger models, or models with larger KV caches during inference, to fit entirely within the 192 GiB of HBM. This avoids costly offloading to slower host memory.
  * **Increased effective batch size** : By reducing the memory required for activations, FP8 enables the use of larger batch sizes. This improves data parallelism and can lead to higher throughput and better utilization of the compute units.
  * **Lower memory bandwidth requirements** : Moving half the amount of data for each operation reduces the demand on the HBM-to-MXU data path. On systems where data movement is a common bottleneck, this helps keep the MXUs saturated with work.


Using FP8 with zero or limited degradation in performance requires the careful selection of quantization techniques. Here are some best practices to consider for FP8 training:
  * **Scaling granularity** : Start with per-tensor scaling as the baseline. If there are quality or performance issues, switch to per-axis scaling. Subchannel scaling may be unnecessary.
  * **Scaling mode** : Dynamic scaling, which computes scaling factors at runtime, is a good default for maintaining quality. While static scaling can offer a significant performance boost by eliminating computations, it requires careful profiling to determine the correct scaling factors and may not be suitable for all use cases, especially when model configurations change. Conversely, some robust models and configurations can fix the scale to the FP8 limit for weights or activations, allowing you to reduce quantization overhead while maintaining accuracy and improving performance.
  * **FP8 formats (E4M3 and E5M2)** : A common and effective approach is to use a mix of FP8 formats. For example, use E4M3 for weights and activations in the forward pass to take advantage of the higher precision of E4M3, and use E5M2 for gradients in the backward pass to accommodate for the wider dynamic range of the gradients.
  * **Rounding** : Using "round to nearest even" (RNE) instead of stochastic rounding for gradients can maintain quality while offering better performance and reproducibility.
  * **Enabling FP8 in MaxText** : [MaxText](https://maxtext.readthedocs.io/en/latest/) supports FP8 training through the QWIX quantization library. To activate quantization, set the following flag in your configuration: `use_qwix_quantization=true`.


## Sharding and parallelism
Sharding is the process of slicing a large model or its training data into smaller pieces and distributing them across multiple TPU chips or cores. Choosing the right sharding strategy is important for achieving high performance on TPU7x.
A naive approach that purely maximizes the degree of parallelism will often result in poor performance by becoming communication-bound. The best approach is often to select the simplest sharding strategy that meets memory constraints, as this minimizes communication overhead and allows the compute units to be efficiently utilized.
Before selecting a sharding strategy, the first step in any performance tuning effort should be an arithmetic intensity analysis. This analysis determines whether a given computation is limited by compute, memory bandwidth, or interconnect bandwidth. It is calculated as the ratio of floating-point operations to the bytes of data that must be moved.
A high arithmetic intensity indicates a compute-bound workload. A low arithmetic intensity suggests a memory- or communication-bound workload, where performance is limited by the speed at which data can be moved from HBM or across the ICI network. This analysis informs the ideal batch size and sharding strategy. For example, a communication-bound workload won't benefit from a sharding strategy that introduces even more communication, such as high-degree tensor parallelism.
### Sharding strategy decision framework
MaxText offers a variety of sharding strategies. The optimal choice depends on the model architecture, sequence length, and the need to balance computational load against communication overhead.
  * **Fully Sharded Data Parallelism (FSDP)** : This is the preferred default strategy for data parallelism. FSDP shards the model weights, gradients, and optimizer states across the data-parallel devices. During computation, each device performs an All-Gather operation to retrieve the necessary full weights for its local microbatch. FSDP is highly effective as long as the per-device batch size is large enough to hide the latency of this All-Gather communication. For Mixture-of-Experts (MoE) models, the arithmetic intensity calculation must account for sparsity.
  * **Tensor Parallelism (TP)** : TP shards individual tensors across devices. Typically, the tensors are weight matrices in multilayer perceptron (MLP) and attention blocks. The hardware's high arithmetic intensity (11.5k) imposes a very high requirement on the model's dimensions to make TP viable over ICI, and attempting to use TP can result in the system being communication-bound.
  * **Expert Parallelism (EP)** : This is the standard and necessary strategy for training MoE models. EP shards the "expert" layers across a set of devices, and an All-to-All communication collective is used to route tokens to their designated expert device. EP can be efficient if the model's MLP dimension is large enough to approach the roofline.
  * **Context Parallelism (CP)** : CP is a specialized strategy that is essential for training models with very long sequence lengths. Its primary function is to manage the memory consumption of activations, which grows quadratically with sequence length and can exceed HBM capacity. CP shards the sequence dimension of the activation tensors, which allows for the use of a fractional per-device batch size. Because CP introduces more communication than FSDP, the general rule is to use the minimum degree of CP necessary to satisfy memory constraints and ensure the batch axis shard remains an integer.


The following table maps common workload types to the optimal sharding strategy:  
| Workload type  | Recommended primary sharding  | Secondary sharding  | Key bottlenecks  | Rationale  |  
| --- | --- | --- | --- | --- |  
| Dense model - short sequence  | FSDP  | N/A  | Rematerialization, FF Matmuls  | FSDP provides the best balance. With short sequences, activation memory may not be a major concern. The key is a large enough global batch to hide FSDP's weight All-Gather. As the batch size increases, activation size increases, and a suitable rematerialization policy is required to ensure this configuration does not run out of memory.  |  
| Dense model - long sequence  | FSDP  | CP  | Flash attention, activation memory  | Activation memory becomes the primary constraint. CP is required to enable fractional per-device batch sizes and avoid out-of-memory (OOMs) issues. Flash attention is the dominant source of compute and wasted time.  |  
| MoE model - short sequence  | FSDP + EP  | N/A  | All-to-All (Expert routing), rematerialization  | MoE models require EP to shard the experts. The All-to-All communication for token routing is a major bottleneck that must be overlapped. Rematerialization is also a significant source of waste.  |  
| MoE model - very large scale  | FSDP + EP + PP  | Model parallelism (MP)  | All previously mentioned bottlenecks, plus pipeline bubbles  | For models that exceed the memory of a single pod, PP is needed to shard layers across pods. This introduces DCN communication and pipeline bubble overheads. This is a highly complex configuration requiring careful tuning.  |  
## Communication optimization
The primary mechanism for overlapping communication and computation on TPU7x is called _SparseCore Collective Offloading_. The Ironwood architecture includes dedicated SparseCore units, which act as independent threads of control capable of managing data movement over the ICI fabric. This allows collective communication operations (like All-Gather or Reduce-Scatter) to execute in parallel with the main computations happening on the TensorCores. This is the recommended method for asynchronous collectives on TPU7x. Use the [recommended flags](https://github.com/AI-Hypercomputer/maxtext/blob/c0abc4c0c0a98e02413d7b6c669927d013467045/benchmarks/xla_flags_library.py#L70-L116) to enable offloading for the most common collectives.
## Activation rematerialization
Activation rematerialization, also known as gradient checkpointing, is a fundamental technique for reducing the HBM footprint of a model. Instead of storing all intermediate activations from the forward pass in HBM to be used during the backward pass, it saves only a few key activations (checkpoints) and recomputes the others on-demand during the backward pass. This saves a significant amount of memory at the cost of increased computation (approximately 25-30% additional FLOPs for a standard transformer block).
The decision of how aggressively to apply rematerialization is a critical tuning parameter that depends entirely on the primary bottleneck, which often varies with sequence length.
**For long-sequence workloads** (such as 128k): In these cases, the size of the activation tensors is the dominant consumer of HBM. The workload is typically memory-bound. Therefore, applying an aggressive rematerialization policy is highly beneficial. The memory savings enable training to proceed without out-of-memory errors and also allow for larger batch sizes, and the computational overhead of recomputing is a worthwhile trade-off.
**For short-sequence workloads** (such as 8k): In these cases, activation memory is much less of a concern, and the workload is more likely to be compute-bound. The computational overhead of rematerialization can be the single largest source of inefficiency.
### Tuning rematerialization policies in MaxText
MaxText provides granular control over rematerialization through a set of preset and custom policies, configured using the `remat_policy` flag.
#### Preset policies
MaxText offers the following built-in policies:
  * **`full`**: The most aggressive policy, rematerializing almost everything. This minimizes HBM usage but maximizes recomputation overhead. Ideal for extremely memory-constrained, long-sequence scenarios.
  * **`minimal`**: The least aggressive policy, storing most activations. This maximizes HBM usage but minimizes recomputation. Best for short-sequence, compute-bound workloads where memory is not a concern.
  * **Intermediate policies** : Options like `save_dot_with_context_except_mlp`, `save_qkv_proj`, and `save_out_proj` provide various trade-offs by selectively checkpointing the outputs of expensive dot-product operations while rematerializing cheaper element-wise operations.


#### Custom policies
For a greater level of control, you can set `remat_policy` to `custom`. This lets you specify the behavior for individual layers within the model's decode module. Each layer can be assigned one of three behaviors:
  * **`device`**: The activation is stored in HBM on the TPU device.
  * **`remat`**: The activation is discarded and will be rematerialized during the backward pass.
  * **`offload`**: The activation is moved from HBM to the CPU host's memory, freeing up HBM at the cost of PCIe transfer latency.


## Scoped VMEM tuning
Kernel performance, like flash attention, depends on the selected tile sizes in the kernel, whose size is limited by the available vector memory (VMEM). Each of the two TensorCores in a TPU7x chip has 64 MiB of vector memory (VMEM). This VMEM capacity can be split between current scope (scoped VMEM) and future weight prefetch. Increasing scoped VMEM allows increasing the tile sizes in the kernel, potentially reducing memory stalls and increasing kernels' performance. You can alter the scoped VMEM size by setting `xla_tpu_scoped_vmem_limit_kib` (in `LIBTPU_INIT_ARGS`), which can be used to explore the kernel performance as well as end-to-end performance limits. Optimizing scoped VMEM size can indirectly affect custom Pallas kernel performance since increasing scoped VMEM unlocks a larger hyperparameter search space for in-kernel tile sizes.
## Tokamax kernels
[Tokamax](https://github.com/openxla/tokamax/tree/main), a high-performance JAX kernels library with many highly optimized TPU kernels, addresses several common hardware-specific bottlenecks:
  * **Splash attention** : Splash attention is used as the primary attention implementation to eliminate the HBM bottleneck of standard attention and uses the most efficient attention implementation on TPUs.
  * **Megablox Grouped Matrix Multiplication (GMM)** : For MoE workloads, Megablox efficiently handles grouped matrix multiplications by computing over the ragged activations representation. It efficiently maps over the ragged dimension, computing matrix multiplications between ragged groups of rows in LHS, and the corresponding expert matrix, avoiding the need to pad batches to a fixed size.
  * **Empirical tuning with`tune-jax`** : The `tune-jax` library has utilities to perform empirical searches for optimal block sizes. Default kernel sizes are often suboptimal; tuning allows choosing hardware-friendly VMEM tile sizes to maximize hardware utilization.
  * **Max logits estimate** : The Tokamax Splash attention kernel can further be optimized by setting a value for `max_logit_const`. If set, it replaces the reduction calculation of the max logit during the softmax operation of attention (softmax(Q * KT)), reducing some computational and synchronization overhead. In MaxText, it is implemented by the config `use_max_logits_estimate`, which can be set to `None` (disabled) or a floating point value. Verify that the logit range of your specific model remains compatible with the estimate to prevent numerical overflow. Convergence testing is recommended if this value is set.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-22 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
  * ### Products and pricing
    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support
    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources
    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage
    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)


[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg) ](https://developers.google.com/)
  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)


  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * [ Manage cookies ](https://docs.cloud.google.com/tpu/docs/ironwood-performance)
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어