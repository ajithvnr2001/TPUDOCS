---
id: "mig_12_torchtpu_numerical_precision"
title: "TorchTPU numerical precision"
url: "https://torchtpu.readthedocs.io/en/latest/numerical_precision/"
category: "Nvidia to tpu migration docs"
description: "Understand numerical differences from CUDA and configure TPU matrix-multiplication precision."
crawled_at: "2026-10-26T12:48:12.303761+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#manage-numerical-precision-in-torchtpu)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
Manage numerical precision in TorchTPU 
[ ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/?q= "Share")
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
    * [ Dynamic shapes  ](https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/)
  * Case studies  Case studies 
    * [ FLUX optimization  ](https://torchtpu.readthedocs.io/en/latest/case_studies_flux/)
    * [ Muse Glimmer 30B: autoregressive decoding  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_inference/)
    * [ Muse Glimmer 30B: training  ](https://torchtpu.readthedocs.io/en/latest/case_studies_muse_glimmer_30b_training/)
    * [ FSDP best practices  ](https://torchtpu.readthedocs.io/en/latest/case_studies_fsdp/)
  * Analyze your workload  Analyze your workload 
    * Manage numerical precision in TorchTPU  [ Manage numerical precision in TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/) Table of contents 
      * [ Compare PyTorch precision on CUDA and TPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#compare-pytorch-precision-on-cuda-and-tpu)
      * [ Specify precision modes  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#specify-precision-modes)
        * [ Compare accuracy across precision modes  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#compare-accuracy-across-precision-modes)
      * [ Verify numerical parity  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#verify-numerical-parity)
        * [ Interpret detailed mismatches  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#interpret-detailed-mismatches)
        * [ Best practices for parity  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#best-practices-for-parity)
      * [ Specify output precision  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#specify-output-precision)
      * [ Control excess precision  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#control-excess-precision)
      * [ Understand TPU MXU precision  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#understand-tpu-mxu-precision)
        * [ Multi-pass polynomial expansion for float32  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#multi-pass-polynomial-expansion-for-float32)
        * [ Evaluate 3-pass and 6-pass performance  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#evaluate-3-pass-and-6-pass-performance)
      * [ Validate bitwise precision behavior  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#validate-bitwise-precision-behavior)
    * [ Performance profiling with XProf  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/)


Table of contents 
  * [ Compare PyTorch precision on CUDA and TPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#compare-pytorch-precision-on-cuda-and-tpu)
  * [ Specify precision modes  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#specify-precision-modes)
    * [ Compare accuracy across precision modes  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#compare-accuracy-across-precision-modes)
  * [ Verify numerical parity  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#verify-numerical-parity)
    * [ Interpret detailed mismatches  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#interpret-detailed-mismatches)
    * [ Best practices for parity  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#best-practices-for-parity)
  * [ Specify output precision  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#specify-output-precision)
  * [ Control excess precision  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#control-excess-precision)
  * [ Understand TPU MXU precision  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#understand-tpu-mxu-precision)
    * [ Multi-pass polynomial expansion for float32  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#multi-pass-polynomial-expansion-for-float32)
    * [ Evaluate 3-pass and 6-pass performance  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#evaluate-3-pass-and-6-pass-performance)
  * [ Validate bitwise precision behavior  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#validate-bitwise-precision-behavior)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/numerical_precision.md "Edit this page")
# Manage numerical precision in TorchTPU[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#manage-numerical-precision-in-torchtpu "Permanent link")
Google TPUs split floating-point operations between two hardware units to balance throughput and numerical accuracy:
  * **Matrix Multiply Unit (MXU):** Executes contracting operations (such as `torch.matmul`, `torch.mm`, `torch.bmm`, and convolutions) using native `bfloat16` inputs (8-bit significand) with 32-bit `float32` accumulation.
  * **Vector Execution Unit (VPU):** Executes non-contracting operations (such as element-wise arithmetic, activations, layer normalization, and softmax) in full IEEE-754 `float32` (24-bit significand).


This guide covers how to configure `float32` matrix multiplication precision modes, verify numerical parity between CPU and TPU, control output accumulator types and excess precision, and validate bitwise MXU behavior in code.
### Compare PyTorch precision on CUDA and TPU[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#compare-pytorch-precision-on-cuda-and-tpu "Permanent link")
TorchTPU supports standard PyTorch precision APIs (`torch.set_float32_matmul_precision` and `torch.get_float32_matmul_precision`) alongside TPU-specific controls (`torch.tpu.Precision` and `torch.tpu.precision`):  
| Dimension  | PyTorch on CUDA  | PyTorch on TPU (TorchTPU)  |  
| --- | --- | --- |  
| **Default precision mode**  |  `"highest"` (pure `float32`)  |  `"medium"` (`Precision.DEFAULT`)  |  
| **Fast math accelerator primitive**  | Tensor Cores (`TF32`)  | Systolic MXUs (`bfloat16`)  |  
| **Fast math bits**  | 1 sign + 8 exponent + 10 mantissa bits (19-bit `TF32`)  | 1 sign + 8 exponent + 7 mantissa bits (16-bit `bfloat16`)  |  
| **Accumulation precision**  |  `float32` (`"highest"`, `"high"`), `TF32` (`"medium"`)  |  `float32` across all modes  |  
| **Higher precision mechanism**  | Dedicated hardware `float32`/`TF32` units  | Multi-pass decomposition (3x or 6x MXU passes)  |  
| **Performance impact of`high` /`highest`**  | Baseline speed or modest slowdown (~1–2x)  | ~3x MXU compute cost for `"high"`; ~6x for `"highest"`  |  
| **Scoping API**  | Global `torch.set_float32_matmul_precision`  | Global   
`torch.set_float32_matmul_precision` + scoped `torch.tpu.precision`  |  
## Specify precision modes[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#specify-precision-modes "Permanent link")
When multiplying `float32` tensors on the MXU, TorchTPU maps PyTorch's precision levels to the `torch.tpu.Precision` enum:
  * `"medium"` / `Precision.DEFAULT` (1-pass): **Default.** Rounds `float32` inputs to `bfloat16` (multiplying the top 8 bits of significand) and accumulates in `float32`. Recommended for nearly all training and inference workloads.
  * `"high"` / `Precision.HIGH` (3-pass): Splits `float32` inputs into high and low `bfloat16` components and computes three cross-terms (multiplying the first 16 bits of significand) at roughly 3x the MXU compute cost.
  * `"highest"` / `Precision.HIGHEST` (6-pass): Splits `float32` inputs into three `bfloat16` components and computes six cross-terms (multiplying all 24 bits of significand) to approximate full IEEE-754 `float32` accuracy at roughly 6x the MXU compute cost.


You can configure matrix multiplication precision in two ways:
  * **Global configuration:** Call `torch.set_float32_matmul_precision("medium"     | "high" | "highest")` to set the default mode for the process.
  * **Scoped context manager:** Use `with torch.tpu.precision(mode):` to apply higher precision only to numerically sensitive layers or submodules.
  * **Performance warning:** Selecting `"high"` or `"highest"` emits a one-time warning (`TORCH_WARN_ONCE`). Keep the default `"medium"` mode unless you observe precision-related convergence issues.


Note
Entering or exiting `torch.tpu.precision` introduces a `torch.compile` graph break. When using `torch.compile(..., fullgraph=True)`, set precision outside the compiled function with `torch.set_float32_matmul_precision(...)` or wrap the outer call in `with torch.tpu.precision(...):`.
Use `torch.tpu.precision` to compare steady-state execution time across the three modes:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-1)import time
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-2)import torch
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-3)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-4)device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-5)precision = torch.tpu.precision  # Context manager
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-6)Precision = torch.tpu.Precision  # Enum class
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-7)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-8)print(f"Default matmul precision: {torch.get_float32_matmul_precision()}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-9)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-10)size = (8, 2048, 2048)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-11)a = torch.randn(size, dtype=torch.float32, device=device)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-12)b = torch.randn(size, dtype=torch.float32, device=device)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-13)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-14)def run_matmul():
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-15)  res = torch.matmul(a, b)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-16)  torch.accelerator.synchronize()
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-17)  return res
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-18)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-19)for mode in [Precision.DEFAULT, Precision.HIGH, Precision.HIGHEST]:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-20)  with precision(mode):
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-21)    # Warm up to compile the graph before timing steady-state execution
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-22)    run_matmul()
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-23)    start = time.perf_counter()
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-24)    run_matmul()
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-0-25)    print(f"{mode} time: {time.perf_counter() - start:.4f}s")

```

### Compare accuracy across precision modes[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#compare-accuracy-across-precision-modes "Permanent link")
Compare the TPU outputs against a CPU `float32` reference on the same inputs to see how each precision mode reduces numerical error:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-1)# CPU float32 reference result
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-2)c_ref = torch.matmul(a.cpu(), b.cpu())
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-3)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-4)for mode in [Precision.DEFAULT, Precision.HIGH, Precision.HIGHEST]:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-5)  with precision(mode):
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-6)    res = torch.matmul(a, b)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-7)    diff = res.cpu() - c_ref
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-8)    print(f"Mode: {mode}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-9)    print(f"  Max Absolute Error: {diff.abs().max():.6e}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-10)    print(
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-11)        "  Mean Relative Error: "
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-12)        f" {(diff.abs() / (c_ref.abs() + 1e-8)).mean():.6e}\n"
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-1-13)    )

```

## Verify numerical parity[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#verify-numerical-parity "Permanent link")
When porting a model to TPU or debugging convergence differences, verify numerical parity by running the same layer or submodule on CPU and TPU with synchronized weights and identical inputs, then comparing the outputs with `torch.testing.assert_close`:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-1)import torch.nn as nn
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-2)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-3)# 1. Set up identical models in bfloat16 for a fair comparison
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-4)model_cpu = nn.Linear(10, 10).cpu().to(torch.bfloat16)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-5)model_tpu = nn.Linear(10, 10).to(device).to(torch.bfloat16)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-6)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-7)# 2. Synchronize weights (mandatory for parity checks)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-8)model_tpu.load_state_dict(model_cpu.state_dict())
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-9)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-10)# 3. Create identical input data for both devices
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-11)input_data = torch.randn(5, 10, dtype=torch.bfloat16)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-12)input_tpu = input_data.to(device)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-13)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-14)# 4. Run the forward pass
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-15)out_cpu = model_cpu(input_data)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-16)out_tpu = model_tpu(input_tpu)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-17)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-18)# 5. Compare results
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-19)# Note: TorchTPU's bfloat16 accumulation and fusion differences can exceed
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-20)# default tolerances, generating the `assert_close` diagnostic report below.
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-21)try:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-22)  torch.testing.assert_close(out_tpu.cpu(), out_cpu)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-23)  print("Parity check passed!")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-24)except AssertionError as e:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-25)  print("Parity check failed (expected for hardware precision drift):\n")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-2-26)  print(e)

```

### Interpret detailed mismatches[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#interpret-detailed-mismatches "Permanent link")
When tensors exceed tolerances, `torch.testing.assert_close` prints a summary that helps distinguish normal floating-point drift from a logic bug:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-3-1)Tensor-likes are not close!
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-3-2)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-3-3)Mismatched elements: 1 / 50 (2.0%)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-3-4)Greatest absolute difference: 0.006596 at index (3, 9) (up to 1e-05 allowed)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-3-5)Greatest relative difference: 0.165375 at index (3, 9) (up to 0.016 allowed)

```

  * **Mismatched elements:** A high percentage of elements with small absolute differences typically indicates standard rounding or accumulation-order differences from compiler fusions rather than a bug.
  * **Greatest absolute / relative difference:** Reports the largest error and its tensor index so you can inspect outliers or choose appropriate `atol` and `rtol` thresholds.


### Best practices for parity[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#best-practices-for-parity "Permanent link")
  * **Match data types on both devices:** Compare `bfloat16` on TPU against `bfloat16` on CPU, or `float32` on TPU (with `Precision.HIGHEST`) against `float32` on CPU. Comparing `bfloat16` against `float32` measures quantization error rather than hardware drift.
  * **Check gradients as well as activations:** After calling `loss.backward()`, compare `model_tpu.weight.grad.cpu()` against `model_cpu.weight.grad` using the same pattern.
  * **Start from standard tolerances:** Use the default tolerances in the [PyTorch testing documentation](https://docs.pytorch.org/docs/stable/testing.html) as a baseline, and relax `atol` or `rtol` only where expected for reduced-precision accumulation.


## Specify output precision[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#specify-output-precision "Permanent link")
When multiplying `bfloat16` tensors with `torch.mm` or `torch.bmm`, the MXU accumulates products in `float32` before rounding the final output back to `bfloat16`. Pass `out_dtype=torch.float32` to return the `float32` accumulator directly without downcasting:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-4-1)a_bmm = torch.randn((2, 256, 256), dtype=torch.bfloat16, device=device)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-4-2)# Using out_dtype to force float32 output accumulator precision
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-4-3)res_bmm = torch.bmm(a_bmm, a_bmm, out_dtype=torch.float32)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-4-4)print(f"Input dtype: {a_bmm.dtype}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-4-5)print(f"Output dtype: {res_bmm.dtype}")

```

## Control excess precision[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#control-excess-precision "Permanent link")
Because the TPU MXU accumulates `bfloat16` matrix multiplications in `float32`, the XLA compiler can optimize fused operations by keeping intermediate values in `float32` instead of rounding them down to `bfloat16` between steps. Retaining these extra intermediate bits is called _excess precision_.
You can configure this behavior globally with `torch.tpu.allow_excess_precision` (which sets the underlying `--xla_allow_excess_precision` compiler flag and defaults to `False`):
  * **Disable excess precision (`False` , default):** Set `torch.tpu.allow_excess_precision = False` to force the compiler to retain intermediate downcasts to `bfloat16` so fused operations match eager `bfloat16` rounding behavior.
  * **Allow excess precision (`True`):** Set `torch.tpu.allow_excess_precision =     True` to allow the compiler to elide intermediate downcasts and keep fused intermediate results in `float32`.


Important
Set `torch.tpu.allow_excess_precision` at the very beginning of your script before running or compiling any TPU operations. The XLA runtime locks this flag when the first compilation starts; attempting to change it to a different value afterward raises a `RuntimeError`.
## Understand TPU MXU precision[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#understand-tpu-mxu-precision "Permanent link")
Understanding how the TPU MXU handles floating-point numbers explains why excess precision and multi-pass `float32` modes work the way they do:
  * **Range vs. precision (`bfloat16`):** [Google Cloud research on `bfloat16`](https://cloud.google.com/blog/products/ai-machine-learning/bfloat16-the-secret-to-high-performance-on-cloud-tpus) showed that neural networks can train with reduced mantissa precision without losing model accuracy, provided they keep the wide dynamic range of `float32` (critical for operations like norms and gradients). While `float32` has 23 mantissa bits (24 bits of significand precision including the implicit leading bit), `bfloat16` keeps the same 8-bit exponent range with only 7 mantissa bits (8 bits of significand precision, for a machine epsilon of `2**-7` or ~0.78%).
  * **Interchange formats vs. arithmetic formats:** Floating-point systems distinguish between **interchange formats** (how numbers are stored in memory) and **arithmetic formats** (how hardware computes and rounds intermediate operations, such as the 3 extra guard, round, and sticky bits in a standard ALU). `bfloat16` can refer to either.
  * **Accumulation along the contracting dimension:** Multiplying two matrices of shape `[I, J] @ [J, K]` computes a grid of inner products of shape `[1,     J] @ [J, 1]`, each summing `J` element-wise products along the **contracting dimension** `J`. Because `bfloat16` has a machine epsilon of `2**-7` (~`0.008`), accumulating `J` products in `bfloat16` would cause large rounding errors. Instead, the MXU accepts `bfloat16` inputs (and `fp8` on newer generations such as TPU v7x) and accumulates intermediate sums in `float32`—playing the same role as guard, round, and sticky bits in an ALU before rounding to the output format.
  * **Input/output format mismatch:** Having `bfloat16` inputs and a `float32` accumulator is the root cause of both _excess precision_ (retaining `float32` intermediates across fused ops) and _less-than-expected precision_ (1-pass `float32` matmul truncating inputs to 8-bit `bfloat16` significands). By contrast, the TPU Vector Execution Unit (VPU) operates on all 23 mantissa bits for `float32` (except for minor IEEE-754 edge cases such as subnormals).


### Multi-pass polynomial expansion for `float32`[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#multi-pass-polynomial-expansion-for-float32 "Permanent link")
Because an MXU only accepts `bfloat16` inputs (8-bit significand), it cannot compute a full 24-bit `float32` matrix multiplication in a single pass. In practice, most modern models store weights in `bfloat16` and rarely execute `float32` matmuls. When full `float32` matmul precision is needed, XLA uses the algorithm from [Leveraging the bfloat16 Artificial Intelligence Datatype For Higher-Precision Computations](https://arxiv.org/pdf/1904.06376) (Henry, Tang, and Heinecke) to represent each 24-bit `float32` significand as a sum of three 8-bit `bfloat16` values (`High + Med + Low`) and expand their product:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-5-1)(a + b + c)(d + e + f) = ad + ae + af + bd + be + bf + cd + ce + cf

```

Multiplying two 3-term sums yields nine `bfloat16` products, of which the three lowest-order terms always underflow in `float32`:  
|   | High  | Med  | Low  |  
| --- | --- | --- | --- |  
| **High**  | High x High _(1-pass)_  | High x Med _(3-pass)_  | High x Low _(6-pass)_  |  
| **Med**  | Med x High _(3-pass)_  | Med x Med _(6-pass)_  | Med x Low _(underflows)_  |  
| **Low**  | Low x High _(6-pass)_  | Low x Med _(underflows)_  | Low x Low _(underflows)_  |  
### Evaluate 3-pass and 6-pass performance[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#evaluate-3-pass-and-6-pass-performance "Permanent link")
Although `Precision.HIGH` (3-pass) and `Precision.HIGHEST` (6-pass) require 3x and 6x as many MXU passes, the end-to-end impact depends on your workload:
  * **Large contracting dimensions:** In modern models trained with `float32` accumulation (such as DeepSeek-V3) that have large contracting dimensions, accumulation noise and non-determinism across thousands of elements dominate the contribution from lower-order mantissa cross-terms, making 1-pass (`Precision.DEFAULT`) sufficient.
  * **Memory-bandwidth-bound models:** Older `float32` models often do not perform enough arithmetic per byte transferred from High Bandwidth Memory (HBM) to saturate the MXU (or GPU Tensor Cores). In these memory-bound workloads, the extra MXU passes for 3-pass and 6-pass execution use otherwise idle MXU cycles, resulting in less than a 3x or 6x end-to-end slowdown.


## Validate bitwise precision behavior[¶](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#validate-bitwise-precision-behavior "Permanent link")
You can verify how the MXU handles mantissa bits and excess precision by constructing inputs using two binary floating-point rules:
  * `1 + 2**-n` creates a number with a binary significand of `1.000...1000...`, placing a fractional `1` at the `n`th mantissa bit.
  * `(1 + m) * (1 + n) = 1 + m + n + mn`: Multiplying two numbers with bits set at mantissa positions 6 and 7 produces a result with bits set at positions 6, 7, and `6 + 7 = 13`. Because `bfloat16` only holds 7 mantissa bits, position 13 overflows `bfloat16` and is only preserved when kept in the `float32` accumulator:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-6-1)value = (1 + 2**-6) * (1 + 2**-7)  # 1.0000_01 * 1.0000_001 = 1.0000_0110_0000_1

```

Wrapping these values in `256 x 256` matrices triggers execution on the MXU and lets you inspect whether the 13th mantissa bit is rounded away or retained:

```
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-1)# Python uses float64 by default.
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-2)bit_6 = 1 + 2**-6
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-3)bit_7 = 1 + 2**-7
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-4)bits_6_7 = 1.0 + 2**-6 + 2**-7
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-5)bits_6_7_13 = 1.0 + 2**-6 + 2**-7 + 2**-13
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-6)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-7)print("=== Python CPU values ===")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-8)print(f"{bit_6=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-9)print(f"{bit_7=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-10)print(f"{bits_6_7=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-11)print(f"{bits_6_7_13=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-12)print(f"{(bit_6 * bit_7)=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-13)assert bit_6 * bit_7 == bits_6_7_13
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-14)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-15)print("=== PyTorch TPU values ===")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-16)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-17)eye = torch.eye(256, dtype=torch.bfloat16, device=device)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-18)bit_6_tensor = eye.clone() * bit_6
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-19)bit_7_tensor = eye.clone() * bit_7
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-20)bits_6_7_tensor = eye.float().clone() * bits_6_7
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-21)bits_6_7_13_tensor = eye.float().clone() * bits_6_7_13
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-22)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-23)# Use a 1-element vector rather than a 0D scalar because PyTorch's type
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-24)# promotion rules ignore 0D scalar tensor dtypes when paired with 2D tensors.
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-25)one_float32 = torch.tensor([1.0], dtype=torch.float32, device=device)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-26)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-27)print(f"{bit_6_tensor[0,0]=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-28)print(f"{bit_7_tensor[0,0]=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-29)print(f"{bits_6_7_tensor[0,0]=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-30)print(f"{bits_6_7_13_tensor[0,0]=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-31)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-32)def mul_add(
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-33)    a: torch.Tensor, b: torch.Tensor, c: torch.Tensor
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-34)) -> torch.Tensor:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-35)  return a @ b * c
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-36)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-37)# In eager execution, `a @ b` rounds to bfloat16 before `* c`, dropping bit 13.
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-38)print("=== TPU values: Eager ===")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-39)eager_res = mul_add(bit_6_tensor, bit_7_tensor, one_float32)[0, 0]
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-40)print(f"{eager_res=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-41)assert eager_res == bits_6_7_tensor[0, 0]
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-42)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-43)# With allow_excess_precision = False, the compiled graph also rounds `a @ b`
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-44)# to bfloat16 before multiplying by `c`, dropping bit 13.
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-45)print("=== TPU values: compiled with allow_excess_precision = False ===")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-46)torch.compiler.reset()
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-47)torch.tpu.allow_excess_precision = False
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-48)mul_add_compiled_false = torch.compile(mul_add, backend="tpu")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-49)print(f"{torch.tpu.allow_excess_precision=}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-50)res_false = mul_add_compiled_false(bit_6_tensor, bit_7_tensor, one_float32)[
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-51)    0, 0
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-52)]
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-53)print(f"{res_false=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-54)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-55)try:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-56)  assert res_false == bits_6_7_tensor[0, 0]
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-57)  print("  [PASSED] Successfully disabled excess precision.")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-58)except AssertionError:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-59)  print(
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-60)      "  [WARNING] Failed to disable excess precision (XLA compiled another"
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-61)      " graph with default 'True' earlier in this session)."
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-62)  )
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-63)
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-64)# Changing allow_excess_precision after XLA compilation has already started in
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-65)# this process raises a RuntimeError because compiler options are locked on
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-66)# the first compilation.
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-67)#
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-68)# When `torch.tpu.allow_excess_precision = True` is set at the start of a
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-69)# fresh Python session before any TPU operations or compilations run, XLA
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-70)# keeps `a @ b` in float32 when fusing with `* c`, preserving the 13th
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-71)# mantissa bit (res_true == bits_6_7_13_tensor[0, 0] == 1.0235595703125).
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-72)print("=== TPU values: compiled with allow_excess_precision = True ===")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-73)torch.compiler.reset()
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-74)try:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-75)  torch.tpu.allow_excess_precision = True
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-76)  mul_add_compiled_true = torch.compile(mul_add, backend="tpu")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-77)  print(f"{torch.tpu.allow_excess_precision=}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-78)  res_true = mul_add_compiled_true(bit_6_tensor, bit_7_tensor, one_float32)[
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-79)      0, 0
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-80)  ]
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-81)  print(f"{res_true=:.20f}")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-82)  assert res_true == bits_6_7_13_tensor[0, 0]
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-83)  print("  [PASSED] Successfully enabled excess precision.")
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-84)except (RuntimeError, AssertionError) as e:
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-85)  print(
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-86)      "  [EXPECTED] Cannot change excess precision after first compilation:"
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-87)      f" {e}"
[](https://torchtpu.readthedocs.io/en/latest/numerical_precision/#__codelineno-7-88)  )

```

Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)