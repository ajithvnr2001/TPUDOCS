---
id: "setup_22_tpu_health"
title: "Monitor Cloud TPU health"
url: "https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health"
category: "TPU setup docs"
description: "Health monitoring and unhealthy-instance detection for TPU VMs, including dashboard and metric labels."
crawled_at: "2026-10-26T12:45:28.102243+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health#main-content)
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
  * [English](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health)
  * [Deutsch](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=es-419)
  * [Français](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=id)
  * [Italiano](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=ja)
  * [한국어](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=ko)

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
# Monitor Cloud TPU health Stay organized with collections  Save and categorize content based on your preferences.
Cloud TPU health monitoring provides real-time information on the health status of TPU VMs and slices. Using either the [Cloud Monitoring](https://cloud.google.com/monitoring) console or [ Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can identify hardware failures as they occur and reallocate resources, avoiding job failures and minimizing performance degradation.
TPU health monitoring assigns either a `HEALTHY` or `UNHEALTHY` status to each TPU instance in use. TPUs functioning as expected are assigned a `HEALTHY` status, and those that are no longer functional or performing at a severely reduced level are assigned an `UNHEALTHY` status.
Along with a health status, TPU health monitoring provides logging metrics for specific jobs. You can use these metrics to further diagnose TPU health and performance issues that are not caused by hardware issues.
## Unhealthy TPU detection
When TPU health monitoring assigns an `UNHEALTHY` status to a TPU, it provides identifying information of the failing TPU through the `compute.googleapis.com/instance/tpu/infra_health` service endpoint.
### TPU health status causes
**Key Term:** Workers are the processes running on a TPU that compile and execute TPU programs (TPU modules).
A machine is categorized as `UNHEALTHY` when there are issues with the physical hardware. When a machine is categorized as `UNHEALTHY`, TPU health monitoring provides one of the following causes:
  * `BAD_TPU_CHIP`: A physical failure within the TPU hardware itself. The VM may be running as intended, but a TPU connected to the VM is faulty.
  * `NETWORKING_ISSUE`: Hardware issues in the underlying network communication between the different workers or components of the distributed TPU system, such as dropped transfer Remote Procedure Calls (RPCs).
  * `BAD_SC_CHIP`: A physical failure within a [SparseCore](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#sparsecore) of a TPU chip.


### Metric labels
TPU health monitoring provides the following metric labels to identify the specific unhealthy TPU:  
| **Label name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `health_status`  | `STRING`  | The overall health state of the TPU instance.  |  
| `unhealthy_category`  | `STRING`  | The health status cause. This label is populated only when the value of the metric is `UNHEALTHY`.  |  
| `machine_type`  | `STRING`  | The Compute Engine machine type of the instance.  |  
| `reservation_id`  | `STRING`  | The ID of the physical machine reservation.  |  
TPU health monitoring also provides the following resource labels:  
| **Label name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `project`  | `STRING`  | The project number.  |  
| `service`  | `STRING`  | The API service (`compute.googleapis.com`).  |  
| `resource_type`  | `STRING`  | The VM instance.  |  
| `location`  | `STRING`  | The zone of the instance.  |  
| `resource_id`  | `STRING`  | The Compute Engine instance ID.  |  
TPU health monitoring provides the following additional metric labels for All Capacity mode reservations through [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview):  
| **Label name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `machine_id`  | `STRING`  | The ID of the physical machine hosting the VM.  |  
| `block_id`  | `STRING`  | The ID of the block within the cluster hosting the VM.  |  
| `cluster_id`  | `STRING`  | The ID of the cluster hosting the VM.  |  
| `subblock_id`  | `STRING`  | The ID of the sub-block hosting the VM.  |  
## Logging
**Key Term:** TPU modules contain the code running on a TPU.
A machine without any physical issues may be impaired or non-functional due to issues unrelated to hardware. In these cases, TPU health monitoring continues to categorize the machine as `HEALTHY`, but also logs potential causes of the issue with Cloud Logging in the associated project. The logs provide details about the issue, including a brief description, the suspected root cause, potential culprits, and actionable next steps.
The logs contain one of the following causes:
  * `FINGERPRINT_MISMATCH`: Programs expected to be running the same TPU module contain different binary fingerprints. This is likely due to inconsistencies caused by compiler issues.
  * `DATA_INPUT_STALL`: TPUs are stuck during Direct Memory Access (DMA) operations or data transfers. TPUs cannot continue until DMA operations complete.
  * `UNRECOVERABLE_ERROR`: One or more workers encountered an unrecoverable error and are in an undefined state.
  * `DIFFERENT_MODULE`: Workers are executing different TPU modules when they are expected to be running the same module.
  * `UNKNOWN_CAUSE`: Undetermined cause of error.


You can view logs using the Logs Explorer or Logs API. For more information about Google Cloud logging, see [ Google Cloud Logging](https://cloud.google.com/logging).
## Monitoring with the console
The Monitoring Dashboard in the Google Cloud console provides real-time visualizations of machine health status, historical trends, and total counts. The **_Failure Event_** table links job failures to their root causes.
To view a prebuilt a dashboard in Cloud Monitoring:
  1. In the Google Cloud console, go to the Cloud Monitoring page.   
[Go to the Monitoring console](https://console.cloud.google.com/monitoring)
  2. In the navigation pane, click **Dashboards**.
  3. In the **Filter search** field, enter "TPU Instance Health Dashboard".


The dashboard displays the following metrics by default:
  * **Overall TPU instance health** : The percentage of TPU instances that are categorized as `HEALTHY`.
  * **Number of instances** : The total number of TPU instances in use.
  * **Number of healthy TPU instances** : The total number of TPU instances categorized as `HEALTHY`.
  * **Number of unhealthy TPU instances** : The total number of TPU instances categorized as `UNHEALTHY`.
  * **VM infra health distribution** : The number of `HEALTHY` instances over time.


To add a custom query, click **Add Query** and write a PromQL query. For example, the following query retrieves all unhealthy TPU instances:

```
count({__name__="compute.googleapis.com/instance/tpu/infra_health", monitored_resource="gce_instance", health_status="UNHEALTHY"})

```

For more information on monitoring with the Google Cloud console, see the [ Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).
## Monitoring with the CLI
The Google Cloud CLI provides real-time TPU health data. The following example request retrieves all `UNHEALTHY` TPU:

```
export TOKEN=$(gcloud auth application-default print-access-token)

export PROMQL_QUERY='count({__name__="compute.googleapis.com/instance/tpu/infra_health", monitored_resource="gce_instance", health_status="UNHEALTHY"})'

export LOCATION="global"

curl -G \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "Content-Type: application/json" \
  --header "X-Goog-User-Project: ${PROJECT_ID}" \
  --data-urlencode "query=${PROMQL_QUERY}" \
  "https://monitoring.googleapis.com/v1/projects/${PROJECT_ID}/location/${LOCATION}/prometheus/api/v1/query"

```

You should expect to see a response similar to the following:

```
{"status":"success","data":{"resultType":"vector","result":[65]}}

```

For more information on gcloud CLI, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud).
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
  * [ Manage cookies ](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health)
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)


  * [English](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health)
  * [Deutsch](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=es-419)
  * [Français](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=id)
  * [Italiano](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=ja)
  * [한국어](https://docs.cloud.google.com/tpu/docs/troubleshooting/tpu-health?hl=ko)