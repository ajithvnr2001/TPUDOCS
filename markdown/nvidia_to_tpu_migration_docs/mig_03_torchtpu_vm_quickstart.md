---
id: "mig_03_torchtpu_vm_quickstart"
title: "TorchTPU VM quickstart"
url: "https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/"
category: "Nvidia to tpu migration docs"
description: "Create a Python environment on a TPU VM, install TorchTPU, and run your first tensor operations."
crawled_at: "2026-10-26T12:47:59.499851+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#get-started-with-torchtpu-on-a-tpu-vm)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
Get started with TorchTPU on a TPU VM 
[ ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/?q= "Share")
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
    * Get started with TorchTPU on a TPU VM  [ Get started with TorchTPU on a TPU VM  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/) Table of contents 
      * [ 1. Install and set up  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#1-install-and-set-up)
        * [ Step 1: Initialize Python 3.12  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#step-1-initialize-python-312)
        * [ Step 2: Install TorchTPU and dependencies  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#step-2-install-torchtpu-and-dependencies)
      * [ 2. Initialize the hardware  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#2-initialize-the-hardware)
      * [ 3. Work with tensors  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#3-work-with-tensors)
      * [ 4. Compute and materialize results  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#4-compute-and-materialize-results)
        * [ 🎉 Success!  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#success)
    * [ Get started with TorchTPU on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/)
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
  * [ 1. Install and set up  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#1-install-and-set-up)
    * [ Step 1: Initialize Python 3.12  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#step-1-initialize-python-312)
    * [ Step 2: Install TorchTPU and dependencies  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#step-2-install-torchtpu-and-dependencies)
  * [ 2. Initialize the hardware  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#2-initialize-the-hardware)
  * [ 3. Work with tensors  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#3-work-with-tensors)
  * [ 4. Compute and materialize results  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#4-compute-and-materialize-results)
    * [ 🎉 Success!  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#success)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/get_started_on_a_vm.md "Edit this page")
# Get started with TorchTPU on a TPU VM[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#get-started-with-torchtpu-on-a-tpu-vm "Permanent link")
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-pytorch/torch_tpu/blob/0.2.0-docs/docs/notebooks/get_started_on_a_vm.ipynb)
The simplest way to use TorchTPU is on a TPU VM. In this example we will run a simple tensor parallel example. We do not focus on the example, just the setup code to get running on a VM. In the following tutorial, we will see how to achieve something similar through GKE, which is necessary to access recent TPU hardware.
## 1. Install and set up[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#1-install-and-set-up "Permanent link")
Before running this notebook, ensure you are running on a [Google Cloud TPU VM](https://docs.cloud.google.com/tpu/docs/intro-to-tpu?hl=en) (e.g., v6e).
Install TorchTPU and its dependencies on your TPU VM. Components must be installed in this order to ensure the PyTorch dispatcher and TPU drivers align correctly.
### Step 1: Initialize Python 3.12[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#step-1-initialize-python-312 "Permanent link")

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-0-1)sudo apt update && sudo apt install -y python3.12 python3.12-venv
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-0-2)python3.12 -m venv env
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-0-3)source env/bin/activate

```

### Step 2: Install TorchTPU and dependencies[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#step-2-install-torchtpu-and-dependencies "Permanent link")

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-1-1)pip install torch_tpu

```

## 2. Initialize the hardware[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#2-initialize-the-hardware "Permanent link")
Similar to a CPU or GPU, the TPU backend must be explicitly initialized. This registers the "tpu" device string with PyTorch.

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-2-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-2-2)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-2-3)device = torch.device("tpu")  # Change from cuda to tpu
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-2-4)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-2-5)print(f"TPU Initialization complete. Primary device: {device}")

```

## 3. Work with tensors[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#3-work-with-tensors "Permanent link")
Once initialized, you can interact with the TPU much like you would with a GPU. You can move existing CPU tensors to the TPU or create new tensors directly on the hardware.
You have two standard ways to specify the TPU device:
  1. Using the `device` object returned by `torch.device()`.
  2. Using the `"tpu"` string identifier.

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-1)# 1. Create a tensor on the CPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-2)cpu_tensor = torch.ones((5, 5))
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-3)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-4)# 2. Move it to the TPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-5)tpu_tensor = cpu_tensor.to(device)  # Using the device object
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-6)# OR
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-7)tpu_tensor_alt = cpu_tensor.to("tpu")  # Using the "tpu" string
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-8)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-9)# 3. Create a tensor directly on the TPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-10)direct_tpu_tensor = torch.randn((5, 5), device="tpu")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-11)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-12)print(f"cpu_tensor is on: {cpu_tensor.device}")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-13)print(f"tpu_tensor is on: {tpu_tensor.device}")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-3-14)print(f"direct_tpu_tensor is on: {direct_tpu_tensor.device}")

```

## 4. Compute and materialize results[¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#4-compute-and-materialize-results "Permanent link")
Performing math on the TPU is seamless. When you perform operations on TPU tensors, the computation happens on the hardware. To retrieve the data back to the CPU for printing or interaction with standard Python libraries, use the `.cpu()` method.

```
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-1)# Perform a simple operation on the TPU
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-2)result_on_tpu = tpu_tensor + direct_tpu_tensor
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-3)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-4)# Bring the result back to the CPU to print or use in other libraries
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-5)result_on_cpu = result_on_tpu.cpu()
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-6)
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-7)print("Computation complete.")
[](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#__codelineno-4-8)print(f"Result Checksum (Sum): {result_on_cpu.sum():.4f}")

```

### 🎉 Success![¶](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/#success "Permanent link")
You have successfully initialized the TPU, mapped tensors to the device, performed a calculation, and retrieved the results.
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)