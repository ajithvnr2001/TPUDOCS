---
id: "setup_04_setup_gcp_account"
title: "Set up a Google Cloud project for TPUs"
url: "https://cloud.google.com/tpu/docs/setup-gcp-account"
category: "tpu_setup_docs"
description: "Account/project, API enablement, IAM, and access prerequisites for TPU work."
crawled_at: "2026-10-26T14:43:49.671049+00:00"
crawler_engine: "Crawl4AI+DevSiteArticleCleaner"
---

# Set up a Google Cloud project for TPUs
**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 
This topic describes how to set up your Google Cloud project to use Cloud TPU VMs:
  * [Create a Google Cloud project](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#create-project)
  * [Configure your Google Cloud project for Cloud TPU](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#config-project)


## Create a Google Cloud project
  1. In the Google Cloud console, [sign in](https://accounts.google.com/Login) to your Google Account or [sign up for a new account](https://accounts.google.com/SignUp).
  2. Create a Google Cloud project. For more information, see [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).
  3. [Enable billing for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled). For more information, see the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs/concepts).
Billing for all Cloud TPU versions uses the standard regional pricing on the [Cloud TPU pricing page](https://cloud.google.com/tpu/pricing).


## Configure your Google Cloud project for Cloud TPU
You can configure your Google Cloud project using the Cloud Shell, a Compute Engine VM, or your local machine. The [Cloud Shell](https://docs.cloud.google.com/shell/docs) lets you interact with TPU VMs without installing any software. The Cloud Shell disconnects after a period of inactivity. If you're running long-running commands, we recommend installing the Google Cloud CLI on your local machine. For more information on the Google Cloud CLI, see the [`gcloud` Reference](https://docs.cloud.google.com/sdk/gcloud/reference).
  1. If you are using a local machine or a Compute Engine VM, [install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). The Google Cloud CLI includes the `gcloud` command you use to work with Google Cloud resources and services.
**Note:** If you need to use a specific release of gcloud CLI components, install these components to ensure that relevant commands and flags are supported. For example, for alpha components, run `gcloud components install alpha`.**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`.
  2. Configure the `gcloud` command to use your project.

```
export PROJECT_ID=your-project-id
gcloud config set project $PROJECT_ID
```

  3. Activate the Cloud TPU API using `gcloud` or the Google Cloud console:
### gcloud

```
gcloud services enable tpu.googleapis.com

```

### Console
    1. In the Google Cloud console, go to the Cloud TPU API page.
[Go to Cloud TPU API](https://console.cloud.google.com/apis/library/tpu.googleapis.com)
    2. Click **Enable**.
  4. Make sure your Google Cloud account has the following roles in your project:
     * [**Service Account Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin): This role lets you create a service account
     * [**Project IAM Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin): This role lets you grant a role in a project
     * [**TPU Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin): This role lets you create a TPU
To view your current roles, see [View current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-view-access-console).
To add any missing roles, see [Grant a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) or ask your administrator to do it for you.
  5. Create a Cloud TPU service agent:
A TPU [service agent](https://docs.cloud.google.com/iam/docs/service-agents) is a Google-managed service account that lets the Cloud TPU service create and manage resources in your Google Cloud project.

```
  gcloud beta services identity create --service tpu.googleapis.com \
  --project $PROJECT_ID
```

  6. Create a TPU service account:
Service accounts provide credentials for your TPU VMs to access other Google Cloud resources. To improve security, create a user-managed service account that has only the permissions your TPU VM requires. To use it, specify the service account with the `--service-account` flag when you create the TPU VM.
    1. Follow the instructions in [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create) to create a user-managed service account.
    2. Grant your service account the following roles so your TPU VM can access common Google Cloud services:
     * [**TPU Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin): This role provides full access to TPU resources
     * [**Storage Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin): This role provides access to Cloud Storage
     * [**Logs Writer**](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter): This role lets you write logs with the Cloud Logging API
     * [**Monitoring Metric Writer**](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter): This role lets you write metrics to Cloud Monitoring
**Note:** If you don't specify a custom service account, your Cloud TPU uses the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).


## What's next
  * Learn how to [plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus)
  * Learn how to [create TPUs](https://docs.cloud.google.com/tpu/docs/create-tpu-vm)
  * Learn how to [manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)
