---
id: "infer_04_vllm_torchtpu_setup"
title: "vLLM-TorchTPU Cloud TPU setup"
url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/"
category: "Inference deployment links"
description: "Official provisioning and hardware guidance for the vLLM-TorchTPU stack."
crawled_at: "2026-10-26T12:47:29.602767+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#cloud-tpu-setup)
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU")
vLLM TorchTPU 
Cloud TPU Setup 
[ ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/?q= "Share")
Type to start searching
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU") vLLM TorchTPU 
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
  * [ Home  ](https://vllm-torchtpu.readthedocs.io/en/latest/)
  * Getting Started  Getting Started 
    * Cloud TPU Setup  [ Cloud TPU Setup  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/) Table of contents 
      * [ TPU Versions and Topologies  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#tpu-versions-and-topologies)
        * [ Recommended  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#recommended)
        * [ Experimental  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#experimental)
      * [ Prerequisites  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#prerequisites)
      * [ Provisioning Cloud TPUs  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#provisioning-cloud-tpus)
      * [ Connecting and Checking Status  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#connecting-and-checking-status)
        * [ Compute Engine (TPU v6e, v5p)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#compute-engine-tpu-v6e-v5p)
        * [ Queued Resources (TPU v7x, v5e, v4)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#queued-resources-tpu-v7x-v5e-v4)
      * [ Verify TPU Devices  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#verify-tpu-devices)
      * [ Clean Up Resources  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#clean-up-resources)
        * [ Compute Engine (TPU v6e, v5p)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#compute-engine-tpu-v6e-v5p_1)
        * [ Queued Resources (TPU v7x, v5e, v4)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#queued-resources-tpu-v7x-v5e-v4_1)
      * [ Next Steps  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#next-steps)
    * [ Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/)
    * [ Quickstart  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/)
    * [ Docker Guide  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/)
  * User Guide  User Guide 
    * [ Supported Models & Features  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/)
    * [ Parallelism & Scaling  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)
    * [ Multi-Host Serving  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)
    * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/disaggregated_serving/)
    * [ Quantization  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/quantization/)
    * [ Speculative Decoding  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/speculative_decoding/)
    * [ Compilation & Warmup Cache  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/)
    * Code Examples  Code Examples 
      * [ Offline Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_inference/)
      * [ Multi Modal Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_lora_inference/)
  * Deployment & Recipes  Deployment & Recipes 
    * [ TPU v7x (Ironwood) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/)
    * [ TPU v6e (Trillium) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v6e_recipes/)
    * [ Kubernetes & GKE  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/kubernetes/)
  * Developer Guide  Developer Guide 
    * [ Contributing  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/contributing/)
    * [ Coding Guidance  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/coding_guidance/)
    * [ Optimization Best Practices  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/optimization_best_practices/)
    * [ TPU Patch Mechanism  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/tpu_patch_mechanism/)
    * [ Type Checking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/type_checking/)
    * [ Testing & CI  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/testing_and_ci/)
    * [ Benchmarking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/benchmarking/)
    * [ Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/)
Profiling 
      * [ Offline (tpu_profiling.py)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/offline/)
      * [ Server-side Capture  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/server/)
      * [ Phased Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/phased/)
      * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/disaggregated/)
      * [ Output Layout  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/output/)
      * [ Viewing Traces  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/viewing/)
      * [ Troubleshooting  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/troubleshooting/)
  * Reference  Reference 
    * [ Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/)
  * [ Roadmap  ](https://vllm-torchtpu.readthedocs.io/en/latest/roadmap/)


Table of contents 
  * [ TPU Versions and Topologies  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#tpu-versions-and-topologies)
    * [ Recommended  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#recommended)
    * [ Experimental  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#experimental)
  * [ Prerequisites  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#prerequisites)
  * [ Provisioning Cloud TPUs  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#provisioning-cloud-tpus)
  * [ Connecting and Checking Status  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#connecting-and-checking-status)
    * [ Compute Engine (TPU v6e, v5p)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#compute-engine-tpu-v6e-v5p)
    * [ Queued Resources (TPU v7x, v5e, v4)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#queued-resources-tpu-v7x-v5e-v4)
  * [ Verify TPU Devices  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#verify-tpu-devices)
  * [ Clean Up Resources  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#clean-up-resources)
    * [ Compute Engine (TPU v6e, v5p)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#compute-engine-tpu-v6e-v5p_1)
    * [ Queued Resources (TPU v7x, v5e, v4)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#queued-resources-tpu-v7x-v5e-v4_1)
  * [ Next Steps  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#next-steps)


[ ](https://github.com/vllm-project/vllm-torchtpu/edit/main/docs/getting_started/tpu_setup.md "Edit this page")
# Cloud TPU Setup[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#cloud-tpu-setup "Permanent link")
Running `vllm-torchtpu` requires access to Google Cloud TPUs (such as **TPU v7x / Ironwood** or **TPU v6e / Trillium**). This guide walks through choosing a TPU generation, setting up a Google Cloud project, and provisioning a TPU VM.
## TPU Versions and Topologies[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#tpu-versions-and-topologies "Permanent link")
Tensor Processing Units (TPUs) are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning workloads. TPUs are available in different versions each with different hardware specifications. For more information about TPUs, see [TPU System Architecture](https://cloud.google.com/tpu/docs/system-architecture-tpu-vm).
The following TPU versions are compatible with `vllm-torchtpu`. Selecting a topology allows you to configure the physical arrangements of the TPU chips, improving throughput and networking performance.
### Recommended[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#recommended "Permanent link")
  * **TPU v7x (Ironwood)**
Recommended
Next-generation architecture for bleeding-edge research and ultra-large models. This is the generation `vllm-torchtpu` is continuously validated on in CI.
[View Topology Guidelines →](https://cloud.google.com/tpu/docs/tpu7x)


### Experimental[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#experimental "Permanent link")
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


## Prerequisites[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#prerequisites "Permanent link")
Before provisioning a TPU VM, ensure you have:
  1. **A Google Cloud project** with billing enabled.
  2. **The Google Cloud CLI (`gcloud`)** installed and authenticated on your workstation:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-0-1)gcloud auth login
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-0-2)gcloud config set project PROJECT_ID

```

  3. **The Cloud TPU and Compute Engine APIs enabled** :

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-1-1)gcloud services enable tpu.googleapis.com compute.googleapis.com

```

  4. **TPU quota** in your target zone. You can check it under **IAM & Admin -> Quotas & System Limits** in the Google Cloud Console. For more information, see [TPU quota](https://cloud.google.com/tpu/docs/quota#tpu_quota).


For TPU pricing information, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).
## Provisioning Cloud TPUs[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#provisioning-cloud-tpus "Permanent link")
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
## Connecting and Checking Status[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#connecting-and-checking-status "Permanent link")
Once your queued resource or GCE instance reaches the `ACTIVE` / `RUNNING` state, SSH into the host.
### Compute Engine (TPU v6e, v5p)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#compute-engine-tpu-v6e-v5p "Permanent link")
Check the status of your instance:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-2-1)gcloud compute instances describe my-tpu-vm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-2-2)  --project=PROJECT_ID \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-2-3)  --zone=ZONE

```

Connect using SSH:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-3-1)gcloud compute ssh my-tpu-vm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-3-2)  --project=PROJECT_ID \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-3-3)  --zone=ZONE

```

### Queued Resources (TPU v7x, v5e, v4)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#queued-resources-tpu-v7x-v5e-v4 "Permanent link")
Check the status of your queued resource:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-4-1)gcloud alpha compute tpus queued-resources describe my-queued-resource \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-4-2)  --project=PROJECT_ID \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-4-3)  --zone=ZONE

```

Connect to worker 0 using SSH:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-5-1)gcloud compute tpus tpu-vm ssh my-tpu-name \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-5-2)  --project=PROJECT_ID \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-5-3)  --zone=ZONE \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-5-4)  --worker=0

```

## Verify TPU Devices[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#verify-tpu-devices "Permanent link")
Inside the TPU VM, verify that the accelerator devices are visible before installing `vllm-torchtpu`:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-6-1)ls /dev/vfio/

```

Once `vllm-torchtpu` is installed (which includes `tpu-info`), you can inspect chip utilization and HBM memory usage at any time with:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-7-1)tpu-info

```

## Clean Up Resources[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#clean-up-resources "Permanent link")
To avoid incurring unnecessary charges when you are finished, delete your TPU resources:
### Compute Engine (TPU v6e, v5p)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#compute-engine-tpu-v6e-v5p_1 "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-8-1)gcloud compute instances delete my-tpu-vm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-8-2)  --project=PROJECT_ID \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-8-3)  --zone=ZONE

```

### Queued Resources (TPU v7x, v5e, v4)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#queued-resources-tpu-v7x-v5e-v4_1 "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-9-1)gcloud alpha compute tpus queued-resources delete my-queued-resource \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-9-2)  --project=PROJECT_ID \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-9-3)  --zone=ZONE \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#__codelineno-9-4)  --force

```

## Next Steps[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/#next-steps "Permanent link")
Once your TPU VM is running, follow the [installation and quickstart instructions](https://github.com/vllm-project/vllm-torchtpu#readme) to install `vllm-torchtpu` and serve your first model.
[**Reach the right audience** on a privacy-first ad network only for software devs:**EthicalAds**](https://server.ethicalads.io/proxy/click/8176/01a17840-4c1d-7f02-ae98-1b21ea1b8b33/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)