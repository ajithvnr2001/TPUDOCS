---
id: "mig_10_torchtpu_distributed_support"
title: "TorchTPU distributed support"
url: "https://torchtpu.readthedocs.io/en/latest/distributed_support/"
category: "Nvidia to tpu migration docs"
description: "Use torch.distributed with tpu_dist, DDP, FSDP, and DTensor across TPU devices."
crawled_at: "2026-10-26T12:48:08.749722+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#torchtpu-distributed-support)
[ ![logo](https://torchtpu.readthedocs.io/en/latest/images/logo.png) ](https://torchtpu.readthedocs.io/en/latest/ "TorchTPU Documentation")
TorchTPU Documentation 
TorchTPU distributed support 
[ ](https://torchtpu.readthedocs.io/en/latest/distributed_support/?q= "Share")
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
    * TorchTPU distributed support  [ TorchTPU distributed support  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/) Table of contents 
      * [ Distributed support  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-support)
        * [ Key architectural differences from GPU  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#key-architectural-differences-from-gpu)
        * [ Collective execution and fusion modes  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#collective-execution-and-fusion-modes)
          * [ Using @torch.tpu.distributed.spmd_safe  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#using-torchtpudistributedspmd_safe)
          * [ Configuring the compilation handshake  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#configuring-the-compilation-handshake)
      * [ Distributed initialization  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-initialization)
        * [ 1. Worker script (train.py)  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#1-worker-script-trainpy)
        * [ 2. Launching with torchrun  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#2-launching-with-torchrun)
      * [ Optimal device mesh mapping  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#optimal-device-mesh-mapping)
        * [ Example: Constructing a topology-aware 2D DeviceMesh  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#example-constructing-a-topology-aware-2d-devicemesh)
      * [ Distributed Pallas Kernels  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-pallas-kernels)
        * [ Writing and Registering a Communicating Pallas Kernel  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#writing-and-registering-a-communicating-pallas-kernel)
        * [ Rank-aligned meshes and device assignment  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#rank-aligned-meshes-and-device-assignment)
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
  * [ Distributed support  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-support)
    * [ Key architectural differences from GPU  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#key-architectural-differences-from-gpu)
    * [ Collective execution and fusion modes  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#collective-execution-and-fusion-modes)
      * [ Using @torch.tpu.distributed.spmd_safe  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#using-torchtpudistributedspmd_safe "Using @torch.tpu.distributed.spmd_safe")
      * [ Configuring the compilation handshake  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#configuring-the-compilation-handshake)
  * [ Distributed initialization  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-initialization)
    * [ 1. Worker script (train.py)  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#1-worker-script-trainpy)
    * [ 2. Launching with torchrun  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#2-launching-with-torchrun)
  * [ Optimal device mesh mapping  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#optimal-device-mesh-mapping)
    * [ Example: Constructing a topology-aware 2D DeviceMesh  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#example-constructing-a-topology-aware-2d-devicemesh)
  * [ Distributed Pallas Kernels  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-pallas-kernels)
    * [ Writing and Registering a Communicating Pallas Kernel  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#writing-and-registering-a-communicating-pallas-kernel)
    * [ Rank-aligned meshes and device assignment  ](https://torchtpu.readthedocs.io/en/latest/distributed_support/#rank-aligned-meshes-and-device-assignment)


[ ](https://github.com/google-pytorch/torch_tpu/edit/master/docs/distributed_support.md "Edit this page")
# TorchTPU distributed support[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#torchtpu-distributed-support "Permanent link")
## Distributed support[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-support "Permanent link")
TorchTPU implements distributed communication at the PyTorch ProcessGroup level (`c10d::Backend`) under the `tpu_dist` backend name. By intercepting collectives at the ProcessGroup layer, TorchTPU supports standard `torch.distributed` APIs in both eager mode and `torch.compile`, and works directly with PyTorch distributed frameworks including DTensor, DistributedDataParallel (DDP), FSDPv2, and [SimpleFSDP](https://arxiv.org/abs/2411.00284).
Like PyTorch on GPU, TorchTPU enforces a one-process-per-device execution model. Under the hood, TPU-to-TPU communication does not use a separate runtime communication library (such as NCCL); instead, collective operations are lowered directly into [StableHLO collective operations](https://openxla.org/stablehlo/spec#collective_ops) (such as `stablehlo.all_reduce`, `stablehlo.all_gather`, `stablehlo.reduce_scatter`, and `stablehlo.all_to_all`) and compiled by XLA into the TPU executable.
### Key architectural differences from GPU[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#key-architectural-differences-from-gpu "Permanent link")
While TorchTPU preserves standard `torch.distributed` semantics, programming TPUs via StableHLO and PjRT introduces three key differences compared to GPU backends:
  * **Pre-initialization hardware topology discovery:** On a multi-GPU host, each process launched by torchrun can inspect all attached GPUs, select its assigned device via `cuda:{local_rank}`, and move models to that device before calling `torch.distributed.init_process_group()`. On a TPU host, each worker process is bound to a single TPU device and cannot own the full set of devices on its own. Before initializing the PjRT runtime or calling `torch.distributed.init_process_group()`, the environment must specify the physical mesh geometry of the [TPU slice](https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#slices) (`TORCH_TPU_TOPOLOGY`), the local coordinator addresses used to construct the Inter-Chip Interconnect (ICI) mesh (`TORCH_TPU_SLICEBUILDER_ADDRESSES`), and the total number of participating TPU devices (`WORLD_SIZE`).
  * **Global Replica Group Resolution for Subgroups:** In PyTorch, a collective call such as [`torch.distributed.all_reduce`](https://docs.pytorch.org/docs/stable/distributed.html#torch.distributed.all_reduce) only receives the ProcessGroup (subgroup) in which the calling rank participates. In contrast, [`stablehlo.all_reduce`](https://openxla.org/stablehlo/spec#all_reduce) requires a complete description of all participating subgroups across the default process group (`replica_groups`), even those the current process does not belong to:

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-0-1)%0 = "stablehlo.all_reduce"(%arg0) <{
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-0-2)  replica_groups = dense<[[4, 0, 1, 3], [5, 2, 6, 7]]> : tensor<2x4xi64>
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-0-3)}> ({ ... })

```

TorchTPU's `tpu_dist` backend automatically exchanges subgroup membership across all ranks in the default process group during collective setup and constructs the global `replica_groups` and `device_assignment` required by XLA. * **SPMD Compilation vs. MPMD Execution:** The XLA compiler and TPU communication stack are designed for Single Program, Multiple Data (SPMD) execution, where every rank compiles and executes an identical StableHLO module containing matching collective operations. However, PyTorch programs can exhibit Multiple Program, Multiple Data (MPMD) behavior across ranks—for example, due to rank-conditional branches (`if dist.get_rank() == 0:`) or uneven tensor sharding when a dimension is not evenly divisible by the number of devices. If different ranks execute different StableHLO modules containing collectives, mismatched synchronization flag IDs or buffer offsets across ranks can cause runtime deadlocks or memory corruption.


### Collective execution and fusion modes[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#collective-execution-and-fusion-modes "Permanent link")
TorchTPU runs each collective as a skinny collective. To let XLA overlap compute and communication, you can opt in to either or both of two mechanisms that fuse collectives with the surrounding computation. The two are independent and can be combined: collectives inside an `@spmd_safe` function are always fused, and, when enabled, the Compilation Handshake decides for the remaining collectives in each `torch.compile` graph.  
| Mode  | Configuration  | Graph Behavior  | Best For  |  
| --- | --- | --- | --- |  
| Skinny collectives (default behavior)  | Always on for any collective that the opt-ins below don't fuse  | Compiles each collective op into its own standalone ("skinny") StableHLO module by inserting graph breaks around collectives.  | General MPMD safety out of the box, at the cost of preventing XLA from overlapping compute and communication.  |  
|  `@spmd_safe` decorator (opt-in)  | `@torch.tpu.distributed.spmd_safe`  | Disables graph breaks around collectives inside the decorated function, fusing compute and collectives into a single StableHLO module.  | Known-SPMD functions or training steps (e.g., SimpleFSDP or manual tensor parallelism) to maximize XLA compute-communication overlap.  |  
| Compilation Handshake (opt-in)  |  `TORCH_TPU_SPMD_HANDSHAKE_STAGE=COMPILE_STAGE` or `DISPATCH_STAGE` (default: OFF)  | In torch.compile graphs, checks that the compiled FX graphs match across all ranks; fuses collectives if they do and falls back to skinny collectives if they don't.  | Automatically enabling collective fusion in `torch.compile` while guarding against accidental MPMD divergence.  |  
#### Using `@torch.tpu.distributed.spmd_safe`[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#using-torchtpudistributedspmd_safe "Permanent link")
When you know a function or model step is strictly SPMD across all ranks (no rank-dependent control flow or uneven tensor shapes), decorate it with `@torch.tpu.distributed.spmd_safe`. Under `torch.compile` (and `DEFER_AND_FUSE` eager mode), this removes graph breaks around collectives so XLA can schedule asynchronous communication alongside matrix computation:

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-2)import torch.distributed as dist
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-3)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-4)@torch.compile
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-5)@torch.tpu.distributed.spmd_safe
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-6)def spmd_train_step(x: torch.Tensor, weight: torch.Tensor) -> torch.Tensor:
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-7)  out = x @ weight
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-8)  dist.all_reduce(out, op=dist.ReduceOp.AVG)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-1-9)  return torch.nn.functional.silu(out)

```

Only apply `@torch.tpu.distributed.spmd_safe` to code that executes the exact same sequence of tensor and collective operations on every rank; applying it to MPMD code can produce different StableHLO modules across ranks and cause TPU execution deadlocks.
#### Configuring the compilation handshake[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#configuring-the-compilation-handshake "Permanent link")
Instead of manually annotating functions with `@spmd_safe`, you can enable TorchTPU's Compilation Handshake via the `TORCH_TPU_SPMD_HANDSHAKE_STAGE` environment variable. When `torch.compile` traces a graph containing global collectives, TorchTPU runs a consensus check across all ranks to verify that their compiled FX graphs match before fusing collectives into the graph:
  * `OFF` (Default):** Disables the handshake; collectives use default Skinny Collectives unless marked `@torch.tpu.distributed.spmd_safe`.
  * `COMPILE_STAGE`: Verifies graph consensus across ranks prior to PjRT compilation. If all ranks produce identical graphs, graph breaks around collectives are elided. Recommended for standard `torch.compile` workloads where all ranks compile together.
  * `DISPATCH_STAGE`: Compiles collectives without graph breaks and verifies consensus across ranks at dispatch time, recompiling with split collectives if ranks diverge. This mode is necessary for workloads that can trigger rank-specific recompilations; it has higher overhead than `COMPILE_STAGE`.


Below is an example of rank-specific recompilation that is supported by `DISPATCH_STAGE`, whereas `COMPILE_STAGE` would time out because only `divergent_rank` recompiles on iteration 1:

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-1)iteration = 0
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-2)divergent_rank = ...
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-3)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-4)def divergence_after_iteration(x, y):
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-5)  z = torch.add(x, y)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-6)  if rank == divergent_rank and iteration == 1:
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-7)    z = torch.mul(z, 5.0)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-8)  dist.all_reduce(z)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-9)  return z
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-10)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-11)compiled_fn = torch.compile(divergence_after_iteration, backend=backend)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-12)res0 = compiled_fn(x, y)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-13)iteration += 1
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-14)# IMPORTANT: If Handshake is in COMPILE_STAGE a recompilation happens only on `divergent_rank`
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-15)# this would initiate a Handshake ONLY ON THAT RANK which would timeout which is why we provide
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-16)# a DISPATCH_STAGE mode.
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-2-17)res1 = compiled_fn(x, y)

```

## Distributed initialization[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-initialization "Permanent link")
Initializing a distributed workload in TorchTPU uses standard `torch.distributed` APIs, paired with TorchTPU's launch environment helper to populate the TPU topology and slice-builder environment variables:  
| Environment Variable  | Description  | Example  |  
| --- | --- | --- |  
| `TORCH_TPU_TOPOLOGY`  | Physical mesh geometry of the TPU slice.  |  `"2,2,1"`, `"2,2,1,2"`, `"4,4,4"`  |  
| `TORCH_TPU_SLICEBUILDER_ADDRESSES`  | Comma-separated `host:port` addresses (one per device) used to construct the ICI mesh.  | `"localhost:8471,localhost:8472,..."`  |  
You need to set these variables before starting the workers. In common setups (a single host, or a GKE TPU slice), TorchTPU can determine the correct values for you: run

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-3-1)eval $(python3 -m torch.tpu.distributed | sed 's/^/export /')

```

In your launch script before torchrun, or call `torch.tpu.distributed.set_tpu_launch_env()` in your parent Python launcher process before spawning workers. Both leave any variable you have already set unchanged, so you can override individual values.
Below is the initialization flow for a distributed TorchTPU workload, followed by a complete worker and launcher example:
[![Distributed Initialization Flow](https://torchtpu.readthedocs.io/en/latest/images/distributed.png)](https://torchtpu.readthedocs.io/en/latest/images/distributed.png)
### 1. Worker script (`train.py`)[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#1-worker-script-trainpy "Permanent link")
Inside each worker process, initialize the `tpu_dist` backend and acquire the local TPU device via `torch.device("tpu")`:

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-2)import torch.distributed as dist
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-3)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-4)def worker_main():
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-5)  # 1. Initialize the distributed process group using the tpu_dist backend`
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-6)  dist.init_process_group(backend="tpu_dist")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-7)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-8)  # 2. Query rank, world size, and acquire the local TPU device
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-9)  rank = dist.get_rank()
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-10)  world_size = dist.get_world_size()
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-11)  device = torch.device("tpu")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-12)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-13)  print(f"[Rank {rank}/{world_size}] Initialized on {device}")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-14)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-15)  # 3. Perform a distributed collective operation across TPU workers
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-16)  x = torch.ones(4, 4, device=device) * (rank + 1)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-17)  dist.all_reduce(x, op=dist.ReduceOp.SUM)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-18)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-19)  print(f"[Rank {rank}] Reduced sum: {x[0, 0].item()}")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-20)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-21)  # 4. Clean up process group resources
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-22)  dist.destroy_process_group()
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-23)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-24)if __name__ == "__main__":
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-4-25)  worker_main()

```

### 2. Launching with torchrun[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#2-launching-with-torchrun "Permanent link")
Use the `torch.tpu.distributed` CLI module to detect the TPU hardware topology and export the required launch variables before invoking `torchrun`:

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-5-1)# Detect and export TORCH_TPU_TOPOLOGY, TORCH_TPU_SLICEBUILDER_ADDRESSES,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-5-2)# WORLD_SIZE, NODE_RANK, and multi-host coordination variables:
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-5-3)eval $(python3 -m torch.tpu.distributed | sed 's/^/export /')
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-5-4)# Launch 1 worker process per TPU device on the host:
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-5-5)torchrun --nproc_per_node=$WORLD_SIZE train.py

```

Alternatively, if you launch workers from Python (for example, with `torch.distributed.launcher.elastic_launch`), call `torch.tpu.distributed.set_tpu_launch_env()` in the parent process prior to spawning workers. Note that the default process group encompasses all devices in the [TPU slice](https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#slices).
## Optimal device mesh mapping[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#optimal-device-mesh-mapping "Permanent link")
To maximize collective bandwidth and minimize latency, align your model's parallelism dimensions with the physical TPU interconnect hierarchy:
  * **Inter-Chip Interconnect (ICI)** : High-speed direct links connecting TPU chips in a 2D/3D torus or twisted-torus mesh within a slice (tens to hundreds of GB/s per link).
  * **Data Center Network (DCN)** : Host-level Ethernet connecting separate TPU slices in multi-slice workloads (lower bandwidth and higher latency than ICI).


Use `torch.tpu.distributed.topology_aware_mesh()` to compute a rank layout aligned with physical ICI rings. Order your logical mesh dimensions from **lowest communication intensity** (outermost) to **highest communication intensity** (innermost):  
| Parallelism Type  | Typical Collectives  | Communication Frequency  | Recommended Physical Placement  |  
| --- | --- | --- | --- |  
| **Tensor Parallel (TP)**  |  `all_reduce`, `reduce_scatter`, `all_gather`  | Every transformer layer (Forward + Backward)  | Fastest local ICI ring (same tray/host, contiguous 1-hop devices)  |  
| **Context / Sequence Parallel (CP/SP)**  |  `all_to_all`, Ring Attention  | Per attention layer  | Local ICI axes (within slice)  |  
| **Expert Parallel (EP)**  |  `all_to_all`, `ragged_all_to_all`  | Per MoE router layer  | Local ICI axes (within slice)  |  
| **Fully Sharded Data Parallel (FSDP)**  |  `all_gather`, `reduce_scatter`  | Per module / transformer block  | ICI axes (within slice)  |  
| **Replicated Data Parallel (DP)**  |  `all_reduce` (gradients only)  | Once per training step  | Outer ICI axis or DCN (across slices)  |  
### Example: Constructing a topology-aware 2D DeviceMesh[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#example-constructing-a-topology-aware-2d-devicemesh "Permanent link")

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-1)import torch
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-2)from torch.distributed.device_mesh import DeviceMesh
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-3)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-4)# Logical mesh shape: (dp=4, tp=2) on an 8-device slice,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-5)# ordered from least communication-intensive (dp) to most intensive (tp):
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-6)mesh_shape = (4, 2)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-7)dim_names = ("dp", "tp")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-8)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-9)# Compute an optimal rank tensor aligned with physical ICI rings
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-10)optimal_rank_tensor = torch.tpu.distributed.topology_aware_mesh(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-11)    mesh_shape=mesh_shape,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-12))
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-13)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-14)# Instantiate the PyTorch DeviceMesh
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-15)mesh_2d = DeviceMesh(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-16)    "tpu",
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-17)    mesh=optimal_rank_tensor,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-18)    mesh_dim_names=dim_names,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-19)    preserve_rank_order=True,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-20))
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-21)dp_mesh = mesh_2d["dp"]
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-6-22)tp_mesh = mesh_2d["tp"]

```

For multi-slice (hybrid DCN + ICI) workloads, passing `dcn_mesh_shape` alongside `mesh_shape` is optional and only needed to choose the split explicitly: by default, `torch.tpu.distributed.topology_aware_mesh()` detects the slices automatically and maps the outermost non-trivial mesh dimension (typically data parallel) across slices over DCN and the inner dimensions within each slice over ICI.
## Distributed Pallas Kernels[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#distributed-pallas-kernels "Permanent link")
TorchTPU supports custom [Pallas](https://docs.jax.dev/en/latest/pallas/index.html) kernels that perform direct inter-device Remote DMA (RDMA) over ICI without host CPU involvement. This enables you to author custom point-to-point or ring communication kernels—such as Ring Attention, custom All-to-All shuffles, pipeline-parallel shifts, or halo exchanges—and invoke them as native PyTorch custom ops in both eager mode and `torch.compile`.
### Writing and Registering a Communicating Pallas Kernel[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#writing-and-registering-a-communicating-pallas-kernel "Permanent link")
Integrating a distributed Pallas kernel involves three steps:  
| Stage  | Key Steps & Operations  |  
| --- | --- |  
| **1. Pallas Kernel Body**  | Query logical coordinates with `jax.lax.axis_index` and `jax.lax.axis_size`, construct an asynchronous transfer descriptor via `pltpu.make_async_remote_copy(..., device_id=(target,))`, and manage completion with `.start()` and `.wait()`.  |  
| **2.`pl.pallas_call` & `jax.shard_map`**  | Allocate DMA semaphores (`pltpu.SemaphoreType.DMA`) in `scratch_shapes` and wrap the kernel with `jax.shard_map` over a rank-aligned, world-sized `jax.sharding.Mesh` and `PartitionSpec`.  |  
| **3. TorchTPU Registration**  | Register a type-annotated JAX wrapper function using `torch.tpu.pallas.jax_op`, passing `mesh`, `input_partition_specs`, and `output_partition_specs`.  |  

```
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-1)import jax
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-2)from jax.experimental import pallas as pl
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-3)from jax.experimental.pallas import tpu as pltpu
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-4)import torch
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-5)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-6)P = jax.sharding.PartitionSpec
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-7)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-8)# 1. Pallas Kernel Body: Asynchronously sends local buffer to neighbor rank (rank + 1)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-9)def pallas_send_to_next_kernel(x_ref, y_ref, send_sem, recv_sem):
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-10)  rank = jax.lax.axis_index("x")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-11)  world_size = jax.lax.axis_size("x")
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-12)  dest_id = (rank + 1) % world_size
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-13)  # Trigger hardware Remote DMA over TPU interconnect
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-14)  async_copy = pltpu.make_async_remote_copy(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-15)      src_ref=x_ref,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-16)      dst_ref=y_ref,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-17)      send_sem=send_sem,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-18)      recv_sem=recv_sem,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-19)      device_id=(dest_id,),
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-20)  )
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-21)  async_copy.start()
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-22)  async_copy.wait()
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-23)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-24)# 2. JAX Wrapper with ShardMap and DMA Semaphores
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-25)def build_jax_fn(mesh):
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-26)  def local_pallas_call(x: jax.Array) -> jax.Array:
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-27)    return pl.pallas_call(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-28)        pallas_send_to_next_kernel,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-29)        out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-30)        grid_spec=pltpu.PrefetchScalarGridSpec(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-31)            num_scalar_prefetch=0,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-32)            in_specs=[pl.BlockSpec(x.shape)],
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-33)            out_specs=pl.BlockSpec(x.shape),
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-34)            scratch_shapes=(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-35)                pltpu.SemaphoreType.DMA,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-36)                pltpu.SemaphoreType.DMA,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-37)            ),  # send & recv semaphores
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-38)        ),
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-39)    )(x)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-40)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-41)  return jax.shard_map(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-42)      local_pallas_call,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-43)      mesh=mesh,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-44)      in_specs=P("x"),
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-45)      out_specs=P("x"),
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-46)      check_vma=False,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-47)  )
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-48)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-49)# 3. Create the TorchTPU callable wrapper
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-50)def get_send_to_next_op(world_size: int):
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-51)  mesh = torch.tpu.pallas.get_pallas_mesh(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-52)      axis_names=("x",), mesh_shape=(world_size,)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-53)  )
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-54)  jax_fn = build_jax_fn(mesh)
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-55)  return torch.tpu.pallas.jax_op(
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-56)      "pallas::send_to_next",
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-57)      jax_fn,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-58)      mesh=mesh,
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-59)      input_partition_specs=[P("x")],
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-60)      output_partition_specs=[P("x")],
[](https://torchtpu.readthedocs.io/en/latest/distributed_support/#__codelineno-7-61)  )

```

### Rank-aligned meshes and device assignment[¶](https://torchtpu.readthedocs.io/en/latest/distributed_support/#rank-aligned-meshes-and-device-assignment "Permanent link")
Device IDs and ranks assigned are not 1 to 1 in many TPU architectures: ranks are assigned such that the neighbors are the adjacent devices (rank 1 is next to rank 0 and rank 2) but the device IDs are 0, 1, and 4 for v7x in this scenario. To smooth the translation, torchTPU provides `torch.tpu.pallas.get_pallas_mesh`, which provides a Pallas/JAX mesh which matches exactly the rank ID that is used throughout the rest of the Torch application.
  * **Rank-aligned mesh construction** : `torch.tpu.pallas.get_pallas_mesh(axis_names=..., mesh_shape=...,     process_group=...)` queries the active PyTorch `ProcessGroup`'s rank-to-device mapping and constructs a `jax.sharding.Mesh` of abstract compile-only devices without initializing a JAX PjRT backend.
  * **World-sized mesh requirement** : Distributed Pallas kernels require a mesh whose total device count equals `dist.get_world_size()`. For multi-dimensional parallel topologies (such as data + tensor parallelism), pass a `mesh_shape` whose product equals `world_size` - for example, `torch.tpu.pallas.get_pallas_mesh(axis_names=("dp", "tp"), mesh_shape=(2,     4))`.
  * **Unified collective and kernel device assignment** : When `mesh` is provided to `torch.tpu.pallas.jax_op`, TorchTPU extracts the mesh's rank-to-device mapping as the XLA `DeviceAssignment` for the kernel and reconciles it with any standard `torch.distributed` collectives fused into the same compiled module. This guarantees that `jax.lax.axis_index`, mesh-addressed DMAs (`device_id={axis: target}`), and PyTorch collectives all route consistently according to PyTorch rank order.


Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)