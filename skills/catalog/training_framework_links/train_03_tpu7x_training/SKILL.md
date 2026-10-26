---
name: train-03-tpu7x-training
description: "Train a model on TPU7x with MaxText or TorchTitan \u2014 Provision Ironwood training infrastructure and use JAX or PyTorch training recipes."
source_url: "https://docs.cloud.google.com/tpu/docs/tpu7x-training"
category: "training_framework_links"
---

# Agent Skill: Train a model on TPU7x with MaxText or TorchTitan

- **Official Source**: [https://docs.cloud.google.com/tpu/docs/tpu7x-training](https://docs.cloud.google.com/tpu/docs/tpu7x-training)
- **Category**: `training_framework_links`
- **Resource ID**: `train_03_tpu7x_training`
- **When to Activate**: Provision Ironwood training infrastructure and use JAX or PyTorch training recipes.

## Document Sections

- **Train a model using TPU7x (Ironwood)**
  - **Before you begin**
  - **Deploy the TPU7x (Ironwood) cluster**
  - **Deploy a training workload with MaxText**
    - **Build and upload the MaxText Docker image**
- **Clone MaxText**
- **Build the Docker image**
    - **Define the MaxText training command**
    - **Submit the MaxText training job**
  - **Deploy a training workload with TorchTitan**
  - **What's next**

## Key CLI Commands & Invocations

```bash
export PROJECT_ID=YOUR_PROJECT_ID
export ZONE=YOUR_ZONE
export CLUSTER_NAME=YOUR_CLUSTER_NAME
export BASE_OUTPUT_DIR="gs://YOUR_BUCKET_NAME"
gcloud storage buckets create ${BASE_OUTPUT_DIR} \
git clone https://github.com/AI-Hypercomputer/maxtext.git
git checkout maxtext-tutorial-v1.0.0
bash docker_build_dependency_image.sh MODE=stable JAX_VERSION=0.8.2
export CLOUD_IMAGE_NAME="${USER}-maxtext-runner"
bash docker_upload_runner.sh CLOUD_IMAGE_NAME=${CLOUD_IMAGE_NAME}
export MAXTEXT_COMMAND="JAX_PLATFORMS=tpu,cpu \
python3 src/MaxText/train.py src/MaxText/configs/base.yml \
```

## Key Environment Variables

- `BASE_OUTPUT_DIR`
- `ENABLE_PJRT_COMPATIBILITY`
- `JAX_PLATFORMS`
- `JAX_VERSION`
- `PROJECT_ID`
- `ZONE`

## Complete Technical Reference

# Train a model using TPU7x (Ironwood)
This document describes how to provision TPU7x resources with [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) and deploy a training workload using either [MaxText](https://github.com/AI-Hypercomputer/maxtext) (JAX) or [TorchTitan on TPU](https://github.com/google-pytorch/torchtitan) (PyTorch).
TPU7x is the first release within the Ironwood family, Google Cloud's seventh generation TPU. The Ironwood generation is designed for large-scale AI training and inference. For more information, see [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x).
For more examples optimized for TPU7x, see the following repositories on GitHub:
  * [Training recipes for Ironwood TPU](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/training/ironwood/README.md)
  * [TorchTitan Ironwood recipes](https://github.com/google-pytorch/torchtitan/tree/main/torchtitan/experiments/tpu/recipes/ironwood)


## Before you begin
Before you start, make sure you meet the following requirements:
  * You have a Google Cloud project with billing enabled.
  * You have [installed and initialized the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * You have [installed Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).


Then complete the following setup steps:
  1. Set the environment variables for your project and cluster:

```
export PROJECT_ID=YOUR_PROJECT_ID
export ZONE=YOUR_ZONE
export CLUSTER_NAME=YOUR_CLUSTER_NAME
export BASE_OUTPUT_DIR="gs://YOUR_BUCKET_NAME"
```

Replace the following:
     * YOUR_PROJECT_ID: Your Google Cloud project ID.
     * YOUR_ZONE: The zone in which to create the cluster.
     * YOUR_CLUSTER_NAME: The name of the new cluster.
     * YOUR_BUCKET_NAME: The name of your Cloud Storage bucket for training output.
  2. If you don't have an existing Cloud Storage bucket, create one:

```
gcloud storage buckets create ${BASE_OUTPUT_DIR} \
    --project=${PROJECT_ID} \
    --location=US \
    --default-storage-class=STANDARD \
    --uniform-bucket-level-access

```

## Deploy the TPU7x (Ironwood) cluster
Deploy a Google Kubernetes Engine (GKE) TPU7x cluster by following the instructions in [Deploy a GKE TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x). Ensure that your cluster node pool topology matches your training workload requirements, such as `4x4x8` for the MaxText example or `2x2x4` for the TorchTitan example.
## Deploy a training workload with MaxText
The following sections show how to build a container image and submit a [MaxText](https://github.com/AI-Hypercomputer/maxtext) training job with Cluster Toolkit.
### Build and upload the MaxText Docker image
**Note:** MaxText supports **Python 3.12 only**. Build your virtual environment with Python 3.12 to install the required dependencies.
Build and push the MaxText Docker image:

```
# Clone MaxText
git clone https://github.com/AI-Hypercomputer/maxtext.git
cd maxtext
git checkout maxtext-tutorial-v1.0.0

# Build the Docker image
bash docker_build_dependency_image.sh MODE=stable JAX_VERSION=0.8.2

export CLOUD_IMAGE_NAME="${USER}-maxtext-runner"
bash docker_upload_runner.sh CLOUD_IMAGE_NAME=${CLOUD_IMAGE_NAME}

```

### Define the MaxText training command
Prepare the command to run your training script inside the Docker container.
The MaxText 1B model configuration trains a language model with approximately 1 billion parameters. Use this model to test small chip scales. Performance is not optimized.

```
export MAXTEXT_COMMAND="JAX_PLATFORMS=tpu,cpu \
    ENABLE_PJRT_COMPATIBILITY=true \
    python3 src/MaxText/train.py src/MaxText/configs/base.yml \
        base_output_directory=${BASE_OUTPUT_DIR} \
        dataset_type=synthetic \
        per_device_batch_size=2 \
        enable_checkpointing=false \
        gcs_metrics=true \
        run_name=maxtext_training \
        steps=30"

```

### Submit the MaxText training job
Submit your training job using `gcluster job submit`. For details on job submission options, see the [Cluster Toolkit Job Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md):

```
gcluster job submit \
    --name="maxtext-1b-$(date +%H%M)" \
    --cluster=${CLUSTER_NAME} \
    --project=${PROJECT_ID} \
    --location=${ZONE} \
    --compute-type=tpu7x-standard-4t \
    --topology=4x4x8 \
    --image="gcr.io/${PROJECT_ID}/${CLOUD_IMAGE_NAME}" \
    --command="${MAXTEXT_COMMAND}"

```

Workload names must be unique within the cluster. This example appends `$(date +%H%M)` to the workload name.
## Deploy a training workload with TorchTitan
TorchTitan uses [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) to run distributed PyTorch training on Cloud TPU. For more information, see the [TorchTitan on TPU README](https://github.com/google-pytorch/torchtitan/blob/main/torchtitan/experiments/tpu/README.md).
## What's next
  * [Learn about PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)
  * [Use the Google Cloud ML Diagnostics platform to optimize and diagnose your workloads](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics)
  * [Run a training workload using a recipe optimized for TPU7x](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/training/ironwood/README.md)
  * [Explore TorchTitan Ironwood recipes](https://github.com/google-pytorch/torchtitan/tree/main/torchtitan/experiments/tpu/recipes/ironwood)
  * [Run a TPU7x microbenchmark](https://github.com/AI-Hypercomputer/accelerator-microbenchmarks/blob/main/Ironwood/Ironwood_Microbenchmarks_readme.md)
