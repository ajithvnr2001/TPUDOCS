---
name: setup-08-regions-zones
description: "TPU regions and zones \u2014 Authoritative availability matrix for TPU generations, configurations, regions, and zones."
source_url: "https://docs.cloud.google.com/tpu/docs/regions-zones"
category: "tpu_setup_docs"
---

# Agent Skill: TPU regions and zones

- **Official Source**: [https://docs.cloud.google.com/tpu/docs/regions-zones](https://docs.cloud.google.com/tpu/docs/regions-zones)
- **Category**: `tpu_setup_docs`
- **Resource ID**: `setup_08_regions_zones`
- **When to Activate**: Authoritative availability matrix for TPU generations, configurations, regions, and zones.

## Document Sections

- **TPU regions and zones**
    - **North America**
    - **Europe**
    - **Asia Pacific**
    - **South America**
  - **What's next**

## Complete Technical Reference

# TPU regions and zones
Google Cloud uses regions, subdivided into zones, to define the geographic location of physical compute resources. For example, the `us-central1` region denotes a region near the geographic center of the United States.
Google Cloud also offers AI zones which are specialized Google Cloud zones for AI/ML training and inference workloads. They provide significant ML accelerator (GPU/TPU) capacity. AI zones are geographically located typically within a 5ms radius from standard Google Cloud zones. For more information see [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).
When you create a TPU VM, you specify the zone in which you want to create it. For more information about regional and zonal resources, see Compute Engine [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). You can create TPU VMs in the zones shown in the following table.
### North America  
| **TPU type (TPU7x)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All TPU7x configurations](https://docs.cloud.google.com/tpu/docs/tpu7x#configurations)  | Varies by slice size  | 
  * `us-central1-ai1a`
  * `us-central1-c`

 |  
| **TPU type (v6e)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations)  | Varies by slice size  | 
  * `us-central1-b`
  * `us-east1-d`
  * `us-east5-a`
  * `us-east5-b`
  * `us-south1-ai1b`

 |  
| **TPU type (v5p)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v5p configurations](https://docs.cloud.google.com/tpu/docs/v5p#configurations)  | Varies by slice size  | 
  * `us-central1-a`
  * `us-east5-a`

 |  
| **TPU type (v5e)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v5e configurations](https://docs.cloud.google.com/tpu/docs/v5e#configurations)  | Varies by slice size  | 
  * `us-central1-a`
  * `us-south1-a`
  * `us-west1-c`
  * `us-west4-a`

 |  
| **TPU type (v4)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v4 configurations](https://docs.cloud.google.com/tpu/docs/v4#configurations)  | Varies by slice size  | 
  * `us-central2-b`

 |  
| **TPU type (v3)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  v3-8   | 8  | 
  * `us-central1-a`
  * `us-central1-b`

 |  
| **TPU type (v2)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  v2-8   | 8  | 
  * `us-central1-b`
  * `us-central1-c`

 |  
|  v2-32   | 32  | 
  * `us-central1-a`

 |  
|  v2-128   | 128  | 
  * `us-central1-a`

 |  
|  v2-256   | 256  | 
  * `us-central1-a`

 |  
|  v2-512   | 512  | 
  * `us-central1-a`

 |  
### Europe  
| **TPU type (v6e)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations)  | Varies by slice size  | 
  * `europe-west4-a`

 |  
| **TPU type (v5p)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v5p configurations](https://docs.cloud.google.com/tpu/docs/v5p#configurations)  | Varies by slice size  | 
  * `europe-west4-b`

 |  
| **TPU type (v5e)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v5e configurations](https://docs.cloud.google.com/tpu/docs/v5e#configurations)  | Varies by slice size  | 
  * `europe-west4-b`

 |  
| **TPU type (v3)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  v3-8   | 8  | 
  * `europe-west4-a`

 |  
|  v3-32   | 32  | 
  * `europe-west4-a`

 |  
|  v3-64   | 64  | 
  * `europe-west4-a`

 |  
|  v3-128   | 128  | 
  * `europe-west4-a`

 |  
|  v3-256   | 256  | 
  * `europe-west4-a`

 |  
|  v3-512   | 512  | 
  * `europe-west4-a`

 |  
|  v3-1024   | 1024  | 
  * `europe-west4-a`

 |  
|  v3-2048   | 2048  | 
  * `europe-west4-a`

 |  
| **TPU type (v2)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  v2-8   | 8  | 
  * `europe-west4-a`

 |  
|  v2-32   | 32  | 
  * `europe-west4-a`

 |  
|  v2-128   | 128  | 
  * `europe-west4-a`

 |  
|  v2-256   | 256  | 
  * `europe-west4-a`

 |  
|  v2-512   | 512  | 
  * `europe-west4-a`

 |  
### Asia Pacific  
| **TPU type (v6e)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations)  | Varies by slice size  | 
  * `asia-northeast1-b`

 |  
| **TPU type (v2)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  v2-8   | 8  | 
  * `asia-east1-c`

 |  
### South America  
| **TPU type (v6e)**  | TPU cores  | Supported zones  |  
| --- | --- | --- |  
|  [All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations)  | Varies by slice size  | 
  * `southamerica-west1-a`

 |  
TPU types with higher numbers of chips or cores are available only in limited quantities. TPU types with lower chip or core counts are more likely to be available.
**Note:** The [Cloud TPU pricing](https://cloud.google.com/tpu/pricing) page might display pricing for regions where public TPU zones aren't generally available. Use the tables on this page to verify which regions and zones currently support each TPU version.
## What's next
  * To see pricing for TPUs in each region, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).
  * To learn how to work with TPUs, see [Get started](https://docs.cloud.google.com/tpu/docs/quick-starts).
  * To learn about TPU architecture, see [TPU Architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm).
  * To learn about the types of models that are well-suited to Cloud TPU, see [When to use TPUs](https://docs.cloud.google.com/tpu/docs/tpus#when_to_use_tpus).
