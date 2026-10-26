# Complete Reference Compendium: `nvidia_to_tpu_migration_docs` (18 Resources)

## `mig_01_pytorch_on_tpu_overview` — PyTorch on Cloud TPU
- **URL**: https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu
- **Description**: Official overview of the current PyTorch TPU stack, including TorchTPU, model serving, training, and migration from PyTorch/XLA.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_01_pytorch_on_tpu_overview/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_01_pytorch_on_tpu_overview.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_01_pytorch_on_tpu_overview.md`

### Sections (31) & Code Examples (2)
- PyTorch on Cloud TPU
- Get started
- TorchTPU: PyTorch-native backend for Cloud TPU
- Motivation
- Design
- Key strengths
- Production inference and serving
- vLLM-TorchTPU and SGLang-TorchTPU: Inference engines
- Motivation
- Design
- Key strengths
- llm-d: Kubernetes-native distributed inference
- Motivation
- Design
- Key strengths

## `mig_02_torchtpu_docs_hub` — TorchTPU documentation hub
- **URL**: https://torchtpu.readthedocs.io/
- **Description**: Index of native PyTorch TPU quickstarts, migration APIs, examples, and performance documentation.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_02_torchtpu_docs_hub/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_02_torchtpu_docs_hub.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_02_torchtpu_docs_hub.md`

### Sections (3) & Code Examples (0)
- Home
- About
- What are you trying to do today?

## `mig_03_torchtpu_vm_quickstart` — TorchTPU VM quickstart
- **URL**: https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/
- **Description**: Create a Python environment on a TPU VM, install TorchTPU, and run your first tensor operations.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_03_torchtpu_vm_quickstart/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_03_torchtpu_vm_quickstart.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_03_torchtpu_vm_quickstart.md`

### Sections (14) & Code Examples (5)
- Get started with TorchTPU on a TPU VM
- 1. Install and set up
- Step 1: Initialize Python 3.12
- Step 2: Install TorchTPU and dependencies
- 2. Initialize the hardware
- 3. Work with tensors
- 1. Create a tensor on the CPU
- 2. Move it to the TPU
- OR
- 3. Create a tensor directly on the TPU
- 4. Compute and materialize results
- Perform a simple operation on the TPU
- Bring the result back to the CPU to print or use in other libraries
- 🎉 Success!

## `mig_04_torchtpu_cuda_api_ref` — TorchTPU CUDA-to-TPU API reference
- **URL**: https://torchtpu.readthedocs.io/en/latest/api_reference/
- **Description**: Mappings from torch.cuda to device-agnostic APIs, plus TPU runtime, precision, distributed, and profiling APIs.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_04_torchtpu_cuda_api_ref/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_04_torchtpu_cuda_api_ref.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_04_torchtpu_cuda_api_ref.md`

### Sections (29) & Code Examples (9)
- TorchTPU API Reference
- **Core Device Queries**
- Initialize hardware
- **Random Number Generation (RNG)**
- Set the seed across all cores
- **Automatic Mixed Precision (AMP)**
- **Streams and Events**
- **TPU-Specific APIs**
- **Execution Modes and Compiler Options**
- **Numerical Precision**
- **Distributed Training and Topology**
- **TPU Custom Operators (`torch.tpu.ops`) and Pallas (`torch.tpu.pallas`)**
- **General, Attention, MoE, and Collective Operators**
- **SparseCore Embedding Operators**
- **Fused Training Step and Optimizers (`torch.tpu.optimizers`)**

## `mig_05_torchtpu_faq` — TorchTPU FAQ
- **URL**: https://torchtpu.readthedocs.io/en/latest/faq/
- **Description**: Migration questions, CUDA versus TPU execution, and the replacement of PyTorch/XLA.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_05_torchtpu_faq/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_05_torchtpu_faq.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_05_torchtpu_faq.md`

### Sections (11) & Code Examples (0)
- What is the difference between PyTorch/XLA and TorchTPU?
- What is the difference between TorchAX and TorchTPU?
- What is happening to PyTorch/XLA?
- Is TorchTPU replacing JAX?
- What is the best way for me to connect with TorchTPU developers?
- Will there be any community engagement forums?
- What support does TorchTPU provide for kernel development?
- Which TPU generations are actively supported? What's the plan for future hardware support?
- Where can we find TorchTPU's supported features & future roadmap?
- Is there an agent to make my onboarding easier?
- Can I use TorchTPU with our custom serving solution?

## `mig_06_torchtpu_feature_set` — TorchTPU supported features and roadmap
- **URL**: https://torchtpu.readthedocs.io/en/latest/feature_set/
- **Description**: Check validated versus experimental hardware, operators, models, kernels, and distributed features.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_06_torchtpu_feature_set/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_06_torchtpu_feature_set.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_06_torchtpu_feature_set.md`

### Sections (2) & Code Examples (0)
- Current supported feature set
- Future work

## `mig_07_torchtpu_repo` — TorchTPU repository (official installation)
- **URL**: https://github.com/google-pytorch/torch_tpu
- **Description**: Official source, supported Python versions, released packages, and installation instructions.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_07_torchtpu_repo/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_07_torchtpu_repo.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_07_torchtpu_repo.md`

### Sections (15) & Code Examples (13)
- TorchTPU (`google-pytorch/torch_tpu`)
- Description
- Features
- User Guide and Interactive Notebooks
- Installation
- Install via pip
- Build from source
- The extra-index-url provides the CPU version of torch rather than the default CUDA build.
- Getting Started
- Dependencies
- Bazel setup
- VSCode `clangd` Setup
- Contributing
- Star History
- License

## `mig_08_torchtpu_intro` — TorchTPU documentation: introduction and feature set
- **URL**: https://torchtpu.readthedocs.io/en/latest/intro_to_torchtpu/
- **Description**: Native PyTorch TPU concepts, migration changes, execution modes, and compilation.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_08_torchtpu_intro/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_08_torchtpu_intro.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_08_torchtpu_intro.md`

### Sections (6) & Code Examples (1)
- Introduction to TorchTPU
- Why use TorchTPU?
- Quickstart: Running on TPU
- Key features
- Limitations and future work
- Getting started

## `mig_09_torchtpu_dynamic_shapes` — TorchTPU compilation and dynamic shapes
- **URL**: https://torchtpu.readthedocs.io/en/latest/dynamic_shapes/
- **Description**: Static and bounded dynamic shapes, recompilation behavior, and current limitations.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_09_torchtpu_dynamic_shapes/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_09_torchtpu_dynamic_shapes.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_09_torchtpu_dynamic_shapes.md`

### Sections (9) & Code Examples (5)
- Dynamic shapes
- How dynamic shapes are handled by TorchTPU
- Compilation
- Execution
- Motivating use case: Autoregressive decoding
- Example: Autoregressive loop with a growing tensor
- 1. Running with `dynamic=False`
- 2. Running with `dynamic=None` (Bounded Dynamism)
- Current limitations

## `mig_10_torchtpu_distributed_support` — TorchTPU distributed support
- **URL**: https://torchtpu.readthedocs.io/en/latest/distributed_support/
- **Description**: Use torch.distributed with tpu_dist, DDP, FSDP, and DTensor across TPU devices.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_10_torchtpu_distributed_support/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_10_torchtpu_distributed_support.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_10_torchtpu_distributed_support.md`

### Sections (26) & Code Examples (8)
- Distributed support
- Key architectural differences from GPU
- Collective execution and fusion modes
- Using `@torch.tpu.distributed.spmd_safe`
- Configuring the compilation handshake
- IMPORTANT: If Handshake is in COMPILE_STAGE a recompilation happens only on `divergent_rank`
- this would initiate a Handshake ONLY ON THAT RANK which would timeout which is why we provide
- a DISPATCH_STAGE mode.
- Distributed initialization
- 1. Worker script (`train.py`)
- 2. Launching with torchrun
- Detect and export TORCH_TPU_TOPOLOGY, TORCH_TPU_SLICEBUILDER_ADDRESSES,
- WORLD_SIZE, NODE_RANK, and multi-host coordination variables:
- Launch 1 worker process per TPU device on the host:
- Optimal device mesh mapping

## `mig_11_torchtpu_custom_kernels` — TorchTPU custom kernels and API reference
- **URL**: https://torchtpu.readthedocs.io/en/latest/custom_kernels/
- **Description**: Integrate prebuilt Tokamax kernels, custom Pallas kernels, or experimental Helion kernels.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_11_torchtpu_custom_kernels/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_11_torchtpu_custom_kernels.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_11_torchtpu_custom_kernels.md`

### Sections (15) & Code Examples (2)
- TorchTPU custom kernels
- Choosing an integration approach
- 1. Using pre-built kernels from Tokamax
- When to use
- How it works
- 2. Writing Custom Pallas Kernels
- How to integrate a Pallas kernel
- 1. Define the Pallas kernel
- 2. Wrap the Pallas kernel into a JAX function
- 3. Wrap it for PyTorch using the functional interface
- 4. Call it like a standard PyTorch function
- 3. Writing portable kernels with Helion (experimental)
- How to write a Helion kernel
- 1. Define the kernel in Helion
- 2. Call it like a standard PyTorch function

## `mig_12_torchtpu_numerical_precision` — TorchTPU numerical precision
- **URL**: https://torchtpu.readthedocs.io/en/latest/numerical_precision/
- **Description**: Understand numerical differences from CUDA and configure TPU matrix-multiplication precision.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_12_torchtpu_numerical_precision/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_12_torchtpu_numerical_precision.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_12_torchtpu_numerical_precision.md`

### Sections (35) & Code Examples (8)
- Manage numerical precision in TorchTPU
- Compare PyTorch precision on CUDA and TPU
- Specify precision modes
- Compare accuracy across precision modes
- CPU float32 reference result
- Verify numerical parity
- 1. Set up identical models in bfloat16 for a fair comparison
- 2. Synchronize weights (mandatory for parity checks)
- 3. Create identical input data for both devices
- 4. Run the forward pass
- 5. Compare results
- Note: TorchTPU's bfloat16 accumulation and fusion differences can exceed
- default tolerances, generating the `assert_close` diagnostic report below.
- Interpret detailed mismatches
- Best practices for parity

## `mig_13_torchtpu_memory_model` — TorchTPU memory model
- **URL**: https://torchtpu.readthedocs.io/en/latest/torchtpu_memory_model/
- **Description**: Explains tensor views, layout transformations, and why CUDA-like view operations can have different TPU performance.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_13_torchtpu_memory_model/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_13_torchtpu_memory_model.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_13_torchtpu_memory_model.md`

### Sections (15) & Code Examples (1)
- TorchTPU and the TPU memory model
- Hardware: CPUs, GPUs, TPUs
- Programming model: CUDA vs XLA
- Buffers: `torch.UntypedStorage`
- `torch.Tensor`
- View decomposition
- Logical values: [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]
- sizes=(10,), strides=(1,), storage_offset=0
- Logical values: [[[1., 1.], [4., 4.]], [[3., 3.], [6., 6.]]]
- Logical values: [[[1., 1.], [4., 4.]], [[3., 3.], [6., 6.]]]
- StableHLO: slice, reshape, slice, transpose, reshape, broadcast_in_dim
- In-place mutations and buffer donation
- Copy-on-write
- Custom kernels
- Takeaways

## `mig_14_pallas_tpu_quickstart` — Pallas TPU kernel quickstart
- **URL**: https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html
- **Description**: Write custom TPU kernels using Pallas; relevant when replacing CUDA-specific kernels.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_14_pallas_tpu_quickstart/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_14_pallas_tpu_quickstart.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_14_pallas_tpu_quickstart.md`

### Sections (13) & Code Examples (4)
- Quickstart: TPU
- TPU memory spaces
- Your first kernel
- Distributing work across TensorCores
- Making it fast: pipelining
- Array([[5., 5., 5., ..., 5., 5., 5.],
- [5., 5., 5., ..., 5., 5., 5.],
- [5., 5., 5., ..., 5., 5., 5.],
- ...,
- [5., 5., 5., ..., 5., 5., 5.],
- [5., 5., 5., ..., 5., 5., 5.],
- [5., 5., 5., ..., 5., 5., 5.]], dtype=float32)
- What’s next

## `mig_15_tokamax_kernel_lib` — Tokamax TPU kernel library
- **URL**: https://github.com/openxla/tokamax
- **Description**: Prebuilt high-performance TPU kernels with PyTorch interoperability.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_15_tokamax_kernel_lib/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_15_tokamax_kernel_lib.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_15_tokamax_kernel_lib.md`

### Sections (6) & Code Examples (2)
- Tokamax
- Documentation
- Getting Started
- Installation
- Usage Examples
- Contributing

## `mig_16_torchtpu_xprof` — TorchTPU performance profiling with XProf
- **URL**: https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/
- **Description**: Capture and inspect TPU execution traces; check documented PyTorch and profiler prerequisites.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_16_torchtpu_xprof/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_16_torchtpu_xprof.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_16_torchtpu_xprof.md`

### Sections (17) & Code Examples (9)
- Performance profiling with XProf
- 1. The TPU profiler
- 2. Custom profiling configuration (`TpuProfilerConfig`)
- Sanctioned configuration options
- 3. Capturing a profile
- Build a small model and optimizer
- Where to save the profiler traces
- Configure TPU-specific tracer levels
- Profile 100 training steps with native PyTorch profiler
- 4. Viewing traces in TensorBoard
- 5. What to look for
- Red flags in traces
- The ideal profile
- 6. Verifying the traces were captured
- 7. Kernel profiling (Fine-grained performance counters)

## `mig_17_tpu_agent_suite` — TPU Agent Suite installation
- **URL**: https://github.com/google-pytorch/tpu-agent-suite/blob/main/docs/install.md
- **Description**: Experimental assisted onboarding and diagnostics; documents TPU environment and dependency setup.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_17_tpu_agent_suite/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_17_tpu_agent_suite.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_17_tpu_agent_suite.md`

### Sections (40) & Code Examples (28)
- Installing TPU agent suite
- 1. Host prerequisites
- 2. Install from release archive
- Download
- Install
- Upgrade
- Uninstall
- 3. Create a package
- The experimental package (`tpu-agent-suite-experimental`)
- 4. Environment configuration
- Headless installs (CI, containers)
- Changing your answers later
- 5. What gets installed
- 6. Set up the compute target
- Cloud TPU VM (`local` and `gce_tpu_vm`)

## `mig_18_torchtpu_engineering_overview` — TorchTPU engineering overview
- **URL**: https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/
- **Description**: Explains native PyTorch TPU execution and the engineering choices behind workload portability.
- **Dedicated Skill**: `skills/catalog/nvidia_to_tpu_migration_docs/mig_18_torchtpu_engineering_overview/SKILL.md`
- **OKF Entity**: `okf/entities/nvidia_to_tpu_migration_docs/mig_18_torchtpu_engineering_overview.okf.json`
- **Markdown Source**: `markdown/nvidia_to_tpu_migration_docs/mig_18_torchtpu_engineering_overview.md`

### Sections (8) & Code Examples (0)
- TorchTPU: Running PyTorch Natively on TPUs at Google Scale
- **Architecting for Usability, Portability, and Performance**
- **Engineering the TorchTPU Stack: The Technical Reality**
- **Eager First: Flexibility Without Compromise**
- **Static Compilation: Dynamo, XLA, and StableHLO**
- **Distributed Training and the MPMD Challenge**
- **TPU Hardware Awareness**
- **The Road Ahead: 2026 and Beyond**
