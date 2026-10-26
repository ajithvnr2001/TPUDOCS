---
id: "train_05_jax_installation"
title: "JAX installation"
url: "https://docs.jax.dev/en/latest/installation.html"
category: "Training framework links"
description: "Official accelerator-specific installation, including jax[tpu] for Cloud TPU VMs."
crawled_at: "2026-10-26T12:45:39.934757+00:00"
crawler_engine: "Crawl4AI"
---

[Skip to main content](https://docs.jax.dev/en/latest/installation.html#main-content)
Back to top `Ctrl`+`K`
[ ![JAX  documentation - Home](https://docs.jax.dev/en/latest/_static/jax_logo_250px.png) ![JAX  documentation - Home](https://docs.jax.dev/en/latest/_static/jax_logo_250px.png) ](https://docs.jax.dev/en/latest/index.html)
Search `Ctrl`+`K`
Getting started
  * [Installation](https://docs.jax.dev/en/latest/installation.html)


Documentation
  * [Newly documented](https://docs.jax.dev/en/latest/whats-new.html)
  * [JAX 101: expressing computations](https://docs.jax.dev/en/latest/101/index.html)
    * [Arrays and `jax.numpy`](https://docs.jax.dev/en/latest/101/arrays.html)
    * [Transformations: `grad` and `vmap`](https://docs.jax.dev/en/latest/101/transformations.html)
    * [Pytrees](https://docs.jax.dev/en/latest/101/pytrees.html)
    * [Pseudorandom numbers](https://docs.jax.dev/en/latest/101/random.html)
    * [Stateful computations](https://docs.jax.dev/en/latest/101/state.html)
    * [Errors](https://docs.jax.dev/en/latest/101/errors.html)
    * [Convolutions](https://docs.jax.dev/en/latest/101/convolutions.html)
    * [Default dtypes and the X64 flag](https://docs.jax.dev/en/latest/101/default_dtypes.html)
    * [Type promotion semantics](https://docs.jax.dev/en/latest/101/type_promotion.html)
    * [Rank promotion warning](https://docs.jax.dev/en/latest/101/rank_promotion_warning.html)
  * [JAX 201: performance and scaling](https://docs.jax.dev/en/latest/201/index.html)
    * [Just-in-time compilation](https://docs.jax.dev/en/latest/201/jit.html)
    * [Ahead-of-time lowering and compilation](https://docs.jax.dev/en/latest/201/aot.html)
    * [Control flow and logical operators with `jit`](https://docs.jax.dev/en/latest/201/control-flow.html)
    * [Data placement](https://docs.jax.dev/en/latest/201/placement.html)
    * [Distributed arrays and automatic parallelization](https://docs.jax.dev/en/latest/201/sharding.html)
    * [Manual parallelism with `shard_map`](https://docs.jax.dev/en/latest/201/shard-map.html)
    * [External callbacks](https://docs.jax.dev/en/latest/201/callbacks.html)
    * [Benchmarking and profiling](https://docs.jax.dev/en/latest/201/profiling.html)
    * [Debugging runtime values](https://docs.jax.dev/en/latest/201/debugging.html)
    * [Debugging slow JAX tracing and XLA compilation](https://docs.jax.dev/en/latest/201/slow-compilation.html)
    * [Matmul precision](https://docs.jax.dev/en/latest/201/precision.html)
    * [Controlling XLA from JAX](https://docs.jax.dev/en/latest/201/controlling-xla.html)
    * [GPU memory allocation](https://docs.jax.dev/en/latest/201/gpu-memory.html)
    * [Memory spaces and host offloading](https://docs.jax.dev/en/latest/201/memory-spaces.html)
  * [JAX 301: advanced autodiff and extending JAX](https://docs.jax.dev/en/latest/301/index.html)
    * [The autodiff cookbook: JVPs and VJPs](https://docs.jax.dev/en/latest/301/cookbook.html)
    * [First-class VJPs](https://docs.jax.dev/en/latest/301/vjp-objects.html)
    * [Autodiff and sharding](https://docs.jax.dev/en/latest/301/sharding-ad.html)
    * [Custom derivative rules with hijax primitives](https://docs.jax.dev/en/latest/301/custom-derivatives.html)
    * [Custom JVPs or VJPs with `custom_jvp` and `custom_vjp`](https://docs.jax.dev/en/latest/301/custom-jvp-vjp.html)
    * [Autodiff with refs](https://docs.jax.dev/en/latest/301/refs.html)
    * [Gradient checkpointing with `jax.checkpoint` (`jax.remat`)](https://docs.jax.dev/en/latest/301/remat.html)
    * [Defining new JAX types with hijax](https://docs.jax.dev/en/latest/301/hijax-types.html)
  * [JAX 401: kernels and FFI](https://docs.jax.dev/en/latest/401/index.html)
    * [Pallas: custom kernels in JAX](https://docs.jax.dev/en/latest/401/pallas.html)
    * [Writing high-performance GPU kernels with CuTe DSL and JAX](https://docs.jax.dev/en/latest/401/cute-dsl.html)
    * [Foreign function interface (FFI)](https://docs.jax.dev/en/latest/401/ffi.html)
  * [JAX 501: systems topics](https://docs.jax.dev/en/latest/501/index.html)
    * [Introduction to multi-controller JAX (aka multi-process/multi-host JAX)](https://docs.jax.dev/en/latest/501/multiprocess.html)
    * [Distributed data loading](https://docs.jax.dev/en/latest/501/data-loading.html)
    * [Fault-tolerant distributed JAX](https://docs.jax.dev/en/latest/501/fault-tolerance.html)
    * [Security considerations](https://docs.jax.dev/en/latest/501/security.html)
    * [Exporting and serializing staged-out computations](https://docs.jax.dev/en/latest/501/export.html)
    * [Shape polymorphism](https://docs.jax.dev/en/latest/501/shape-polymorphism.html)
    * [Persistent compilation cache](https://docs.jax.dev/en/latest/501/compilation-cache.html)
    * [Transfer guard](https://docs.jax.dev/en/latest/501/transfer-guard.html)
  * [JAX 601: internals](https://docs.jax.dev/en/latest/601/index.html)
    * [The jaxpr language](https://docs.jax.dev/en/latest/601/jaxpr.html)
    * [Primitives](https://docs.jax.dev/en/latest/601/jax-primitives.html)
    * [Autodidax: JAX core from scratch](https://docs.jax.dev/en/latest/autodidax.html)
    * [Autodidax2, part 1: JAX from scratch, again](https://docs.jax.dev/en/latest/autodidax2_part1.html)
  * [🔪 JAX - The Sharp Bits 🔪](https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html)
  * [Pallas: a JAX kernel language](https://docs.jax.dev/en/latest/pallas/index.html)
    * [Pallas TPU](https://docs.jax.dev/en/latest/pallas/tpu/index.html)
      * [Quickstart: TPU](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html)
      * [Writing TPU kernels with Pallas](https://docs.jax.dev/en/latest/pallas/tpu/details.html)
      * [TPU Pipelining](https://docs.jax.dev/en/latest/pallas/tpu/pipelining.html)
      * [Matrix Multiplication](https://docs.jax.dev/en/latest/pallas/tpu/matmul.html)
      * [Scalar Prefetch and Block-Sparse Computation](https://docs.jax.dev/en/latest/pallas/tpu/sparse.html)
      * [Distributed Computing in Pallas for TPUs](https://docs.jax.dev/en/latest/pallas/tpu/distributed.html)
      * [Pallas Core-specific Programming](https://docs.jax.dev/en/latest/pallas/tpu/core_map.html)
      * [SparseCore Kernel Writing](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)
      * [Fuser API: Fuse operations around kernels](https://docs.jax.dev/en/latest/pallas/tpu/fuser.html)
      * [Pseudo-Random Number Generation](https://docs.jax.dev/en/latest/pallas/tpu/prng.html)
      * [TPU Hardware Reference](https://docs.jax.dev/en/latest/pallas/tpu/hardware.html)
    * [Pallas Mosaic GPU](https://docs.jax.dev/en/latest/pallas/gpu/index.html)
      * [Quickstart: GPU](https://docs.jax.dev/en/latest/pallas/gpu/quickstart.html)
      * [Mosaic GPU Pipelining](https://docs.jax.dev/en/latest/pallas/gpu/pipelining.html)
      * [Writing high-performance matrix multiplication kernels for Blackwell](https://docs.jax.dev/en/latest/pallas/gpu/blackwell_matmul.html)
      * [Collective matrix multiplication](https://docs.jax.dev/en/latest/pallas/gpu/collective_matmul.html)
      * [Writing Mosaic GPU kernels with Pallas](https://docs.jax.dev/en/latest/pallas/gpu/reference.html)
    * [Pallas Quickstart](https://docs.jax.dev/en/latest/pallas/quickstart.html)
    * [Grids and BlockSpecs](https://docs.jax.dev/en/latest/pallas/grid_blockspec.html)
    * [Software Pipelining](https://docs.jax.dev/en/latest/pallas/pipelining.html)
    * [API reference](https://docs.jax.dev/en/latest/jax.experimental.pallas.html)
      * [Pallas TPU (TensorCore)](https://docs.jax.dev/en/latest/jax.experimental.pallas.tpu.html)
      * [Pallas MGPU](https://docs.jax.dev/en/latest/jax.experimental.pallas.mosaic_gpu.html)
      * [Triton](https://docs.jax.dev/en/latest/jax.experimental.pallas.triton.html)
    * [Pallas Design Notes](https://docs.jax.dev/en/latest/pallas/design/index.html)
      * [Pallas Design](https://docs.jax.dev/en/latest/pallas/design/design.html)
      * [Pallas Async Operations](https://docs.jax.dev/en/latest/pallas/design/async_note.html)
    * [Pallas Changelog](https://docs.jax.dev/en/latest/pallas/CHANGELOG.html)


Resources
  * [Additional guides](https://docs.jax.dev/en/latest/advanced_guides.html)
    * [Colocated Python](https://docs.jax.dev/en/latest/notebooks/colocated-python.html)
    * [The Training Cookbook](https://docs.jax.dev/en/latest/the-training-cookbook.html)
    * [GPU performance tips](https://docs.jax.dev/en/latest/gpu_performance_tips.html)
  * [Numerical accuracy](https://docs.jax.dev/en/latest/accuracy.html)
  * [API Reference](https://docs.jax.dev/en/latest/jax.html)
    * [`jax.numpy` module](https://docs.jax.dev/en/latest/jax.numpy.html)
      * [jax.numpy.fft.fft](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.fft.html)
      * [jax.numpy.fft.fft2](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.fft2.html)
      * [jax.numpy.fft.fftfreq](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.fftfreq.html)
      * [jax.numpy.fft.fftn](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.fftn.html)
      * [jax.numpy.fft.fftshift](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.fftshift.html)
      * [jax.numpy.fft.hfft](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.hfft.html)
      * [jax.numpy.fft.ifft](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.ifft.html)
      * [jax.numpy.fft.ifft2](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.ifft2.html)
      * [jax.numpy.fft.ifftn](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.ifftn.html)
      * [jax.numpy.fft.ifftshift](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.ifftshift.html)
      * [jax.numpy.fft.ihfft](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.ihfft.html)
      * [jax.numpy.fft.irfft](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.irfft.html)
      * [jax.numpy.fft.irfft2](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.irfft2.html)
      * [jax.numpy.fft.irfftn](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.irfftn.html)
      * [jax.numpy.fft.rfft](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.rfft.html)
      * [jax.numpy.fft.rfft2](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.rfft2.html)
      * [jax.numpy.fft.rfftfreq](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.rfftfreq.html)
      * [jax.numpy.fft.rfftn](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.fft.rfftn.html)
    * [`jax.scipy` module](https://docs.jax.dev/en/latest/jax.scipy.html)
      * [jax.scipy.stats.bernoulli.logpmf](https://docs.jax.dev/en/latest/_autosummary/jax.scipy.stats.bernoulli.logpmf.html)
      * [jax.scipy.stats.bernoulli.pmf](https://docs.jax.dev/en/latest/_autosummary/jax.scipy.stats.bernoulli.pmf.html)
      * [jax.scipy.stats.bernoulli.cdf](https://docs.jax.dev/en/latest/_autosummary/jax.scipy.stats.bernoulli.cdf.html)
      * [jax.scipy.stats.bernoulli.ppf](https://docs.jax.dev/en/latest/_autosummary/jax.scipy.stats.bernoulli.ppf.html)
    * [`jax.lax` module](https://docs.jax.dev/en/latest/jax.lax.html)
    * [`jax.random` module](https://docs.jax.dev/en/latest/jax.random.html)
    * [`jax.sharding` module](https://docs.jax.dev/en/latest/jax.sharding.html)
    * [`jax.ad_checkpoint` module](https://docs.jax.dev/en/latest/jax.ad_checkpoint.html)
    * [`jax.debug` module](https://docs.jax.dev/en/latest/jax.debug.html)
    * [`jax.dlpack` module](https://docs.jax.dev/en/latest/jax.dlpack.html)
    * [`jax.distributed` module](https://docs.jax.dev/en/latest/jax.distributed.html)
    * [`jax.dtypes` module](https://docs.jax.dev/en/latest/jax.dtypes.html)
    * [`jax.ffi` module](https://docs.jax.dev/en/latest/jax.ffi.html)
    * [`jax.flatten_util` module](https://docs.jax.dev/en/latest/jax.flatten_util.html)
    * [`jax.image` module](https://docs.jax.dev/en/latest/jax.image.html)
    * [`jax.nn` module](https://docs.jax.dev/en/latest/jax.nn.html)
      * [`jax.nn.initializers` module](https://docs.jax.dev/en/latest/jax.nn.initializers.html)
    * [`jax.ops` module](https://docs.jax.dev/en/latest/jax.ops.html)
    * [`jax.profiler` module](https://docs.jax.dev/en/latest/jax.profiler.html)
    * [`jax.ref` module](https://docs.jax.dev/en/latest/jax.ref.html)
    * [`jax.stages` module](https://docs.jax.dev/en/latest/jax.stages.html)
    * [`jax.test_util` module](https://docs.jax.dev/en/latest/jax.test_util.html)
    * [`jax.tree` module](https://docs.jax.dev/en/latest/jax.tree.html)
    * [`jax.tree_util` module](https://docs.jax.dev/en/latest/jax.tree_util.html)
    * [`jax.typing` module](https://docs.jax.dev/en/latest/jax.typing.html)
    * [`jax.export` module](https://docs.jax.dev/en/latest/jax.export.html)
    * [`jax.extend` module](https://docs.jax.dev/en/latest/jax.extend.html)
      * [`jax.extend.backend` module](https://docs.jax.dev/en/latest/jax.extend.backend.html)
      * [`jax.extend.core` module](https://docs.jax.dev/en/latest/jax.extend.core.html)
      * [`jax.extend.linear_util` module](https://docs.jax.dev/en/latest/jax.extend.linear_util.html)
      * [`jax.extend.lowering` module](https://docs.jax.dev/en/latest/jax.extend.lowering.html)
      * [`jax.extend.mlir` module](https://docs.jax.dev/en/latest/jax.extend.mlir.html)
      * [`jax.extend.pallas` module](https://docs.jax.dev/en/latest/jax.extend.pallas.html)
      * [`jax.extend.random` module](https://docs.jax.dev/en/latest/jax.extend.random.html)
      * [`jax.extend.xla` module](https://docs.jax.dev/en/latest/jax.extend.xla.html)
    * [`jax.example_libraries` module](https://docs.jax.dev/en/latest/jax.example_libraries.html)
      * [`jax.example_libraries.optimizers` module](https://docs.jax.dev/en/latest/jax.example_libraries.optimizers.html)
      * [`jax.example_libraries.stax` module](https://docs.jax.dev/en/latest/jax.example_libraries.stax.html)
    * [`jax.experimental` module](https://docs.jax.dev/en/latest/jax.experimental.html)
      * [`jax.experimental.checkify` module](https://docs.jax.dev/en/latest/jax.experimental.checkify.html)
      * [`jax.experimental.compilation_cache` module](https://docs.jax.dev/en/latest/jax.experimental.compilation_cache.html)
      * [`jax.experimental.custom_partitioning` module](https://docs.jax.dev/en/latest/jax.experimental.custom_partitioning.html)
      * [`jax.experimental.jet` module](https://docs.jax.dev/en/latest/jax.experimental.jet.html)
      * [`jax.experimental.key_reuse` module](https://docs.jax.dev/en/latest/jax.experimental.key_reuse.html)
      * [`jax.experimental.mesh_utils` module](https://docs.jax.dev/en/latest/jax.experimental.mesh_utils.html)
      * [`jax.experimental.multihost_utils` module](https://docs.jax.dev/en/latest/jax.experimental.multihost_utils.html)
      * [`jax.experimental.pallas` module](https://docs.jax.dev/en/latest/jax.experimental.pallas.html)
        * [Pallas TPU (TensorCore)](https://docs.jax.dev/en/latest/jax.experimental.pallas.tpu.html)
        * [Pallas MGPU](https://docs.jax.dev/en/latest/jax.experimental.pallas.mosaic_gpu.html)
        * [Triton](https://docs.jax.dev/en/latest/jax.experimental.pallas.triton.html)
      * [`jax.experimental.random` module](https://docs.jax.dev/en/latest/jax.experimental.random.html)
      * [`jax.experimental.serialize_executable` module](https://docs.jax.dev/en/latest/jax.experimental.serialize_executable.html)
      * [`jax.experimental.sparse` module](https://docs.jax.dev/en/latest/jax.experimental.sparse.html)
        * [jax.experimental.sparse.BCOO](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.BCOO.html)
        * [jax.experimental.sparse.bcoo_broadcast_in_dim](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_broadcast_in_dim.html)
        * [jax.experimental.sparse.bcoo_concatenate](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_concatenate.html)
        * [jax.experimental.sparse.bcoo_dot_general](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_dot_general.html)
        * [jax.experimental.sparse.bcoo_dot_general_sampled](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_dot_general_sampled.html)
        * [jax.experimental.sparse.bcoo_dynamic_slice](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_dynamic_slice.html)
        * [jax.experimental.sparse.bcoo_extract](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_extract.html)
        * [jax.experimental.sparse.bcoo_fromdense](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_fromdense.html)
        * [jax.experimental.sparse.bcoo_gather](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_gather.html)
        * [jax.experimental.sparse.bcoo_multiply_dense](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_multiply_dense.html)
        * [jax.experimental.sparse.bcoo_multiply_sparse](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_multiply_sparse.html)
        * [jax.experimental.sparse.bcoo_update_layout](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_update_layout.html)
        * [jax.experimental.sparse.bcoo_reduce_sum](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_reduce_sum.html)
        * [jax.experimental.sparse.bcoo_reshape](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_reshape.html)
        * [jax.experimental.sparse.bcoo_slice](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_slice.html)
        * [jax.experimental.sparse.bcoo_sort_indices](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_sort_indices.html)
        * [jax.experimental.sparse.bcoo_squeeze](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_squeeze.html)
        * [jax.experimental.sparse.bcoo_sum_duplicates](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_sum_duplicates.html)
        * [jax.experimental.sparse.bcoo_todense](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_todense.html)
        * [jax.experimental.sparse.bcoo_transpose](https://docs.jax.dev/en/latest/_autosummary/jax.experimental.sparse.bcoo_transpose.html)
      * [`jax.experimental.xla_metadata` module](https://docs.jax.dev/en/latest/jax.experimental.xla_metadata.html)
    * [jax.Array.addressable_shards](https://docs.jax.dev/en/latest/_autosummary/jax.Array.addressable_shards.html)
    * [jax.Array.all](https://docs.jax.dev/en/latest/_autosummary/jax.Array.all.html)
    * [jax.Array.any](https://docs.jax.dev/en/latest/_autosummary/jax.Array.any.html)
    * [jax.Array.argmax](https://docs.jax.dev/en/latest/_autosummary/jax.Array.argmax.html)
    * [jax.Array.argmin](https://docs.jax.dev/en/latest/_autosummary/jax.Array.argmin.html)
    * [jax.Array.argpartition](https://docs.jax.dev/en/latest/_autosummary/jax.Array.argpartition.html)
    * [jax.Array.argsort](https://docs.jax.dev/en/latest/_autosummary/jax.Array.argsort.html)
    * [jax.Array.astype](https://docs.jax.dev/en/latest/_autosummary/jax.Array.astype.html)
    * [jax.Array.at](https://docs.jax.dev/en/latest/_autosummary/jax.Array.at.html)
    * [jax.Array.byteswap](https://docs.jax.dev/en/latest/_autosummary/jax.Array.byteswap.html)
    * [jax.Array.choose](https://docs.jax.dev/en/latest/_autosummary/jax.Array.choose.html)
    * [jax.Array.clip](https://docs.jax.dev/en/latest/_autosummary/jax.Array.clip.html)
    * [jax.Array.compress](https://docs.jax.dev/en/latest/_autosummary/jax.Array.compress.html)
    * [jax.Array.committed](https://docs.jax.dev/en/latest/_autosummary/jax.Array.committed.html)
    * [jax.Array.conj](https://docs.jax.dev/en/latest/_autosummary/jax.Array.conj.html)
    * [jax.Array.conjugate](https://docs.jax.dev/en/latest/_autosummary/jax.Array.conjugate.html)
    * [jax.Array.copy](https://docs.jax.dev/en/latest/_autosummary/jax.Array.copy.html)
    * [jax.Array.copy_to_host_async](https://docs.jax.dev/en/latest/_autosummary/jax.Array.copy_to_host_async.html)
    * [jax.Array.cumprod](https://docs.jax.dev/en/latest/_autosummary/jax.Array.cumprod.html)
    * [jax.Array.cumsum](https://docs.jax.dev/en/latest/_autosummary/jax.Array.cumsum.html)
    * [jax.Array.device](https://docs.jax.dev/en/latest/_autosummary/jax.Array.device.html)
    * [jax.Array.diagonal](https://docs.jax.dev/en/latest/_autosummary/jax.Array.diagonal.html)
    * [jax.Array.dot](https://docs.jax.dev/en/latest/_autosummary/jax.Array.dot.html)
    * [jax.Array.dtype](https://docs.jax.dev/en/latest/_autosummary/jax.Array.dtype.html)
    * [jax.Array.flat](https://docs.jax.dev/en/latest/_autosummary/jax.Array.flat.html)
    * [jax.Array.flatten](https://docs.jax.dev/en/latest/_autosummary/jax.Array.flatten.html)
    * [jax.Array.global_shards](https://docs.jax.dev/en/latest/_autosummary/jax.Array.global_shards.html)
    * [jax.Array.imag](https://docs.jax.dev/en/latest/_autosummary/jax.Array.imag.html)
    * [jax.Array.is_fully_addressable](https://docs.jax.dev/en/latest/_autosummary/jax.Array.is_fully_addressable.html)
    * [jax.Array.is_fully_replicated](https://docs.jax.dev/en/latest/_autosummary/jax.Array.is_fully_replicated.html)
    * [jax.Array.item](https://docs.jax.dev/en/latest/_autosummary/jax.Array.item.html)
    * [jax.Array.itemsize](https://docs.jax.dev/en/latest/_autosummary/jax.Array.itemsize.html)
    * [jax.Array.max](https://docs.jax.dev/en/latest/_autosummary/jax.Array.max.html)
    * [jax.Array.mean](https://docs.jax.dev/en/latest/_autosummary/jax.Array.mean.html)
    * [jax.Array.min](https://docs.jax.dev/en/latest/_autosummary/jax.Array.min.html)
    * [jax.Array.nbytes](https://docs.jax.dev/en/latest/_autosummary/jax.Array.nbytes.html)
    * [jax.Array.ndim](https://docs.jax.dev/en/latest/_autosummary/jax.Array.ndim.html)
    * [jax.Array.nonzero](https://docs.jax.dev/en/latest/_autosummary/jax.Array.nonzero.html)
    * [jax.Array.prod](https://docs.jax.dev/en/latest/_autosummary/jax.Array.prod.html)
    * [jax.Array.ptp](https://docs.jax.dev/en/latest/_autosummary/jax.Array.ptp.html)
    * [jax.Array.ravel](https://docs.jax.dev/en/latest/_autosummary/jax.Array.ravel.html)
    * [jax.Array.real](https://docs.jax.dev/en/latest/_autosummary/jax.Array.real.html)
    * [jax.Array.repeat](https://docs.jax.dev/en/latest/_autosummary/jax.Array.repeat.html)
    * [jax.Array.reshape](https://docs.jax.dev/en/latest/_autosummary/jax.Array.reshape.html)
    * [jax.Array.round](https://docs.jax.dev/en/latest/_autosummary/jax.Array.round.html)
    * [jax.Array.searchsorted](https://docs.jax.dev/en/latest/_autosummary/jax.Array.searchsorted.html)
    * [jax.Array.shape](https://docs.jax.dev/en/latest/_autosummary/jax.Array.shape.html)
    * [jax.Array.sharding](https://docs.jax.dev/en/latest/_autosummary/jax.Array.sharding.html)
    * [jax.Array.size](https://docs.jax.dev/en/latest/_autosummary/jax.Array.size.html)
    * [jax.Array.sort](https://docs.jax.dev/en/latest/_autosummary/jax.Array.sort.html)
    * [jax.Array.squeeze](https://docs.jax.dev/en/latest/_autosummary/jax.Array.squeeze.html)
    * [jax.Array.std](https://docs.jax.dev/en/latest/_autosummary/jax.Array.std.html)
    * [jax.Array.sum](https://docs.jax.dev/en/latest/_autosummary/jax.Array.sum.html)
    * [jax.Array.swapaxes](https://docs.jax.dev/en/latest/_autosummary/jax.Array.swapaxes.html)
    * [jax.Array.take](https://docs.jax.dev/en/latest/_autosummary/jax.Array.take.html)
    * [jax.Array.to_device](https://docs.jax.dev/en/latest/_autosummary/jax.Array.to_device.html)
    * [jax.Array.trace](https://docs.jax.dev/en/latest/_autosummary/jax.Array.trace.html)
    * [jax.Array.transpose](https://docs.jax.dev/en/latest/_autosummary/jax.Array.transpose.html)
    * [jax.Array.var](https://docs.jax.dev/en/latest/_autosummary/jax.Array.var.html)
    * [jax.Array.view](https://docs.jax.dev/en/latest/_autosummary/jax.Array.view.html)
    * [jax.Array.T](https://docs.jax.dev/en/latest/_autosummary/jax.Array.T.html)
    * [jax.Array.mT](https://docs.jax.dev/en/latest/_autosummary/jax.Array.mT.html)
  * [API compatibility](https://docs.jax.dev/en/latest/api_compatibility.html)
  * [Python and NumPy version support policy](https://docs.jax.dev/en/latest/deprecation.html)
  * [Developer notes](https://docs.jax.dev/en/latest/contributor_guide.html)
    * [Contributing to JAX](https://docs.jax.dev/en/latest/contributing.html)
    * [Building from source](https://docs.jax.dev/en/latest/developer.html)
    * [Investigating a regression](https://docs.jax.dev/en/latest/investigating_a_regression.html)
    * [JAX Enhancement Proposals (JEPs)](https://docs.jax.dev/en/latest/jep/index.html)
      * [263: JAX PRNG Design](https://docs.jax.dev/en/latest/jep/263-prng.html)
      * [2026: Custom JVP/VJP rules for JAX-transformable functions](https://docs.jax.dev/en/latest/jep/2026-custom-derivatives.html)
      * [4008: Custom VJP and `nondiff_argnums` update](https://docs.jax.dev/en/latest/jep/4008-custom-vjp-update.html)
      * [4410: Omnistaging](https://docs.jax.dev/en/latest/jep/4410-omnistaging.html)
      * [9263: Typed keys & pluggable RNGs](https://docs.jax.dev/en/latest/jep/9263-typed-keys.html)
      * [9407: Design of Type Promotion Semantics for JAX](https://docs.jax.dev/en/latest/jep/9407-type-promotion.html)
      * [9419: Jax and Jaxlib versioning](https://docs.jax.dev/en/latest/jep/9419-jax-versioning.html)
      * [10657: Sequencing side-effects in JAX](https://docs.jax.dev/en/latest/jep/10657-sequencing-effects.html)
      * [11830: `jax.remat` / `jax.checkpoint` new implementation](https://docs.jax.dev/en/latest/jep/11830-new-remat-checkpoint.html)
      * [12049: Type Annotation Roadmap for JAX](https://docs.jax.dev/en/latest/jep/12049-type-annotations.html)
      * [14273: `shard_map` (`shmap`) for simple per-device code](https://docs.jax.dev/en/latest/jep/14273-shard-map.html)
      * [15856: `jax.extend`, an extensions module](https://docs.jax.dev/en/latest/jep/15856-jex.html)
      * [17111: Efficient transposition of `shard_map` (and other maps)](https://docs.jax.dev/en/latest/jep/17111-shmap-transpose.html)
      * [18137: Scope of JAX NumPy & SciPy Wrappers](https://docs.jax.dev/en/latest/jep/18137-numpy-scipy-scope.html)
      * [25516: Effort-based versioning](https://docs.jax.dev/en/latest/jep/25516-effver.html)
      * [28661: Supporting the `__jax_array__` protocol](https://docs.jax.dev/en/latest/jep/28661-jax-array-protocol.html)
      * [28845: Stateful Randomness in JAX](https://docs.jax.dev/en/latest/jep/28845-stateful-rng.html)
    * [JAX Internal Implementation Notes](https://docs.jax.dev/en/latest/internals/index.html)
      * [Handling of closed-over constants](https://docs.jax.dev/en/latest/internals/constants.html)
  * [Extension guides](https://docs.jax.dev/en/latest/extensions.html)
    * [Writing custom Jaxpr interpreters in JAX](https://docs.jax.dev/en/latest/notebooks/Writing_custom_interpreters_in_Jax.html)
    * [`jax.extend` module](https://docs.jax.dev/en/latest/jax.extend.html)
      * [`jax.extend.backend` module](https://docs.jax.dev/en/latest/jax.extend.backend.html)
      * [`jax.extend.core` module](https://docs.jax.dev/en/latest/jax.extend.core.html)
      * [`jax.extend.linear_util` module](https://docs.jax.dev/en/latest/jax.extend.linear_util.html)
      * [`jax.extend.lowering` module](https://docs.jax.dev/en/latest/jax.extend.lowering.html)
      * [`jax.extend.mlir` module](https://docs.jax.dev/en/latest/jax.extend.mlir.html)
      * [`jax.extend.pallas` module](https://docs.jax.dev/en/latest/jax.extend.pallas.html)
      * [`jax.extend.random` module](https://docs.jax.dev/en/latest/jax.extend.random.html)
      * [`jax.extend.xla` module](https://docs.jax.dev/en/latest/jax.extend.xla.html)
    * [Building on JAX](https://docs.jax.dev/en/latest/building_on_jax.html)
  * [About the project](https://docs.jax.dev/en/latest/about.html)


  * [Frequently asked questions (FAQ)](https://docs.jax.dev/en/latest/faq.html)
  * [Change log](https://docs.jax.dev/en/latest/changelog.html)
  * [Glossary of terms](https://docs.jax.dev/en/latest/glossary.html)


  * [Configuration Options](https://docs.jax.dev/en/latest/config_options.html)


  * [ ](https://docs.jax.dev/en/latest/index.html)
  * Installation


[ ](https://github.com/jax-ml/jax)
  * [ .md ](https://docs.jax.dev/en/latest/_sources/installation.md)
  * .pdf


Light Dark System Settings
# Installation
##  Contents 
  * [Supported platforms](https://docs.jax.dev/en/latest/installation.html#supported-platforms)
  * [CPU](https://docs.jax.dev/en/latest/installation.html#cpu)
    * [pip installation: CPU](https://docs.jax.dev/en/latest/installation.html#pip-installation-cpu)
  * [NVIDIA GPU](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu)
    * [pip installation: NVIDIA GPU (CUDA, installed via pip, easier)](https://docs.jax.dev/en/latest/installation.html#pip-installation-nvidia-gpu-cuda-installed-via-pip-easier)
    * [pip installation: NVIDIA GPU (CUDA, installed locally, harder)](https://docs.jax.dev/en/latest/installation.html#pip-installation-nvidia-gpu-cuda-installed-locally-harder)
    * [NVIDIA GPU Docker containers](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu-docker-containers)
  * [Google Cloud TPU](https://docs.jax.dev/en/latest/installation.html#google-cloud-tpu)
    * [pip installation: Google Cloud TPU](https://docs.jax.dev/en/latest/installation.html#pip-installation-google-cloud-tpu)
  * [Mac GPU](https://docs.jax.dev/en/latest/installation.html#mac-gpu)
  * [AMD GPU (Linux)](https://docs.jax.dev/en/latest/installation.html#amd-gpu-linux)
    * [ROCm version compatibility](https://docs.jax.dev/en/latest/installation.html#rocm-version-compatibility)
    * [pip installation: AMD GPU (ROCm, pre-installed)](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-pre-installed)
    * [pip installation: AMD GPU (ROCm, installed via pip)](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-installed-via-pip)
    * [AMD GPU Docker containers](https://docs.jax.dev/en/latest/installation.html#amd-gpu-docker-containers)
    * [Getting help](https://docs.jax.dev/en/latest/installation.html#getting-help)
  * [Intel GPU](https://docs.jax.dev/en/latest/installation.html#intel-gpu)
    * [pip installation: Intel GPU (oneAPI)](https://docs.jax.dev/en/latest/installation.html#pip-installation-intel-gpu-oneapi)
  * [Conda (community-supported)](https://docs.jax.dev/en/latest/installation.html#conda-community-supported)
    * [Conda installation](https://docs.jax.dev/en/latest/installation.html#conda-installation)
  * [JAX nightly installation](https://docs.jax.dev/en/latest/installation.html#jax-nightly-installation)
  * [Building JAX from source](https://docs.jax.dev/en/latest/installation.html#building-jax-from-source)
  * [Installing older `jaxlib` wheels](https://docs.jax.dev/en/latest/installation.html#installing-older-jaxlib-wheels)


# Installation[#](https://docs.jax.dev/en/latest/installation.html#installation "Link to this heading")
Using JAX requires installing two packages: `jax`, which is pure Python and cross-platform, and `jaxlib` which contains compiled binaries, and requires different builds for different operating systems and accelerators.
**Summary:** For most users, a typical JAX installation may look something like this:
  * **CPU-only (Linux/macOS/Windows)**

```
pip install -U jax

```
Copy to clipboard
  * **GPU (NVIDIA, CUDA 13)**

```
pip install -U "jax[cuda13]"

```
Copy to clipboard
  * **GPU (AMD, ROCm)**

```
pip install -U "jax[rocm7-local]"

```
Copy to clipboard
  * **TPU (Google Cloud TPU VM)**

```
pip install -U "jax[tpu]"

```
Copy to clipboard
  * **GPU (Intel, oneAPI)**

```
pip install -U "jax[oneapi]"

```
Copy to clipboard


## Supported platforms[#](https://docs.jax.dev/en/latest/installation.html#supported-platforms "Link to this heading")
The table below shows all supported platforms and installation options. Check if your setup is supported; and if it says _“yes”_ or _“experimental”_ , then click on the corresponding link to learn how to install JAX in greater detail.  
|   | Linux, x86_64  | Linux, aarch64  | Mac, aarch64  | Windows, x86_64  | Windows WSL2, x86_64  |  
| --- | --- | --- | --- | --- | --- |  
| CPU  | [yes](https://docs.jax.dev/en/latest/installation.html#install-cpu)  | [yes](https://docs.jax.dev/en/latest/installation.html#install-cpu)  | [yes](https://docs.jax.dev/en/latest/installation.html#install-cpu)  | [yes](https://docs.jax.dev/en/latest/installation.html#install-cpu)  | [yes](https://docs.jax.dev/en/latest/installation.html#install-cpu)  |  
| NVIDIA GPU  | [yes](https://docs.jax.dev/en/latest/installation.html#install-nvidia-gpu)  | [yes](https://docs.jax.dev/en/latest/installation.html#install-nvidia-gpu)  | n/a  | no  | [experimental](https://docs.jax.dev/en/latest/installation.html#install-nvidia-gpu)  |  
| Google Cloud TPU  | [yes](https://docs.jax.dev/en/latest/installation.html#install-google-tpu)  | n/a  | n/a  | n/a  | n/a  |  
| AMD GPU  | [yes](https://docs.jax.dev/en/latest/installation.html#install-amd-gpu)  | no  | n/a  | no  | [experimental](https://docs.jax.dev/en/latest/installation.html#install-amd-gpu)  |  
| Apple GPU  | n/a  | no  | [experimental](https://docs.jax.dev/en/latest/installation.html#install-mac-gpu)  | n/a  | n/a  |  
| Intel GPU  | [experimental](https://docs.jax.dev/en/latest/installation.html#install-intel-gpu)  | n/a  | n/a  | no  | no  |  
## CPU[#](https://docs.jax.dev/en/latest/installation.html#cpu "Link to this heading")
### pip installation: CPU[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-cpu "Link to this heading")
Currently, the JAX team releases `jaxlib` wheels for the following operating systems and architectures:
  * Linux, x86_64
  * Linux, aarch64
  * macOS, Apple ARM-based
  * Windows, x86_64 (_experimental_)


To install a CPU-only version of JAX, which might be useful for doing local development on a laptop, you can run:

```
pip install --upgrade pip
pip install --upgrade jax

```
Copy to clipboard
On Windows, you may also need to install the [Microsoft Visual Studio 2019 Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022) if it is not already installed on your machine.
Other operating systems and architectures require building from source. Trying to pip install on other operating systems and architectures may lead to `jaxlib` not being installed alongside `jax`, although `jax` may successfully install (but fail at runtime).
## NVIDIA GPU[#](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu "Link to this heading")
On CUDA 12, JAX supports NVIDIA GPUs that have SM version 5.2 (Maxwell) or newer. Note that Kepler-series GPUs are no longer supported by JAX since NVIDIA has dropped support for Kepler GPUs in its software. On CUDA 13, JAX supports NVIDIA GPUs that have SM version 7.5 or newer. NVIDIA dropped support for previous GPUs in CUDA 13.
You must first install the NVIDIA driver. You’re recommended to install the newest driver available from NVIDIA, but the driver version must be >= 525 for CUDA 12 on Linux, and >= 580 for CUDA 13 on Linux.
If you need to use a newer CUDA toolkit with an older driver, for example on a cluster where you cannot update the NVIDIA driver easily, you may be able to use the [CUDA forward compatibility packages](https://docs.nvidia.com/deploy/cuda-compatibility/) that NVIDIA provides for this purpose.
### pip installation: NVIDIA GPU (CUDA, installed via pip, easier)[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-nvidia-gpu-cuda-installed-via-pip-easier "Link to this heading")
There are two ways to install JAX with NVIDIA GPU support:
  * Using NVIDIA CUDA and cuDNN installed from pip wheels
  * Using a self-installed CUDA/cuDNN


The JAX team strongly recommends installing CUDA and cuDNN using the pip wheels, since it is much easier!
NVIDIA has released CUDA packages only for x86_64 and aarch64.

```
pip install --upgrade pip

# NVIDIA CUDA 13 installation
# Note: wheels only available on linux.
pip install --upgrade "jax[cuda13]"

# Alternatively, for CUDA 12, use
# pip install --upgrade "jax[cuda12]"

```
Copy to clipboard
We recommend migrating to the CUDA 13 wheels; at some point in the future we will drop CUDA 12 support.
If JAX detects the wrong version of the NVIDIA CUDA libraries, there are several things you need to check:
  * Make sure that `LD_LIBRARY_PATH` is not set, since `LD_LIBRARY_PATH` can override the NVIDIA CUDA libraries.
  * Make sure that the NVIDIA CUDA libraries installed are those requested by JAX. Rerunning the installation command above should work.


### pip installation: NVIDIA GPU (CUDA, installed locally, harder)[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-nvidia-gpu-cuda-installed-locally-harder "Link to this heading")
If you prefer to use a preinstalled copy of NVIDIA CUDA, you must first install NVIDIA [CUDA](https://developer.nvidia.com/cuda-downloads) and [cuDNN](https://developer.nvidia.com/CUDNN).
JAX provides pre-built CUDA-compatible wheels for **Linux x86_64 and Linux aarch64 only**. Other combinations of operating system and architecture are possible, but require building from source (refer to [Building from source](https://docs.jax.dev/en/latest/developer.html#building-from-source) to learn more}.
You should use an NVIDIA driver version that is at least as new as your [NVIDIA CUDA toolkit’s corresponding driver version](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions__table-cuda-toolkit-driver-versions). If you need to use a newer CUDA toolkit with an older driver, for example on a cluster where you cannot update the NVIDIA driver easily, you may be able to use the [CUDA forward compatibility packages](https://docs.nvidia.com/deploy/cuda-compatibility/) that NVIDIA provides for this purpose.
JAX currently ships two CUDA wheel variants: CUDA 12 and CUDA 13:
The CUDA 12 wheel is:  
| Built with  | Compatible with  |  
| --- | --- |  
| CUDA 12.3  | CUDA >=12.1  |  
| CUDNN 9.10  | CUDNN >=9.10.2, <10.0  |  
| NCCL 2.19  | NCCL >=2.18  |  
The CUDA 13 wheel is:  
| Built with  | Compatible with  |  
| --- | --- |  
| CUDA 13.0  | CUDA >=13.0  |  
| CUDNN 9.12  | CUDNN >=9.12, <10.0  |  
| NCCL 2.19  | NCCL >=2.18  |  
JAX checks the versions of your libraries, and will report an error if they are not sufficiently new. Setting the `JAX_SKIP_CUDA_CONSTRAINTS_CHECK` environment variable will disable the check, but using older versions of CUDA may lead to errors, or incorrect results.
NCCL is an optional dependency, required only if you are performing multi-GPU computations.
To install, run:

```
pip install --upgrade pip


# Installs the wheel compatible with NVIDIA CUDA 13 and cuDNN 9.12 or newer.
# Note: wheels only available on linux.
pip install --upgrade "jax[cuda13-local]"

# Installs the wheel compatible with NVIDIA CUDA 12 and cuDNN 9.10 or newer.
# Note: wheels only available on linux.
# pip install --upgrade "jax[cuda12-local]"

```
Copy to clipboard
**These`pip` installations do not work with Windows, and may fail silently; refer to the table [above](https://docs.jax.dev/en/latest/installation.html#supported-platforms).**
You can find your CUDA version with the command:

```
nvcc --version

```
Copy to clipboard
JAX uses `LD_LIBRARY_PATH` to find CUDA libraries and `PATH` to find binaries (`ptxas`, `nvlink`). Please make sure that these paths point to the correct CUDA installation.
JAX requires libdevice10.bc, which typically comes from the cuda-nvvm package. Make sure that it is present in your CUDA installation.
Please let the JAX team know on [the GitHub issue tracker](https://github.com/jax-ml/jax/issues) if you run into any errors or problems with the pre-built wheels.
### NVIDIA GPU Docker containers[#](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu-docker-containers "Link to this heading")
NVIDIA provides the [JAX Toolbox](https://github.com/NVIDIA/JAX-Toolbox) containers, which are bleeding edge containers containing nightly releases of jax and some models/frameworks.
## Google Cloud TPU[#](https://docs.jax.dev/en/latest/installation.html#google-cloud-tpu "Link to this heading")
### pip installation: Google Cloud TPU[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-google-cloud-tpu "Link to this heading")
JAX provides pre-built wheels for [Google Cloud TPU](https://cloud.google.com/tpu/docs/users-guide-tpu-vm). To install JAX along with appropriate versions of `jaxlib` and `libtpu`, you can run the following in your cloud TPU VM:

```
pip install "jax[tpu]"

```
Copy to clipboard
For users of Colab (https://colab.research.google.com/), be sure you are using _TPU v2_ and not the older, deprecated TPU runtime.
## Mac GPU[#](https://docs.jax.dev/en/latest/installation.html#mac-gpu "Link to this heading")
JAX is not supported on Mac/OSX GPU; instead use the standard [CPU installation](https://docs.jax.dev/en/latest/installation.html#install-cpu) commands.
## AMD GPU (Linux)[#](https://docs.jax.dev/en/latest/installation.html#amd-gpu-linux "Link to this heading")
AMD GPU support is provided by a ROCm JAX plugin supported by AMD. The [ROCm compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html) lists the GPU SKUs supported by ROCm.
There are two install paths:
  * **ROCm from pip** (`jax[rocm7-device-gfx950]`, `jax[rocm10-device-gfx942]`, and so on). TheRock wheels come from AMD’s stable index, named with `--extra-index-url`. ROCm 7: `https://repo.amd.com/rocm/whl-multi-arch/`. ROCm 10: `https://stable.repo.amd.com/rocm/whl-next/`.
  * **System ROCm** (`jax[rocm7-local]`). ROCm is already installed, typically under `/opt/rocm`. Follow the [ROCm installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) before installing JAX.


### ROCm version compatibility[#](https://docs.jax.dev/en/latest/installation.html#rocm-version-compatibility "Link to this heading")
Each JAX ROCm plugin release targets a specific ROCm version, so the installed ROCm must match the version the plugin was built against. AMD maintains the authoritative mapping in the [JAX on ROCm compatibility matrix](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html); consult it to confirm which ROCm version your target JAX release requires before installing. The `rocm7` plugin packages require a ROCm 7.x installation. The `rocm10` extra requires a ROCm 10.x installation from its own index.
### pip installation: AMD GPU (ROCm, pre-installed)[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-pre-installed "Link to this heading")
With a compatible ROCm already installed (see above), install JAX and the ROCm plugins via:

```
pip install --upgrade "jax[rocm7-local]"

```
Copy to clipboard
ROCm-specific fixes are shipped as _post-releases_ of the ROCm plugin/PJRT packages (for example, `jax-rocm7-plugin==X.Y.Z.post1`). Upgrading `jax[rocm7-local]` will pick up the newest compatible post-release available from your configured package indexes.

```
python3 -c "import jax; print(jax.devices())"

```
Copy to clipboard
If the installation is working, this lists your ROCm devices (for example, `[RocmDevice(id=0), RocmDevice(id=1), ...]`).
To build the ROCm JAX wheels from source, see [Build ROCm JAX from Source](https://github.com/jax-ml/jax/blob/main/build/rocm/README.md).
### pip installation: AMD GPU (ROCm, installed via pip)[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-installed-via-pip "Link to this heading")
JAX can pull [TheRock](https://github.com/ROCm/TheRock) ROCm wheels from AMD’s package index, so no system ROCm is needed. Those wheels are not on PyPI, so pass `--extra-index-url` for the index of the ROCm line you want.
Name your GPU architecture in the extra. The ROCm math libraries (rocBLAS, MIOpen, and others) ship their GPU kernels in a separate per-architecture wheel, and pip does no hardware detection at install time, so the architecture has to come from the command line:

```
# ROCm 7, on gfx950 (MI350 series)
pip install --upgrade "jax[rocm7-device-gfx950]" \
  --extra-index-url https://repo.amd.com/rocm/whl-multi-arch/

# ROCm 10, on gfx942 (MI300 series)
pip install --upgrade "jax[rocm10-device-gfx942]" \
  --extra-index-url https://stable.repo.amd.com/rocm/whl-next/

```
Copy to clipboard
To find your architecture on a machine with ROCm installed:

```
rocminfo | grep -m1 -o 'gfx[0-9a-f]\+'

```
Copy to clipboard
Without ROCm, AMD’s `rocm-bootstrap` package on PyPI detects it instead:

```
pip install rocm-bootstrap && rocm-bootstrap-detect

```
Copy to clipboard
`gfx908`, `gfx90a`, `gfx942`, and `gfx950` cover the Instinct accelerators; the `gfx10xx`, `gfx11xx`, and `gfx12xx` targets cover Radeon cards.
If the GPU is not known at install time, the architecture-free extras need no architecture flag and pull the kernels for every supported target instead:

```
# any ROCm 7 target; jax[rocm] is an alias of jax[rocm7]
pip install --upgrade "jax[rocm7]" \
  --extra-index-url https://repo.amd.com/rocm/whl-multi-arch/

# any ROCm 10 target
pip install --upgrade "jax[rocm10]" \
  --extra-index-url https://stable.repo.amd.com/rocm/whl-next/

```
Copy to clipboard
As part of the same preview effort, the ROCm JAX fork ([ROCm/jax](https://github.com/ROCm/jax)) publishes [TheRock](https://github.com/ROCm/TheRock)-based JAX wheels — built against TheRock ROCm — as downloadable release assets. Grab the `wheelhouse_*_theRock*.zip` archive from the [latest ROCm/jax release](https://github.com/ROCm/jax/releases/latest), unzip it, and `pip install` the contained `jax-rocm7-pjrt` and `jax-rocm7-plugin` wheels (the release notes give the exact commands for each version). This path is also a preview and intended for evaluation.
When using these TheRock-based JAX wheels with a ROCm installation under `/opt/rocm`, `/opt/rocm` must also contain a TheRock-based ROCm distribution, including `lib/rocm_sysdeps/lib`. A classic ROCm installation does not provide the `librocm_sysdeps_*` libraries required by the plugin.
For generally available releases, use the pre-installed-ROCm path [above](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-pre-installed).
### AMD GPU Docker containers[#](https://docs.jax.dev/en/latest/installation.html#amd-gpu-docker-containers "Link to this heading")
AMD provides prebuilt ROCm JAX Docker images that bundle ROCm, JAX, and all required dependencies — the simplest way to get started, since you don’t need to install ROCm yourself. Pull the latest image with:

```
docker pull rocm/jax:latest

```
Copy to clipboard
See the [JAX on ROCm installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html) for the recommended `docker run` flags and for version-pinned image tags.
**Note** : ROCm support on Windows WSL2 is experimental. For WSL installation, you may need to:
  1. Install [ROCm for WSL](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/) following AMD’s official guide
  2. Follow the standard Linux ROCm JAX installation steps within your WSL environment
  3. Be aware that performance and stability may differ from native Linux installations


### Getting help[#](https://docs.jax.dev/en/latest/installation.html#getting-help "Link to this heading")
The ROCm JAX plugin is maintained by AMD. For ROCm-specific JAX issues — such as installation problems, ROCm/driver compatibility, or plugin/runtime errors — please report them on the [ROCm issue tracker](https://github.com/ROCm/ROCm/issues), which AMD monitors. For issues with JAX itself that are not ROCm-specific, use the [JAX issue tracker](https://github.com/jax-ml/jax/issues).
## Intel GPU[#](https://docs.jax.dev/en/latest/installation.html#intel-gpu "Link to this heading")
Intel provides experimental oneAPI PJRT and plugin wheels for JAX on PyPI. These enable JAX applications to run on Intel GPUs using XLA’s SYCL platform support.
Before installing JAX, install the `intel-gpu-compute` package in one of the following ways:
  * By following the [Intel GPU software installation guide](https://dgpu-docs.intel.com/installation-guides/installing-omix.html).
  * By using the [Intel Compute Runtime container](https://hub.docker.com/r/intel/compute-runtime) which already contains the necessary driver components. Follow [Running the container](https://hub.docker.com/r/intel/compute-runtime#running-the-container) section for more information.


### pip installation: Intel GPU (oneAPI)[#](https://docs.jax.dev/en/latest/installation.html#pip-installation-intel-gpu-oneapi "Link to this heading")
Once the required GPU drivers are installed, the oneAPI PJRT and plugin wheels can be installed via:

```
pip install --upgrade "jax[oneapi]"

```
Copy to clipboard
This automatically installs all required software dependencies. No further manual setup is needed beyond the GPU drivers installed above.

```
python3 -c "import jax; print(jax.devices())"

```
Copy to clipboard
If the installation works correctly, this lists all the available oneAPI devices (e.g. `[OneapiDevice(id=0), OneapiDevice(id=1), ...]`).
For supported platforms and required driver versions, see [oneAPI JAX release notes](https://github.com/Intel-tensorflow/jax/releases).
## Conda (community-supported)[#](https://docs.jax.dev/en/latest/installation.html#conda-community-supported "Link to this heading")
### Conda installation[#](https://docs.jax.dev/en/latest/installation.html#conda-installation "Link to this heading")
There is a community-supported Conda build of `jax`. To install it using `conda`, simply run:

```
conda install jax -c conda-forge

```
Copy to clipboard
If you run this command on machine with an NVIDIA GPU, this should install a CUDA-enabled package of `jaxlib`.
To ensure that the jax version you are installing is indeed CUDA-enabled, run:

```
conda install "jaxlib=*=*cuda*" jax -c conda-forge

```
Copy to clipboard
If you would like to override which release of CUDA is used by JAX, or to install the CUDA build on a machine without GPUs, follow the instructions in the [Tips & tricks](https://conda-forge.org/docs/user/tipsandtricks.html#installing-cuda-enabled-packages-like-tensorflow-and-pytorch) section of the `conda-forge` website.
Go to the `conda-forge` [jaxlib](https://github.com/conda-forge/jaxlib-feedstock#installing-jaxlib) and [jax](https://github.com/conda-forge/jax-feedstock#installing-jax) repositories for more details.
## JAX nightly installation[#](https://docs.jax.dev/en/latest/installation.html#jax-nightly-installation "Link to this heading")
Nightly releases reflect the state of the main JAX repository at the time they are built, and may not pass the full test suite.
Unlike the instructions for installing a JAX release, here we name all of JAX’s packages explicitly on the command line, so `pip` will upgrade them if a newer version is available.
JAX publishes nightlies, release candidates(RCs), and releases to several non-pypi [PEP 503](https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/) indexes.
All JAX packages can be reached from the index `https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/` as well as PyPI mirrored packages. This additional mirroring enables nightly installation to use –index (-i) as the install method with pip.
**Note:** The unified index could return an RC or release as the newest version even with `--pre` immediately after a release before the newest nightly is rebuilt. If automation or testing must be done against nightlies or you cannot use our full index, use the extra index `https://us-python.pkg.dev/ml-oss-artifacts-published/jax-public-nightly-artifacts-registry/simple/` which only contains nightly artifacts.
The nightly index URLs can also be browsed directly. The `--index` URL is a [PEP 503](https://peps.python.org/pep-0503/) simple repository index for `pip`, and each package has its own sub-directory. For example, you can see the available `jax` packages at <https://us-python.pkg.dev/ml-oss-artifacts-published/jax-public-nightly-artifacts-registry/simple/jax>, `jax-cuda12-pjrt` packages at <https://us-python.pkg.dev/ml-oss-artifacts-published/jax-public-nightly-artifacts-registry/simple/jax-cuda12-pjrt>, and `jax-cuda13-pjrt` packages at <https://us-python.pkg.dev/ml-oss-artifacts-published/jax-public-nightly-artifacts-registry/simple/jax-cuda13-pjrt>.
  * CPU only:

```
pip install -U --pre jax jaxlib -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/

```
Copy to clipboard
  * Google Cloud TPU:

```
pip install -U --pre jax jaxlib libtpu requests -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/ -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

```
Copy to clipboard
  * NVIDIA GPU (CUDA 13):

```
pip install -U --pre jax jaxlib "jax-cuda13-plugin[with-cuda]" jax-cuda13-pjrt -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/

```
Copy to clipboard
  * NVIDIA GPU (CUDA 12):

```
pip install -U --pre jax jaxlib "jax-cuda12-plugin[with-cuda]" jax-cuda12-pjrt -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/

```
Copy to clipboard
## Building JAX from source[#](https://docs.jax.dev/en/latest/installation.html#building-jax-from-source "Link to this heading")
Refer to [Building from source](https://docs.jax.dev/en/latest/developer.html#building-from-source).
## Installing older `jaxlib` wheels[#](https://docs.jax.dev/en/latest/installation.html#installing-older-jaxlib-wheels "Link to this heading")
Due to storage limitations on the Python package index, the JAX team periodically removes older `jaxlib` wheels from the releases on http://pypi.org/project/jax. These can still be installed directly via the URLs here. For example:

```
# Install jaxlib on CPU via the wheel archive
pip install "jax[cpu]==0.3.25" -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/

# Install the jaxlib 0.3.25 CPU wheel directly
pip install jaxlib==0.3.25 -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/

```
Copy to clipboard
For specific older GPU wheels, be sure to use the `jax_cuda_releases.html` URL; for example

```
pip install jaxlib==0.3.25+cuda11.cudnn82 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

```
Copy to clipboard
[ previous JAX: High performance array computing ](https://docs.jax.dev/en/latest/index.html "previous page") [ next Newly documented ](https://docs.jax.dev/en/latest/whats-new.html "next page")
Contents 
  * [Supported platforms](https://docs.jax.dev/en/latest/installation.html#supported-platforms)
  * [CPU](https://docs.jax.dev/en/latest/installation.html#cpu)
    * [pip installation: CPU](https://docs.jax.dev/en/latest/installation.html#pip-installation-cpu)
  * [NVIDIA GPU](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu)
    * [pip installation: NVIDIA GPU (CUDA, installed via pip, easier)](https://docs.jax.dev/en/latest/installation.html#pip-installation-nvidia-gpu-cuda-installed-via-pip-easier)
    * [pip installation: NVIDIA GPU (CUDA, installed locally, harder)](https://docs.jax.dev/en/latest/installation.html#pip-installation-nvidia-gpu-cuda-installed-locally-harder)
    * [NVIDIA GPU Docker containers](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu-docker-containers)
  * [Google Cloud TPU](https://docs.jax.dev/en/latest/installation.html#google-cloud-tpu)
    * [pip installation: Google Cloud TPU](https://docs.jax.dev/en/latest/installation.html#pip-installation-google-cloud-tpu)
  * [Mac GPU](https://docs.jax.dev/en/latest/installation.html#mac-gpu)
  * [AMD GPU (Linux)](https://docs.jax.dev/en/latest/installation.html#amd-gpu-linux)
    * [ROCm version compatibility](https://docs.jax.dev/en/latest/installation.html#rocm-version-compatibility)
    * [pip installation: AMD GPU (ROCm, pre-installed)](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-pre-installed)
    * [pip installation: AMD GPU (ROCm, installed via pip)](https://docs.jax.dev/en/latest/installation.html#pip-installation-amd-gpu-rocm-installed-via-pip)
    * [AMD GPU Docker containers](https://docs.jax.dev/en/latest/installation.html#amd-gpu-docker-containers)
    * [Getting help](https://docs.jax.dev/en/latest/installation.html#getting-help)
  * [Intel GPU](https://docs.jax.dev/en/latest/installation.html#intel-gpu)
    * [pip installation: Intel GPU (oneAPI)](https://docs.jax.dev/en/latest/installation.html#pip-installation-intel-gpu-oneapi)
  * [Conda (community-supported)](https://docs.jax.dev/en/latest/installation.html#conda-community-supported)
    * [Conda installation](https://docs.jax.dev/en/latest/installation.html#conda-installation)
  * [JAX nightly installation](https://docs.jax.dev/en/latest/installation.html#jax-nightly-installation)
  * [Building JAX from source](https://docs.jax.dev/en/latest/installation.html#building-jax-from-source)
  * [Installing older `jaxlib` wheels](https://docs.jax.dev/en/latest/installation.html#installing-older-jaxlib-wheels)


By The JAX authors 
© Copyright 2024, The JAX Authors.