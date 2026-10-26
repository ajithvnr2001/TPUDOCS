---
id: "setup_05_create_instance_compute"
title: "Create a Cloud TPU VM instance using Compute Engine"
url: "https://docs.cloud.google.com/tpu/docs/create-instance-compute"
category: "TPU setup docs"
description: "Detailed Compute Engine creation guide for on-demand, Spot, reservation-bound, and flex-start TPU VMs."
crawled_at: "2026-10-26T12:45:01.543523+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/tpu/docs/create-instance-compute#main-content)
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


Send feedback 
# Create a Cloud TPU VM instance using Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 
This document shows you how to create a single TPU VM with the Compute Engine `gcloud compute instances create` command. You can also create a TPU VM instance by specifying an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates). For more information, see [Create a VM from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).
## Prerequisites
Complete the following prerequisites:
  1. Create a Google Cloud project for your TPUs as described in [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).
  2. Determine your TPU requirements as described in [Plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).


## Create a TPU VM instance
The parameters you use to create a TPU VM instance depend on the consumption option you are using: on-demand, Spot, reservation-bound, or flex-start. For more information, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus) .
### Create an on-demand TPU VM instance
To create an _on-demand_ TPU VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).
###  gcloud 

```
gcloud compute instances create TPU_NAME \
  --machine-type=MACHINE_TYPE \
  --image-family=IMAGE_FAMILY \
  --image-project=IMAGE_PROJECT \
  --zone=ZONE \
  --maintenance-policy=TERMINATE

```

###  REST 

```
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TPU_NAME",
    "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
    "disks": [
      {
        "boot": true,
        "initializeParams": {
          "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
        }
      }
    ],
    "scheduling": {
      "onHostMaintenance": "TERMINATE"
    },
    "networkInterfaces": [
      {
        "network": "global/networks/default"
      }
    ]
  }' \
  "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

```

Replace the following placeholders:
  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).


### Create a TPU Spot VM instance
To create a TPU Spot VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--provisioning-model=SPOT` flag:
**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).
###  gcloud 

```
gcloud compute instances create TPU_NAME \
  --machine-type=MACHINE_TYPE \
  --image-family=IMAGE_FAMILY \
  --image-project=IMAGE_PROJECT \
  --zone=ZONE \
  --provisioning-model=SPOT \
  --instance-termination-action=DELETE \
  --maintenance-policy=TERMINATE

```

###  REST 

```
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TPU_NAME",
    "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
    "disks": [
      {
        "boot": true,
        "initializeParams": {
          "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
        }
      }
    ],
    "scheduling": {
      "onHostMaintenance": "TERMINATE",
      "provisioningModel": "SPOT",
      "instanceTerminationAction": "DELETE"
    },
    "networkInterfaces": [
      {
        "network": "global/networks/default"
      }
    ]
  }' \
  "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

```

Replace the following placeholders:
  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).


### Create a TPU VM instance using a reservation
To create a TPU VM instance using the _reservation-bound_ consumption option, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--reservation-affinity=specific` and `--reservation` flags:
**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core). **Note:** You can't use the [`--request-valid-for-duration`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--request-valid-for-duration) flag with All Capacity mode reservations.
###  gcloud 

```
gcloud compute instances create TPU_NAME \
  --machine-type=MACHINE_TYPE \
  --image-family=IMAGE_FAMILY \
  --image-project=IMAGE_PROJECT \
  --zone=ZONE \
  --provisioning-model=reservation-bound \
  --reservation-affinity=specific \
  --reservation=RESERVATION_NAME \
  --instance-termination-action=DELETE \
  --maintenance-policy=TERMINATE

```

###  REST 

```
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TPU_NAME",
    "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
    "disks": [
      {
        "boot": true,
        "initializeParams": {
          "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
        }
      }
    ],
    "scheduling": {
      "onHostMaintenance": "TERMINATE",
      "provisioningModel": "RESERVATION_BOUND",
      "instanceTerminationAction": "DELETE"
    },
    "networkInterfaces": [
      {
        "network": "global/networks/default"
      }
    ],
    "reservationAffinity": {
      "consumeReservationType": "SPECIFIC_RESERVATION",
      "key": "compute.googleapis.com/reservation-name",
      "values": [
        "RESERVATION_NAME"
      ]
    }
  }' \
  "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

```

Replace the following placeholders:
  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * RESERVATION_NAME: The name of the specific reservation to consume. For All Capacity mode reservations, you can target a block or sub-block by specifying the reservation URL as follows:
    * Specify a block:

```
RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

```

    * Specify a sub-block:

```
RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUBBLOCK_NAME

```

### Create a TPU Flex-start VM
To create a TPU _Flex-start_ VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--provisioning-model=FLEX_START` flag:
**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).
###  gcloud 

```
gcloud compute instances create TPU_NAME \
  --machine-type=MACHINE_TYPE \
  --image-family=IMAGE_FAMILY \
  --image-project=IMAGE_PROJECT \
  --zone=ZONE \
  --provisioning-model=FLEX_START \
  --max-run-duration=MAX_RUN_DURATION \
  --request-valid-for-duration=VALID_DURATION \
  --instance-termination-action=DELETE \
  --maintenance-policy=TERMINATE

```

###  REST 

```
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TPU_NAME",
    "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
    "disks": [
      {
        "boot": true,
        "initializeParams": {
          "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
        }
      }
    ],
    "params": {
      "requestValidForDuration": {
        "seconds": VALID_DURATION
      }
    },
    "scheduling": {
      "onHostMaintenance": "TERMINATE",
      "provisioningModel": "FLEX_START",
      "instanceTerminationAction": "DELETE",
      "maxRunDuration": {
        "seconds": MAX_RUN_DURATION
      }
    },
    "networkInterfaces": [
      {
        "network": "global/networks/default"
      }
    ]
  }' \
  "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

```

Replace the following placeholders:
  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * MAX_RUN_DURATION: The maximum run duration for the TPU VM (for example `6h`). For REST, specify this as a number of seconds (for example `21600` for 6 hours).
  * VALID_DURATION: The maximum duration for which the request is valid. For REST, specify this as a number of seconds (for example `3600` for 1 hour).


For more information about creating Compute Engine instances, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
## What's next
  * Learn how to [Create a MIG with single-host Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/create-single-host-mig).
  * Learn how to [Create a MIG with a multi-host Cloud TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig).
  * Learn how to [manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).


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
  * [ Manage cookies ](https://docs.cloud.google.com/tpu/docs/create-instance-compute)
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