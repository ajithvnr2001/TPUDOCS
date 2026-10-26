---
id: "train_06_thinking_in_jax"
title: "Thinking in JAX"
url: "https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html"
category: "Training framework links"
description: "JAX programming concepts for portable CPU, GPU, and TPU computation."
crawled_at: "2026-10-26T12:45:40.303967+00:00"
crawler_engine: "Crawl4AI"
---

[Skip to main content](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#main-content)
Back to top `Ctrl`+`K`
This page is part of an older version of the JAX documentation, kept for reference. See [the current documentation](https://docs.jax.dev/en/latest/101/index.html) for the maintained version of this material. 
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
  * Quickstart: How to think in JAX


[ ](https://github.com/jax-ml/jax)
  * [ .ipynb ](https://docs.jax.dev/en/latest/_sources/notebooks/thinking_in_jax.ipynb)
  * .pdf


Light Dark System Settings
# Quickstart: How to think in JAX
##  Contents 
  * [Installation](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#installation)
  * [JAX vs. NumPy](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-vs-numpy)
  * [JAX arrays (`jax.Array`)](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-arrays-jax-array)
    * [Array creation](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#array-creation)
    * [Array devices and sharding](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#array-devices-and-sharding)
  * [Just-in-time compilation with `jax.jit`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#just-in-time-compilation-with-jax-jit)
  * [Taking derivatives with `jax.grad`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#taking-derivatives-with-jax-grad)
  * [Auto-vectorization with `jax.vmap`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#auto-vectorization-with-jax-vmap)
  * [Pseudorandom numbers](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#pseudorandom-numbers)
  * [Debugging](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#debugging)
    * [`jax.debug.print`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-debug-print)
    * [Debugging flags](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#debugging-flags)


# Quickstart: How to think in JAX[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#quickstart-how-to-think-in-jax "Link to this heading")
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jax-ml/jax/blob/main/docs/notebooks/thinking_in_jax.ipynb) [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/jax-ml/jax/blob/main/docs/notebooks/thinking_in_jax.ipynb)
**JAX is a library for array-oriented numerical computation (_à la_ [NumPy](https://numpy.org/)), with automatic differentiation and JIT compilation to enable high-performance machine learning research**.
This document provides a quick overview of essential JAX features, so you can get started with JAX:
  * JAX provides a unified NumPy-like interface to computations that run on CPU, GPU, or TPU, in local or distributed settings.
  * JAX features built-in Just-In-Time (JIT) compilation via [Open XLA](https://github.com/openxla), an open-source machine learning compiler ecosystem.
  * JAX functions support efficient evaluation of gradients via its automatic differentiation transformations.
  * JAX functions can be automatically vectorized to efficiently map them over arrays representing batches of inputs.


## Installation[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#installation "Link to this heading")
JAX can be installed for CPU on Linux, Windows, and macOS directly from the [Python Package Index](https://pypi.org/project/jax/):

```
pip install jax

```
Copy to clipboard
or, for NVIDIA GPU:

```
pip install -U "jax[cuda13]"

```
Copy to clipboard
For more detailed platform-specific installation information, check out [Installation](https://docs.jax.dev/en/latest/installation.html).
## JAX vs. NumPy[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-vs-numpy "Link to this heading")
**Key concepts:**
  * JAX provides a NumPy-inspired interface for convenience.
  * Through [duck-typing](https://en.wikipedia.org/wiki/Duck_typing), JAX arrays can often be used as drop-in replacements of NumPy arrays.
  * Unlike NumPy arrays, JAX arrays are always immutable.


NumPy provides a well-known, powerful API for working with numerical data. For convenience, JAX provides [`jax.numpy`](https://docs.jax.dev/en/latest/jax.numpy.html) which closely mirrors the NumPy API and provides easy entry into JAX. Almost anything that can be done with `numpy` can be done with `jax.numpy`, which is typically imported under the `jnp` alias:

```
import jax.numpy as jnp

```
Copy to clipboard
With this import, you can immediately use JAX in a similar manner to typical NumPy programs, including using NumPy-style array creation functions, Python functions and operators, and array attributes and methods:

```
import matplotlib.pyplot as plt

x_jnp = jnp.linspace(0, 10, 1000)
y_jnp = 2 * jnp.sin(x_jnp) * jnp.cos(x_jnp)
plt.plot(x_jnp, y_jnp);

```
Copy to clipboard
![../_images/34dac26eee2d637cfd8e007b166f01d637b4e35da283ef862d55cb0f5f2b3860.png](https://docs.jax.dev/en/latest/_images/34dac26eee2d637cfd8e007b166f01d637b4e35da283ef862d55cb0f5f2b3860.png)
The code blocks are identical to what you would expect with NumPy, aside from replacing `np` with `jnp`, and the results are the same. As we can see, JAX arrays can often be used directly in place of NumPy arrays for things like plotting.
The arrays themselves are implemented as different Python types:

```
import numpy as np
import jax.numpy as jnp

x_np = np.linspace(0, 10, 1000)
x_jnp = jnp.linspace(0, 10, 1000)

```
Copy to clipboard

```
type(x_np)

```
Copy to clipboard

```
numpy.ndarray

```
Copy to clipboard

```
type(x_jnp)

```
Copy to clipboard

```
jaxlib._jax.ArrayImpl

```
Copy to clipboard
Python’s duck-typing allows JAX arrays and NumPy arrays to be used interchangeably in many places. However, there is one important difference between JAX and NumPy arrays: JAX arrays are immutable, meaning that once created their contents cannot be changed.
Here is an example of mutating an array in NumPy:

```
# NumPy: mutable arrays
x = np.arange(10)
x[0] = 10
print(x)

```
Copy to clipboard

```
[10  1  2  3  4  5  6  7  8  9]

```
Copy to clipboard
The equivalent in JAX results in an error, as JAX arrays are immutable:

```
%xmode minimal

```
Copy to clipboard

```
Exception reporting mode: Minimal

```
Copy to clipboard

```
# JAX: immutable arrays
x = jnp.arange(10)
x[0] = 10

```
Copy to clipboard

```
TypeError: JAX arrays are immutable and do not support in-place item assignment. Instead of x[idx] = y, use x = x.at[idx].set(y) or another .at[] method: https://docs.jax.dev/en/latest/_autosummary/jax.numpy.ndarray.at.html

```
Copy to clipboard
For updating individual elements, JAX provides an [indexed update syntax](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.ndarray.at.html#jax-numpy-ndarray-at) that returns an updated copy:

```
y = x.at[0].set(10)
print(x)
print(y)

```
Copy to clipboard

```
[0 1 2 3 4 5 6 7 8 9]
[10  1  2  3  4  5  6  7  8  9]

```
Copy to clipboard
You’ll find a few differences between JAX arrays and NumPy arrays once you begin digging in. See also:
  * [Key concepts](https://docs.jax.dev/en/latest/key-concepts.html#jax-arrays-jax-array) for an introduction to the key concepts of JAX, such as transformations, tracing, jaxprs and pytrees.
  * [🔪 JAX - The Sharp Bits 🔪](https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html) for common gotchas when using JAX.


## JAX arrays (`jax.Array`)[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-arrays-jax-array "Link to this heading")
**Key concepts:**
  * Create arrays using JAX API functions.
  * JAX array objects have a `devices` attribute that indicates where the array is stored.
  * JAX arrays can be _sharded_ across multiple devices for parallel computation.


The default array implementation in JAX is [`jax.Array`](https://docs.jax.dev/en/latest/_autosummary/jax.Array.html#jax.Array). In many ways it is similar to the [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray) type that you may be familiar with from the NumPy package, but it has some important differences.
### Array creation[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#array-creation "Link to this heading")
We typically don’t call the `jax.Array` constructor directly, but rather create arrays via JAX API functions. For example, [`jax.numpy`](https://docs.jax.dev/en/latest/jax.numpy.html#module-jax.numpy) provides familiar NumPy-style array construction functionality such as `jax.numpy.zeros`, `jax.numpy.linspace`, `jax.numpy.arange`, etc.

```
import jax
import jax.numpy as jnp

x = jnp.arange(5)
isinstance(x, jax.Array)

```
Copy to clipboard

```
True

```
Copy to clipboard
If you use Python type annotations in your code, `jax.Array` is the appropriate annotation for jax array objects (see [`jax.typing`](https://docs.jax.dev/en/latest/jax.typing.html#module-jax.typing) for more discussion).
### Array devices and sharding[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#array-devices-and-sharding "Link to this heading")
JAX Array objects have a `devices` method that lets you inspect where the contents of the array are stored. In the simplest cases, this will be a single CPU device:

```
x.devices()

```
Copy to clipboard

```
{CpuDevice(id=0)}

```
Copy to clipboard
In general, an array may be [_sharded_](https://docs.jax.dev/en/latest/parallel.html) across multiple devices, in a manner that can be inspected via the `sharding` attribute:

```
x.sharding

```
Copy to clipboard

```
SingleDeviceSharding(device=CpuDevice(id=0), memory_kind=device)

```
Copy to clipboard
Here the array is on a single device, but in general a JAX array can be sharded across multiple devices, or even multiple hosts. To read more about sharded arrays and parallel computation, refer to [Introduction to parallel programming](https://docs.jax.dev/en/latest/parallel.html).
## Just-in-time compilation with `jax.jit`[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#just-in-time-compilation-with-jax-jit "Link to this heading")
**Key concepts:**
  * By default JAX executes operations one at a time, in sequence.
  * Using a just-in-time (JIT) compilation decorator, sequences of operations can be optimized together and run at once.
  * Not all JAX code can be JIT compiled, as it requires array shapes to be static & known at compile time.


JAX runs transparently on the GPU or TPU (falling back to CPU if you don’t have one), with all JAX operations being expressed in terms of XLA. If we have a sequence of operations, we can use the [`jax.jit`](https://docs.jax.dev/en/latest/_autosummary/jax.jit.html) function to compile this sequence of operations together using the XLA compiler.
For example, consider this function that normalizes the rows of a 2D matrix, expressed in terms of `jax.numpy` operations:

```
import jax.numpy as jnp

def norm(X):
  X = X - X.mean(0)
  return X / X.std(0)

```
Copy to clipboard
A just-in-time compiled version of the function can be created using the `jax.jit` transform:

```
from jax import jit
norm_compiled = jit(norm)

```
Copy to clipboard
This function returns the same results as the original, up to standard floating-point accuracy:

```
np.random.seed(1701)
X = jnp.array(np.random.rand(10000, 10))
np.allclose(norm(X), norm_compiled(X), atol=1E-6)

```
Copy to clipboard

```
True

```
Copy to clipboard
But due to the compilation (which includes fusing of operations, avoidance of allocating temporary arrays, and a host of other tricks), execution times can be orders of magnitude faster in the JIT-compiled case. We can use IPython’s `%timeit` to quickly benchmark our function, using `block_until_ready()` to account for JAX’s [asynchronous dispatch](https://docs.jax.dev/en/latest/async_dispatch.html):

```
%timeit norm(X).block_until_ready()
%timeit norm_compiled(X).block_until_ready()

```
Copy to clipboard

```
431 μs ± 4.6 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
311 μs ± 1.25 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

```
Copy to clipboard
That said, `jax.jit` does have limitations: in particular, it requires all arrays to have static shapes. That means that some JAX operations are incompatible with JIT compilation.
For example, this operation can be executed in op-by-op mode:

```
def get_negatives(x):
  return x[x < 0]

x = jnp.array(np.random.randn(10))
get_negatives(x)

```
Copy to clipboard

```
Array([-0.10570311, -0.59403396, -0.8680282 , -0.23489487], dtype=float32)

```
Copy to clipboard
But it returns an error if you attempt to execute it in jit mode:

```
jit(get_negatives)(x)

```
Copy to clipboard

```
NonConcreteBooleanIndexError: Array boolean indices must be concrete; got bool[10]

See https://docs.jax.dev/en/latest/101/errors.html#jax.errors.NonConcreteBooleanIndexError

```
Copy to clipboard
This is because the function generates an array whose shape is not known at compile time: the size of the output depends on the values of the input array, and so it is not compatible with JIT.
For more on JIT compilation in JAX, check out [Just-in-time compilation](https://docs.jax.dev/en/latest/jit-compilation.html).
## Taking derivatives with `jax.grad`[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#taking-derivatives-with-jax-grad "Link to this heading")
**Key concepts:**
  * JAX provides automatic differentiation via the `jax.grad` transformation.
  * The `jax.grad` and `jax.jit` transformations compose and can be mixed arbitrarily.


In addition to transforming functions via JIT compilation, JAX also provides other transformations. One such transformation is [`jax.grad`](https://docs.jax.dev/en/latest/_autosummary/jax.grad.html), which performs [automatic differentiation (autodiff)](https://en.wikipedia.org/wiki/Automatic_differentiation):

```
from jax import grad

def sum_logistic(x):
  return jnp.sum(1.0 / (1.0 + jnp.exp(-x)))

x_small = jnp.arange(3.)
derivative_fn = grad(sum_logistic)
print(derivative_fn(x_small))

```
Copy to clipboard

```
[0.25       0.19661197 0.10499357]

```
Copy to clipboard
Let’s verify with finite differences that our result is correct.

```
def first_finite_differences(f, x, eps=1E-3):
  return jnp.array([(f(x + eps * v) - f(x - eps * v)) / (2 * eps)
                   for v in jnp.eye(len(x))])

print(first_finite_differences(sum_logistic, x_small))

```
Copy to clipboard

```
[0.24998187 0.1964569  0.10502338]

```
Copy to clipboard
The [`jax.grad`](https://docs.jax.dev/en/latest/_autosummary/jax.grad.html) and [`jax.jit`](https://docs.jax.dev/en/latest/_autosummary/jax.jit.html) transformations compose and can be mixed arbitrarily. For instance, while the `sum_logistic` function was differentiated directly in the previous example, it could also be JIT-compiled, and these operations can be combined. We can go further:

```
print(grad(jit(grad(jit(grad(sum_logistic)))))(1.0))

```
Copy to clipboard

```
-0.0353256

```
Copy to clipboard
Beyond scalar-valued functions, the [`jax.jacobian`](https://docs.jax.dev/en/latest/_autosummary/jax.jacobian.html) transformation can be used to compute the full Jacobian matrix for vector-valued functions:

```
from jax import jacobian
print(jacobian(jnp.exp)(x_small))

```
Copy to clipboard

```
[[1.        0.        0.       ]
 [0.        2.7182817 0.       ]
 [0.        0.        7.389056 ]]

```
Copy to clipboard
For more advanced autodiff operations, you can use [`jax.vjp`](https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html) for reverse-mode vector-Jacobian products, and [`jax.jvp`](https://docs.jax.dev/en/latest/_autosummary/jax.jvp.html) and [`jax.linearize`](https://docs.jax.dev/en/latest/_autosummary/jax.linearize.html) for forward-mode Jacobian-vector products. The two can be composed arbitrarily with one another, and with other JAX transformations. For example, `jax.jvp` and `jax.vjp` are used to define the forward-mode [`jax.jacfwd`](https://docs.jax.dev/en/latest/_autosummary/jax.jacfwd.html) and reverse-mode [`jax.jacrev`](https://docs.jax.dev/en/latest/_autosummary/jax.jacrev.html) for computing Jacobians in forward- and reverse-mode, respectively. Here’s one way to compose them to make a function that efficiently computes full Hessian matrices:

```
from jax import jacfwd, jacrev
def hessian(fun):
  return jit(jacfwd(jacrev(fun)))
print(hessian(sum_logistic)(x_small))

```
Copy to clipboard

```
[[-0.         -0.         -0.        ]
 [-0.         -0.09085776 -0.        ]
 [-0.         -0.         -0.07996249]]

```
Copy to clipboard
This kind of composition produces efficient code in practice; this is more-or-less how JAX’s built-in [`jax.hessian`](https://docs.jax.dev/en/latest/_autosummary/jax.hessian.html) function is implemented.
For more on automatic differentiation in JAX, check out [Automatic differentiation](https://docs.jax.dev/en/latest/automatic-differentiation.html).
## Auto-vectorization with `jax.vmap`[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#auto-vectorization-with-jax-vmap "Link to this heading")
**Key concepts:**
  * JAX provides automatic vectorization via the [`jax.vmap`](https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html) transformation.
  * `jax.vmap` can be composed with `jax.jit` to produce efficient vectorized code.


Another useful transformation is [`jax.vmap`](https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html), the vectorizing map. It has the familiar semantics of mapping a function along array axes, but instead of explicitly looping over function calls, it transforms the function into a natively vectorized version for better performance. When composed with [`jax.jit`](https://docs.jax.dev/en/latest/_autosummary/jax.jit.html), it can be just as performant as manually rewriting your function to operate over an extra batch dimension.
We’re going to work with a simple example, and promote matrix-vector products into matrix-matrix products using [`jax.vmap`](https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html). Although this is easy to do by hand in this specific case, the same technique can apply to more complicated functions.

```
from jax import random

key = random.key(1701)
key1, key2 = random.split(key)
mat = random.normal(key1, (150, 100))
batched_x = random.normal(key2, (10, 100))

def apply_matrix(x):
  return jnp.dot(mat, x)

```
Copy to clipboard
The `apply_matrix` function maps a vector to a vector, but we may want to apply it row-wise across a matrix. We could do this by looping over the batch dimension in Python, but this usually results in poor performance.

```
def naively_batched_apply_matrix(v_batched):
  return jnp.stack([apply_matrix(v) for v in v_batched])

print('Naively batched')
%timeit naively_batched_apply_matrix(batched_x).block_until_ready()

```
Copy to clipboard

```
Naively batched
429 μs ± 1.03 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

```
Copy to clipboard
A programmer familiar with the `jnp.dot` function might recognize that `apply_matrix` can be rewritten to avoid explicit looping, using the built-in batching semantics of `jnp.dot`:

```
import numpy as np

@jit
def batched_apply_matrix(batched_x):
  return jnp.dot(batched_x, mat.T)

np.testing.assert_allclose(naively_batched_apply_matrix(batched_x),
                           batched_apply_matrix(batched_x), atol=1E-4, rtol=1E-4)
print('Manually batched')
%timeit batched_apply_matrix(batched_x).block_until_ready()

```
Copy to clipboard

```
Manually batched
32 μs ± 286 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

```
Copy to clipboard
However, as functions become more complicated, this kind of manual batching becomes more difficult and error-prone. The `jax.vmap` transformation is designed to automatically transform a function into a batch-aware version:

```
from jax import vmap

@jit
def vmap_batched_apply_matrix(batched_x):
  return vmap(apply_matrix)(batched_x)

np.testing.assert_allclose(naively_batched_apply_matrix(batched_x),
                           vmap_batched_apply_matrix(batched_x), atol=1E-4, rtol=1E-4)
print('Auto-vectorized with vmap')
%timeit vmap_batched_apply_matrix(batched_x).block_until_ready()

```
Copy to clipboard

```
Auto-vectorized with vmap
46.7 μs ± 159 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

```
Copy to clipboard
As you would expect, `jax.vmap` can be arbitrarily composed with `jax.jit`, `jax.grad`, and any other JAX transformation.
For more on automatic vectorization in JAX, check out [Automatic vectorization](https://docs.jax.dev/en/latest/automatic-vectorization.html).
## Pseudorandom numbers[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#pseudorandom-numbers "Link to this heading")
**Key concepts:**
  * JAX uses a different model for pseudo random number generation than NumPy.
  * JAX random functions consume a random `key` that must be split to generate new independent keys.
  * JAX’s random key model is thread-safe and avoids issues with global state.


Generally, JAX strives to be compatible with NumPy, but pseudo random number generation is a notable exception. NumPy supports a method of pseudo random number generation that is based on a global `state`, which can be set using [`numpy.random.seed`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html). Global random state interacts poorly with JAX’s compute model and makes it difficult to enforce reproducibility across different threads, processes, and devices. JAX instead tracks state explicitly via a random `key`:

```
from jax import random

key = random.key(43)
print(key)

```
Copy to clipboard

```
Array((), dtype=key<fry>) overlaying:
[ 0 43]

```
Copy to clipboard
The key is effectively a stand-in for NumPy’s hidden state object, but we pass it explicitly to [`jax.random`](https://docs.jax.dev/en/latest/jax.random.html) functions. Importantly, random functions consume the key, but do not modify it: feeding the same key object to a random function will always result in the same sample being generated.

```
print(random.normal(key))
print(random.normal(key))

```
Copy to clipboard

```
0.07520543
0.07520543

```
Copy to clipboard
**The rule of thumb is: never reuse keys (unless you want identical outputs).**
In order to generate different and independent samples, you must [`jax.random.split`](https://docs.jax.dev/en/latest/_autosummary/jax.random.split.html) the key explicitly before passing it to a random function:

```
for i in range(3):
  new_key, subkey = random.split(key)
  del key  # The old key is consumed by split() -- we must never use it again.

  val = random.normal(subkey)
  del subkey  # The subkey is consumed by normal().

  print(f"draw {i}: {val}")
  key = new_key  # new_key is safe to use in the next iteration.

```
Copy to clipboard

```
draw 0: -1.9133632183074951
draw 1: -1.4749839305877686
draw 2: -0.36703771352767944

```
Copy to clipboard
Note that this code is thread safe, since the local random state eliminates possible race conditions involving global state. `jax.random.split` is a deterministic function that converts one `key` into several independent (in the pseudorandomness sense) keys.
For more on pseudo random numbers in JAX, see the [Pseudorandom numbers tutorial](https://docs.jax.dev/en/latest/random-numbers.html).
## Debugging[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#debugging "Link to this heading")
Debugging JAX code can be challenging due to its functional programming model and the fact that JAX code is often transformed via JIT compilation or vectorization. However, JAX provides several tools to help with debugging.
###  `jax.debug.print`[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-debug-print "Link to this heading")
For simple inspection, use [`jax.debug.print`](https://docs.jax.dev/en/latest/_autosummary/jax.debug.print.html).
Python’s built-in `print` executes at trace-time, before the runtime values exist. Because of this, `print` will only show tracer values within `jax.jit`-decorated code.

```
import jax
import jax.numpy as jnp

@jax.jit
def f(x):
  print("print(x) ->", x)
  y = jnp.sin(x)
  print("print(y) ->", y)
  return y

result = f(2.)

```
Copy to clipboard

```
print(x) -> JitTracer(~float32[])
print(y) -> JitTracer(~float32[])

```
Copy to clipboard
If you want to print the actual runtime values, you can use `jax.debug.print`:

```
@jax.jit
def f(x):
  jax.debug.print("jax.debug.print(x) -> {x}", x=x)
  y = jnp.sin(x)
  jax.debug.print("jax.debug.print(y) -> {y}", y=y)
  return y

result = f(2.)

```
Copy to clipboard

```
jax.debug.print(x) -> 2.0
jax.debug.print(y) -> 0.9092974066734314

```
Copy to clipboard
### Debugging flags[#](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#debugging-flags "Link to this heading")
JAX offers flags and context managers that enable catching errors more easily. For example, you can enable the `jax.debug_nans` flag to automatically detect when NaNs are produced in `jax.jit`-compiled code. You can also enable the `jax_disable_jit` flag to disable JIT-compilation, enabling use of traditional Python debugging tools like `print` and `pdb`.
For more details, see [Introduction to debugging](https://docs.jax.dev/en/latest/debugging.html).
* * *
This is just a taste of what JAX can do. We’re really excited to see what you do with it!
Contents 
  * [Installation](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#installation)
  * [JAX vs. NumPy](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-vs-numpy)
  * [JAX arrays (`jax.Array`)](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-arrays-jax-array)
    * [Array creation](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#array-creation)
    * [Array devices and sharding](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#array-devices-and-sharding)
  * [Just-in-time compilation with `jax.jit`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#just-in-time-compilation-with-jax-jit)
  * [Taking derivatives with `jax.grad`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#taking-derivatives-with-jax-grad)
  * [Auto-vectorization with `jax.vmap`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#auto-vectorization-with-jax-vmap)
  * [Pseudorandom numbers](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#pseudorandom-numbers)
  * [Debugging](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#debugging)
    * [`jax.debug.print`](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#jax-debug-print)
    * [Debugging flags](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#debugging-flags)


By The JAX authors 
© Copyright 2024, The JAX Authors.