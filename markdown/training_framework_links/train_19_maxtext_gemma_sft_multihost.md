---
id: "train_19_maxtext_gemma_sft_multihost"
title: "MaxText multi-host Gemma SFT"
url: "https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext"
category: "Training framework links"
description: "Multi-host v6e/GKE recipe for Gemma 4 31B SFT with MaxText, Cluster Toolkit, UltraChat, and export back to Hugging Face format."
crawled_at: "2026-10-26T12:47:17.390435+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext#main-content)
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
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/ai-hypercomputer-color.svg) ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)


[Start free](https://console.cloud.google.com/freetrial)
[ Overview ](https://docs.cloud.google.com/ai-hypercomputer/docs) [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview) [ Resources ](https://docs.cloud.google.com/ai-hypercomputer/docs/release-notes)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
  * [ Documentation  ](https://docs.cloud.google.com/docs)
    * More 
    * [ Overview  ](https://docs.cloud.google.com/ai-hypercomputer/docs)
    * [ Guides  ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
    * [ Resources  ](https://docs.cloud.google.com/ai-hypercomputer/docs/release-notes)
  * [ Console  ](https://console.cloud.google.com/)


  * Discover
  * [Overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
  * [Choose your accelerator infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure)
  * [Choose an orchestrator and deployment option](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-platform)
  * Accelerators
    * [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus)
    * [General GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)
    * [Clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)
  * Performance-optimized infrastructure
    * Networking services
      * [GPU networking overview](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview)
      * [Network services for deployments](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-services)
      * [Networking best practices](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-best-practices)
    * [Storage services](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)
  * Open software
    * [OS and Docker images](https://docs.cloud.google.com/ai-hypercomputer/docs/images)
  * [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models)
  * Cluster management
    * [Cluster management overview](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities)
    * [Cluster management configurations](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations)
  * [Terminology](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology)
  * Get started
  * [Plan and create your AI infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview)
  * [Choose between general GPUs and clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy)
  * [Design your AI infrastructure with Gemini](https://docs.cloud.google.com/ai-hypercomputer/docs/design-with-gemini)
  * Obtain capacity and quota
    * [Overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity)
    * [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity)
    * [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity)
  * Quickstarts
    * [Create a fully managed Slurm cluster with A4 VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-managed-slurm-cluster-with-a4)
    * [Create a self-managed Slurm cluster with A4 VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-slurm-cluster-with-a4)
  * Deploy infrastructure
  * [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview)
  * [Compact placement policy and workload policy overview](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy)
  * Deploy AI-optimized VMs and clusters
    * Create GKE clusters
      * [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)
      * [Create an AI-optimized GKE cluster that uses A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max)
      * [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x)
      * [Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)
      * [Create a GKE Standard cluster that uses A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega)
      * [Create a GKE Autopilot cluster that uses A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-autopilot-a3-high-mega)
      * [Create an AI-optimized GKE cluster that uses A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a3-edge)
      * [Create an AI-optimized GKE cluster that uses A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a2)
      * [Create an AI-optimized GKE cluster that uses G2 or G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-g2-g4)
      * [Create an AI-optimized GKE cluster that uses N1](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-n1)
    * Create Slurm clusters
      * [Create a fully managed cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
      * [Create a self-managed cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)
    * Create an instance
      * [Create A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instance)
      * [Create A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a4x)
      * [Create A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm)
      * [Create A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-high-mega)
      * [Create A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-edge)
      * [Create A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a2)
      * [Create G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g4)
      * [Create G2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g2)
      * [Create N1 with GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-n1)
    * Create instances in bulk
      * [Create A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instances-in-bulk)
      * [Create A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a4x)
      * [Create A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk)
      * [Create A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-high-mega)
      * [Create A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-edge)
      * [Create A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a2)
      * [Create G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-g4)
      * [Create G2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-g2)
      * [Create N1 with GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-n1)
    * Create a managed instance group (MIG)
      * [Create A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-mig)
      * [Create A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4x)
      * [Create A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra)
      * [Create A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-high-mega)
      * [Create A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-edge)
      * [Create A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a2)
      * [Create G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-g4)
      * [Create G2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-g2)
      * [Create N1 with GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-n1)
  * Run workloads
  * Run workloads with Pathways on Cloud
    * [Introduction to Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro)
    * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
    * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
    * [Run an interactive workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
    * [Perform multihost inference using Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
    * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
    * [Port JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
    * [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)
  * Schedule GKE workloads
    * [Schedule workloads with Topology Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas)
    * [Enable node health prediction](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction)
  * [Use Kueue to orchestrate workloads](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro)
  * AI workload tutorials
    * [Overview](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials)
    * GPU
      * Run inference with vLLM on GKE
        * [DeepSeek V3.1](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/deepseek-vllm-inference)
        * [DeepSeek V3.2-Speciale](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/vllm-gke-deepseek-speciale)
        * [Gemma 3](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-vllm-inference)
        * [GPT-OSS](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gpt-oss-vllm-inference)
        * [Llama 4](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/vllm-gke-llama4)
        * [Qwen3](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/qwen3-vllm-inference)
      * Run fine-tuning
        * [Gemma 4 on a GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-cluster)
        * [Gemma 4 on a multi-host GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-multi-host-cluster)
        * [Gemma 3 on a multi-host GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma3-finetune-a4-gke-multi-host-cluster)
        * [Gemma 3 on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-slurm-cluster)
        * [Gemma 3 for vision tasks on GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/use-ray-fine-tune-gemma-vision-task-gke)
        * [Llama 4 on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/fsdp-llama4)
        * [Mixtral-8x7b on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/fsdp-mixtral-8x7b)
      * Run training
        * [Qwen2 on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/train-qwen2-a4-slurm-cluster)
    * TPU
      * Serve workloads
        * [Serve Qwen3.5-397B with vLLM TorchTPU on TPU7x](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-vllm-torchtpu)
        * [Serve Gemma 4 26B with multi-host vLLM TorchTPU on Trillium TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-gemma4-26b-gke-trillium-vllm)
        * [Serve Qwen3.5-397B with multi-host vLLM TorchTPU on TPU7x](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-multi-host-vllm-torchtpu)
        * [Serve Qwen3-Coder-480B with multi-host SGLang TorchTPU on TPU7x](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-coder-gke-ironwood-multi-host-torchtpu)
      * Run fine-tuning
        * [Run SFT for Gemma 4 31B on multi-host TPU v6e](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext)
        * [Run supervised fine-tuning on a TPU VM with MaxText](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext)
        * [Run RL training on a v6e-8 TPU VM](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-rl-v6e-8-tpu-vm)
        * [Run multi-host RL training for Gemma 4 26B on TPU v6e](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-26b-rl-maxtext)
        * [Run multi-host RL training on Qwen3-30B-A3B on TPU v6e](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-qwen3-30b-a3b-rl-maxtext)
  * Manage infrastructure
  * Manage GKE clusters
    * [View GKE node topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/node-topology)
    * [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters)
  * Manage instances and Slurm clusters
    * [View topology of an instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
    * Manage host events
      * [Host events in instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)
      * [Host events in reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations)
    * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)
  * Test and optimize
  * [Optimize cluster networking by using NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview)
  * Integrating NCCL/gIB into your workload
    * [Install gIB NCCL plugins](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl)
    * [Use gIB NCCL plugins in NVIDIA NGC containers](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/ngc-containers)
  * Run NCCL tests
    * [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms)
    * [Run NCCL on GKE clusters that use Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke)
    * [Run NCCL on GKE clusters that use A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x-max)
    * [Run NCCL on GKE clusters that use A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x)
    * [Run NCCL on GKE clusters that use A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom)
    * [Run NCCL on GKE clusters that use A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a3-mega-high)
    * [Run NCCL on GKE clusters that use A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a3-edge)
    * [Run NCCL on Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm)
  * [Collect and understand NCCL logs for troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand)
  * Test workloads with recipes
    * [Benchmarking recipes](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview)
    * [Goodput optimization recipes](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/goodput-recipes)
  * NCCL/gIB release notes
    * [NCCL/gIB release notes (x86 64-bit)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-x86)
    * [NCCL/gIB release notes (ARM 64-bit)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-arm64)
  * Monitor
  * [Monitor VMs and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * Manage how CoMMA collects NCCL telemetry
    * [Collective Communication Analyzer (CoMMA)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma)
    * [Enable, disable, and configure CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma)
  * Troubleshoot
  * [Known issues](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/known-issues)
  * [Troubleshoot slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance)
  * [Troubleshoot reporting a faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api)
  * [Troubleshoot CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-comma)


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
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)


Send feedback 
#  Run SFT for Gemma 4 31B on multi-host TPU v6e Stay organized with collections  Save and categorize content based on your preferences. 
This tutorial shows you how to run supervised fine-tuning (SFT) on a multi-host Tensor Processing Unit (TPU) v6e cluster by using MaxText and Cluster Toolkit. You use Cluster Toolkit to execute a multi-host training workload and export the results back to Hugging Face format for serving.
## Workload summary
Running this SFT workload on Cloud TPU and GKE involves the following components:
  * **Model:** Gemma 4 31B (`google/gemma-4-31b-it`), an advanced open-weights model. In this tutorial, the model weights are downloaded from Hugging Face, converted into MaxText-compatible format, and deployed on a GKE cluster with Cloud TPU v6e (`v6e-32`) infrastructure.
  * **Training method:** SFT using MaxText. The workload executes a scalable fine-tuning pipeline on Cloud TPU v6e using JAX. It optimizes model parameters over 1000 steps using MaxText's built-in SFT trainer (`maxtext.trainers.post_train.sft.train_sft`) and instruction-tuning datasets.
  * **Dataset and template:** UltraChat 200k (`HuggingFaceH4/ultrachat_200k`), a large-scale, high-quality multi-turn dialogue dataset. The workload uses this dataset to fine-tune the model and improve its conversational and instruction-following capabilities.
  * **Infrastructure and framework:** GKE, managed using Cluster Toolkit, on Cloud TPU v6e (`v6e-32`, with a `4x8` topology). The framework is MaxText (`tpu_post_training:0.2.4`) with a JAX backend.


## Objectives
  * Install Cluster Toolkit and its dependencies.
  * Deploy a Cluster Toolkit cluster.
  * Convert a Hugging Face model to MaxText format.
  * Run an SFT training workload on the TPU.
  * Convert the fine-tuned model back to Hugging Face format for serving.


## Costs
In this document, you use the following billable components of Google Cloud: 
  * [ Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [ Cloud TPU](https://cloud.google.com/tpu/pricing)
  * [ Cloud Storage](https://cloud.google.com/storage/pricing)
  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)


To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 
New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 
When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see [Clean up](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext#clean-up).
**Important:** To complete this tutorial, you must have access to `v6e-32` TPUs. This tutorial assumes that you already have a reservation for these TPUs in your Google Cloud project to ensure that you have the capacity available when you need it. To learn more about your options for reserving Cloud TPU capacity for a future date and time, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).
## Before you begin
  * You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:
    1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
    2. On the **Access tokens** page, click **Create new token**.
    3. Select the **Read** token type and enter a name for your token.
    4. Your access token is displayed. Save the token in a safe place.


  * On the [`google/gemma-4-31b-it` model card on Hugging Face](https://huggingface.co/google/gemma-4-31b-it), accept the license agreement for the model.


To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 
  * To complete this tutorial: 
    * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
    * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
    * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
    * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)


For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 
## Set up your environment variables
Set up your environment variables:

```
export PROJECT="YOUR_PROJECT_ID"
export REGION="YOUR_REGION"
export ZONE="YOUR_ZONE"
export CLUSTER_NAME="YOUR_CLUSTER_NAME"
export GCS_BUCKET="YOUR_BUCKET_NAME"
export CLOUD_IMAGE_NAME="us-docker.pkg.dev/cloud-tpu-images/maxtext-images/tpu_post_training:0.2.4"
export TPU_TYPE="v6e-32"
export RESERVATION="YOUR_RESERVATION_NAME"
export HF_TOKEN="YOUR_HF_TOKEN"
export MODEL_NAME="gemma4-31b"
export CLUSTER_TOOLKIT_VERSION="v1.103.0"
```

Replace the following:
  * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
  * `YOUR_REGION`: the region where your TPU reservation is located and where you deploy your cluster.
  * `YOUR_ZONE`: the zone where your TPU reservation is located and where you deploy your cluster.
  * `YOUR_BUCKET_NAME`: a globally unique name for a Cloud Storage bucket.
  * `YOUR_RESERVATION_NAME`: the name of your TPU v6e reservation.
  * `YOUR_HF_TOKEN`: your Hugging Face access token.


By default, the script sets `MODEL_NAME` to `gemma4-31b` (the MaxText model name for `google/gemma-4-31b-it`) and `CLUSTER_NAME` to `gke-tpu-v6e`. If you customize `CLUSTER_NAME`, the name must start with a lowercase letter, contain only lowercase letters, numbers, and hyphens, and be 20 characters or fewer so that generated service account IDs stay within the 30-character limit.
## Install Cluster Toolkit dependencies
To complete this tutorial from a Linux or macOS client or workstation, follow the relevant steps in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) in the Cluster Toolkit documentation.
If you're using Cloud Shell, then you can skip this section.
## Install Cluster Toolkit
Download and extract the prebuilt bundle for the specific version of Cluster Toolkit defined in `CLUSTER_TOOLKIT_VERSION` (`v1.103.0`) into your current working directory:

```
case "$(uname -s)-$(uname -m)" in
  Linux-x86_64)              BUNDLE="gcluster_bundle_linux_amd64.tgz" ;;
  Linux-aarch64|Linux-arm64) BUNDLE="gcluster_bundle_linux_arm64.tgz" ;;
  Darwin-x86_64)             BUNDLE="gcluster_bundle_mac_amd64.tgz" ;;
  Darwin-arm64)              BUNDLE="gcluster_bundle_mac_arm64.tgz" ;;
  *) BUNDLE=""; echo "Unsupported platform: $(uname -s)-$(uname -m)" >&2 ;;
esac
mkdir -p cluster-toolkit
curl -fsSL "https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/${CLUSTER_TOOLKIT_VERSION:?}/${BUNDLE:?}" \
  | tar -xz -C cluster-toolkit
cd cluster-toolkit
```

**Note:** The [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install-bundle) documentation describes how to download the latest release into a `cluster-toolkit` directory. However, because blueprint variables can differ across Cluster Toolkit versions, for this tutorial you must install the exact version specified in `CLUSTER_TOOLKIT_VERSION` (`v1.103.0`) rather than the latest release. Extracting the bundle provides the `gcluster` binary and the `examples/` blueprints that you use in the steps that follow. If you extracted the bundle into a `cluster-toolkit` directory, make sure that you change to that directory (`cd cluster-toolkit`) before running the subsequent commands.
## Authenticate your environment
To ensure that Cluster Toolkit can provision resources and push images to Artifact Registry on your behalf, authenticate the Google Cloud CLI and set your Application Default Credentials:

```
gcloud auth login
gcloud auth application-default login --no-launch-browser
gcloud config set project "${PROJECT:?}"
gcloud auth application-default set-quota-project "${PROJECT:?}"

gcloud auth configure-docker gcr.io --quiet
gcloud auth configure-docker "${REGION:?}-docker.pkg.dev" --quiet
```

## Create your Cluster Toolkit cluster
To create and deploy a Cluster Toolkit cluster with 32 `v6e` TPU chips, complete the following steps:
  1. Create a Cloud Storage bucket:

```
gcloud storage buckets create "gs://${GCS_BUCKET:?}" --project="${PROJECT:?}" --location="${REGION:?}" || true
```

  2. Stage the blueprint configuration and copy the example deployment blueprint to an isolated working directory:

```
mkdir -p tmp
cp examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml tmp/
```

  3. Update `tmp/gke-tpu-v6e-advanced.yaml` to grant your cluster node pool service account (`gke-np-sa`) the Storage Admin role (`roles/storage.admin`) for writing checkpoints to your Cloud Storage bucket, switch the system node pool machine type to `e2-standard-8`, and pin the system node pool to your target zone to avoid regional machine-type stockouts:

```
# Grant the GKE Node Pool Service Account storage.admin access for checkpoint writes
sed -i "s/- storage.objectViewer/- storage.admin/" tmp/gke-tpu-v6e-advanced.yaml
# Change n2-standard-8 to e2-standard-8 to avoid GCE_STOCKOUT in some regions
sed -i "s/n2-standard-8/e2-standard-8/" tmp/gke-tpu-v6e-advanced.yaml
# Pin system node pool to a single zone to avoid cross-zone stockouts
sed -i '/system_node_pool_machine_type/a \      system_node_pool_zones: [$(vars.zone)]' tmp/gke-tpu-v6e-advanced.yaml
```

  4. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy your Cluster Toolkit cluster by using the blueprint `tmp/gke-tpu-v6e-advanced.yaml` and passing the required variables by using the `--vars` flag:

```
./gcluster deploy tmp/gke-tpu-v6e-advanced.yaml \
    --vars "project_id=${PROJECT:?},deployment_name=${CLUSTER_NAME:?},region=${REGION:?},zone=${ZONE:?},num_slices=1,tpu_topology=4x8,authorized_cidr=0.0.0.0/0,reservation=${RESERVATION:-}" \
    --download-dependencies \
    -l IGNORE \
    --auto-approve -w
```

## Convert the model to MaxText format
To train the model in MaxText format, you must convert it from Hugging Face format to MaxText format.
  1. To simplify subsequent commands, use the [`gcluster job config` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-config) to configure your default project, cluster, and location:

```
# Configure gcluster Defaults
./gcluster job config set project "${PROJECT:?}"
./gcluster job config set cluster "${CLUSTER_NAME:?}"
./gcluster job config set location "${REGION:?}"
```

  2. Use the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) to convert the model from Hugging Face format to MaxText format and store it in your Cloud Storage bucket:

```
./gcluster job submit --name hf-to-mt \
    --compute-type "${TPU_TYPE:?}" \
    --num-slices 1 \
    --image "${CLOUD_IMAGE_NAME:?}" \
    --await-job-completion \
    --command "[ \"\$JOB_COMPLETION_INDEX\" != \"0\" ] || \
      python3 -m maxtext.checkpoint_conversion.to_maxtext \
        model_name=${MODEL_NAME:?} \
        hf_access_token=${HF_TOKEN:?} \
        base_output_directory=gs://${GCS_BUCKET:?}/${MODEL_NAME}/max-text-format/ \
        scan_layers=True \
        use_multimodal=False \
        skip_jax_distributed_system=true \
        checkpoint_storage_use_zarr3=0 \
        checkpoint_storage_use_ocdbt=0 \
        hardware=cpu \
        --lazy_load_tensors=True"
```

The command includes the `--await-job-completion` flag, which means that it waits in your current terminal until the conversion finishes.
  3. Optional: To stream the conversion logs while the job is running, open a separate terminal in the working directory where you extracted `gcluster`, and run the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs):

```
# Use the list command to check status
./gcluster job list

# Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
./gcluster job logs hf-to-mt --main-only -f
```

  4. In your original terminal, verify that the converted model files are available in your Cloud Storage bucket:

```
gcloud storage ls "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/max-text-format/"
```

## Start the training workload
  1. After the conversion process has completed, start the SFT workload:

```
./gcluster job submit --name sft \
    --compute-type "${TPU_TYPE:?}" \
    --num-slices 1 \
    --image "${CLOUD_IMAGE_NAME:?}" \
    --await-job-completion \
    --command "JAX_PLATFORMS=tpu,cpu ENABLE_PJRT_COMPATIBILITY=true JAX_TRACEBACK_FILTERING=off LIBTPU_INIT_ARGS=' --xla_tpu_scoped_vmem_limit_kib=61440 --xla_tpu_bf16_emission_mode=NATIVE_EMISSION --xla_tpu_enable_sparse_core_collective_offload_all_reduce=true --xla_tpu_use_single_sparse_core_for_all_gather_offload=true ' \
      python3 -m maxtext.trainers.post_train.sft.train_sft \
      run_name=sft \
      base_output_directory=gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/trained/ \
      model_name=${MODEL_NAME} \
      load_parameters_path=gs://${GCS_BUCKET}/${MODEL_NAME}/max-text-format/0/items/ \
      hf_access_token=${HF_TOKEN:?} \
      dataset_type=hf \
      hf_path=HuggingFaceH4/ultrachat_200k \
      per_device_batch_size=1 steps=1000 \
      profiler=xplane \
      checkpoint_storage_use_zarr3=0 \
      checkpoint_storage_use_ocdbt=0 \
      skip_jax_distributed_system=False"
```

The command includes the `--await-job-completion` flag, which means that it waits in your current terminal until the training job finishes.
  2. Optional: To stream the live training logs while the job is running, open a separate terminal in the working directory where you extracted `gcluster`, and run the `gcluster job logs` command:

```
# Use the list command to check status
./gcluster job list

# Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
./gcluster job logs sft --main-only -f
```

After initial XLA compilation completes, the coordinator logs output progress for each step across the 1000-step run in the format `completed step: <step>, seconds: ..., TFLOP/s/device: ..., loss: ...`, with the training loss decreasing from approximately `1.57` at step 5 to approximately `0.82` at step 1000. Before you proceed to the next section, wait until step 1000 finishes and the output from the `./gcluster job list` command shows the status of `sft` as `Succeeded`.
**Note:** Completed JobSets on GKE are automatically cleaned up after their configured time to live (TTL) expires, which is one hour by default (`--gke-ttl-after-finished=1h`). Completed workloads are not listed in the output of the `./gcluster job list` command after their TTL expires; however, all checkpoints and model weights are stored in your Cloud Storage bucket.
  3. In your original terminal, verify that the SFT training checkpoints are generated in your Cloud Storage bucket:

```
gcloud storage ls "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/trained/sft/checkpoints/1000/model_params/"
```

## Convert the trained model back into Hugging Face format
  1. After the training workload has completed, convert the model back to Hugging Face format:

```
./gcluster job submit --name mt-to-hf \
    --compute-type "${TPU_TYPE:?}" \
    --num-slices 1 \
    --image "${CLOUD_IMAGE_NAME:?}" \
    --await-job-completion \
    --command "[ \"\$JOB_COMPLETION_INDEX\" != \"0\" ] || \
      python3 -m maxtext.checkpoint_conversion.to_huggingface \
        model_name=${MODEL_NAME:?} \
        hf_access_token=${HF_TOKEN:?} \
        load_parameters_path=gs://${GCS_BUCKET:?}/${MODEL_NAME}/trained/sft/checkpoints/1000/model_params/ \
        base_output_directory=gs://${GCS_BUCKET}/${MODEL_NAME}/hf-trained/ \
        skip_jax_distributed_system=true \
        hardware=cpu \
        scan_layers=True \
        use_multimodal=False \
        weight_dtype=bfloat16 \
        --override_model_architecture"
```

The command includes the `--await-job-completion` flag, which means that it waits in your current terminal until the conversion finishes.
  2. Optional: To stream the live conversion logs while the job is running, open a separate terminal in the working directory where you extracted `gcluster`, and run the `gcluster job logs` command:

```
# Use the list command to check status
./gcluster job list

# Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
./gcluster job logs mt-to-hf --main-only -f

# The trained model is now available in gs://${GCS_BUCKET}/${MODEL_NAME}/hf-trained/ 
```

  3. In your original terminal, verify that the final Hugging Face Safetensors weights are generated in your Cloud Storage bucket:

```
gcloud storage ls -l --readable-sizes "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/hf-trained/"
```

## Clean up
To avoid incurring additional charges, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to delete the resources created during this tutorial:

```
./gcluster destroy "${CLUSTER_NAME:?}" --robust --auto-approve
gcloud storage rm -r "gs://${GCS_BUCKET:?}"

# To delete the local deployment folder and staged blueprint
rm -rf .ghpc "${CLUSTER_NAME:?}" tmp
```

## What's next
  * For more information about Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * For architecture and configuration details for the `v6e-32` TPU, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).


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
  * [ Manage cookies ](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext)
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