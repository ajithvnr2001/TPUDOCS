---
id: "legacy_02_run_calculation_jax_legacy"
title: "Run JAX on a Cloud TPU VM — legacy API"
url: "https://docs.cloud.google.com/tpu/docs/run-calculation-jax"
category: "Legacy docs"
description: "Older Cloud TPU API quickstart; use the Compute Engine quickstart for new provisioning."
crawled_at: "2026-10-26T12:44:51.819307+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/tpu/docs/run-calculation-jax#main-content)
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
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
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
# Run a calculation on a Cloud TPU VM using JAX
**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 
This document provides a brief introduction to working with JAX and Cloud TPU.
**Note:** This example shows how to run code on a v5litepod-8 (v5e) TPU which is a single-host TPU. Single-host TPUs have only 1 TPU VM. To run code on TPUs with more than one TPU VM (for example, v5litepod-16 or larger), see [Run JAX code on Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods).
## Before you begin
Before running the commands in this document, you must create a Google Cloud account, install the Google Cloud CLI, and configure the `gcloud` command. For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).
### Required roles
To get the permissions that you need to create a TPU and connect to it using SSH, ask your administrator to grant you the following IAM roles on your project: 
  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)


For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 
## Create a Cloud TPU VM using `gcloud`
  1. Define some environment variables to make commands easier to use.

```
export PROJECT_ID=your-project-id
export TPU_NAME=your-tpu-name
export ZONE=us-east5-a
export ACCELERATOR_TYPE=v5litepod-8
export RUNTIME_VERSION=v2-alpha-tpuv5-lite
```

#### Environment variable descriptions
     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  2. Create your TPU VM by running the following command from a Cloud Shell or your computer terminal where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) is installed.

```
$ gcloud compute tpus tpu-vm create $TPU_NAME \
    --project=$PROJECT_ID \
    --zone=$ZONE \
    --accelerator-type=$ACCELERATOR_TYPE \
    --version=$RUNTIME_VERSION
```

## Connect to your Cloud TPU VM
Connect to your TPU VM over SSH by using the following command:

```
$ gcloud compute tpus tpu-vm ssh $TPU_NAME \
    --project=$PROJECT_ID \
    --zone=$ZONE
```

If you fail to connect to a TPU VM using SSH, it might be because the TPU VM doesn't have an external IP address. To access a TPU VM without an external IP address, follow the instructions in [Connect to a TPU VM without a public IP address](https://docs.cloud.google.com/tpu/docs/tpu-iap).
## Install JAX on your Cloud TPU VM

```
(vm)$ pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

## System check
Verify that JAX can access the TPU and can run basic operations:
  1. Start the Python 3 interpreter:

```
(vm)$ python3
```

```
>>> import jax
```

  2. Display the number of TPU cores available:

```
>>> jax.device_count()
```

The number of TPU cores is displayed. The number of cores displayed is dependent on the TPU version you are using. For more information, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
### Perform a calculation

```
>>> jax.numpy.add(1, 1)
```

The result of the numpy add is displayed:
Output from the command: 

```
Array(2, dtype=int32, weak_type=True)
```

### Exit the Python interpreter

```
>>> exit()
```

## Running JAX code on a TPU VM
You can now run any JAX code you want. The [Flax examples](https://github.com/google/flax/tree/master/examples) are a great place to start with running standard ML models in JAX. For example, to train a basic MNIST convolutional network:
  1. Install Flax examples dependencies:

```
(vm)$ pip install --upgrade clu
(vm)$ pip install tensorflow
(vm)$ pip install tensorflow_datasets
(vm)$ pip install tensorboard
```

  2. Install Flax:

```
(vm)$ git clone https://github.com/google/flax.git
(vm)$ pip install --user flax
```

  3. Run the Flax MNIST training script:

```
(vm)$ cd flax/examples/mnist
(vm)$ python3 main.py --workdir=/tmp/mnist \
    --config=configs/default.py \
    --config.learning_rate=0.05 \
    --config.num_epochs=5
```

The script downloads the dataset and starts training. The script output should look like this:

```
I0214 18:00:50.660087 140369022753856 train.py:146] epoch:  1, train_loss: 0.2421, train_accuracy: 92.97, test_loss: 0.0615, test_accuracy: 97.88
I0214 18:00:52.015867 140369022753856 train.py:146] epoch:  2, train_loss: 0.0594, train_accuracy: 98.16, test_loss: 0.0412, test_accuracy: 98.72
I0214 18:00:53.377511 140369022753856 train.py:146] epoch:  3, train_loss: 0.0418, train_accuracy: 98.72, test_loss: 0.0296, test_accuracy: 99.04
I0214 18:00:54.727168 140369022753856 train.py:146] epoch:  4, train_loss: 0.0305, train_accuracy: 99.06, test_loss: 0.0257, test_accuracy: 99.15
I0214 18:00:56.082807 140369022753856 train.py:146] epoch:  5, train_loss: 0.0252, train_accuracy: 99.20, test_loss: 0.0263, test_accuracy: 99.18
```

## Clean up
To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 
When you are done with your TPU VM, follow these steps to clean up your resources.
  1. Disconnect from the Cloud TPU instance, if you have not already done so:

```
(vm)$ exit
```

Your prompt should now be username@projectname, showing you are in the Cloud Shell.
  2. Delete your Cloud TPU:

```
$ gcloud compute tpus tpu-vm delete $TPU_NAME \
    --project=$PROJECT_ID \
    --zone=$ZONE
```

  3. Verify the resources have been deleted by running the following command. Make sure your TPU is no longer listed. The deletion might take several minutes.

```
$ gcloud compute tpus tpu-vm list \
    --zone=$ZONE
```

## Performance notes
Here are a few important details that are particularly relevant to using TPUs in JAX.
### Padding
One of the most common causes for slow performance on TPUs is introducing inadvertent padding:
  * Arrays in the Cloud TPU are tiled. This entails padding one of the dimensions to a multiple of 8, and a different dimension to a multiple of 128. 
  * The matrix multiplication unit performs best with pairs of large matrices that minimize the need for padding.


### bfloat16 dtype
By default, matrix multiplication in JAX on TPUs uses [bfloat16](https://docs.cloud.google.com/tpu/docs/bfloat16) with float32 accumulation. This can be controlled with the precision argument on relevant `jax.numpy` function calls (matmul, dot, einsum, etc). In particular:
  * `precision=jax.lax.Precision.DEFAULT`: uses mixed bfloat16 precision (fastest)
  * `precision=jax.lax.Precision.HIGH`: uses multiple MXU passes to achieve higher precision
  * `precision=jax.lax.Precision.HIGHEST`: uses even more MXU passes to achieve full float32 precision


JAX also adds the bfloat16 dtype, which you can use to explicitly cast arrays to `bfloat16`. For example, `jax.numpy.array(x, dtype=jax.numpy.bfloat16)`.
## What's next
For more information about Cloud TPU, see:
  * [Run JAX code on TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods)
  * [Manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)
  * [Cloud TPU System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)


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
  * [ Manage cookies ](https://docs.cloud.google.com/tpu/docs/run-calculation-jax)
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)


  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어