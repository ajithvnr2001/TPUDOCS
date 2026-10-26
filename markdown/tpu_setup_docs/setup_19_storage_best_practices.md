---
id: "setup_19_storage_best_practices"
title: "Cloud TPU storage best practices"
url: "https://docs.cloud.google.com/tpu/docs/storage-best-practices"
category: "TPU setup docs"
description: "Choose storage for data loading, model weights, and synchronous or asynchronous checkpoints."
crawled_at: "2026-10-26T12:45:23.516359+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/tpu/docs/storage-best-practices#main-content)
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
# Storage best practices for AI/ML workloads on TPU VMs
To maximize the performance and cost-efficiency of your AI/ML workloads on TPU VMs, select and configure the right storage solution for your workload. By removing I/O bottlenecks, you can reduce the amount of time that your TPU accelerators are idle, which reduces training time and costs.
This document provides workload-specific storage recommendations and optimization best practices for training, checkpointing, serving, and caching on TPU VMs. Before applying these practices, review the available [Storage options for TPU data](https://docs.cloud.google.com/tpu/docs/storage-options). This document assumes that you are familiar with TPU VMs and have basic experience provisioning Cloud Storage resources.
## Workload-specific guidance
The following table provides storage recommendations, listed in order of preference, for different workloads:  
| Workload  | Recommendation  | Optimization and tooling (if applicable)  |  
| --- | --- | --- |  
| **Training datasets, including data preparation**  | 
  1. Use [Cloud Storage regional buckets](https://docs.cloud.google.com/storage/docs/buckets) with [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) and client-side tuning (such as read-ahead reads) for the lowest cost. 
  2. Use [Cloud Storage Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) for the best performance and scale. 
  3. Use [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) if you're standardizing on Lustre (file system storage) due to high metadata concurrency or small files (less than 1 MB). 

 | 
  * For regional Cloud Storage buckets, enable [hierarchical namespace](https://docs.cloud.google.com/tpu/docs/storage-best-practices#hierarchical-namespace). 
  * For regional Cloud Storage buckets or Rapid Bucket, use Cloud Storage FUSE and [gRPC](https://grpc.io/). For GKE, use the [`gcsfusecsi-training` profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles#select-performance-profile). 
  * For Managed Lustre, consider using the Dynamic tier to reduce costs and automatically optimize performance. 

 |  
| **Checkpointing and reinforcement learning weights**  | 
  1. Use [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) for high performance without extensive tuning for low latency (less than 1 ms) requirements, such as synchronous checkpoints and high-speed weight propagation for reinforcement learning. 
  2. Use [Cloud Storage Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) for the highest throughput for asynchronous and multi-tiered checkpointing and parallelizing checkpoint operations to storage. Rapid Bucket provides the high throughput needed for these workloads. 

 |  For Rapid Bucket, use the [`gcsfusecsi-checkpointing` profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles#select-performance-profile).   |  
| **Model storage and download**  | 
  1. Use [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml) for small model caching and up to 2,500 instances. 
  2. Use the same storage solution that you use for training datasets (Managed Lustre, Rapid Bucket, or regional buckets) if you want to standardize on a single storage solution. 

 |  For downloading models, use [GKE Run:ai Model Streamer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer) or Cloud Storage FUSE with a separate mount point using the [`gcsfusecsi-serving` profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles#select-performance-profile).   |  
| **Key-value (KV) cache offload**  | 
  1. Always use host CPU memory (RAM) as the primary tier to free up VRAM without adding significant latency. 
  2. If CPU memory is insufficient, use [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) as a parallel, low-latency second tier in the cache hierarchy to meet the ultra low latency (less than 1 ms) needs of KV cache offloading at high throughput (up to 10 TB/s). 

 |   |  
## Cloud Storage optimizations
The following sections describe best practices to optimize performance when using Cloud Storage with TPU VMs.
### Enable hierarchical namespace for metadata optimization
To improve metadata performance, enable hierarchical namespace when you create regional buckets for AI/ML workloads. Metadata performance refers to how quickly Cloud Storage can process operations that involve looking up, listing, or modifying object paths and folders, rather than reading or writing the file contents themselves.
In buckets without hierarchical namespace enabled, folders don't exist as actual resources, but are instead [simulated folders](https://docs.cloud.google.com/storage/docs/folder-types) represented by object name prefixes delimited by forward slashes (`/`). This makes operations like listing directory contents or renaming directories slow because the system must scan all objects with that prefix. Hierarchical namespace provides a true file system structure, which is important for AI/ML workloads for several reasons:
  * **Atomic directory renames** : ML frameworks use directory renames to finalize checkpoints. Hierarchical namespace supports atomic renames, ensuring that checkpoints are finalized quickly.
  * **Higher initial QPS** : Hierarchical namespace supports up to eight times higher initial queries per second (QPS) for reads and writes compared to buckets without hierarchical namespace enabled. This prevents bottlenecks when many TPUs access storage simultaneously.
  * **Efficient folder-level operations** : Finding and listing files within specific directories is much faster, reducing response times during training and data loading.


Zonal buckets, offered through Rapid Bucket, use hierarchical namespace by default. For more information, see [Hierarchical namespace overview](https://docs.cloud.google.com/storage/docs/hns-overview).
### Use Cloud Storage FUSE with appropriate profiles
[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) is a FUSE adapter that lets you mount buckets as a local file system. When using Google Kubernetes Engine, we recommend using the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) and the [Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles) to automate performance tuning.
For more information about best practices for using Cloud Storage FUSE, see [Performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).
## Customize the TPU VM boot disk
You can customize the guest OS environment on a TPU VM by using startup scripts or by creating custom images. Customizing the boot disk is useful for the following scenarios:
  * **Pre-loading software and libraries** : Install specific ML frameworks, dependencies, or custom software to reduce VM startup time and ensure consistent environments.
  * **Using non-standard OS distributions** : Use an OS distribution or version not included in the [Google-managed list](https://docs.cloud.google.com/tpu/docs/tpu-os-images#google-managed_os_images).
  * **Applying security and monitoring configurations** : Apply custom security settings, install monitoring agents, or set environment variables.


However, boot disk recovery for TPU VMs is limited. You can't detach or snapshot the boot disk for offline repair, so use caution when making changes that affect the boot process. By following these best practices, you can reduce the risk of boot failures when customizing your TPU VM environments.
Keep the following key principles in mind when customizing your boot disk:
  * **Minimize boot disk modifications** : Whenever possible, install applications and store data on Persistent Disk or Hyperdisk volumes rather than heavily modifying the boot disk.
  * **Use UUIDs for mounting** : When adding entries to the `/etc/fstab` file, always use UUIDs to identify disks and partitions (`UUID=...`) rather than device names like `/dev/sdb1`. Auto-generated device names are not guaranteed to be stable across reboots.


Follow these recommendations to reduce the risk of boot failures when making system changes:
  * **Error handling** : Implement robust error checking and graceful failure modes in your scripts. Log detailed messages to the serial console and Cloud Logging to aid in debugging.
  * **Critical dependencies** : Be extremely careful when modifying files essential for booting, such as the `/etc/fstab` file, network configurations, or bootloader settings. A syntax error or incorrect entry can render the VM unbootable.
  * **Secondary disks** : If your script relies on secondary disks, ensure it handles cases where the disk might not be present or takes longer to attach than expected. Avoid making the boot process critically dependent on secondary disk mounts unless absolutely necessary.
The following are examples of recommended and not recommended `/etc/fstab` entries for mounting a secondary disk:
    * **Recommended** : `UUID=a1b2c3d4-e5f6-7890-1234-567890abcdef /mnt/mydata ext4 defaults,nofail 0 2`
    * **Not recommended** : `/dev/sdb1 /mnt/mydata ext4 defaults 0 2`
Using the `nofail` option can prevent the system from halting if the disk isn't found, but ensure your application can handle the mount point being unavailable.
  * **Package management** : Be cautious when adding third-party repositories. Ensure they are trusted and compatible with the base OS image. Understand the dependencies of any packages you install and their potential impact on system libraries.
  * **Disk space** : Monitor boot disk usage. Extensive logging or large software installations can fill the boot disk, preventing the VM from starting.
  * **Logging** : Configure your applications and scripts to log verbosely to the serial console, as this is the primary tool for diagnosing boot issues on TPU VMs.


## Plan your storage capacity
It's important to plan the amount of storage capacity that your workload will need to fully utilize your accelerators. This includes the storage capacity and checkpoint bandwidth.
### Estimate storage
You can use the following estimates as a starting point for your storage requirements:  
| Workload type  | Dataset storage  | Checkpoint storage  |  
| --- | --- | --- |  
| LLM pre-training  | 2 TB per TPU  | 200 GB per TPU  |  
| Multimodal training  | 12 TB per TPU  | 1 TB per TPU  |  
| Inference  | 1 TB per TPU  | 1 GB per TPU  |  
### Estimate checkpoint bandwidth
You can estimate the minimum checkpointing bandwidth required for training workloads using the following formula. For data reads, multiple training runs, or training and inference, increase your estimated bandwidth requirements proportionally.
  1. **Checkpoint size** : _Number of parameters_ ×  _bytes per parameter_ (approximately 12-16 bytes per parameter for FP16 + optimizer state). Add a buffer (approximately 3×) for optimizer states and different precisions.
  2. **Checkpoint interval** : How often you save a checkpoint (for example, every 15 minutes).
  3. **Required bandwidth** : _Checkpoint size_ ÷  _checkpoint interval_.


The following example shows how to estimate the minimum checkpointing bandwidth for Qwen3-72B:
  1. **Checkpoint size** : 72B parameters × 12 bytes ≈ 864 GB per checkpoint. With buffer, 3 × 864 GB ≈ 2.5 TB.
  2. **Checkpoint interval** : 2 minutes = 120 seconds.
  3. **Required bandwidth** : 2.5 TB ÷ 120 seconds ≈ 20 GBps.


## Reference recipes
For examples of storage configurations for specific hardware and workloads, see the following recipes:
  * **TPU7x inference** : 
    * [Cloud Storage recipe](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/inference/ironwood/vLLM/GPT-OSS/README-gcs.md)
    * [Managed Lustre recipe](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/inference/ironwood/vLLM/GPT-OSS/README-lustre.md)
  * **TPU7x training** : 
    * [Cloud Storage recipe](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/deepseek3-671b/4k-bf16-tpu7x-4x8x8-gcs)
    * [Managed Lustre recipe](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/deepseek3-671b/4k-bf16-tpu7x-4x8x8-lustre)
    * [Provision Managed Lustre on GKE using Cluster Toolkit](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ct-lustre-tpu)


## Quotas and bandwidth limits
The bandwidth for Cloud Storage and Compute Engine offerings is limited by default quotas. If you exceed a quota, your input and output requests might be throttled.
For information about Cloud Storage quotas and how to request increases, see [Quotas & limits](https://docs.cloud.google.com/storage/quotas) in the Cloud Storage documentation. For information about Compute Engine quotas for Hyperdisk and Persistent Disk, see [Disk quotas](https://docs.cloud.google.com/compute/resource-usage#disk_quota).
## What's next
  * [Storage options for TPU data](https://docs.cloud.google.com/tpu/docs/storage-options)
  * [Connect TPU VMs to Cloud Storage buckets](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute)
  * [Attach durable block storage to a TPU VM](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute)
  * [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance)


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
  * [ Manage cookies ](https://docs.cloud.google.com/tpu/docs/storage-best-practices)
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