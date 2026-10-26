---
name: infer-04-vllm-torchtpu-setup
description: "vLLM-TorchTPU Cloud TPU setup \u2014 Official provisioning and hardware guidance for the vLLM-TorchTPU stack."
source_url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/"
category: "inference_deployment_links"
---

# Agent Skill: vLLM-TorchTPU Cloud TPU setup

- **Official Source**: [https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/)
- **Category**: `inference_deployment_links`
- **Resource ID**: `infer_04_vllm_torchtpu_setup`
- **When to Activate**: Official provisioning and hardware guidance for the vLLM-TorchTPU stack.

## Document Sections

- **Cloud TPU Setup**
  - **TPU Versions and Topologies**
    - **Recommended**
    - **Experimental**
  - **Prerequisites**
  - **Provisioning Cloud TPUs**
  - **Connecting and Checking Status**
    - **Compute Engine (TPU v6e, v5p)**
    - **Queued Resources (TPU v7x, v5e, v4)**
  - **Verify TPU Devices**
  - **Clean Up Resources**
    - **Compute Engine (TPU v6e, v5p)**
    - **Queued Resources (TPU v7x, v5e, v4)**
  - **Next Steps**

## Key CLI Commands & Invocations

```bash
gcloud auth login
gcloud config set project PROJECT_ID
gcloud services enable tpu.googleapis.com compute.googleapis.com
gcloud alpha compute tpus queued-resources create my-queued-resource \
gcloud compute instances describe my-tpu-vm \
gcloud compute ssh my-tpu-vm \
gcloud alpha compute tpus queued-resources describe my-queued-resource \
gcloud compute tpus tpu-vm ssh my-tpu-name \
gcloud compute instances delete my-tpu-vm \
gcloud alpha compute tpus queued-resources delete my-queued-resource \
```

## Complete Technical Reference

# Cloud TPU Setup
Running `vllm-torchtpu` requires access to Google Cloud TPUs (such as **TPU v7x / Ironwood** or **TPU v6e / Trillium**). This guide walks through choosing a TPU generation, setting up a Google Cloud project, and provisioning a TPU VM.
## TPU Versions and Topologies
Tensor Processing Units (TPUs) are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning workloads. TPUs are available in different versions each with different hardware specifications. For more information about TPUs, see [TPU System Architecture](https://cloud.google.com/tpu/docs/system-architecture-tpu-vm).
The following TPU versions are compatible with `vllm-torchtpu`. Selecting a topology allows you to configure the physical arrangements of the TPU chips, improving throughput and networking performance.
### Recommended
  * **TPU v7x (Ironwood)**
Recommended
Next-generation architecture for bleeding-edge research and ultra-large models. This is the generation `vllm-torchtpu` is continuously validated on in CI.
[View Topology Guidelines →](https://cloud.google.com/tpu/docs/tpu7x)


### Experimental
  * **TPU v6e (Trillium)**
Experimental
Optimal performance for mainstream AI workloads with balanced memory and compute.
[View Topology Guidelines →](https://cloud.google.com/tpu/docs/v6e#configurations)
  * **TPU v5e**
Experimental
Cost-effective performance for medium-to-large scale inference and training.
[View Topology Guidelines →](https://cloud.google.com/tpu/docs/v5e#tpu-v5e-config)
  * **TPU v5p**
Experimental
High-performance architecture optimized for peak compute and memory bandwidth.
[View Topology Guidelines →](https://cloud.google.com/tpu/docs/v5p#tpu-v5p-config)
  * **TPU v4**
Experimental
Previous generation flagship architecture for large-scale training.
[View Topology Guidelines →](https://cloud.google.com/tpu/docs/v4#tpu-v4-config)


## Prerequisites
Before provisioning a TPU VM, ensure you have:
  1. **A Google Cloud project** with billing enabled.
  2. **The Google Cloud CLI (`gcloud`)** installed and authenticated on your workstation:

```
gcloud auth login
gcloud config set project PROJECT_ID

```

  3. **The Cloud TPU and Compute Engine APIs enabled** :

```
gcloud services enable tpu.googleapis.com compute.googleapis.com

```

  4. **TPU quota** in your target zone. You can check it under **IAM & Admin -> Quotas & System Limits** in the Google Cloud Console. For more information, see [TPU quota](https://cloud.google.com/tpu/docs/quota#tpu_quota).


For TPU pricing information, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).
## Provisioning Cloud TPUs
Google Cloud supports two primary APIs for provisioning TPUs:
  * **[Compute Engine API](https://cloud.google.com/tpu/docs/tpus-in-compute-engine) (`gcloud compute instances create`)**: Used for **TPU v6e (Trillium)** and **TPU v5p**.
  * **[Cloud TPU API](https://cloud.google.com/tpu/docs/queued-resources) (`gcloud alpha compute tpus queued-resources create`)**: Used for **TPU v7x (Ironwood)** , **TPU v5e** , and **TPU v4**.


You can also choose between two capacity models:
  * **Standard (On-Demand)** : Immediate allocation at standard pay-as-you-go rates.
  * **Flex-start (DWS)** : Discounted capacity via Dynamic Workload Scheduler (DWS) that runs uninterrupted for up to 7 days. Flex-start is supported on **TPU v7x** , **TPU v6e** , **TPU v5p** , and **TPU v5e** (not on **TPU v4**). For more details, see [About Flex-start VMs](https://cloud.google.com/compute/docs/instances/about-flex-start-vms) and [DWS Pricing](https://cloud.google.com/products/dws/pricing#flex-start-tpu-vm-pricing).


Select your target TPU generation, chip count, and provisioning model below to generate the `gcloud` provisioning command. Be sure to replace placeholder variables (like `PROJECT_ID` and `ZONE`) with your own values before running.
1. Hardware Generation
TPU v7x (Ironwood) TPU v6e (Trillium) TPU v5p TPU v5e TPU v4
2. Chip Count
1 Chip 4 Chips 8 Chips 16 Chips 32 Chips 64 Chips
3. Provisioning Model
Standard / Reserved Flex-start (DWS)
Provision a standard **4-chip TPU V7X (8 TensorCores)** using the legacy Queued Resources API. Replace `PROJECT_ID` and `ZONE` with your values. `--service-account` is optional; remove it to use the Compute Engine default service account.

```
gcloud alpha compute tpus queued-resources create my-queued-resource \
  --node-id my-tpu-name \
  --project PROJECT_ID \
  --zone ZONE \
  --accelerator-type tpu7x-8 \
  --runtime-version v2-alpha-tpuv7x \
  --service-account SERVICE_ACCOUNT
```
  
| Parameter  | Description  |  
| --- | --- |  
| `PROJECT_ID`  | Your Google Cloud project ID.  |  
| `ZONE`  | The Google Cloud zone where you have TPU quota (e.g., `us-central1-c`, `us-east5-a`, `europe-west4-a`, `us-central2-b`). See [TPU regions and zones](https://cloud.google.com/tpu/docs/regions-zones) for availability.  |  
| `SERVICE_ACCOUNT`  | The email address for your service account, found in the Cloud Console under IAM Service Accounts (e.g., `tpu-service-account@<your_project_ID>.iam.gserviceaccount.com`). Optional for Cloud TPU API (queued resources) commands; if you omit `--service-account`, the Compute Engine default service account is used.  |  
| `RUNTIME_VERSION`  | Automatically populated by the generator above based on your selected TPU hardware generation.  |  
TPU v7x dual-core architecture
Each physical **TPU v7x (Ironwood)** chip exposes **2 logical TensorCore devices** to PyTorch and JAX. A single 4-chip TPU v7x host (`tpu7x-8`) provides **8 logical TPU devices** (`--tensor-parallel-size=8`) and 768 GB of total HBM.
## Connecting and Checking Status
Once your queued resource or GCE instance reaches the `ACTIVE` / `RUNNING` state, SSH into the host.
### Compute Engine (TPU v6e, v5p)
Check the status of your instance:

```
gcloud compute instances describe my-tpu-vm \
  --project=PROJECT_ID \
  --zone=ZONE

```

Connect using SSH:

```
gcloud compute ssh my-tpu-vm \
  --project=PROJECT_ID \
  --zone=ZONE

```

### Queued Resources (TPU v7x, v5e, v4)
Check the status of your queued resource:

```
gcloud alpha compute tpus queued-resources describe my-queued-resource \
  --project=PROJECT_ID \
  --zone=ZONE

```

Connect to worker 0 using SSH:

```
gcloud compute tpus tpu-vm ssh my-tpu-name \
  --project=PROJECT_ID \
  --zone=ZONE \
  --worker=0

```

## Verify TPU Devices
Inside the TPU VM, verify that the accelerator devices are visible before installing `vllm-torchtpu`:

```
ls /dev/vfio/

```

Once `vllm-torchtpu` is installed (which includes `tpu-info`), you can inspect chip utilization and HBM memory usage at any time with:

```
tpu-info

```

## Clean Up Resources
To avoid incurring unnecessary charges when you are finished, delete your TPU resources:
### Compute Engine (TPU v6e, v5p)

```
gcloud compute instances delete my-tpu-vm \
  --project=PROJECT_ID \
  --zone=ZONE

```

### Queued Resources (TPU v7x, v5e, v4)

```
gcloud alpha compute tpus queued-resources delete my-queued-resource \
  --project=PROJECT_ID \
  --zone=ZONE \
  --force

```

## Next Steps
Once your TPU VM is running, follow the [installation and quickstart instructions](https://github.com/vllm-project/vllm-torchtpu#readme) to install `vllm-torchtpu` and serve your first model.
[**Reach the right audience** on a privacy-first ad network only for software devs:**EthicalAds**](https://server.ethicalads.io/proxy/click/8176/01a17840-4c1d-7f02-ae98-1b21ea1b8b33/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)
