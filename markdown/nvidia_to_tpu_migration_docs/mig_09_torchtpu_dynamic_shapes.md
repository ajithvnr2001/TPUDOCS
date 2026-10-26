---
id: "mig_09_torchtpu_dynamic_shapes"
title: "TorchTPU compilation and dynamic shapes"
url: "https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/"
category: "Nvidia to tpu migration docs"
description: "Static and bounded dynamic shapes, recompilation behavior, and current limitations."
crawled_at: "2026-10-26T12:48:08.848600+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#dynamic-shapes)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
Dynamic shapes 
[ ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/?q= "Share")
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
    * [ TorchTPU custom kernels  ](https://torchtpu.readthedocs.io/en/latest/custom_kernels/)
    * Dynamic shapes  [ Dynamic shapes  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/) Table of contents 
      * [ How dynamic shapes are handled by TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#how-dynamic-shapes-are-handled-by-torchtpu)
        * [ Compilation  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#compilation)
        * [ Execution  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#execution)
      * [ Motivating use case: Autoregressive decoding  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#motivating-use-case-autoregressive-decoding)
      * [ Example: Autoregressive loop with a growing tensor  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#example-autoregressive-loop-with-a-growing-tensor)
        * [ 1. Running with dynamic=False  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#1-running-with-dynamicfalse)
        * [ 2. Running with dynamic=None (Bounded Dynamism)  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#2-running-with-dynamicnone-bounded-dynamism)
      * [ Current limitations  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#current-limitations)
  * Case studies  Case studies 
    * [ FLUX optimization  ](https://torchtpu.readthedocs.io/en/latest/case_studies_flux/)
    * [ Muse Glimmer 30B: autoregressive decoding  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_inference/)
    * [ Muse Glimmer 30B: training  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_training/)
    * [ FSDP best practices  ](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/)
  * Analyze your workload  Analyze your workload 
    * [ Manage numerical precision in TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/)
    * [ Performance profiling with XProf  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/)


Table of contents 
  * [ How dynamic shapes are handled by TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#how-dynamic-shapes-are-handled-by-torchtpu)
    * [ Compilation  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#compilation)
    * [ Execution  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#execution)
  * [ Motivating use case: Autoregressive decoding  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#motivating-use-case-autoregressive-decoding)
  * [ Example: Autoregressive loop with a growing tensor  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#example-autoregressive-loop-with-a-growing-tensor)
    * [ 1. Running with dynamic=False  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#1-running-with-dynamicfalse)
    * [ 2. Running with dynamic=None (Bounded Dynamism)  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#2-running-with-dynamicnone-bounded-dynamism)
  * [ Current limitations  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#current-limitations)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/dynamic_shapes.md "Edit this page")
# Dynamic shapes[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#dynamic-shapes "Permanent link")
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-pytorch/torch_tpu/blob/0.2.0-docs/docs/notebooks/dynamic_shapes.ipynb)
When you compile a model with `torch.compile(model)`, TorchTPU lowers the computation to StableHLO and compiles it with the XLA compiler (see [How TorchTPU works](https://torchtpu.readthedocs.io/en/latest/how_torchtpu_works/)). The XLA compiler is traditionally designed around **statically known tensor shapes** so that High Bandwidth Memory (HBM) buffers can be laid out ahead of time, operator pipelines can be fused, and matrix multiplications can be tiled for the TPU's systolic arrays (MXUs). When input tensor dimensions vary across calls in a `torch.compile` workload, compiling for each exact shape would invalidate Dynamo's shape guards and trigger a costly full XLA recompilation on every new shape.
To support **dynamic shapes** without constant recompilations, TorchTPU uses **Bounded Dynamism** , where the compile-time upper bounds of dynamic dimensions are fixed while the actual runtime dimension sizes are tracked dynamically by XLA.
## How dynamic shapes are handled by TorchTPU[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#how-dynamic-shapes-are-handled-by-torchtpu "Permanent link")
When you compile a model or function with default dynamism, that is `torch.compile(model, dynamic=None)` (as input shapes vary across calls) or explicitly mark dynamic dimensions with `torch._dynamo.mark_dynamic`, Dynamo traces the computation and produces an FX graph where changing dimensions are represented as symbolic integer variables (`torch.SymInt`) instead of fixed constants. TorchTPU handles these symbolic dimensions as follows:
### Compilation[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#compilation "Permanent link")
  * TorchTPU intercepts the traced FX graph, determines an overall `[lower_bound, upper_bound]` range for each symbolic dimension (from `mark_dynamic(..., min=..., max=...)` or inferred by Dynamo from the initial runtime size `S`), and divides that range into contiguous buckets aligned to multiples of `bucket_size` (default `128`, matching the TPU's 128-lane tile dimension), up to `num_dynamic_buckets` (default `1`, maximum `8`):
    * The first bucket covers from `lower_bound` up to the next multiple of `128` at or after `S` (`U_1`), the second bucket covers from `U_1 + 1` up to the next multiple of `128` (`U_2`), and so on (for example, `[lower_bound, 128]`, `[129, 256]`, ...).
    * TorchTPU registers a single range guard across the full span of all buckets with Dynamo, so Dynamo only triggers recompilation if the dimension grows beyond the overall `upper_bound`.
  * For each bucket, TorchTPU replaces the symbolic dimension with the bucket's static upper bound `U`, passes the actual runtime dimension size as an input, and lowers the graph to StableHLO with bounded tensor types that track both the static upper bound `U` and the active runtime size across all operations.
  * The resulting module is compiled by XLA for each configured bucket upper bound `U`.


### Execution[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#execution "Permanent link")
  * At runtime, based on the actual size of the dynamic dimension, TorchTPU selects the corresponding compiled bucket executable.
  * When executing the compiled module, XLA pads the dynamic input tensor up to the bucket's static upper bound `U` and resets values in the padded region beyond the active runtime size to algebraic identity values, ensuring that padded elements do not affect the output result.
  * For dynamic output tensors, padding remains at the end of the buffer, allowing TorchTPU to return the buffer to PyTorch with a lightweight shape metadata update rather than physically slicing the tensor.


## Motivating use case: Autoregressive decoding[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#motivating-use-case-autoregressive-decoding "Permanent link")
A primary workload that motivates bounded dynamism is **autoregressive LLM decoding** with a dynamically growing KV cache. In a standard decode loop, each step appends the new token's key and value states to the cached history along the sequence dimension via `torch.cat`:
  * **Prefill:** Input prompt has shape `[B, S]` (batch size `B`, prompt sequence length `S`), producing a KV cache of shape `[B, H_kv, S, D]` (`H_kv` key/value heads, head dimension `D`).
  * **Decode step 1:** Input token has shape `[B, 1]`, concatenating with the cache to produce shape `[B, H_kv, S + 1, D]`.
  * **Decode step`t` :** The KV cache sequence length grows to `S + t`.


With static-shape compilation (`dynamic=False`), Dynamo guards on the exact sequence length of the KV cache. Every decode step changes the tensor shape, invalidates the guard, and triggers a **full XLA recompilation on every generated token** —turning millisecond decode steps into multi-second compilations unless you rewrite the model to preallocate static buffers and perform in-place mutations.
**Bounded dynamism** solves this without requiring model rewrites: as the KV cache grows across decode steps (`S + 1`, `S + 2`, ...), all shapes within the compiled bucket (`<= 128`, `<= 256`, ...) reuse the same XLA executable.
For a hands-on walkthrough applying bounded dynamism to a full LLM decode loop (and comparing against static KV cache preallocation), see [LLM inference end-to-end](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_inference/).
## Example: Autoregressive loop with a growing tensor[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#example-autoregressive-loop-with-a-growing-tensor "Permanent link")
To see how static compilation (`dynamic=False`) and bounded dynamism using default dynamism (`dynamic=None`) behave in practice, consider a minimal autoregressive loop where each step appends a new token along the sequence dimension (`dim=2`) using `torch.cat`:

```
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-1)import time
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-2)import torch
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-3)from torch._functorch._aot_autograd import autograd_cache
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-4)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-5)torch._logging.set_logs()  # pylint: disable=protected-access
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-6)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-7)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-8)def decode_step(
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-9)    kv_cache: torch.Tensor, new_token: torch.Tensor
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-10)) -> torch.Tensor:
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-11)  return torch.cat([kv_cache, new_token], dim=2)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-12)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-13)def run_decode_loop(
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-14)    compiled_step, num_steps: int = 10, prefix: str = ""
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-15)) -> None:
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-16)  kv_cache = torch.ones((1, 8, 16, 128), dtype=torch.bfloat16, device=device)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-17)  new_token = torch.ones((1, 8, 1, 128), dtype=torch.bfloat16, device=device)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-18)  torch.accelerator.synchronize()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-19)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-20)  for step in range(num_steps):
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-21)    start = time.perf_counter()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-22)    kv_cache = compiled_step(kv_cache, new_token)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-23)    torch.accelerator.synchronize()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-24)    step_ms = (time.perf_counter() - start) * 1000
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-25)    print(
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-26)        f"{prefix}Step {step + 1}/{num_steps} (seq_len={kv_cache.shape[2]}):"
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-27)        f" {step_ms:.2f} ms",
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-28)        flush=True,
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-0-29)    )

```

### 1. Running with `dynamic=False`[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#1-running-with-dynamicfalse "Permanent link")

```
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-1-1)torch._dynamo.reset()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-1-2)autograd_cache.AOTAutogradCache.clear()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-1-3)torch._dynamo.config.recompile_limit = 64
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-1-4)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-1-5)step_static = torch.compile(decode_step, backend="tpu", dynamic=False)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-1-6)run_decode_loop(step_static, prefix="[dynamic=False] ")

```

Sample output:

```
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-1)[dynamic=False] Step 1/10 (seq_len=17): 49.54 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-2)[dynamic=False] Step 2/10 (seq_len=18): 43.51 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-3)[dynamic=False] Step 3/10 (seq_len=19): 39.52 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-4)[dynamic=False] Step 4/10 (seq_len=20): 38.63 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-5)[dynamic=False] Step 5/10 (seq_len=21): 38.40 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-6)[dynamic=False] Step 6/10 (seq_len=22): 38.23 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-7)[dynamic=False] Step 7/10 (seq_len=23): 38.11 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-8)[dynamic=False] Step 8/10 (seq_len=24): 38.55 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-9)[dynamic=False] Step 9/10 (seq_len=25): 37.89 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-2-10)[dynamic=False] Step 10/10 (seq_len=26): 37.75 ms

```

**What happened:** With `dynamic=False`, Dynamo guards on the exact sequence length of `kv_cache` (`16`, `17`, `18`, ...). Because `torch.cat` increases `dim=2` by `1` on every iteration, the shape guard fails on every call and triggers a full XLA recompilation at every step.
### 2. Running with `dynamic=None` (Bounded Dynamism)[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#2-running-with-dynamicnone-bounded-dynamism "Permanent link")

```
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-3-1)torch._dynamo.reset()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-3-2)autograd_cache.AOTAutogradCache.clear()
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-3-3)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-3-4)step_dynamic = torch.compile(decode_step, backend="tpu", dynamic=None)
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-3-5)run_decode_loop(step_dynamic, prefix="[dynamic=None] ")

```

Sample output:

```
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-1)[dynamic=None] Step 1/10 (seq_len=17): 49.59 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-2)[dynamic=None] Step 2/10 (seq_len=18): 206.68 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-3)[dynamic=None] Step 3/10 (seq_len=19): 64.29 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-4)[dynamic=None] Step 4/10 (seq_len=20): 0.51 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-5)[dynamic=None] Step 5/10 (seq_len=21): 0.43 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-6)[dynamic=None] Step 6/10 (seq_len=22): 0.38 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-7)[dynamic=None] Step 7/10 (seq_len=23): 0.40 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-8)[dynamic=None] Step 8/10 (seq_len=24): 0.44 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-9)[dynamic=None] Step 9/10 (seq_len=25): 0.45 ms
[](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#__codelineno-4-10)[dynamic=None] Step 10/10 (seq_len=26): 0.37 ms

```

**What happened:** With `dynamic=None`, only the first 3 iterations incur compilation overhead, and from step 4 onward execution drops to about 0.4 ms per step (~100x faster) with zero recompilations:
  * **Step 1 (`seq_len=16 -> 17`):** Dynamo sees the inputs for the first time and compiles a static executable for `seq_len=16`.
  * **Step 2 (`seq_len=17 -> 18`):** Because `dim=2` changed from `16` to `17`, Dynamo automatically marks `dim=2` as dynamic (`SymInt`) and TorchTPU compiles a bounded-dynamic executable for the `[17, 128]` bucket using the initial input tensor layout.
  * **Step 3 (`seq_len=18 -> 19`):** The bounded-dynamic output buffer produced by step 2 has XLA's padded output layout, so TorchTPU compiles the `[17,     128]` bucket once more for that steady-state XLA layout.
  * **Steps 4–10 (`seq_len=19 -> 26`):** Both the sequence length (within the `<= 128` bucket) and the XLA buffer layout match the cached executable, so every subsequent step dispatches the pre-compiled XLA executable directly without recompiling.


Tip
If you already know which dimension will vary ahead of time, you can call `torch._dynamo.mark_dynamic(kv_cache, 2, min=16, max=128)` before the first step. This tells Dynamo to trace `dim=2` as dynamic immediately on Step 1—skipping the initial static compilation on Step 1 and letting you specify explicit `[min, max]` bounds.
## Current limitations[¶](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/#current-limitations "Permanent link")
Bounded dynamism in TorchTPU is actively evolving and is currently optimized around the **autoregressive KV cache** use case. Keep the following limitations in mind when applying it to your models:
  * **Bucket limit and unbounded dynamism:** At most **8 buckets** (`num_dynamic_buckets <= 8`) are compiled per trace. Unbounded dynamism is not supported yet—if a dynamic dimension grows past the highest compiled bucket's upper bound, a recompilation is triggered.
  * **Dynamo shape constraints:** Bucket upper bounds must satisfy active Dynamo shape constraints (such as divisibility requirements from `reshape` or `view`). Otherwise, TorchTPU falls back to a single bucket with upper bound `2 * S` (twice the initial runtime size `S`).
  * **Compute and HBM overhead up to the bucket upper bound:** Because execution runs on buffers padded to the bucket's static upper bound `U`, HBM footprint and FLOPs scale with `U` rather than the actual runtime size. Setting a very large `bucket_size` or `mark_dynamic(..., max=U)` when the actual size is much smaller than `U` pays the compute and memory cost of `U`.
  * **XLA layout changes:** Even when a tensor's shape falls within an already-compiled bucket, a change in the underlying XLA physical layout of an input buffer will trigger a bucket recompilation.
  * **No persistent compilation cache (`AOTAutogradCache`):** Bounded-dynamic executables are not serialized to `AOTAutogradCache` yet, so they are recompiled on each new process start.
  * **Operator coverage:** Not all PyTorch operators support bounded dynamic shapes yet.
  * **Views as model inputs:** Support for passing tensor views directly as inputs to the compiled model is limited.
  * **Data-dependent dynamism:** Operations whose output shapes depend on runtime tensor values (such as `torch.nonzero`) are not supported.
  * **Custom kernels:** Bounded dynamic shapes are not supported with custom TPU kernels (such as Pallas kernels registered via `torch.tpu.pallas.jax_op`).
  * **dynamic=True:** torch.compile() _dynamic=True_ mode is not supported.


Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)