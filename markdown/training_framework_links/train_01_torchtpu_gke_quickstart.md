---
id: "train_01_torchtpu_gke_quickstart"
title: "TorchTPU GKE quickstart"
url: "https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/"
category: "Training framework links"
description: "Deploy TorchTPU containers on GKE for single-device, single-host, or multi-host workloads."
crawled_at: "2026-10-26T12:45:31.881178+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#get-started-with-torchtpu-on-gke)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
Get started with TorchTPU on GKE 
[ ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/?q= "Share")
Type to start searching
[ GitHub 
  * 741
  * 60

](https://github.com/google-pytorch/torch_tpu "Go to repository")
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation") TorchTPU Documentation 
[ GitHub 
  * 741
  * 60

](https://github.com/google-pytorch/torch_tpu "Go to repository")
  * [ Home  ](https://torchtpu.readthedocs.io/en/latest/)
  * Get started with TorchTPU  Get started with TorchTPU 
    * [ Introduction to TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/)
    * [ Get started with TorchTPU on a TPU VM  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/)
    * Get started with TorchTPU on GKE  [ Get started with TorchTPU on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/) Table of contents 
      * [ Before you begin  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#before-you-begin)
        * [ Prerequisites  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#prerequisites)
        * [ Set environment variables  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#set-environment-variables)
        * [ Authenticate and get cluster credentials  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#authenticate-and-get-cluster-credentials)
      * [ Submit workloads with kubectl  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#submit-workloads-with-kubectl)
      * [ Run a single-device workload (one TensorCore of a 4-chip host)  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-a-single-device-workload-one-tensorcore-of-a-4-chip-host)
      * [ Run distributed workloads on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-distributed-workloads-on-gke)
        * [ Single host, multiple chips (4 chips / 8 devices on one host)  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#single-host-multiple-chips-4-chips-8-devices-on-one-host)
        * [ Multiple hosts (64 chips / 128 devices across 16 hosts)  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#multiple-hosts-64-chips-128-devices-across-16-hosts)
      * [ Run an upstream PyTorch example  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-an-upstream-pytorch-example)
        * [ Example: Running upstream MNIST on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#example-running-upstream-mnist-on-gke)
        * [ Choosing a manifest template for other upstream examples  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#choosing-a-manifest-template-for-other-upstream-examples)
        * [ Porting an upstream PyTorch example to run on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#porting-an-upstream-pytorch-example-to-run-on-gke)
    * [ TorchTPU supported feature set and future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/)
    * [ TorchTPU API Reference  ](https://torchtpu.readthedocs.io/en/latest/api_reference/)
    * [ TorchTPU FAQ  ](https://torchtpu.readthedocs.io/en/latest/faq/)
  * In-depth  In-depth 
    * [ How TorchTPU works  ](https://torchtpu.readthedocs.io/en/latest/how_torchtpu_works/)
    * [ TorchTPU execution model  ](https://torchtpu.readthedocs.io/en/latest/torchtpu_execution_model/)
    * [ TorchTPU and the TPU memory model  ](https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/)
    * [ TorchTPU distributed support  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/)
    * [ TorchTPU custom kernels  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/)
    * [ Dynamic shapes  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/)
  * Case studies  Case studies 
    * [ FLUX optimization  ](https://torchtpu.readthedocs.io/en/latest/case_studies_flux/)
    * [ Muse Glimmer 30B: autoregressive decoding  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_inference/)
    * [ Muse Glimmer 30B: training  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_training/)
    * [ FSDP best practices  ](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/)
  * Analyze your workload  Analyze your workload 
    * [ Manage numerical precision in TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/)
    * [ Performance profiling with XProf  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/)


Table of contents 
  * [ Before you begin  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#before-you-begin)
    * [ Prerequisites  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#prerequisites)
    * [ Set environment variables  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#set-environment-variables)
    * [ Authenticate and get cluster credentials  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#authenticate-and-get-cluster-credentials)
  * [ Submit workloads with kubectl  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#submit-workloads-with-kubectl)
  * [ Run a single-device workload (one TensorCore of a 4-chip host)  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-a-single-device-workload-one-tensorcore-of-a-4-chip-host)
  * [ Run distributed workloads on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-distributed-workloads-on-gke)
    * [ Single host, multiple chips (4 chips / 8 devices on one host)  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#single-host-multiple-chips-4-chips-8-devices-on-one-host)
    * [ Multiple hosts (64 chips / 128 devices across 16 hosts)  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#multiple-hosts-64-chips-128-devices-across-16-hosts)
  * [ Run an upstream PyTorch example  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-an-upstream-pytorch-example)
    * [ Example: Running upstream MNIST on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#example-running-upstream-mnist-on-gke)
    * [ Choosing a manifest template for other upstream examples  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#choosing-a-manifest-template-for-other-upstream-examples)
    * [ Porting an upstream PyTorch example to run on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#porting-an-upstream-pytorch-example-to-run-on-gke)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/get_started_on_gke.md "Edit this page")
# Get started with TorchTPU on GKE[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#get-started-with-torchtpu-on-gke "Permanent link")
This tutorial walks through running PyTorch workloads on a Google Kubernetes Engine (GKE) TPU cluster in three parts:
  1. **Run a simple single-device example** (`examples/simple_pytorch/simple_pytorch.py`) as a Kubernetes `Job`.
  2. **Run a multi-device distributed example** (`examples/tensor_parallel/manual/tp_worker.py`) on a single 4-chip host (`Job`) and across a multi-host 64-chip slice (`JobSet`).
  3. **Run an upstream PyTorch example** from [`pytorch/examples`](https://github.com/pytorch/examples) (such as MNIST).


We assume you already have a GKE Standard cluster with a TPU node pool; see [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus) if you need to create one.
## Before you begin[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#before-you-begin "Permanent link")
### Prerequisites[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#prerequisites "Permanent link")
  * A GKE cluster with a `tpu7x` node pool. This tutorial uses a 4-chip (`2x2x1`) node pool.
  * The [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).


### Set environment variables[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#set-environment-variables "Permanent link")
All steps in this tutorial rely on the following variables; set them accordingly. `LOCATION` is the zone or region of your cluster.

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-0-1)export PROJECT=<YOUR_PROJECT_ID>
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-0-2)export CLUSTER=<YOUR_CLUSTER_NAME>
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-0-3)export LOCATION=<YOUR_CLUSTER_ZONE_OR_REGION>
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-0-4)export NODEPOOL_NAME=<YOUR_4CHIP_NODEPOOL_NAME>
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-0-5)export DOCKER_IMAGE=us-docker.pkg.dev/ml-oss-artifacts-published/torch-tpu-public-release-container/torch-tpu:latest

```

### Authenticate and get cluster credentials[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#authenticate-and-get-cluster-credentials "Permanent link")

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-1-1)gcloud auth login
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-1-2)gcloud auth application-default login
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-1-3)gcloud components install kubectl gke-gcloud-auth-plugin
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-1-4)gcloud container clusters get-credentials ${CLUSTER} --location=${LOCATION} --project=${PROJECT}

```

See [Install kubectl and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl) for details.
## Submit workloads with kubectl[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#submit-workloads-with-kubectl "Permanent link")
Workloads are submitted as standard Kubernetes `Job` or `JobSet` manifests. The Python example scripts are already pre-installed inside the public container image at `/workspace/examples/`, while the reference Kubernetes `.yaml` manifests (`examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml`, `examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml`, and `examples/tensor_parallel/torchtpu_multihost_slice_jobset.yaml`) live in the `examples/` directory of the TorchTPU repository. Run the `sed` and `kubectl apply` commands below from the root of a local `torch_tpu` repository checkout.
## Run a single-device workload (one TensorCore of a 4-chip host)[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-a-single-device-workload-one-tensorcore-of-a-4-chip-host "Permanent link")
The manifest `examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml` reserves one host with 4 TPU v7x chips. Each v7x chip has two TensorCores, and TorchTPU exposes each TensorCore as one device, so the host has 8 TPU devices and its slice topology is `2x2x1`:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-2-1)    cloud.google.com/gke-tpu-slice-topology: 2x2x1
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-2-2)    ...
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-2-3)    cloud.google.com/gke-tpu-topology: 2x2x1

```

The example runs a single process on a single TPU device (one TensorCore) and leaves the other 7 devices on the host idle. This is expressed as a `1x1x1x1` TorchTPU topology, where the fourth number is the number of TensorCores per chip that the job uses:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-3-1)    - name: TORCH_TPU_TOPOLOGY
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-3-2)      value: "1,1,1,1"

```

The container runs `simple_pytorch.py`, which ships in the image under `/workspace/examples/`:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-1)  command:
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-2)    - /bin/bash
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-3)    - -c
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-4)    - |
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-5)      set -ex
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-6)      export PYTHONUNBUFFERED=1
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-7)      export TPU_LAUNCH_BLOCKING=1
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-8)      export ABSL_LOGGING_MIN_LOG_LEVEL=0
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-9)      echo "=== Starting Single-Device 1-Chip, 1-Device TPU v7x Workload ==="
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-10)      cd /workspace/examples/simple_pytorch/
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-11)      python3 ./simple_pytorch.py
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-4-12)      echo "=== Single-Host single-device Workload Completed Successfully ==="

```

This is the whole program:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-2)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-3)device = torch.device("tpu")  # Change from cuda to tpu
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-4)print(f"TPU Initialization complete. Primary device: {device}")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-5)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-6)# 1. Create a tensor on the CPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-7)cpu_tensor = torch.ones((5, 5))
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-8)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-9)# 2. Move it to the TPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-10)tpu_tensor = cpu_tensor.to(device)  # Using the device object
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-11)# OR
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-12)tpu_tensor_alt = cpu_tensor.to("tpu")  # Using the "tpu" string
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-13)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-14)# 3. Create a tensor directly on the TPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-15)direct_tpu_tensor = torch.randn((5, 5), device="tpu")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-16)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-17)print(f"cpu_tensor is on: {cpu_tensor.device}")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-18)print(f"tpu_tensor is on: {tpu_tensor.device}")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-5-19)print(f"direct_tpu_tensor is on: {direct_tpu_tensor.device}")

```

Patch the image and node pool into the manifest and apply it:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-6-1)sed -i "s|<DOCKER_IMAGE>|${DOCKER_IMAGE}|g" examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-6-2)sed -i "s|<NODEPOOL_NAME>|${NODEPOOL_NAME}|g" examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-6-3)kubectl apply -f examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml

```

Check job and pod status, then read the logs:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-7-1)kubectl get job,pods -n default
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-7-2)kubectl logs -n default -l job-name=torchtpu-singledevice-1chip-job -f

```

The job runs to completion and prints the four lines shown above.
## Run distributed workloads on GKE[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-distributed-workloads-on-gke "Permanent link")
### Single host, multiple chips (4 chips / 8 devices on one host)[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#single-host-multiple-chips-4-chips-8-devices-on-one-host "Permanent link")
The first step up from the single-device example is to use every TPU device on one host. Submit a single-host Kubernetes `Job` by first updating the manifest with your Docker image and node pool name and then launching the job using `kubectl`.
The manifest `examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml` applies to a single host of 4 v7x TPUs (8 TensorCores), so the slice topology is `2x2x1`:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-8-1)    cloud.google.com/gke-tpu-slice-topology: 2x2x1

```

TorchTPU interprets this as a `2x2x1x2` topology because it launches one process per TPU TensorCore:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-9-1)    - name: TORCH_TPU_TOPOLOGY
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-9-2)      value: "2,2,1,2"

```

It runs the manual tensor-parallel example from the Docker image:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-1)  command:
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-2)    - /bin/bash
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-3)    - -c
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-4)    - |
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-5)      set -ex
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-6)      export PYTHONUNBUFFERED=1
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-7)      export TPU_LAUNCH_BLOCKING=1
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-8)      export ABSL_LOGGING_MIN_LOG_LEVEL=0
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-9)      echo "=== Starting Single-Host 4-Chip (8-Device) TPU v7x Workload ==="
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-10)      cd /workspace/examples/tensor_parallel/manual/
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-11)      bash ./launch_singlehost.sh
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-10-12)      echo "=== Single-Host 4-Chip Workload Completed Successfully ==="

```

`examples/tensor_parallel/manual/launch_singlehost.sh` detects the TPU topology, exports it, and starts one process per TPU device with `torch.distributed.run` (`torchrun`) running `examples/tensor_parallel/manual/tp_worker.py`:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-1)# Detect and export TPU configuration dynamically.
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-2)eval "$(python3 -m torch.tpu.distributed)"
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-3)export TORCH_TPU_TOPOLOGY TORCH_TPU_SLICEBUILDER_ADDRESSES
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-4)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-5)python3 -m torch.distributed.run --nnodes=1 --node_rank=0 \
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-6)    --master_addr=localhost --master_port=29500 \
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-11-7)    --nproc_per_node=8 ./tp_worker.py

```

The worker and launch scripts are in `examples/tensor_parallel/manual/`.
Patch the image and node pool into the manifest and apply it:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-12-1)sed -i "s|<DOCKER_IMAGE>|${DOCKER_IMAGE}|g" examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-12-2)sed -i "s|<NODEPOOL_NAME>|${NODEPOOL_NAME}|g" examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-12-3)kubectl apply -f examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml

```

Check job and pod status:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-13-1)kubectl get job,pods -n default

```

### Multiple hosts (64 chips / 128 devices across 16 hosts)[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#multiple-hosts-64-chips-128-devices-across-16-hosts "Permanent link")
To scale past one host, the same example runs as a Kubernetes `JobSet`: one pod per host, 16 hosts for a `4x4x4` slice, with `examples/tensor_parallel/manual/launch_multihost.sh` deriving each host's rank from its position in the slice. Update the manifest with your Docker image and 64-chip node pool name and apply it with `kubectl`:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-14-1)sed -i "s|<DOCKER_IMAGE>|${DOCKER_IMAGE}|g" examples/tensor_parallel/torchtpu_multihost_slice_jobset.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-14-2)sed -i "s|<NODEPOOL_NAME>|${NODEPOOL_NAME}|g" examples/tensor_parallel/torchtpu_multihost_slice_jobset.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-14-3)kubectl apply -f examples/tensor_parallel/torchtpu_multihost_slice_jobset.yaml

```

Check `JobSet` and pod status:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-15-1)kubectl get jobset,pods -n default

```

## Run an upstream PyTorch example[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#run-an-upstream-pytorch-example "Permanent link")
Because TorchTPU is a native PyTorch backend (`device="tpu"`, `torch.accelerator`, distributed `backend="tpu_dist"`), you can pull and run standard scripts from the upstream [`pytorch/examples`](https://github.com/pytorch/examples) repository directly on GKE.
### Example: Running upstream MNIST on GKE[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#example-running-upstream-mnist-on-gke "Permanent link")
The upstream [`pytorch/examples/mnist`](https://github.com/pytorch/examples/tree/main/mnist) training script (`mnist/main.py`) uses PyTorch's device-agnostic `torch.accelerator` API:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-16-1)if use_accel:
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-16-2)    device = torch.accelerator.current_accelerator()
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-16-3)else:
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-16-4)    device = torch.device("cpu")

```

When `torch_tpu` is installed in the container, `torch.accelerator.current_accelerator()` automatically selects the `"tpu"` device, requiring **zero code changes** to `mnist/main.py`.
To run `mnist/main.py` on a single TPU device on GKE starting from `examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml`:
  1. **Update the container`command:` block** in `examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml` to install `git`, clone [`https://github.com/pytorch/examples.git`](https://github.com/pytorch/examples), keep `DataLoader` `num_workers` at its default (`0`) so it does not fork a worker subprocess that attempts to re-acquire the `libtpu` device lockfile, and run `mnist/main.py`:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-1)  command:
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-2)    - /bin/bash
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-3)    - -c
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-4)    - |
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-5)      set -ex
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-6)      export PYTHONUNBUFFERED=1
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-7)      apt-get update && apt-get install -y git
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-8)      git clone --depth 1 https://github.com/pytorch/examples.git /tmp/pytorch_examples
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-9)      cd /tmp/pytorch_examples/mnist
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-10)      sed -i "/'num_workers': 1,/d; /'persistent_workers': True,/d" main.py
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-17-11)      python3 main.py --epochs=1 --dry-run

```

  2. **Delete any previous run of the job** (since Kubernetes `Job` specs are immutable once created), patch the placeholders if needed, apply the updated manifest, and stream the MNIST training logs:

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-18-1)kubectl delete -f examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml --ignore-not-found
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-18-2)sed -i "s|<DOCKER_IMAGE>|${DOCKER_IMAGE}|g" examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-18-3)sed -i "s|<NODEPOOL_NAME>|${NODEPOOL_NAME}|g" examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-18-4)kubectl apply -f examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#__codelineno-18-5)kubectl logs -n default -l job-name=torchtpu-singledevice-1chip-job -f

```

### Choosing a manifest template for other upstream examples[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#choosing-a-manifest-template-for-other-upstream-examples "Permanent link")
To run other single-device or distributed upstream examples, pick the reference manifest template matching your target topology:  
| Workload Type  | Manifest Path  | TPU Topology (`gke-tpu-topology`)  | `TORCH_TPU_TOPOLOGY`  | Description  |  
| --- | --- | --- | --- | --- |  
|  **Single-Device** (1 TensorCore on a 4-chip host)  | `examples/simple_pytorch/torchtpu_singledevice_slice_job.yaml`  | `2x2x1`  | `"1,1,1,1"`  | Runs a single Python process on 1 TPU device.  |  
|  **Single-Host Distributed** (4 chips / 8 cores)  | `examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml`  | `2x2x1`  | `"2,2,1,2"`  | Runs 8 distributed ranks (`WORLD_SIZE=8`) on a single 4-chip host via `torchrun`.  |  
|  **Multi-Host Distributed** (64 chips / 128 cores)  | `examples/tensor_parallel/torchtpu_multihost_slice_jobset.yaml`  | `4x4x4`  | `"4,4,4,2"`  | Kubernetes `JobSet` coordinating 16 worker pods across a 64-chip slice.  |  
To target other TPU slice topologies, update `cloud.google.com/gke-tpu-slice-topology`, `cloud.google.com/gke-tpu-topology`, and `TORCH_TPU_TOPOLOGY` in the manifest (see [TPU VM system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm) and [TPU machine types and topologies](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines)).
### Porting an upstream PyTorch example to run on GKE[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/#porting-an-upstream-pytorch-example-to-run-on-gke "Permanent link")
Because TorchTPU is a native PyTorch backend, getting an upstream PyTorch example or test running on GKE is a minimal process:
  * **No code changes needed for non-distributed examples** : Non-distributed examples written for standard PyTorch devices (via `torch.accelerator` or `torch.device`) work with TorchTPU without code changes.
  * **Non-deprecated examples are expected to work** : Actively maintained, non-deprecated upstream PyTorch examples and modern APIs work out of the box (see [Supported feature set](https://torchtpu.readthedocs.io/en/latest/feature_set/) for details).
  * **Distributed examples may need minor modifications** : Some upstream distributed examples are overtuned to other devices (such as GPU- or NCCL-specific backends, flags, or sharding assumptions) and may require minor modifications to run on TPU (see the distributed sections above and [FSDP best practices](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/)).


Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)