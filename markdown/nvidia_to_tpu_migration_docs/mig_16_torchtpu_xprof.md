---
id: "mig_16_torchtpu_xprof"
title: "TorchTPU performance profiling with XProf"
url: "https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/"
category: "Nvidia to tpu migration docs"
description: "Capture and inspect TPU execution traces; check documented PyTorch and profiler prerequisites."
crawled_at: "2026-10-26T12:48:16.448398+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#performance-profiling-with-xprof)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
Performance profiling with XProf 
[ ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/?q= "Share")
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
    * [ Manage numerical precision in TorchTPU  ](https://torchtpu.readthedocs.io/en/latest/numerical_precision/)
    * Performance profiling with XProf  [ Performance profiling with XProf  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/) Table of contents 
      * [ 1. The TPU profiler  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#1-the-tpu-profiler)
      * [ 2. Custom profiling configuration (TpuProfilerConfig)  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#2-custom-profiling-configuration-tpuprofilerconfig)
        * [ Sanctioned configuration options  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#sanctioned-configuration-options)
      * [ 3. Capturing a profile  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#3-capturing-a-profile)
      * [ 4. Viewing traces in TensorBoard  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#4-viewing-traces-in-tensorboard)
      * [ 5. What to look for  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#5-what-to-look-for)
        * [ Red flags in traces  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#red-flags-in-traces)
        * [ The ideal profile  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#the-ideal-profile)
      * [ 6. Verifying the traces were captured  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#6-verifying-the-traces-were-captured)
      * [ 7. Kernel profiling (Fine-grained performance counters)  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#7-kernel-profiling-fine-grained-performance-counters)
        * [ Enabling performance counters  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#enabling-performance-counters)
      * [ 8. Quick reference  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#8-quick-reference)


Table of contents 
  * [ 1. The TPU profiler  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#1-the-tpu-profiler)
  * [ 2. Custom profiling configuration (TpuProfilerConfig)  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#2-custom-profiling-configuration-tpuprofilerconfig)
    * [ Sanctioned configuration options  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#sanctioned-configuration-options)
  * [ 3. Capturing a profile  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#3-capturing-a-profile)
  * [ 4. Viewing traces in TensorBoard  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#4-viewing-traces-in-tensorboard)
  * [ 5. What to look for  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#5-what-to-look-for)
    * [ Red flags in traces  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#red-flags-in-traces)
    * [ The ideal profile  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#the-ideal-profile)
  * [ 6. Verifying the traces were captured  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#6-verifying-the-traces-were-captured)
  * [ 7. Kernel profiling (Fine-grained performance counters)  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#7-kernel-profiling-fine-grained-performance-counters)
    * [ Enabling performance counters  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#enabling-performance-counters)
  * [ 8. Quick reference  ](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#8-quick-reference)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/performance_profiling_with_xprof.md "Edit this page")
# Performance profiling with XProf[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#performance-profiling-with-xprof "Permanent link")
Understanding where time is spent is critical for training large models on TPU. This guide covers how to capture execution traces with the TPU Profiler and analyze them in TensorBoard.
Warning
**Prerequisite:** TensorBoard requires `setuptools<81`. The latest version removes `pkg_resources`, which TensorBoard depends on. Install it first:

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-0-1)pip install "setuptools<81"
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-0-2)pip install xprof tensorboard

```

Note
**PyTorch version:** the native `torch.profiler` TPU integration requires PyTorch 2.12 or newer.
## 1. The TPU profiler[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#1-the-tpu-profiler "Permanent link")
Standard `torch.profiler` (integrated with `torch_tpu`) provides a **context manager** interface for tracing both CPU and TPU activities. You wrap the code you want to profile in a `torch.profiler.profile()` block, and the collected traces are saved to disk for viewing in TensorBoard.
**Key components:**  
| Component  | Role  |  
| --- | --- |  
| `torch.profiler.profile()`  | Standard context manager that starts/stops   
trace collection  |  
| `torch.profiler.ProfilerActivity.CPU`  | Traces CPU-side operations (dispatch, data   
loading)  |  
| `torch.profiler.ProfilerActivity.TPU`  | Traces TPU hardware execution (compute,   
memory, interconnect)  |  
| `torch.profiler.tensorboard_trace_handler`  | Callback that saves traces to a directory for   
TensorBoard  |  
| `TpuProfilerConfig`  | Helper for custom TPU profiling configuration  |  

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-1-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-1-2)from torch.tpu.profiler import TpuProfilerConfig
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-1-3)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-1-4)device = torch.device("tpu")

```

## 2. Custom profiling configuration (`TpuProfilerConfig`)[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#2-custom-profiling-configuration-tpuprofilerconfig "Permanent link")
Options passed via `TpuProfilerConfig` allow fine-grained control over host and device tracer levels as well as output directory structures.
### Sanctioned configuration options[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#sanctioned-configuration-options "Permanent link")  
| Option Key  | Type  | Default  | Description  |  
| --- | --- | --- | --- |  
| `host_tracer_level`  | `int`  | `2`  | Controls CPU host tracer verbosity   
(0=off, 1=critical, 2=all).  |  
| `device_tracer_level`  | `int`  | `1`  | Controls TPU hardware device tracer   
verbosity (0=off, 1=on).  |  
| `python_tracer_level`  | `int`  | `0`  | Controls Python function tracing   
level (0=off, 1=on).  |  
| `run_dir`  | `pathlib.Path`  | `None`  | Output directory where TPU hardware trace   
files (`.xplane.pb`) are saved.  |  

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-1)import pathlib
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-2)import torch
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-3)from torch.tpu.profiler import TpuProfilerConfig
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-4)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-5)config = TpuProfilerConfig(
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-6)    host_tracer_level=2,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-7)    device_tracer_level=1,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-8)    python_tracer_level=0,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-9)    run_dir=pathlib.Path("./profiler_output"),
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-10))
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-11)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-12)with torch.profiler.profile(
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-13)    activities=[
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-14)        torch.profiler.ProfilerActivity.CPU,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-15)        torch.profiler.ProfilerActivity.TPU,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-16)    ],
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-17)    experimental_config=config,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-18)    on_trace_ready=torch.profiler.tensorboard_trace_handler("./profiler_output"),
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-19)) as prof:
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-2-20)    model(inputs)

```

## 3. Capturing a profile[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#3-capturing-a-profile "Permanent link")
The cell below runs a small training loop inside the profiler context. The key points:
  1. Wrap your training loop inside `torch.profiler.profile()`
  2. Specify activities — `CPU` for host-side ops, `TPU` for hardware execution
  3. Set `on_trace_ready` to save traces to a directory using `torch.profiler.tensorboard_trace_handler`
  4. (Optional) Pass `experimental_config` with `TpuProfilerConfig` to control tracer levels


Important
The profiler adds overhead. Profile only a representative subset of steps (e.g., 100–1000), not your entire training run.

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-1)# Build a small model and optimizer
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-2)model = (
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-3)    torch.nn.Sequential(
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-4)        torch.nn.Linear(128, 64), torch.nn.ReLU(), torch.nn.Linear(64, 10)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-5)    )
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-6)    .to(device)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-7)    .to(torch.bfloat16)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-8))
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-9)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-10)optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-11)data = torch.randn(32, 128, device=device, dtype=torch.bfloat16)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-12)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-13)# Where to save the profiler traces
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-14)log_dir = "/tmp/profiler_output"
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-15)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-16)# Configure TPU-specific tracer levels
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-17)config = TpuProfilerConfig(
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-18)    host_tracer_level=2,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-19)    device_tracer_level=1,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-20))
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-21)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-22)# Profile 100 training steps with native PyTorch profiler
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-23)with torch.profiler.profile(
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-24)    activities=[
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-25)        torch.profiler.ProfilerActivity.CPU,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-26)        torch.profiler.ProfilerActivity.TPU,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-27)    ],
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-28)    experimental_config=config,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-29)    on_trace_ready=torch.profiler.tensorboard_trace_handler(log_dir),
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-30)) as prof:
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-31)  for step in range(100):
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-32)    optimizer.zero_grad()
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-33)    loss = model(data).sum()
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-34)    loss.backward()
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-35)    optimizer.step()
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-36)    torch.accelerator.synchronize()
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-37)    prof.step()
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-38)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-3-39)print(f"✅ Profile captured: {100} steps saved to {log_dir}")

```

## 4. Viewing traces in TensorBoard[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#4-viewing-traces-in-tensorboard "Permanent link")
Run the following commands:
**Step 1:** Install the profiler plugin (required for the dashboard to appear):

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-4-1)pip install tensorboard-plugin-profile "setuptools<81"

```

**Step 2:** Launch TensorBoard:

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-5-1)tensorboard --logdir=/tmp/profiler_output --port=6006

```

XProf can also be run as a standalone server.

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-6-1)xprof --logdir=/tmp/profiler_output --port=6006

```

**Step 3:** Open `http://localhost:6006` in your browser and select the **"Profile"** tab.
Note
You must run TensorBoard from the VS Code integrated terminal so that port forwarding works automatically.
**On GKE:** write the trace directory to a Cloud Storage bucket mounted with the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) so the traces outlive the pod, then open them with `xprof --logdir=gs://<bucket>/profiler_output`.  
| View  | What it shows  |  
| --- | --- |  
| **Overview**  | High-level summary: step time, device utilization, top ops  |  
| **Trace Viewer**  | Timeline of every op on CPU and TPU — look for gaps (idle hardware)  |  
| **Op Profile**  | Breakdown of time per operation — find the most expensive ops  |  
| **Memory Profile**  | HBM usage over time — detect memory spikes  |  
## 5. What to look for[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#5-what-to-look-for "Permanent link")
### Red flags in traces[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#red-flags-in-traces "Permanent link")  
| Pattern  | Meaning  | Fix  |  
| --- | --- | --- |  
| Large gaps between TPU ops  | Host-side bottleneck   
(data loading, Python overhead)  | Prefetch data, reduce Python logic in the loop  |  
| Frequent short TPU bursts  | Too many graph breaks → frequent recompilation  | Reduce `.item()` / `.cpu()` calls, use `torch.compile`  |  
| Low MXU utilization  | Tensor dimensions not aligned to tile size (128)  | Pad dimensions to multiples of 128  |  
### The ideal profile[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#the-ideal-profile "Permanent link")
A well-optimized TPU workload shows:
  * **Long, continuous TPU compute blocks** — the compiler fused many ops into one execution
  * **Minimal CPU→TPU gaps** — data loading is overlapped with compute
  * **High MXU utilization ( >60%)** — tensor shapes are hardware-aligned


## 6. Verifying the traces were captured[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#6-verifying-the-traces-were-captured "Permanent link")
The cell below checks that the profiler output directory contains trace files.

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-1)import os
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-2)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-3)trace_files = os.listdir(log_dir)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-4)print(f"Trace directory: {log_dir}")
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-5)print(f"Files found: {len(trace_files)}")
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-6)for f in sorted(trace_files)[:10]:
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-7)  size_kb = os.path.getsize(os.path.join(log_dir, f)) / 1024
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-8)  print(f"  {f} ({size_kb:.1f} KB)")
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-9)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-10)if trace_files:
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-11)  print(f"\n✅ Traces ready. View with:")
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-12)  print(f"   tensorboard --logdir={log_dir}")
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-13)else:
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-7-14)  print("\n❌ No trace files found. Check profiler configuration.")

```

## 7. Kernel profiling (Fine-grained performance counters)[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#7-kernel-profiling-fine-grained-performance-counters "Permanent link")
Kernel profiling enables the collection of fine-grained hardware performance counters (e.g., for Pallas kernels) to diagnose performance bottlenecks that are otherwise invisible in standard event traces.
Note
Fine-grained performance counter sampling is an advanced hardware feature available for **Ironwood (TPU v7/TPU7x)** and subsequent TPU generations.
### Enabling performance counters[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#enabling-performance-counters "Permanent link")
You can enable performance counters by passing the counter configuration via `experimental_options` in `TpuProfilerConfig`:

```
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-1)from torch.tpu.profiler import TpuProfilerConfig
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-2)
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-3)config = TpuProfilerConfig(
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-4)    experimental_options={
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-5)        "tpu_enable_periodic_counter_sampling": True,
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-6)        "tpu_tc_perf_counter_sampling_options": (
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-7)            "interval_us:1 scaling:0 counter_size_bits:1 indices:10"
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-8)            " indices:11 indices:56 indices:57 indices:58"
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-9)        ),
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-10)    }
[](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#__codelineno-8-11))

```

For the detailed list of configuration parameters (such as sampling intervals, scaling, and trigger modes) and instructions on how to determine counter indices, refer to the official [OpenXLA Kernel Profiling Guide](https://openxla.org/xprof/kernel-profiling).
## 8. Quick reference[¶](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/#8-quick-reference "Permanent link")  
| Step  | Command / Code  |  
| --- | --- |  
| **Import**  | `from torch.tpu.profiler import TpuProfilerConfig`  |  
| **Profile**  | `with torch.profiler.profile(activities=[...], on_trace_ready=...):`  |  
| **Save**  | `torch.profiler.tensorboard_trace_handler("/tmp/profiler_output")`  |  
| **View**  | `tensorboard --logdir=/tmp/profiler_output`  |  
Note
Profile only 100–1000 steps to keep trace files manageable. The profiler adds ~5–10% overhead per step.
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)