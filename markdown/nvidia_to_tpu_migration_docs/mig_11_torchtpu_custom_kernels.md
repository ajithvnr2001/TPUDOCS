---
id: "mig_11_torchtpu_custom_kernels"
title: "TorchTPU custom kernels and API reference"
url: "https://torchtpu.readthedocs.io/en/latest/custom_kernels/"
category: "Nvidia to tpu migration docs"
description: "Integrate prebuilt Tokamax kernels, custom Pallas kernels, or experimental Helion kernels."
crawled_at: "2026-10-26T12:48:08.094119+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#torchtpu-custom-kernels)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
TorchTPU custom kernels 
[ ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/?q= "Share")
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
    * [ Get started with TorchTPU on GKE  ](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/)
    * [ TorchTPU supported feature set and future work  ](https://torchtpu.readthedocs.io/en/latest/feature_set/)
    * [ TorchTPU API Reference  ](https://torchtpu.readthedocs.io/en/latest/api_reference/)
    * [ TorchTPU FAQ  ](https://torchtpu.readthedocs.io/en/latest/faq/)
  * In-depth  In-depth 
    * [ How TorchTPU works  ](https://torchtpu.readthedocs.io/en/latest/how_torchtpu_works/)
    * [ TorchTPU execution model  ](https://torchtpu.readthedocs.io/en/latest/torchtpu_execution_model/)
    * [ TorchTPU and the TPU memory model  ](https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/)
    * [ TorchTPU distributed support  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/)
    * TorchTPU custom kernels  [ TorchTPU custom kernels  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/) Table of contents 
      * [ Choosing an integration approach  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#choosing-an-integration-approach)
      * [ 1. Using pre-built kernels from Tokamax  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#1-using-pre-built-kernels-from-tokamax)
        * [ When to use  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#when-to-use)
        * [ How it works  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-it-works)
      * [ 2. Writing Custom Pallas Kernels  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#2-writing-custom-pallas-kernels)
        * [ How to integrate a Pallas kernel  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-to-integrate-a-pallas-kernel)
      * [ 3. Writing portable kernels with Helion (experimental)  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#3-writing-portable-kernels-with-helion-experimental)
        * [ How to write a Helion kernel  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-to-write-a-helion-kernel)
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
  * [ Choosing an integration approach  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#choosing-an-integration-approach)
  * [ 1. Using pre-built kernels from Tokamax  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#1-using-pre-built-kernels-from-tokamax)
    * [ When to use  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#when-to-use)
    * [ How it works  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-it-works)
  * [ 2. Writing Custom Pallas Kernels  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#2-writing-custom-pallas-kernels)
    * [ How to integrate a Pallas kernel  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-to-integrate-a-pallas-kernel)
  * [ 3. Writing portable kernels with Helion (experimental)  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#3-writing-portable-kernels-with-helion-experimental)
    * [ How to write a Helion kernel  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-to-write-a-helion-kernel)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/custom_kernels.md "Edit this page")
# TorchTPU custom kernels[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#torchtpu-custom-kernels "Permanent link")
While TorchTPU natively accelerates standard PyTorch framework operators (such as [`torch.nn.functional.scaled_dot_product_attention`](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)), you may need to integrate custom kernels to accelerate model-specific operations, fuse operations to reduce memory bandwidth overhead, or implement novel architectures not yet covered by standard PyTorch operators.
## Choosing an integration approach[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#choosing-an-integration-approach "Permanent link")
TorchTPU provides three ways to use custom kernels on TPU, depending on your use case:  
| Approach  | Status  | Best For  |  
| --- | --- | --- |  
| **Tokamax**  | Production Ready  | Drop-in acceleration for common LLM/MoE building blocks without writing kernel code.  |  
| **Pallas (`torch.tpu.pallas.jax_op`)**  | Production Ready  | Writing bespoke, maximum-performance TPU kernels in JAX/Pallas and calling them from PyTorch.  |  
| **Helion**  | Experimental  | Writing kernels that are portable across accelerators (e.g. GPU, TPU) using a PyTorch-native DSL.  |  
## 1. Using pre-built kernels from Tokamax[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#1-using-pre-built-kernels-from-tokamax "Permanent link")
Before writing a custom kernel from scratch, check if the operator is available in [Tokamax](http://openxla.org/tokamax)—a library of high-performance TPU kernels with native PyTorch interoperability.
### When to use[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#when-to-use "Permanent link")
Use Tokamax when your model requires standard high-performance building blocks, including:
  * **Mixture-of-Experts (MoE):** Grouped matrix multiplication, token gathers, and scatters.
  * **Attention Variants:** Paged attention, Gated DeltaNet, Kimi Delta Attention, and Multi-head Latent Attention (MLA).
  * **Selection:** Optimized `TopK` computation.


### How it works[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-it-works "Permanent link")
Tokamax kernels are authored in JAX/Pallas and backed by integrated autotuning (such as automated tile-size search), low-overhead XProf benchmarking, and regression testing across TPU generations. Under the hood, Tokamax uses `torch.tpu.pallas.jax_op` to handle framework interoperability transparently and exposes native PyTorch APIs directly to your model.
## 2. Writing Custom Pallas Kernels[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#2-writing-custom-pallas-kernels "Permanent link")
If you need a bespoke operation not covered by PyTorch or Tokamax, you can write a TPU kernel in [Pallas](https://docs.jax.dev/en/latest/pallas/index.html) and register it as a PyTorch operator using `torch.tpu.pallas.jax_op`.
### How to integrate a Pallas kernel[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-to-integrate-a-pallas-kernel "Permanent link")
  1. **Define the Pallas kernel** using input and output memory references (`Ref`s).
  2. **Wrap the kernel in a JAX function** using `pl.pallas_call` to specify output shapes and dtypes.
  3. **Register the JAX function with TorchTPU** via `torch.tpu.pallas.jax_op`.

```
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-1)import jax
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-2)from jax.experimental import pallas as pl
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-3)import torch
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-4)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-5)# 1. Define the Pallas kernel
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-6)def add_vectors_pallas_kernel(x_ref, y_ref, o_ref):
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-7)  x, y = x_ref[...], y_ref[...]
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-8)  o_ref[...] = x + y
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-9)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-10)# 2. Wrap the Pallas kernel into a JAX function
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-11)def add_vectors_jax(x: jax.Array, y: jax.Array) -> jax.Array:
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-12)  return pl.pallas_call(
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-13)      add_vectors_pallas_kernel,
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-14)      out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-15)  )(x, y)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-16)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-17)# 3. Wrap it for PyTorch using the functional interface
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-18)add_vectors_fn = torch.tpu.pallas.jax_op(
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-19)    "pallas::add_vectors",
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-20)    add_vectors_jax,
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-21))
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-22)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-23)# 4. Call it like a standard PyTorch function
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-24)x = torch.tensor([1.0, 2.0, 3.0], device="tpu")
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-25)y = torch.tensor([4.0, 5.0, 6.0], device="tpu")
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-0-26)z = add_vectors_fn(x, y)

```

## 3. Writing portable kernels with Helion (experimental)[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#3-writing-portable-kernels-with-helion-experimental "Permanent link")
If you want your kernels to be portable across accelerators (e.g. TPU, GPU), you can use [Helion](https://helionlang.com/), a PyTorch-native DSL for kernel authoring.
Note
Helion support on TorchTPU is currently **experimental**. For production workloads, use Tokamax or `torch.tpu.pallas.jax_op`.
### How to write a Helion kernel[¶](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#how-to-write-a-helion-kernel "Permanent link")
Decorate your function with `@helion.kernel`. Use standard PyTorch operations for host-side setup, and `hl.tile` to define the device execution loop over partitioned tiles:

```
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-1)import helion
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-2)import helion.language as hl
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-3)import torch
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-4)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-5)# 1. Define the kernel in Helion
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-6)@helion.kernel
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-7)def add_vectors(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-8)  # Standard PyTorch host-side setup
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-9)  x, y = torch.broadcast_tensors(x, y)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-10)  out = torch.empty_like(x)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-11)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-12)  # Device execution loop over automatically partitioned tiles
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-13)  for tile in hl.tile(out.size()):
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-14)    out[tile] = x[tile] + y[tile]
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-15)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-16)  return out
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-17)
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-18)# 2. Call it like a standard PyTorch function
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-19)x = torch.tensor([1.0, 2.0, 3.0], device="tpu")
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-20)y = torch.tensor([4.0, 5.0, 6.0], device="tpu")
[](https://torchtpu.readthedocs.io/en/latest/custom_kernels/#__codelineno-1-21)z = add_vectors(x, y)

```

For more information about Helion, see the [Helion documentation](https://helionlang.com/), ask questions in the [PyTorch developer discussion forum](https://dev-discuss.pytorch.org/c/helion/31), or [report issues on GitHub](https://github.com/pytorch/helion/issues).
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)