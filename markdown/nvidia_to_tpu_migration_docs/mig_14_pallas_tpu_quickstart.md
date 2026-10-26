---
id: "mig_14_pallas_tpu_quickstart"
title: "Pallas TPU kernel quickstart"
url: "https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html"
category: "Nvidia to tpu migration docs"
description: "Write custom TPU kernels using Pallas; relevant when replacing CUDA-specific kernels."
crawled_at: "2026-10-26T12:48:12.573624+00:00"
crawler_engine: "Crawl4AI"
---

[Skip to main content](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#main-content)
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
  * [Pallas: a JAX kernel language](https://docs.jax.dev/en/latest/pallas/index.html)
  * [Pallas TPU](https://docs.jax.dev/en/latest/pallas/tpu/index.html)
  * Quickstart: TPU


[ ](https://github.com/jax-ml/jax)
  * [ .ipynb ](https://docs.jax.dev/en/latest/_sources/pallas/tpu/quickstart.ipynb)
  * .pdf


Light Dark System Settings
# Quickstart: TPU
##  Contents 
  * [TPU memory spaces](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#tpu-memory-spaces)
  * [Your first kernel](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#your-first-kernel)
    * [Distributing work across TensorCores](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#distributing-work-across-tensorcores)
  * [Making it fast: pipelining](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#making-it-fast-pipelining)
  * [What’s next](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#what-s-next)


# Quickstart: TPU[#](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#quickstart-tpu "Link to this heading")
This quickstart covers the basics of writing Pallas kernels for TPU: memory spaces, `pl.kernel`, and pipelining.

```
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

```
Copy to clipboard
## TPU memory spaces[#](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#tpu-memory-spaces "Link to this heading")
Pallas kernels interact with memory through **Refs** – JAX’s mutable array references. On TPU, each Ref lives in a specific **memory space** :
  * **HBM** : large but slow. Kernel inputs and outputs live here.
  * **VMEM** : small but fast. Computation happens here.


You can’t compute directly on HBM Refs. Data has to be copied to VMEM first, and results copied back.
## Your first kernel[#](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#your-first-kernel "Link to this heading")
Here’s a kernel that fills an output array with a constant. We allocate a temporary VMEM buffer, write the constant there, and copy it to the output HBM Ref.

```
@pl.kernel(
    out_type=jax.ShapeDtypeStruct((128,), jnp.float32),
    mesh=pltpu.TensorCoreMesh(axis_name='core'),
    scratch_types=dict(o_vmem=pltpu.VMEM((128,), jnp.float32)),
)
def fill_42(o_ref, o_vmem):
  # Compute in VMEM
  o_vmem[...] = jnp.full_like(o_vmem, 42.0)

  # VMEM → HBM (blocks until the transfer completes)
  pltpu.sync_copy(o_vmem, o_ref)

result = fill_42()  # [42.0, 42.0, ...]

```
Copy to clipboard
`pl.kernel` wraps a kernel function to make it callable with standard JAX arrays. It handles allocating the necessary Refs and executing the kernel on-device:
  * `out_type` allocates an output Ref in HBM for the result.
  * `scratch_types` allocates the VMEM buffers (like `o_vmem`) that get passed as extra arguments to the kernel.


Note
If your chip has multiple TensorCores (e.g. TPU v5p has 2), the kernel runs on all of them. As written, both cores will redundantly perform the exact same computation. In a real kernel, you would distribute work across cores either manually or by using pipelining.
### Distributing work across TensorCores[#](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#distributing-work-across-tensorcores "Link to this heading")
To process a larger array, we can distribute work across multiple TensorCores manually. Each core runs a separate invocation of the kernel.

```
def iota() -> jax.Array:
  tpu_info = pltpu.get_tpu_info()

  @pl.kernel(
      out_type=jax.ShapeDtypeStruct((128 * tpu_info.num_cores,), jnp.float32),
      mesh=pltpu.TensorCoreMesh(axis_name='core'),
      scratch_types=dict(o_vmem=pltpu.VMEM((128,), jnp.float32)),
  )
  def kernel(o_ref, o_vmem):
    i = jax.lax.axis_index('core')

    # Compute our chunk in VMEM
    o_vmem[...] = jnp.arange(128, dtype=jnp.float32) + i * 128

    # Copy back to our slice of HBM
    pltpu.sync_copy(o_vmem, o_ref.at[pl.ds(i * 128, 128)])

  return kernel()

result = iota()  # [0.0, 1.0, 2.0, ...]

```
Copy to clipboard
`jax.lax.axis_index('core')` tells you which TensorCore you’re on – use it to determine your slice of the output.
## Making it fast: pipelining[#](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#making-it-fast-pipelining "Link to this heading")
The examples above work, but are inefficient. They copy data in, compute, then copy out – each `sync_copy` blocks until the transfer completes. The TensorCores sit idle while memory is moving, and vice versa.
**Pipelining** fixes this by breaking the work into blocks and overlapping memory transfers with compute. While the TensorCores process block N, the DMA engine is already fetching block N+1.
`pltpu.emit_pipeline` handles the double-buffering machinery for you. It takes:
  * A **grid** : how many pipeline blocks to process.
  * **`BlockSpec`s** : how to slice the arrays into blocks.
  * A **body** function: the computation to run for each block.


Here’s an elementwise addition kernel using pipelining:

```
def add_matrices_pipelined(x: jax.Array, y: jax.Array) -> jax.Array:
  @pl.kernel(
      out_type=jax.ShapeDtypeStruct.like(x),
      mesh=pltpu.TensorCoreMesh(axis_name='core'),
  )
  def kernel(x_hbm, y_hbm, o_hbm):
    def add_body(x_vmem, y_vmem, o_vmem):
      o_vmem[...] = x_vmem[...] + y_vmem[...]

    pltpu.emit_pipeline(
        add_body,
        grid=(x_hbm.shape[0] // 128, x_hbm.shape[1] // 128),
        in_specs=[
            pl.BlockSpec((128, 128), lambda i, j: (i, j)),
            pl.BlockSpec((128, 128), lambda i, j: (i, j)),
        ],
        out_specs=pl.BlockSpec((128, 128), lambda i, j: (i, j)),
        core_axis_name='core',
        dimension_semantics=(pltpu.PARALLEL, pltpu.ARBITRARY),
    )(x_hbm, y_hbm, o_hbm)
  return kernel(x, y)

x = 2 * jnp.ones((256, 256))
y = 3 * jnp.ones((256, 256))
add_matrices_pipelined(x, y)
# Array([[5., 5., 5., ..., 5., 5., 5.],
#        [5., 5., 5., ..., 5., 5., 5.],
#        [5., 5., 5., ..., 5., 5., 5.],
#        ...,
#        [5., 5., 5., ..., 5., 5., 5.],
#        [5., 5., 5., ..., 5., 5., 5.],
#        [5., 5., 5., ..., 5., 5., 5.]], dtype=float32)

```
Copy to clipboard
Notice the body is just the compute – no `sync_copy`, no scratch allocation. `emit_pipeline` takes care of the memory movement and buffer management.
We also passed `core_axis_name='core'` and `dimension_semantics`. This tells the pipeline how to map the grid to the hardware:
  * `pltpu.PARALLEL` means the first dimension of the grid is distributed across the TensorCores, splitting the work automatically.
  * `pltpu.ARBITRARY` indicates that Pallas cannot make assumptions about data independence along this dimension; it therefore cannot be parallelized across cores and is instead executed sequentially on a single core.


## What’s next[#](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#what-s-next "Link to this heading")
  * [TPU Details](https://docs.jax.dev/en/latest/pallas/tpu/details.html) – the full picture of TPU memory spaces and supported ops
  * [TPU Pipelining](https://docs.jax.dev/en/latest/pallas/tpu/pipelining.html) – deeper dive into pipelining, reductions, and accumulation
  * [Matrix Multiplication](https://docs.jax.dev/en/latest/pallas/tpu/matmul.html) – putting it all together in a full kernel


[ previous Pallas TPU ](https://docs.jax.dev/en/latest/pallas/tpu/index.html "previous page") [ next Writing TPU kernels with Pallas ](https://docs.jax.dev/en/latest/pallas/tpu/details.html "next page")
Contents 
  * [TPU memory spaces](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#tpu-memory-spaces)
  * [Your first kernel](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#your-first-kernel)
    * [Distributing work across TensorCores](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#distributing-work-across-tensorcores)
  * [Making it fast: pipelining](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#making-it-fast-pipelining)
  * [What’s next](https://docs.jax.dev/en/latest/pallas/tpu/quickstart.html#what-s-next)


By The JAX authors 
© Copyright 2024, The JAX Authors.