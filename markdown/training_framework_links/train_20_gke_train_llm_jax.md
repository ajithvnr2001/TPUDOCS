---
id: "train_20_gke_train_llm_jax"
title: "Fine-tune an LLM on GKE with JAX"
url: "https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-llm-tpus-gke-jax"
category: "Training framework links"
description: "Introductory distributed Gemma fine-tuning tutorial on TPUs using JAX; points production LLM fine-tuning to MaxText and diffusion work to MaxDiffusion."
crawled_at: "2026-10-26T12:47:16.613336+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-llm-tpus-gke-jax#main-content)
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
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/kubernetes-engine-color.svg) ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)


[Start free](https://console.cloud.google.com/freetrial)
[ Overview ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra) [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
  * [ Documentation  ](https://docs.cloud.google.com/docs)
    * More 
    * [ Overview  ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
    * [ Guides  ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)
  * [ Console  ](https://console.cloud.google.com/)


  * Discover
  * [Introduction to AI/ML workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)
  * Explore GKE documentation
    * [Overview](https://docs.cloud.google.com/kubernetes-engine/ai-ml/explore-gke-docs)
    * [Main GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
    * [GKE AI/ML documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)
    * [GKE networking documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)
    * [GKE security documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)
    * [GKE fleet management documentation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)
  * [Select how to obtain and consume accelerators on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option)
  * [Design for resource obtainability with Gemini](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini-obtainability)
  * [GKE AI/ML conformance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ai-conformance)
  * Get started
  * [Why use GKE for AI/ML inference](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/why-use-gke-ai-ml-overview)
  * [Simplified autoscaling concepts for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/understand-autoscaling)
  * [Quickstart: Serve your first AI model on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-terraform)
  * Serve AI models for inference
  * [About AI/ML model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference)
  * [Analyze model serving performance and costs with GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart)
  * [Expose AI applications with GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway)
  * Best practices for inference
    * [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference)
    * [Choose a load balancing strategy for inference](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/choose-lb-strategy)
    * [Autoscale inference workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling)
    * [Autoscale LLM inference workloads on TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu)
    * [Optimize LLM inference workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization)
    * [Optimize batch inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/batch-inference)
  * Try inference examples
    * GPUs
      * [Serve Gemma open models using GPUs with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm)
      * [Serve LLMs like DeepSeek-R1 671B or Llama 3.1 405B](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-gpu)
      * [Serve an LLM with GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-with-gke-inference-gateway)
      * [Serve an LLM with multiple GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu)
      * [Serve T5 with Torch Serve](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scalable-ml-models-torchserve)
    * TPUs
      * [Serve Llama on TPUs with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu)
      * [Serve LLMs using multi-host TPUs with JetStream and Pathways](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-tpu-jetstream)
      * [Serve Stable Diffusion XL on TPUs with MaxDiffusion](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu)
      * [Serve open models on TPUs with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-tpu-terraform)
  * Train AI models at scale
  * [Train large-scale models with Multi-tier Checkpointing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing)
  * Try training examples
    * [Train a model with GPUs on GKE Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard)
    * [Train a model with GPUs on GKE Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-autopilot)
    * [Train a Llama model on GPUs with Megatron-LM](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/training-megatron-llama-workload)
    * [Fine-tune a LLM using TPUs on GKE with JAX](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-llm-tpus-gke-jax)
  * Run reinforcement learning workloads on GKE
    * [Fine-tune and scale reinforcement learning with verl](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scaling-rl-verl-gke)
    * [Fine-tune and scale reinforcement learning with NeMo RL](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/nemo-rl-gke)
    * [Monitor reinforcement learning workloads with OpenTelemetry](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/monitor-reinforcement-learning-workloads)
  * Deploy and orchestrate AI agents
  * [Deploy AI agents with the ADK and Agent Platform API](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex)
  * [Deploy AI agents with the ADK and a self-hosted LLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vllm)
  * Scale AI agentic workloads with Agent Substrate on GKE
    * [About Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate)
    * [Install Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate)
  * Manage identities for AI agents in GKE
    * [About Agent Identity for GKE](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity)
    * [Request an identity for a GKE agent](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity)
    * [Manage access to Google Cloud APIs for GKE agents](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access)
    * [Authenticate by using an agent identity in GKE](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity)
  * Secure AI agentic workloads with Agent Sandbox on GKE
    * [About Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox)
    * [Choose storage for AI agentic workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox-storage)
    * [Enable Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox)
    * [Isolate AI code execution with Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox)
    * [Manage Agent Sandbox on GKE storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-storage)
    * [Save and restore Agent Sandbox on GKE environments](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots)
    * [Trigger Agent Sandbox on GKE snapshots from inside a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-trigger-inside-cluster)
  * Use Ray for distributed AI/ML applications
  * [About Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)
  * [Quickstart: Deploy your first Ray application on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/quickstarts/ray-gpu-cluster)
  * [Enable managed KubeRay with the Ray Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke)
  * Deploy AI/ML workloads with Ray on GKE
    * Serve AI models with Ray Serve on GKE
      * [Serve an LLM on GPUs with Ray Serve](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-llm-l4-ray)
      * [Serve an LLM with multi-cluster Ray Serve and Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-multi-cluster-ray-inference-gateway)
      * [Serve an LLM on TPUs with Ray Serve](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray)
      * [Serve Gemma open models using multi-host TPUs on GKE with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multi-host-tpu-llm)
      * [Serve LLMs on multi-host TPUs with Ray and TorchTPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray-torchtpu)
      * [Serve a diffusion model on GPUs with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/tutorials/deploy-ray-serve-stable-diffusion)
      * [Serve a diffusion model on TPUs with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/tutorials/deploy-ray-serve-stable-diffusion-tpu)
    * Train AI models with Ray on GKE
      * [Train with PyTorch, Ray, and GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/tutorials/train-model-ray-pytorch)
      * [Train an LLM using Jax and Ray Train on TPUs with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu)
      * [Multislice and Elastic Training on TPUs using Ray Train on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/multi-slice-training-ray)
      * [Fine-tune models on multi-host TPUs with Ray and TorchTPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-models-tpu-ray-torchtpu)
    * Share compute between teams with Kueue
      * [Start RayJobs faster across multiple compute options](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/ephemeral-rayjobs-kueue-concurrent-admission)
  * Use GPUs with Ray on GKE
    * [Set up Ray on GKE with A4X and GB200](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/ray-a4x)
  * Use TPUs with Ray on GKE
    * [Set up Ray on GKE with TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kuberay-trillium)
    * [Optimize AI training on TPUs with DWS and Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/ray-kueue-dws)
    * [View TPU metrics on the Ray Dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-tpu-metrics)
  * Monitor Ray on GKE
    * [View logs for the Ray Operator on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-ray-operator-logs)
    * [View logs and metrics for Ray clusters on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics)
    * [Debug completed Ray jobs with Ray History Server](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-history-server)
  * Use Slurm Operator for HPC and AI/ML workloads
  * [About Slurm on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview)
  * [Quickstart: Deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke)
  * [Enable the Slurm Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon)
  * [Build custom Slurm Docker images](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-custom-images)
  * [Autoscale a Slurm cluster using metrics](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/autoscale-slurm-cluster-metrics)
  * Configure shared storage for Slurm on GKE
    * [Configure Filestore for Slurm](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-shared-storage-filestore)
    * [Managed Lustre for Slurm](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-shared-storage-lustre)
  * Manage GPUs on GKE
  * [About GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
  * Configure GPUs for AI/ML workloads
    * [Configure A3 or A4 VMs with AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)
    * [Deploy GPU workloads in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus)
    * [Deploy GPU workloads in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)
    * [Configure autoscaling for LLM workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling)
    * [Manage the GPU stack with the NVIDIA GPU Operator](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator)
    * [Encrypt GPU workloads in-place](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes)
  * Provision resources for high performance computing (HPC)
    * [Deploy AI Hypercomputer clusters (A3, A4 VMs)](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)
  * Optimize GPU utilization with GPU sharing strategies
    * [About GPU sharing strategies on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus)
    * [Use multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)
    * [Configure timesharing GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus)
    * [Use NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus)
  * Optimize GPU provisioning with flex-start
    * [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws)
    * [Run a large-scale workload with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest)
    * [Run a small batch workload with GPUs and flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training)
  * Manage TPUs on GKE
  * [About TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)
  * Versions
    * [Ironwood (TPU7x)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood)
  * [Plan TPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus)
  * Configure TPUs for AI/ML workloads
    * [Deploy TPU workloads on Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus)
    * [Deploy TPU workloads on Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot)
    * [Deploy high-performance TPU workloads with auto-networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators)
    * [Deploy TPU Multislices on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice)
    * [Orchestrate TPU Multislice workloads using JobSet and Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue)
  * [Configure autoscaling for LLM workloads on TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling-tpu)
  * Optimize TPU provisioning with flex-start
    * [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws)
    * [Run a small batch workload with TPUs and flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu)
    * [Request TPUs with future reservation in calendar mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-calendar-mode)
  * Optimize TPU utilization with dynamic slicing
    * [About TPU All Capacity mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-all-capacity-mode)
    * About TPU dynamic slicing
      * [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing)
      * [Use dynamic slicing with a custom scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-dynamic-slices)
      * [Schedule dynamic slices with Kueue and TAS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-gke-dynamic-slicing)
  * Manage GKE node disruption for GPUs and TPUs
  * [About node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu)
  * Use Kueue for job queuing and resource optimization
    * [Best practices for running batch workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke)
    * [Deploy a batch system using Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro)
    * [Implement a Job queuing system with quota sharing](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-cohort)
    * [Optimize resource utilization for mixed AI/ML training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/mixed-workloads)
    * [Optimize AI/ML workload prioritization](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/optimize-ai-utilization)
    * [Orchestrate TPU Multislice workloads using JobSet and Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue)
  * Manage networking for AI/ML workloads
  * [Allocate network resources using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra)
  * [Configure auto-networking for accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators)
  * Manage data and storage for AI/ML workloads
  * [About storage for GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview)
  * Accelerate data access and performance
    * [Accelerate model loading with Run:ai Model Streamer and vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer)
    * [About Cloud Storage FUSE CSI driver for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver)
    * [Accelerate AI/ML data loading with Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-ml)
    * [Accelerate read performance of stateful workloads with GKE Data Cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/data-cache)
    * [About the GKE Volume Populator](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-volume-populator)
  * Build applications with vector databases and RAG
    * [Build a RAG chatbot with GKE and Cloud Storage](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/build-rag-chatbot)
    * [Deploy a Qdrant vector database on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-qdrant)
  * Secure AI/ML workloads
  * [Best practices for AI workload security on GKE](https://docs.cloud.google.com/kubernetes-engine/security/ai-security-best-practices)
  * Monitor AI/ML workloads
  * [Deploy automatic application monitoring for AI/ML workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring)
  * Troubleshoot
  * Troubleshoot accelerator issues
    * [Troubleshoot GPU issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/gpus)
    * [Troubleshoot TPU issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus)


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
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)


Send feedback 
#  Fine-tune a LLM using TPUs on GKE with JAX Stay organized with collections  Save and categorize content based on your preferences. 
[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
This tutorial shows you how to fine-tune a large language model (LLM) using Tensor Processing Units (TPUs) on Google Kubernetes Engine (GKE) with JAX. Fine-tuning lets you adapt a foundation model like Gemma 3 to a specific domain or task. This process improves the precision and accuracy of the model by updating its parameters with your own specialized dataset.
This guide is a good starting point if you need the granular control, customization, scalability, resilience, portability, and cost-effectiveness of managed Kubernetes when fine-tuning your AI/ML workloads.
## Background
By using TPUs on GKE with Jax to fine-tune an LLM, you can build a robust, production-ready fine-tuning solution with all the benefits of managed Kubernetes.
### Gemma
[Gemma](https://ai.google.dev/gemma) is a set of openly available, lightweight, generative AI/ML multimodal models released under an open license. These AI models are available to run in your applications, hardware, mobile devices, or hosted services. Gemma 3 introduces multimodality, and it supports vision-language input and text outputs. It handles context windows of up to 128,000 tokens and supports over 140 languages. Gemma 3 also offers improved math, reasoning, and chat capabilities, including structured outputs and function calling.
You can use the Gemma models for text generation, or you can also tune these models for specialized tasks.
For more information, see the [Gemma documentation](https://ai.google.dev/gemma/docs).
### TPUs
TPUs are application-specific integrated circuits (ASICs) that Google custom-developed to accelerate machine learning and AI models that are built using frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [JAX](https://github.com/google/jax).
Before you use TPUs in GKE, we recommend that you complete the following learning path:
  1. Learn about current TPU version availability with the [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  2. Learn [about TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).


### JAX
[JAX](https://github.com/google/jax) is a high-performance machine learning framework that is designed to be used with TPUs and GPUs. JAX provides an API for building and training machine learning models.
To learn more, see the [JAX repository](https://github.com/google/jax).
## Objectives
This tutorial covers the following steps:
  1. Create a GKE Autopilot or Standard cluster with the recommended TPU topology, based on the model characteristics. During this tutorial, you perform the fine-tuning on single-host node pools.
  2. Add data to a Cloud Storage bucket and mount it to the container through Cloud Storage FUSE.
  3. Deploy the LLM fine-tuning Job on GKE.
  4. Monitor the fine-tuning Job and view the logs.


## Before you begin
  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
**Roles required to select or create a project**
    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 
  * Enable the required API, if it is not already enabled. 
**Roles required to enable APIs**
To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
**Roles required to select or create a project**
    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 
  * Enable the required API, if it is not already enabled. 
**Roles required to enable APIs**
To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * Make sure that you have the following role or roles on the project: roles/container.admin,roles/iam.serviceAccountAdmin,roles/storage.admin 
#### Check for the roles
    1. In the Google Cloud console, go to the **IAM** page. 
[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 
    4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 
#### Grant the roles
    1. In the Google Cloud console, go to the **IAM** page. 
[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. Click person_add **Grant access**. 
    4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.
    5. Click **Select a role** , then search for the role. 
    6. To grant additional roles, click add **Add another role** and add each additional role. 
    7. Click **Save**. 


  * Ensure that you have sufficient quota for 16 TPU Trillium (v6e) chips. In this tutorial, you use a node pool configuration that requires 16 chips and [on-demand instances](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota).
  * Ensure that you have a Docker repository. If you don't have one, [create a standard repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) in Artifact Registry.


## Prepare the environment
In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).
To set up your environment with Cloud Shell, follow these steps:
  1. In the Google Cloud console, launch a Cloud Shell session and click ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) **Activate Cloud Shell**. This action launches a session in the bottom pane of the Google Cloud console.
  2. Set the default environment variables:

```
gcloud config set project PROJECT_ID
gcloud config set billing/quota_project PROJECT_ID
export PROJECT_ID=$(gcloud config get project)
export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
export CLUSTER_NAME=CLUSTER_NAME
export REGION=CONTROL_PLANE_LOCATION
export ZONE=ZONE
export GCS_BUCKET_NAME=BUCKET_NAME

```

Replace the following values:
     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) where your GKE cluster and TPU nodes are located. The region must contain zones where TPU Trillium (v6e) machine types are available.
     * `ZONE`: a zone within your selected `CONTROL_PLANE_LOCATION` region where TPU Trillium (v6e) machine types are available. To list zones where TPU Trillium (v6e) TPUs are available, run the following command:

```
  gcloud compute accelerator-types list --filter="name~ct6e" --format="value(zone)"

```

     * `BUCKET_NAME`: the name of the Cloud Storage bucket that contains your training data.
  3. Clone the sample repository:

```
git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
cd kubernetes-engine-samples

```

  4. Navigate to the working directory:

```
cd ai-ml/llm-training-jax-tpu-gemma3

```

## Create and configure Google Cloud resources
In this section, you create and configure Google Cloud resources.
### Create a GKE cluster
You can fine-tune an LLM on TPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).
### Autopilot
Create a GKE Autopilot cluster that uses [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and has Cloud Storage FUSE enabled.

```
gcloud container clusters create-auto ${CLUSTER_NAME} \
    --location=${REGION}

```

The cluster creation might take several minutes.
### Standard
  1. Create a regional GKE Standard cluster that uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and has Cloud Storage FUSE enabled.

```
gcloud container clusters create ${CLUSTER_NAME} \
    --enable-ip-alias \
    --addons GcsFuseCsiDriver \
    --machine-type=n2-standard-4 \
    --num-nodes=2 \
    --workload-pool=${PROJECT_ID}.svc.id.goog \
    --location=${REGION}

```

The cluster creation might take several minutes.
  2. Create a single-host node pool:

```
gcloud container node-pools create jax-tpu-nodepool \
    --cluster=${CLUSTER_NAME} \
    --machine-type=ct6e-standard-1t \
    --num-nodes=1 \
    --location=${REGION} \
    --node-locations=${ZONE} \
    --workload-metadata=GKE_METADATA

```

GKE creates a TPU Trillium node pool with a `1x1` topology and one node. The `--workload-metadata=GKE_METADATA` flag configures the node pool to use the GKE metadata server.
### Install JobSet
  1. Configure `kubectl` to communicate with your cluster:

```
gcloud container clusters get-credentials ${CLUSTER_NAME} --location=${REGION}

```

  2. Install the latest released version of [JobSet](https://jobset.sigs.k8s.io/docs/installation/):

```
kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/JOBSET_VERSION/manifests.yaml

```

Replace `JOBSET_VERSION` with the [latest released version of JobSet](https://github.com/kubernetes-sigs/jobset/releases). For example, `v0.11.0`.
  3. Verify the JobSet installation:

```
kubectl get pods -n jobset-system

```

The output is similar to the following:

```
NAME                                         READY   STATUS    RESTARTS   AGE
jobset-controller-manager-6c56668494-l4dhc   1/1     Running   0          4m45s

```

You might need to add more nodes if JobSet is waiting for resources.


### Configure Cloud Storage FUSE
To fine-tune the LLM, you need to provide training data. In this tutorial, you use the [TinyStories dataset](https://huggingface.co/datasets/roneneldan/TinyStories) from Hugging Face. This dataset contains short stories, synthetically generated by GPT-3.5 and GPT-4, that use a limited vocabulary.
This section covers the steps to configure Cloud Storage FUSE to read data from a Cloud Storage bucket.
  1. Download the dataset:

```
wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStories-train.txt?download=true -O TinyStories-train.txt

```

  2. Upload the data into a new Cloud Storage bucket:

```
gcloud storage buckets create gs://${GCS_BUCKET_NAME} \
    --location=${REGION} \
    --enable-hierarchical-namespace \
    --uniform-bucket-level-access
gcloud storage cp TinyStories-train.txt gs://${GCS_BUCKET_NAME}

```

  3. To allow your workload to read data through Cloud Storage FUSE, create a Kubernetes ServiceAccount (`jaxserviceaccount`) in the `default` namespace:

```
kubectl create serviceaccount jaxserviceaccount --namespace default

```

  4. Grant the `jaxserviceaccount` Kubernetes ServiceAccount the Storage Object Viewer role (`roles/storage.objectViewer`) on the Cloud Storage bucket:

```
gcloud storage buckets add-iam-policy-binding gs://${GCS_BUCKET_NAME} \
    --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/jaxserviceaccount" \
    --role="roles/storage.objectViewer" \
    --condition=None

```

Any Pod running in the `default` namespace of your GKE cluster that uses the `jaxserviceaccount` ServiceAccount now has read access to the objects stored in the `gs://${GCS_BUCKET_NAME}` bucket, which is required for the fine-tuning Job to access the dataset by using Cloud Storage FUSE.


## Create the fine-tuning script
In this section, you explore the training script that performs a fine-tuning operation on a Gemma 3 model. This script uses the `Gemma3Tokenizer`.
Review the following `Gemma3LLMTrain.py` fine-tuning script:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import grain.python as pygrain
import jax
import jax.numpy as jnp
import optax
import pandas as pd
import time
import argparse

from dataclasses import dataclass
from functools import partial
from gemma import gm
from flax.training import train_state
from jax.sharding import Mesh, PartitionSpec, NamedSharding

jax.distributed.initialize()
print("Global device count:", jax.device_count())
print("jax version:", jax.__version__)

tokenizer = gm.text.Gemma3Tokenizer()
num_epochs = 1
learning_rate = 2e-5

@dataclass
class TextDataset:
    data: list
    maxlen: int
    tokenizer: gm.text.Gemma3Tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx: int):
        encoding = self.tokenizer.encode(self.data[idx])[:self.maxlen]  # Tokenize and truncate
        return encoding + [0] * (self.maxlen - len(encoding))  # Pad to maxlen

def load_and_preprocess_data(file_path, batch_size, maxlen, datacount, tokenizer):

    with open(file_path, 'r') as f:
      text = f.read()

    stories = text.split('<|endoftext|>')
    stories = [story for story in stories if story.strip()][:datacount]
    df = pd.DataFrame({'text': stories})
    data = df['text'].dropna().tolist()
    dataset = TextDataset(data, maxlen, tokenizer)

    sampler = pygrain.IndexSampler(
        len(dataset),
        shuffle=False,
        seed=42,
        shard_options=pygrain.NoSharding(),
        num_epochs=num_epochs,
    )

    dataloader = pygrain.DataLoader(
        data_source=dataset,
        sampler=sampler,
        operations=[pygrain.Batch(batch_size=batch_size, drop_remainder=True)],
    )

    return dataloader

def generate_text(model, params, tokenizer, prompt):
    sampler = gm.text.Sampler(
        model=model,
        params=params,
        tokenizer=tokenizer,
    )
    print("Generating response for: " + prompt)
    out = sampler.sample(prompt, max_new_tokens=32)
    print("Reponse: \n" + out + "\n")
    return out

prep_target_batch = jax.vmap(lambda tokens: jnp.concatenate((tokens[1:], jnp.array([0]))))

@partial(jax.jit, donate_argnums=(0,))
def train_step(state, batch):
    """Performs one supervised fine-tuning step."""

    def loss_fn(params):
        # Run the forward pass. The model returns logits.
        logits = state.apply_fn({'params': params}, batch[0]).logits

        # Calculate the cross-entropy loss.
        loss = optax.softmax_cross_entropy_with_integer_labels(
            logits=logits, labels=batch[1]
        ).mean()

        return loss

    # Compute gradients
    grad_fn = jax.value_and_grad(loss_fn)
    loss, grads = grad_fn(state.params)

    # Update the model state
    state = state.apply_gradients(grads=grads)

    metrics = {'loss': loss}
    return state, metrics

def train_model(state, text_dl, num_epochs, sharding):
    batchCount = 0
    start_time = time.time()
    for epoch in range(num_epochs):
        start_time = time.time()
        for batch in text_dl:
            if len(batch) % len(jax.devices()) != 0:
              continue  # skip the remaining elements
            input_batch = jnp.array(jnp.array(batch).T)
            target_batch = prep_target_batch(input_batch)
            state, metrics = train_step(state, jax.device_put((input_batch, target_batch), sharding))

            if batchCount % 10 == 0:
                print(f"Loss after batch {batchCount}: {metrics['loss']}")
            batchCount += 1

    end_time = time.time()
    print(f"Completed training model. Total time for training {end_time - start_time} seconds \n")
    return state

def run_training(maxlen, batch_size, datacount):
    print(f"Batch size: {batch_size}, Max length: {maxlen}, Data count: {datacount}")
    #Load the training data
    tiny_stories_dl = load_and_preprocess_data('/data/TinyStories-train.txt', batch_size, maxlen, datacount, tokenizer)
    # Get the Gemma3 model
    model = gm.nn.Gemma3_270M()
    # Load the pretrained parameters
    params = gm.ckpts.load_params(gm.ckpts.CheckpointPath.GEMMA3_270M_PT)
    # Create an optimizer
    optimizer = optax.adamw(learning_rate=learning_rate)
    # Define sharding for data parallel training
    mesh = Mesh(jax.devices(), ('batch',))
    sharding = NamedSharding(mesh, PartitionSpec('batch', None))

    # Testing out current state of the model
    test_prompt = "Once upon a time, there was a girl named Amy."
    generate_text(model, params, tokenizer, test_prompt)

    state = train_state.TrainState.create(
        apply_fn=model.apply,
        params=params,
        tx=optimizer
    )

    # Perform post training
    print("Start training model")
    state = train_model(state, tiny_stories_dl, num_epochs, sharding)

    # Final text generation
    generate_text(model, state.params, tokenizer, test_prompt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train Gemma model with custom parameters.')
    parser.add_argument('--maxlen', type=int, default=256, help='Maximum sequence length')
    parser.add_argument('--batch_size', type=int, default=128, help='Batch size')
    parser.add_argument('--datacount', type=int, default=296000, help='Number of data samples to use')
    args = parser.parse_args()

    run_training(maxlen=args.maxlen, batch_size=args.batch_size, datacount=args.datacount)
```

In this script, the following applies:
  * A `Gemma3Tokenizer` converts text data into tokens that the model can process.
  * The `load_and_preprocess_data` function reads the training data from a file, splits it into individual stories, and uses the tokenizer to convert the text into padded sequences of tokens.
  * The `generate_text` function takes the model, its parameters, and a prompt to generate text.
  * The `train_step` function defines a single iteration of training that includes the forward pass, loss calculation (using cross-entropy), gradient computation, and parameter updates.
  * The `train_model` function iterates through the dataset for a specified number of epochs, which calls the `train_step` function for each batch.
  * The `run_training` function orchestrates the entire process to load data, initialize the Gemma 3 model (`Gemma3_270M`) and optimizer, load pre-trained parameters, set up data sharding for parallel processing, run a test generation, execute the training loop, and perform a final text generation to demonstrate the effect of fine-tuning.
  * The script uses `argparse` library to accept command-line arguments for `maxlen`, `batch_size`, and `datacount` parameters.


Now that you have explored the fine-tuning script, containerize it to run on GKE.
## Containerize the fine-tuning script
Before you run the fine-tuning script in a GKE cluster, you need to containerize it. This tutorial uses a [JAX AI image](https://docs.cloud.google.com/ai-hypercomputer/docs/images#current_jax_ai_images) as the base image.
  1. Open the `Dockerfile` in the same directory as the `Gemma3LLMTrain.py` file:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.7.2-rev1
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install gemma grain

WORKDIR /app

# Copy your training script into the container
COPY Gemma3LLMTrain.py .

```

This Dockerfile installs the necessary dependencies and copies the `Gemma3LLMTrain.py` file into the container.
  2. Build the Docker image and push it to an image repository:

```
export REPOSITORY=REPOSITORY_NAME
export IMAGE_NAME="jax-gemma3-training"
export IMAGE_TAG="latest"
export DOCKERFILE_PATH="./Dockerfile"
export IMAGE_URI="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}"

docker build -t "${IMAGE_URI}" -f "${DOCKERFILE_PATH}" .
gcloud auth configure-docker "${REGION}-docker.pkg.dev" -q
docker push "${IMAGE_URI}"

```

Replace `REPOSITORY_NAME` with the name of your Artifact Registry repository.
  3. Add role bindings to the service account:

```
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format 'get(projectNumber)')
gcloud artifacts repositories add-iam-policy-binding ${REPOSITORY} \
    --project=${PROJECT_ID} \
    --location=${REGION} \
    --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
    --role="roles/artifactregistry.reader"

```

With the image in the repository, you can now deploy the fine-tuning Job into a GKE cluster.
## Deploy the LLM fine-tuning Job
This section shows you how to deploy the LLM fine-tuning Job to your GKE cluster.
  1. Open the `training_singlehost.yaml` manifest:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: batch/v1
kind: Job
metadata:
  name: jax-gemma3-train-singlehost
spec:
  template:
    metadata:
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      serviceAccountName: jaxserviceaccout
      containers:
      - name: training-container
        image: ${IMAGE_URI}
        imagePullPolicy: "Always"
        command: ["python", "Gemma3LLMTrain.py", "--maxlen", "256", "--batch_size", "64", "--datacount", "355120"]
        resources:
          limits:
            google.com/tpu: 1
        volumeMounts:
        - name: gcs-fuse-csi-ephemeral
          mountPath: /data
      nodeSelector:
        cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
        cloud.google.com/gke-tpu-topology: 1x1
      restartPolicy: Never
      volumes:
      - name: gcs-fuse-csi-ephemeral
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: ${GCS_BUCKET_NAME}
            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
  backoffLimit: 1
```

  2. Apply the manifest:

```
envsubst < training_singlehost.yaml | kubectl apply -f -

```

GKE creates a Job that launches a Pod on a TPU Trillium (v6e) node. This Pod runs the Python fine-tuning script, which accesses the fine-tuning data from the specified Cloud Storage bucket mounted at `/data` path by using Cloud Storage FUSE. The script then fine-tunes the Gemma model.
**Success:** You've successfully fine-tuned a LLM model by using JAX and TPU Trillium (v6e) in GKE!
## Monitor the training Job
In this section, you monitor the progress of the fine-tuning Job and its performance.
### See fine-tuning progress
  1. List the Pods:

```
# Find the Pods
kubectl get pods

```

  2. Follow the log output:

```
kubectl logs -f pods/POD_NAME

```

Replace `POD_NAME` with the name of your Pod.
The output is similar to the following:

```
Global device count: 1
Batch size: 128, Max length: 256, Data count: 96000
I1028 00:12:55.925999 1387 google_auth_provider.cc:181] Running on GCE, using service account ...
Generating response for: Once upon a time, there was a girl named Amy.
Response:
Amy lived in a small house. The house was in a big field. Amy liked to play in the big field. She
Start training model
Loss after batch 0: 10.25
Loss after batch 10: 4.3125
.
.
.
Loss after batch 740: 1.41406
Completed training model. Total time for training 294.6791355609894 seconds
Generating response for: Once upon a time, there was a girl named Amy.
Response:
She loved to play with her toys. One day, Amy's mom told her that she had to go to the store to

```

  3. Analyze the output:
     * The `Global device count: 1` line indicates the TPU cores used.
     * The model generates reasonable text before this fine-tuning run because it loads from a pre-trained checkpoint.
     * The output generated after fine-tuning shows more resemblance to the start of a short story, indicating the model is learning from the new dataset.
     * Fine-tuning on the full dataset should produce even more refined outputs.


### Observe metrics
See the performance of the fine-tuning Job by checking the TPU and CPU metrics. To view observability metrics for your cluster, perform the steps in [View cluster and workload observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#view_metrics).
## Alternative fine-tuning configurations
This section outlines alternative configurations for your fine-tuning workload.
### Model selection
This tutorial used the `Gemma3_270M` model, which is a small model that fits into a single-host TPU Trillium (v6e) node pool. For larger models that require more memory and compute for fine-tuning, you can use multi-host or multislice node pool configurations.
For a complete list of available models, see the [Gemma documentation](https://gemma-llm.readthedocs.io/en/latest/api/gm/nn/index.html).
**Important:** When you use other models, ensure that you use the correct tokenizer for the selected model.
### Node pool configurations
This tutorial used a single-host node pool. You can also create [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) or [multislice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice#whats_tpu_multislice), depending on your needs.
The following tabs show how to create for multi-host and multislice node pools:
### Multi-host
  1. In Cloud Shell, run the following command:

```
gcloud container node-pools create jax-tpu-multihost1 \
    --cluster=${CLUSTER_NAME} \
    --machine-type=ct6e-standard-4t \
    --num-nodes=2 \
    --tpu-topology=2x4 \
    --location=${REGION} \
    --node-locations=${ZONE}

```

GKE creates a TPU Trillium node pool with a `2x4` topology and two nodes.
  2. Open the `training_multihost_jobset.yaml` Job definition:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: jax-gemma3-train-multihost
spec:
  replicatedJobs:
    - name: trainers
      replicas: 1
      template:
        spec:
          parallelism: 2
          completions: 2
          backoffLimit: 1
          template:
            metadata:
              annotations:
                gke-gcsfuse/volumes: "true"
            spec:
              serviceAccountName: jaxserviceaccout
              nodeSelector:
                cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                cloud.google.com/gke-tpu-topology: 2x4
                cloud.google.com/gke-nodepool: jax-tpu-multihost1
              containers:
              - name: training-container
                image: ${IMAGE_URI} 
                imagePullPolicy: "Always"
                ports:
                  - containerPort: 8471
                command: ["python", "Gemma3LLMTrain.py", "--maxlen", "256", "--batch_size", "64", "--datacount", "5120"]
                resources:
                  limits:
                    google.com/tpu: 4
                volumeMounts:
                - name: gcs-fuse-csi-ephemeral
                  mountPath: /data
              volumes:
                - name: gcs-fuse-csi-ephemeral
                  csi:
                    driver: gcsfuse.csi.storage.gke.io
                    volumeAttributes:
                      bucketName: ${GCS_BUCKET_NAME}
                      mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"

```

  3. Deploy the fine-tuning Job:

```
envsubst < training_multihost_jobset.yaml | kubectl apply -f -

```

### Multislice
  1. In Cloud Shell, run the following command:

```
gcloud container node-pools create jax-tpu-multihost1 \
  --cluster=${CLUSTER_NAME} \
  --machine-type=ct6e-standard-4t \
  --num-nodes=2 \
  --tpu-topology=2x4 \
  --location=${REGION} \
  --node-locations=${ZONE}

gcloud container node-pools create jax-tpu-multihost2 \
  --cluster=${CLUSTER_NAME} \
  --machine-type=ct6e-standard-4t \
  --num-nodes=2 \
  --tpu-topology=2x4 \
  --location=${REGION} \
  --node-locations=${ZONE}

```

GKE creates two TPU Trillium node pools. Each node pool has a `2x4` topology and two nodes.
  2. Open the `training_multislice_jobset.yaml` Job definition:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: jax-gemma3-train-multislice
spec:
  replicatedJobs:
    - name: trainers
      replicas: 2
      template:
        spec:
          parallelism: 2
          completions: 2
          backoffLimit: 1
          template:
            metadata:
              annotations:
                gke-gcsfuse/volumes: "true"
            spec:
              serviceAccountName: jaxserviceaccout
              nodeSelector:
                cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                cloud.google.com/gke-tpu-topology: 2x4
              containers:
              - name: training-container
                image: ${IMAGE_URI}
                imagePullPolicy: "Always"
                ports:
                  - containerPort: 8471
                command: ["python", "Gemma3LLMTrain.py", "--maxlen", "256", "--batch_size", "64", "--datacount", "5120"]
                resources:
                  limits:
                    google.com/tpu: 4
                volumeMounts:
                - name: gcs-fuse-csi-ephemeral
                  mountPath: /data
              volumes:
                - name: gcs-fuse-csi-ephemeral
                  csi:
                    driver: gcsfuse.csi.storage.gke.io
                    volumeAttributes:
                      bucketName: ${GCS_BUCKET_NAME}
                      mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:100"

```

  3. Deploy the fine-tuning Job:

```
envsubst < training_multislice_jobset.yaml | kubectl apply -f -

```

### Performance analysis and optimization
To analyze and optimize the performance of your machine learning fine-tuning, you can use [XProf](https://github.com/openxla/xprof). XProf is a suite of tools that profiles and inspects ML workloads built with JAX, TensorFlow, or PyTorch/XLA. By showing execution traces, memory usage, and other data, XProf lets you fine-tune your models and training setup for better efficiency and faster training.
To analyze the performance of your fine-tuning workload by using XProf, you complete the following steps in this section:
  * Install the `xprof` package. Modify your training script to start the XProf server.
  * Modify your Kubernetes Job manifest to include a volume mount for XProf logs.
  * Give the Kubernetes ServiceAccount permissions to write XProf logs to a Cloud Storage bucket.
  * Run XProf within your Pod and set up port forwarding to access the XProf dashboard.


#### Install the XProf package
  1. Navigate to the directory that contains the XProf samples:

```
  cd ai-ml/llm-training-jax-tpu-gemma3/xprof-enabled

```

  2. Build the Docker image and push it to an image repository:

```
export REPOSITORY=REPOSITORY_NAME
export IMAGE_NAME="jax-gemma3-training-xp"
export IMAGE_TAG="latest"
export DOCKERFILE_PATH="./Dockerfile"
export IMAGE_URI="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}"

docker build -t "${IMAGE_URI}" -f "${DOCKERFILE_PATH}" .
gcloud auth configure-docker "${REGION}-docker.pkg.dev" -q
docker push "${IMAGE_URI}"

```

Replace `REPOSITORY_NAME` with the name of your Artifact Registry repository.
  3. Run the `Dockerfile` script:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.7.2-rev1
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install gemma grain equinox
RUN pip install xprof

WORKDIR /app

# Copy your training script into the container
COPY Gemma3LLMTrain.py .

```

This Dockerfile installs XProf dependencies.


#### Copy your fine-tuning script into the container
In this section, create and apply a Kubernetes Job manifest that includes the necessary volume mounts for XProf logs.
  1. Open the `training_singlehost.yaml` Job definition:

```
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: batch/v1
kind: Job
metadata:
  name: jax-gemma3-train-singlehost
spec:
  template:
    metadata:
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      serviceAccountName: jaxserviceaccout
      containers:
      - name: training-container
        image: ${IMAGE_URI}
        imagePullPolicy: "Always"
        command: ["python", "Gemma3LLMTrain.py", "--maxlen", "256", "--batch_size", "64", "--datacount", "851200"]
        resources:
          limits:
            google.com/tpu: 1
        volumeMounts:
        - name: gcs-fuse-csi-ephemeral
          mountPath: /data
        - name: gcs-fuse-csi-ephemeral2
          mountPath: /xprof
      nodeSelector:
        cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
        cloud.google.com/gke-tpu-topology: 1x1
      restartPolicy: Never
      volumes:
      - name: gcs-fuse-csi-ephemeral
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: ${GCS_BUCKET_NAME}
            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
      - name: gcs-fuse-csi-ephemeral2
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: ${XPROF_GCS_BUCKET_NAME}
            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
  backoffLimit: 1
```

  2. Apply the manifest:

```
envsubst < training_singlehost.yaml | kubectl apply -f -

```

#### Give the Kubernetes ServiceAccount permissions to write XProf logs
  1. To enable the `jaxserviceaccount` Kubernetes ServiceAccount to write and read XProf logs, grant it the Storage Object User role (`roles/storage.objectUser`) on the bucket:

```
export XPROF_GCS_BUCKET_NAME="XPROF_GCS_BUCKET_NAME"

gcloud storage buckets add-iam-policy-binding "gs://${XPROF_GCS_BUCKET_NAME}" \
    --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/jaxserviceaccount" \
    --role="roles/storage.objectUser" \
    --project="${PROJECT_ID}" \
    --condition=None

```

Replace `XPROF_GCS_BUCKET_NAME` with the name of the bucket to which to grant the role.
  2. Run XProf within your Pod:

```
kubectl exec POD_NAME -c training-container -it -- bash # exec into the container
xprof --port 9001 --logdir /xprof # start xprof

```

Replace `POD_NAME` with the name of your Pod.


#### Access the XProf dashboard
  1. Set up port forwarding to the XProf server in the Pod:

```
kubectl port-forward POD_NAME 9001:9001

```

  2. In your browser's address bar, enter the following:

```
http://localhost:9001/

```

The XProf Trace Viewer opens.
  3. In the TensorBoard window, click **Capture profile**.
  4. In the **Profile Service URL(s) or TPU name** field, enter `localhost:9002`.
  5. To capture more details, in the **Host Trace (TraceMe) Level** , select **verbose** and enable Python trace logging.
  6. To view the dashboard, click **Capture**.
TensorBoard captures the profile and lets you analyze the performance of the training script. The graph shows the execution timeline for both TPU and CPU performance profiles:


![An example of the XProf trace viewer that shows a performance matrix graph](https://docs.cloud.google.com/static/kubernetes-engine/images/xprof-performance-matrix.png)
For more profiling options to analyze your training workload performance, see the JAX documentation on [Profiling computation](https://jax.readthedocs.io/en/latest/profiling.html).
## Fine-tuning in production environments
This tutorial showed you how to test test JAX-based training in a distributed environment. For optimized LLM fine-tuning in production, use the [Maxtext](https://github.com/google/maxtext) library. If you are interested in diffusion models, use [Maxdiffusion](https://github.com/google/maxdiffusion) implementations.
For long-running training or fine-tuning workloads in production, set up workload checkpointing to minimize progress loss during a failure. To learn more about setting up multi-tier checkpointing, see [Train large-scale machine learning models on GKE with Multi-Tier Checkpointing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing).
## Clean up
To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 
### Delete the individual resources
To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources by running the following commands:
  1. Delete the resources you created in this tutorial:

```
gcloud container clusters delete ${CLUSTER_NAME} --location=${REGION}
gcloud storage rm --recursive gs://${GCS_BUCKET_NAME}
gcloud artifacts docker images delete ${IMAGE_URI} --delete-tags

```

  2. If you don't need the data generated by XProf, remove the Cloud Storage bucket used by XProf:

```
gcloud storage rm --recursive gs://${XPROF_GCS_BUCKET_NAME}

```

## What's next
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Explore the [JAX repository](https://github.com/google/jax).


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
  * [ Manage cookies ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-llm-tpus-gke-jax)
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