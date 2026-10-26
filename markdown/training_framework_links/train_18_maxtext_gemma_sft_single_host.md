---
id: "train_18_maxtext_gemma_sft_single_host"
title: "MaxText single-host Gemma supervised fine-tuning"
url: "https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext"
category: "Training framework links"
description: "Fine-tune Gemma on a v6e-8 TPU VM and convert checkpoints between Hugging Face and MaxText."
crawled_at: "2026-10-26T12:47:11.881220+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext#main-content)
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
#  Run supervised fine-tuning on a TPU VM by using MaxText Stay organized with collections  Save and categorize content based on your preferences. 
This tutorial provides a step-by-step guide for running supervised fine-tuning (SFT) on a single `v6e-8` Tensor Processing Unit (TPU) virtual machine (VM) instance on Google Cloud by using MaxText, a high-performance JAX-based training stack for large language models (LLMs).
## Workload summary
Running this SFT workload on a Cloud TPU VM involves the following components:
  * **Model:** Gemma 3 4B (`gemma3-4b`), an open-weights lightweight language model. In this tutorial, the model weights are converted from Hugging Face format into MaxText-compatible format (`mt-format`) and prepared for execution on a single Cloud TPU `v6e-8` VM using JAX.
  * **Training method:** SFT using MaxText. The workload executes a fine-tuning pipeline on a single Cloud TPU `v6e-8` instance using JAX. It optimizes model parameters over 1000 steps using MaxText's built-in SFT trainer (`maxtext.trainers.post_train.sft.train_sft`) and dialogue-focused instruction-tuning datasets.
  * **Dataset and template:** UltraChat 200k (`HuggingFaceH4/ultrachat_200k`), a large-scale, high-quality multi-turn dialogue dataset (`train_sft` split with `messages` column). It is used to fine-tune the model and improve its conversational and instruction-following capabilities.
  * **Infrastructure and framework:** a single Cloud TPU `v6e-8` VM instance (`ct6e-standard-8t`). The framework is MaxText (`maxtext[tpu-post-train]`) powered by JAX.


## Objectives
  * Set up a Cloud TPU VM instance.
  * Install MaxText and its dependencies.
  * Convert a Hugging Face model to MaxText format.
  * Run an SFT training workload on the TPU.
  * Convert the fine-tuned model back to Hugging Face format for serving.


## Costs
In this document, you use the following billable components of Google Cloud: 
  * [ Cloud TPU](https://cloud.google.com/tpu/pricing)


To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 
New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 
When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see [Clean up](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext#clean-up).
**Important:** To complete this tutorial, you must have access to `v6e-8` TPUs. This tutorial assumes that you already have a reservation for these TPUs in your Google Cloud project to ensure that you have the capacity available when you need it. To learn more about your options for reserving Cloud TPU capacity for a future date and time, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).
## Before you begin
  * You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:
    1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
    2. On the **Access tokens** page, click **Create new token**.
    3. Select the **Read** token type and enter a name for your token.
    4. Your access token is displayed. Save the token in a safe place.


  * On the [Hugging Face website](https://huggingface.co/), accept the license agreement for the model that you plan to train. This tutorial uses the model `gemma3-4b`.


To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 
  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.editor) (`roles/compute.editor`)


For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 
## Set up the environment
Set up your environment variables by running the following script:

```
export PROJECT="YOUR_PROJECT_ID"
export ZONE="YOUR_ZONE"
export RESERVATION="YOUR_RESERVATION_NAME"
export NAME="YOUR_TPU_NAME"
export NETWORK="default"
```

Replace the following:
  * YOUR_PROJECT_ID: your Google Cloud project ID
  * YOUR_ZONE: the zone that you want to use
  * YOUR_RESERVATION_NAME: your capacity reservation
  * YOUR_TPU_NAME: the name of your Cloud TPU VM instance


Authenticate with Google Cloud by running the following command:

```
gcloud auth login

```

## Create your Cloud TPU VM
Create a Cloud TPU VM instance with 8 `v6e` TPU chips, bound to your capacity reservation.

```
gcloud compute instances create "${NAME}" \
    --zone="${ZONE}" \
    --project="${PROJECT}" \
    --network="${NETWORK}" \
    --tags="${NAME}" \
    --machine-type=ct6e-standard-8t \
    --image-project=ubuntu-os-accelerator-images \
    --image-family=ubuntu-accel-2204-amd64-tpu-v5e-v5p-v6e \
    --boot-disk-size=200GB \
    --maintenance-policy=TERMINATE \
    --instance-termination-action=DELETE \
    --provisioning-model=RESERVATION_BOUND \
    --reservation-affinity=specific \
    --reservation="${RESERVATION}"
```

After the VM instance has been created, connect to it by using SSH.

```
gcloud compute ssh "${NAME}" --zone "${ZONE}" --project "${PROJECT}"
```

Complete the steps that follow within your TPU VM instance.
## Install MaxText
Update the system packages within the TPU VM instance.

```
sudo apt update && sudo apt upgrade -y --fix-missing
```

Install Python 3.12, which MaxText requires, and its virtual environment package.

```
sudo apt install -y build-essential cmake ninja-build
```

Use `uv` to speed up the installation of the Python package.

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "${HOME}/.local/bin/env"
```

Create a virtual environment named `maxtext_venv` and activate it.

```
uv python install 3.12
uv venv --python 3.12 --seed maxtext_venv
source maxtext_venv/bin/activate
```

Install MaxText and the dependencies that it requires for post-training tasks.

```
UV_TORCH_BACKEND=cpu uv pip install "maxtext[tpu-post-train]==0.2.2" --resolution=lowest
```

Install the remaining required dependencies by running the following command:

```
install_tpu_post_train_extra_deps
```

## Convert the model to MaxText format
To train the model in MaxText format, you must convert it from Hugging Face format to MaxText format.
Specify your environment variables, such as your Hugging Face access token, the name of the model that you want to use, and the directory where you want to save the model in MaxText format.

```
export HF_TOKEN="YOUR_HF_TOKEN"
export MODEL_NAME='gemma3-4b'
export MODEL_CHECKPOINT_DIRECTORY=/dev/shm/$MODEL_NAME/mt-format/
export USE_PATHWAYS=0 # Set to 1 for Pathways, 0 for McJAX
export LAZY_LOAD_TENSORS=False # True to use lazy load, False to use eager load.
```

Replace YOUR_HF_TOKEN with the Hugging Face access token that you previously created.
To convert the model from Hugging Face format to MaxText format, run the following script. This conversion takes about five minutes to complete.

```
python3 -m maxtext.checkpoint_conversion.to_maxtext \
    model_name="${MODEL_NAME?}" \
    hf_access_token="${HF_TOKEN?}" \
    base_output_directory="${MODEL_CHECKPOINT_DIRECTORY?}" \
    scan_layers=True \
    use_multimodal=False \
    hardware=cpu \
    skip_jax_distributed_system=true \
    checkpoint_storage_use_zarr3=$((1 - USE_PATHWAYS)) \
    checkpoint_storage_use_ocdbt=$((1 - USE_PATHWAYS)) \
    --lazy_load_tensors="${LAZY_LOAD_TENSORS?}"
```

## Start the training workload
After the conversion process has completed, you can start the SFT workload.
  1. Configure the SFT workload training parameters.

```
# -- MaxText configuration --
export BASE_OUTPUT_DIRECTORY=/dev/shm/$MODEL_NAME/post-train/
RUN_NAME=$(date +%Y-%m-%d-%H-%M-%S)
export RUN_NAME
export STEPS=1000
export PER_DEVICE_BATCH_SIZE=1

# -- Dataset configuration --
export DATASET_NAME="HuggingFaceH4/ultrachat_200k"
export TRAIN_SPLIT="train_sft"
export TRAIN_DATA_COLUMNS="['messages']"

export MAXTEXT_CKPT_PATH=$MODEL_CHECKPOINT_DIRECTORY/0/items
export TPU_ACCELERATOR_TYPE=v6e-8
export TPU_WORKER_ID=0
TPU_NAME=$(hostname)
export TPU_NAME
export TPU_SKIP_MDS_QUERY=1
export TPU_WORKER_HOSTNAMES=localhost
export TPU_TOPOLOGY=2x4
export TPU_CHIPS_PER_HOST_BOUNDS=2,4,1
export TPU_HOST_BOUNDS=1,1,1
```

  2. Start the training job. This takes about 10 minutes on a `v6e-8` VM instance.

```
python3 -m maxtext.trainers.post_train.sft.train_sft \
    run_name="${RUN_NAME?}" \
    base_output_directory="${BASE_OUTPUT_DIRECTORY?}" \
    model_name="${MODEL_NAME?}" \
    load_parameters_path="${MAXTEXT_CKPT_PATH?}" \
    per_device_batch_size="${PER_DEVICE_BATCH_SIZE?}" \
    steps="${STEPS?}" \
    hf_path="${DATASET_NAME?}" \
    train_split="${TRAIN_SPLIT?}" \
    train_data_columns="${TRAIN_DATA_COLUMNS?}" \
    profiler=xplane
```

## Convert the trained model back into Hugging Face format
After the training workload has completed, convert the model back to Hugging Face format.
  1. Set the paths for export and the trained parameters.

```
export HF_EXPORT=/dev/shm/$MODEL_NAME/hf-trained/
export POST_TRAIN_PATH=$BASE_OUTPUT_DIRECTORY/$RUN_NAME/checkpoints/$STEPS/model_params
```

  2. Run the conversion back to Hugging Face format.

```
python3 -m maxtext.checkpoint_conversion.to_huggingface \
    model_name="${MODEL_NAME}" \
    load_parameters_path="${POST_TRAIN_PATH}" \
    base_output_directory="${HF_EXPORT}" \
    scan_layers=True \
    use_multimodal=False \
    weight_dtype=bfloat16
```

After the conversion has completed, your tuned model stored in `/dev/shm/gemma3-4b/hf-trained` is ready to be used. Because you lose access to the contents of the `/dev/shm` folder when the VM reboots, you should move the tuned model to persistent storage or upload it to the Hugging Face Hub.
## Clean up
To avoid incurring additional charges, delete the resources created during this tutorial.
### Delete your TPU VM instance
Exit your Cloud TPU VM instance, and then delete it.

```
# 1. Delete TPU instance
echo "Deleting TPU instance: ${NAME}..."
gcloud compute instances delete "${NAME}" \
    --zone="${ZONE}" \
    --project="${PROJECT}" \
    --quiet || true

# 2. Delete IAP firewall rule
echo "Deleting firewall rule: ${FIREWALL_RULE_NAME}..."
gcloud compute firewall-rules delete "${FIREWALL_RULE_NAME}" \
    --project="${PROJECT}" \
    --quiet || true
```

## What's next
  * For more information about Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * For architecture and configuration details for the `v6e-8` TPU, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).


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
  * [ Manage cookies ](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext)
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