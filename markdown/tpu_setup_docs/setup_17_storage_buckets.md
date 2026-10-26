---
id: "setup_17_storage_buckets"
title: "Connect TPU VMs to Cloud Storage"
url: "https://docs.cloud.google.com/tpu/docs/storage-buckets-compute"
category: "TPU setup docs"
description: "Access datasets and model artifacts from TPU VMs; includes Compute Engine cleanup commands."
crawled_at: "2026-10-26T12:45:19.223292+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to main content ](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute#main-content)
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
# Connect TPU VMs to Cloud Storage buckets Stay organized with collections  Save and categorize content based on your preferences. 
This page introduces [Cloud Storage](https://docs.cloud.google.com/storage/docs) as an option for storing your machine learning data and training output, and describes how to give your TPU VM access to the data objects on Cloud Storage.
## Before you begin
You need a service account attached to your TPU VM in order to access a Cloud Storage bucket. If you don't specify a service account when creating a TPU VM, it uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
**Note:** Once you set up a service account for your project, it stays set while the project is active; you don't have to set up the service account every time you run a training workload in the same project.
To setup a Google Cloud project for TPUs and create a TPU VM instance, follow the instructions in:
  1. [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).
  2. [Create a TPU VM instance using Compute Engine](https://docs.cloud.google.com/tpu/docs/create-instance-compute)


## Write data to Cloud Storage
**Note:** Set up the Cloud Storage bucket in the same location (region) that you set up the TPU VM. See [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) for all options available for managing storage buckets.
###  Console 
  1. Go to the Cloud Storage page on the Google Cloud console.
[Go to the Cloud Storage page](https://console.cloud.google.com/storage/browser)
  2. Create a new bucket, specifying the following options:
     * A unique name of your choosing.
     * Default storage class: `Standard`
     * Location: The region where you created the TPU VM. For more information about regions and TPU availability, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).


###  CLI 
  1. Use the `gcloud storage buckets create` command to create a Cloud Storage bucket:

```
gcloud storage buckets create gs://BUCKET_NAME --location REGION

```

Replace the following placeholders:
     * BUCKET_NAME is the name of the bucket you want to create.
     * REGION is the region where you created the TPU VM. For more information about regions and TPU availability, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
  2. Use the `gcloud storage cp` command to write files to the Cloud Storage bucket:

```
gcloud storage cp -r LOCAL_DATA_DIR gs://BUCKET_NAME

```

Replace the following placeholders:
     * LOCAL_DATA_DIR is a local path to your data. For example: $HOME/your-data
     * BUCKET_NAME is the name of the bucket you want to write to.


## Give your TPU VM access to Cloud Storage
You need to give your TPU VM read and write access to your Cloud Storage objects. To do that, you must grant the required access to the service account attached to your TPU VM. The following sections show how to find the attached service account and grant the necessary access.
### Authorize the attached service account
The recommended way to authorize the attached service account is by using fine-grained access control lists (ACLs). You can also grant broader permissions using IAM permissions.
#### Using fine-grained ACLs for TPU VM (Recommended)
If you store training data on Cloud Storage, the attached service account needs read and write permission on the bucket.
###  Console 
  1. Go to the Cloud Storage browser page to view the buckets you own.
[Go to the Cloud Storage browser](https://console.cloud.google.com/storage/browser)
  2. Select the bucket whose ACL you want to modify.
  3. Select the **Permissions** tab.
  4. Select **Grant access** to add a new permission and type the complete service account name in the **New principals** edit box.
  5. If you are _reading_ from this bucket, you must authorize the attached service account to read from the resource. Do this by granting the service account the `Storage Legacy > Storage Legacy Bucket Reader` role.
  6. If you are _writing_ to this bucket, you must authorize the attached service account to write to the resource. Do this by granting the service account the `Storage Legacy > Storage Legacy Bucket Writer` role.


###  CLI 
  1. If you are _reading_ from this bucket, grant read permission for the attached service account:

```
 gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=serviceAccount:SERVICE_ACCOUNT --role=roles/storage.objectViewer

```

Replace the following placeholders:
     * BUCKET_NAME is the name of the bucket you want to read from.
     * SERVICE_ACCOUNT is the name of the service account attached to your TPU VM.
  2. If you are _writing_ to this bucket, grant write permission for the attached service account:

```
 gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=serviceAccount:SERVICE_ACCOUNT --role=roles/storage.objectCreator

```

Replace the following placeholders:
     * BUCKET_NAME is the name of the bucket you want to write to.
     * SERVICE_ACCOUNT is the name of the service account attached to your TPU VM.


#### Using IAM permissions for TPU VM (Alternative)
If you want to grant broader permissions instead of granting access to each bucket explicitly, you can grant the Identity Access Management (IAM) Storage Admin role to the service account attached to your TPU VM.
  1. [Go to IAM](https://console.cloud.google.com/iam-admin/iam)
  2. Click the **Grant access** button to add principals to the project.
  3. Enter the name of the attached service account in the **Principals** field.
  4. Click the **Roles** drop-down list.
  5. Enable the following roles:
     * **Project > Viewer**
     * **Storage > Storage Admin**


### Cloud Storage FUSE
Cloud Storage FUSE lets you mount and access Cloud Storage buckets as local file systems. This lets applications read and write objects in your bucket using standard file system semantics.
See the [Cloud Storage FUSE documentation](https://docs.cloud.google.com/storage/docs/gcs-fuse) for details about how Cloud Storage FUSE works and a description of how Cloud Storage FUSE operations map to Cloud Storage operations. You can find additional information about how to use Cloud Storage FUSE, such as how to install the `gcsfuse` CLI and mounting buckets on [GitHub.](https://github.com/GoogleCloudPlatform/gcsfuse/tree/master/docs)
## Clean up
  1. Disconnect from the TPU VM, if you have not already done so:

```
exit

```

  2. In your Cloud Shell or terminal, delete the TPU VM:

```
gcloud compute instances delete TPU_NAME --zone=ZONE

```

Replace the following placeholders:
     * TPU_NAME: The name of the TPU VM you created.
     * ZONE: The zone where the TPU VM was created.
  3. Verify the VM has been deleted by running `gcloud compute instances list`. The deletion might take several minutes.

```
gcloud compute instances list --zone=ZONE

```

Replace ZONE with the zone where the TPU VM was created.
If the response doesn't list your TPU instance, it has been successfully deleted.
  4. Run the following command to delete the Cloud Storage bucket and its contents, replacing BUCKET_NAME with the name of the bucket you created:

```
gcloud storage rm --recursive gs://BUCKET_NAME

```

Replace the following placeholders:
     * BUCKET_NAME: The name of the bucket you want to delete.


## What's next
  * For more information about creating Cloud Storage buckets and writing data to those buckets, see the [Cloud Storage create buckets documentation](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * For more information about service accounts, see the [authentication overview](https://docs.cloud.google.com/docs/authentication).
  * For more information about storage best practices, see [Storage best practices for AI/ML on TPU VMs](https://docs.cloud.google.com/tpu/docs/storage-best-practices).


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
  * [ Manage cookies ](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute)
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