---
id: "infer_05_vllm_torchtpu_supported_models"
title: "vLLM-TorchTPU supported models and features"
url: "https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/"
category: "inference_deployment_links"
description: "Check validated checkpoints, attention backends, quantization, and serving feature support."
crawled_at: "2026-10-26T14:43:56.622197+00:00"
crawler_engine: "Crawl4AI+MkDocsSphinxCleaner"
---

# Supported Models & Features
`vllm-torchtpu` executes models through vLLM's native PyTorch model runner (`TPUModelRunner`) compiled with `torch.compile(backend="tpu")`, paired with custom JAX/Pallas kernels for attention, Mixture-of-Experts (MoE), and quantized matrix multiplication.
This page has two sections:
  * [Validated Models](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/#validated-models) — Models running on TPU, which checkpoints are tested, and in which way.
  * [Feature Support](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/#feature-support) — Supported features, how to turn them on, and which models they have been validated with.


Both tables describe what is supported **today**. For planned models and features, see the [Roadmap](https://vllm-torchtpu.readthedocs.io/en/latest/roadmap/).
Validation levels used in both tables:  
| Level  | Meaning  |  
| --- | --- |  
| ✅ **CI**  | Runs on every pull request (performance / accuracy evaluation or integration pipeline on TPU v7x)  |  
| 🌙 **Nightly**  | Runs in the scheduled nightly pipeline  |  
| 🧪 **Tests**  | Covered by unit, kernel, or component tests only (no end-to-end serving run in CI)  |  
| 📝 **Example**  | Example script, benchmark config, or recipe exists but is not scheduled in CI  |  
* * *
## Validated Models
Click a family to see its architecture-specific TPU support.  
| Family  | Validated checkpoints  | Architecture-specific TPU support  |  
| --- | --- | --- |  
|  **Qwen3.5**  
hybrid GDN + full attention, MoE, MTP heads  | 
  * 🌙 `Qwen/Qwen3.5-397B-A17B-FP8`
  * ✅ `Qwen/Qwen3.5-35B-A3B-FP8`
  * ✅ `Qwen/Qwen3.5-4B` (MTP tests)

 | Gated DeltaNet chunked-prefill and recurrent-decode Pallas kernels; unified KV block pool shared by GDN state and full-attention KV; native MTP drafting  |  
|  Architecture-specific TPU supportGated DeltaNet chunked-prefill and recurrent-decode Pallas kernels; unified KV block pool shared by GDN state and full-attention KV; native MTP drafting |  
|  **Kimi-Linear**  
hybrid KDA + MLA  | 
  * 🧪 `Kimi-Linear-48B`

 | Kimi Delta Attention kernels (fused conv1d + delta rule) with pooled KDA state  |  
|  Architecture-specific TPU supportKimi Delta Attention kernels (fused conv1d + delta rule) with pooled KDA state |  
|  **Qwen3 / Qwen3-Coder**  
dense and MoE  | 
  * 🌙 `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
  * ✅ `Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8`
  * ✅ `nvidia/Qwen3-30B-A3B-NVFP4`
  * ✅ `Qwen/Qwen3-0.6B`
  * ✅ `Qwen/Qwen3-4B` (DFlash / DSpark tests)
  * 📝 `nvidia/Qwen3-Coder-480B-A35B-Instruct-NVFP4`

 | Reference dense / MoE path: Ragged Paged Attention v3, fused EP MoE (GMM / SparseCore), FP8 and NVFP4 checkpoints  |  
|  Architecture-specific TPU supportReference dense / MoE path: Ragged Paged Attention v3, fused EP MoE (GMM / SparseCore), FP8 and NVFP4 checkpoints |  
|  **DeepSeek-V2 / V4**  
MLA, sparse attention, MoE  | 
  * 🌙 `deepseek-ai/DeepSeek-V4-Pro-0813`
  * 🌙 `deepseek-ai/DeepSeek-V4-Flash`
  * ✅ `deepseek-ai/DeepSeek-V2`

 | Dedicated DeepSeek-V4 model implementation; Sparse MLA with SparseCore top-k selection and `sparsecore` / `tc` KV layouts; `deepseek_v4_fp8` FP8 + W4A8 MoE path; DSpark drafting  |  
|  Architecture-specific TPU supportDedicated DeepSeek-V4 model implementation; Sparse MLA with SparseCore top-k selection and `sparsecore` / `tc` KV layouts; `deepseek_v4_fp8` FP8 + W4A8 MoE path; DSpark drafting |  
|  **Kimi-K2.6 / K3**  
MLA; K3 adds KDA layers and the MoonViT vision tower  | 
  * ✅ `moonshotai/Kimi-K3` (expert-pruned variant in PR CI, full model in on-demand v7x-32 sweeps)
  * 🌙 `moonshotai/Kimi-K2.6`

 | Dedicated Kimi-K3 implementation (MLA + KDA layers, MoonViT encoder); W4A16 Kimi-K2.6; DSpark drafting  |  
|  Architecture-specific TPU supportDedicated Kimi-K3 implementation (MLA + KDA layers, MoonViT encoder); W4A16 Kimi-K2.6; DSpark drafting |  
|  **GLM-5.2**  
MLA, MoE  | 
  * 🌙 `zai-org/GLM-5.2-FP8`
  * 🌙 `nvidia/GLM-5.2-NVFP4`

 | Calibrated MLA kernel dispatch profile for the GLM-5.2 geometry; NVFP4 MoE with host KV offload  |  
|  Architecture-specific TPU supportCalibrated MLA kernel dispatch profile for the GLM-5.2 geometry; NVFP4 MoE with host KV offload |  
|  **Gemma 4**  
dense 31B and MoE 26B-A4B, multimodal, hybrid sliding-window attention  | 
  * ✅ `RedHatAI/gemma-4-31B-it-FP8-Dynamic`
  * ✅ `RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic`
  * 🧪 `google/gemma-4-31B-it`

 | Sliding-window / global hybrid attention page sizing; multimodal path with MMMU-Pro accuracy baselines  |  
|  Architecture-specific TPU supportSliding-window / global hybrid attention page sizing; multimodal path with MMMU-Pro accuracy baselines |  
|  **Llama 3.x**  
dense  | 
  * ✅ `meta-llama/Llama-3.1-8B-Instruct` (EAGLE-3 tests)
  * 📝 `meta-llama/Llama-3.2-1B-Instruct`

 | Reference dense path; EAGLE-3 drafting with `yuhuili/EAGLE3-LLaMA3.1-Instruct-8B`  |  
|  Architecture-specific TPU supportReference dense path; EAGLE-3 drafting with `yuhuili/EAGLE3-LLaMA3.1-Instruct-8B`  |  
|  **Qwen2.5-VL / Qwen3-VL**  
vision-language  | 
  * ✅ `Qwen/Qwen2.5-VL-3B-Instruct`
  * 📝 `Qwen/Qwen2.5-VL-7B-Instruct`
  * 🧪 `Qwen/Qwen3-VL-4B`

 | 3D M-RoPE, vision-encoder attention patches, multimodal encoder manager with video frame chunking  |  
|  Architecture-specific TPU support3D M-RoPE, vision-encoder attention patches, multimodal encoder manager with video frame chunking |  
| **Embedding & safety classifiers**  | 
  * 📝 `Qwen/Qwen3-VL-Embedding-8B`
  * 📝 `meta-llama/Llama-Guard-4-12B`

 | TPU-native on-device pooling with request bucketing and static compilation; safety classification on the AILuminate prompt set  |  
|  Architecture-specific TPU supportTPU-native on-device pooling with request bucketing and static compilation; safety classification on the AILuminate prompt set |  
See the [TPU v7x serving recipes](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/) for the exact slice topologies, parallelism layouts, and `vllm serve` flags used for the CI checkpoints. The [TPU v6e serving recipes](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v6e_recipes/) are reference configurations that are not run in CI.
* * *
## Feature Support
All features below are merged in `main`. "Validated with" lists the models and validation level behind each feature; a model missing from a row means the combination has not been run in CI, not that it is unsupported. Click a feature to see how to enable it.  
| Feature  | How to enable  | Validated with  | Guide  |  
| --- | --- | --- | --- |  
| **Ragged Paged Attention (RPA v3)**  | Default attention backend for MHA / GQA (`--attention-backend CUSTOM` in the recipes); `VLLM_TPU_BLOCK_MAJOR_KV=1` for the block-major KV layout, `USE_RPA_PIPELINED_DMA_STAGING=1`  | 
  * Every text model in CI, with `bf16` and `fp8` KV cache

 | [Env vars](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/)  |  
|  How to enableDefault attention backend for MHA / GQA (`--attention-backend CUSTOM` in the recipes); `VLLM_TPU_BLOCK_MAJOR_KV=1` for the block-major KV layout, `USE_RPA_PIPELINED_DMA_STAGING=1`  |  
| **Multi-head Latent Attention (MLA)**  | Automatic for MLA architectures; `TPU_SPARSE_MLA_NOPE_LAYOUT` / `TPU_SPARSE_MLA_ROPE_LAYOUT`, `TPU_LATENT_PROJ_INTRA_CHIP_TP`, `TPU_MLA_MASKED_DENSE_ENABLED`  | 
  * ✅ DeepSeek-V2
  * 🌙 DeepSeek-V4
  * ✅ Kimi-K3
  * 🌙 GLM-5.2

 | —  |  
|  How to enableAutomatic for MLA architectures; `TPU_SPARSE_MLA_NOPE_LAYOUT` / `TPU_SPARSE_MLA_ROPE_LAYOUT`, `TPU_LATENT_PROJ_INTRA_CHIP_TP`, `TPU_MLA_MASKED_DENSE_ENABLED`  |  
| **Hybrid linear attention (GDN / KDA)**  | Automatic for hybrid architectures; `TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL=1` shares one block pool between linear-attention state and KV cache  | 
  * ✅ Qwen3.5-35B
  * 🌙 Qwen3.5-397B
  * ✅ Kimi-K3
  * 🧪 Kimi-Linear

 | —  |  
|  How to enableAutomatic for hybrid architectures; `TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL=1` shares one block pool between linear-attention state and KV cache |  
| **Tensor / Data / Expert parallelism**  |  `--tensor-parallel-size`, `--data-parallel-size`, `--enable-expert-parallel`; `TPU_MOE_HIERARCHICAL_EP=1` on dual-core TPU v7x  | 
  * Every CI recipe, from `TP=1, DP=8 + EP` to `TP=32 + EP`

 | [Parallelism](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)  |  
|  How to enable`--tensor-parallel-size`, `--data-parallel-size`, `--enable-expert-parallel`; `TPU_MOE_HIERARCHICAL_EP=1` on dual-core TPU v7x |  
| **Pipeline & context parallelism (PP, PCP, DCP)**  |  `--pipeline-parallel-size`, `--prefill-context-parallel-size`, `--decode-context-parallel-size`; `TPU_PP_DYNAMIC_CHUNKS`, `TPU_PCP_TOPOLOGY_AWARE_MESH`, `TPU_DCP_LSE_MERGE_A2A`  | 
  * PCP + DCP:
    * ✅ Qwen3.5 (PCP4 / DP4 and PCP4-TP1 to TP4-DCP2 disaggregated correctness tests)
  * 🧪 PP:
    * 🌙 Qwen3.5 (PP4 / DP4 disaggregated with host offload)

 | [Parallelism](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)  |  
|  How to enable`--pipeline-parallel-size`, `--prefill-context-parallel-size`, `--decode-context-parallel-size`; `TPU_PP_DYNAMIC_CHUNKS`, `TPU_PCP_TOPOLOGY_AWARE_MESH`, `TPU_DCP_LSE_MERGE_A2A`  |  
| **Multi-host serving**  |  `mp` backend (`--nnodes`, or multi-host `--data-parallel-size`) or `TPU_MULTIHOST_BACKEND=ray`  | 
  * ✅ Qwen3-0.6B (v7x-16 presubmit)
  * 🌙 GLM-5.2 (v7x-16)
  * 🌙 DeepSeek-V4-Pro (v7x-16)
  * Kimi-K3 (on-demand v7x-32)

 | [Multi-Host Serving](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)  |  
|  How to enable`mp` backend (`--nnodes`, or multi-host `--data-parallel-size`) or `TPU_MULTIHOST_BACKEND=ray`  |  
| **Quantization**  | Auto-detected from the checkpoint, or `--quantization fp8`, `compressed-tensors`, `mxfp4`, `nvfp4`, `awq`, `gptq`, `deepseek_v4_fp8`, `online_fp8`; `--kv-cache-dtype fp8`; load-time requantization via `REQUANTIZE_*` / `MOE_REQUANTIZE_*`  | 
  * FP8 weights + KV:
    * ✅ Qwen3-Coder-30B
    * 🌙 Qwen3-Coder-480B
    * ✅ Qwen3.5-35B
    * 🌙 Qwen3.5-397B
    * 🌙 GLM-5.2
    * ✅ Kimi-K3
    * ✅ Gemma 4
  * NVFP4:
    * ✅ Qwen3-30B
    * 🌙 GLM-5.2
  * W4A16:
    * 🌙 Kimi-K2.6
  * `deepseek_v4_fp8` (W4A8 MoE):
    * 🌙 DeepSeek-V4

 | [Quantization](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/quantization/)  |  
|  How to enableAuto-detected from the checkpoint, or `--quantization fp8`, `compressed-tensors`, `mxfp4`, `nvfp4`, `awq`, `gptq`, `deepseek_v4_fp8`, `online_fp8`; `--kv-cache-dtype fp8`; load-time requantization via `REQUANTIZE_*` / `MOE_REQUANTIZE_*`  |  
| **Automatic prefix caching**  |  `--enable-prefix-caching` (with prefix-aware request scheduling, `PrefixAwareScheduler`)  | 
  * ✅ Qwen3.5
  * ✅ Kimi-K3 (including hybrid KDA state)

 | —  |  
|  How to enable`--enable-prefix-caching` (with prefix-aware request scheduling, `PrefixAwareScheduler`) |  
| **Chunked prefill & async scheduling**  |  `--max-num-batched-tokens`, `--async-scheduling`; `TPU_TOKEN_BUCKET_EXTRA` / `TPU_TOKEN_BUCKET_LINEAR`, `DP_SCHED_ENABLED`  | 
  * Every CI recipe

 | [v7x recipes](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/)  |  
|  How to enable`--max-num-batched-tokens`, `--async-scheduling`; `TPU_TOKEN_BUCKET_EXTRA` / `TPU_TOKEN_BUCKET_LINEAR`, `DP_SCHED_ENABLED`  |  
| **KV cache offloading**  | `--kv-transfer-config '{"kv_connector": "TPURaidenOffloadingConnector", "kv_connector_module_path": "vllm_torchtpu.offload.raiden_connector", "kv_role": "kv_both", ...}'`  | 
  * ✅ Qwen3.5 (host DRAM pool + store node)
  * ✅ Kimi-K3
  * 🌙 DeepSeek-V4-Flash
  * 🌙 GLM-5.2-NVFP4

 | —  |  
|  How to enable`--kv-transfer-config '{"kv_connector": "TPURaidenOffloadingConnector", "kv_connector_module_path": "vllm_torchtpu.offload.raiden_connector", "kv_role": "kv_both", ...}'`  |  
| **Disaggregated serving (P/D)**  |  `--kv-transfer-config` with `TpuRaidenConnector` (or `TPUMultiConnector` to combine with offloading); `TPU_RAIDEN_*`  | 
  * ✅ Qwen3.5 (P4D2, PCP / TP / DCP resharding)
  * 🌙 DeepSeek-V4-Flash
  * 📝 Kimi-K3 1P1D

 | [Disaggregated Serving](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/disaggregated_serving/)  |  
|  How to enable`--kv-transfer-config` with `TpuRaidenConnector` (or `TPUMultiConnector` to combine with offloading); `TPU_RAIDEN_*`  |  
| **Speculative decoding**  | `--speculative-config '{"method": "eagle3" / "mtp" / "dflash" / "dspark" / "ngram" / "suffix", ...}'`  | 
  * EAGLE-3:
    * ✅ Llama-3.1-8B
  * MTP:
    * ✅ Qwen3.5-4B / 35B
  * DFlash:
    * ✅ Qwen3-4B
    * ✅ Qwen3.5-35B
  * DSpark:
    * 🌙 DeepSeek-V4-Flash
    * ✅ Qwen3-4B
  * ✅ N-gram

 | [Speculative Decoding](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/speculative_decoding/)  |  
|  How to enable`--speculative-config '{"method": "eagle3" / "mtp" / "dflash" / "dspark" / "ngram" / "suffix", ...}'`  |  
| **Structured outputs**  |  `--structured-outputs-config '{"backend": "xgrammar"}'` plus `structured_outputs` in the request  | 
  * 🧪 Qwen3-0.6B (`tests/entrypoints/llm/test_structured_output.py`)
  * 📝 Qwen3-0.6B (`qwen3-0.6b-structured-*` benchmark configs)

 | —  |  
|  How to enable`--structured-outputs-config '{"backend": "xgrammar"}'` plus `structured_outputs` in the request |  
| **Multi-LoRA**  |  `--enable-lora`, `--max-lora-rank`  | 
  * 📝 Qwen2.5-3B (`examples/offline_lora_inference.py`)

 | —  |  
|  How to enable`--enable-lora`, `--max-lora-rank`  |  
| **Multimodal inputs**  |  `--limit-mm-per-prompt`; `--language-model-only` to serve VLM checkpoints text-only; `MM_ENCODER_FRAME_CHUNK_PATCH_SIZE` for video frame chunking  | 
  * ✅ Gemma 4 (MMMU-Pro)
  * ✅ Qwen2.5-VL-3B (image and video chunking tests)

 | [Quickstart](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/)  |  
|  How to enable`--limit-mm-per-prompt`; `--language-model-only` to serve VLM checkpoints text-only; `MM_ENCODER_FRAME_CHUNK_PATCH_SIZE` for video frame chunking |  
| **Embedding & pooling**  |  `--runner pooling` (or `PoolerConfig(task="embed")` in Python)  | 
  * 📝 Qwen3-VL-Embedding-8B

 | —  |  
|  How to enable`--runner pooling` (or `PoolerConfig(task="embed")` in Python) |  
| **Compilation & warmup cache**  |  `VLLM_XLA_CACHE_PATH`, `--compilation-config '{"compile_sizes": [...]}'`, `TPU_PARALLEL_PRECOMPILE=1`, `VLLM_XLA_CHECK_RECOMPILATION=1`  | 
  * ✅ Qwen3-0.6B (compilation-cache end-to-end test)
  * Every recipe

 | [Compilation Cache](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/)  |  
|  How to enable`VLLM_XLA_CACHE_PATH`, `--compilation-config '{"compile_sizes": [...]}'`, `TPU_PARALLEL_PRECOMPILE=1`, `VLLM_XLA_CHECK_RECOMPILATION=1`  |  
| **Weight streaming & loading**  |  `--load-format runai_streamer` (from `gs://`), `--enable-ep-weight-filter`, `--safetensors-load-strategy prefetch`, `--model-loader-extra-config '{"memory_limit": ...}'`  | 
  * 🌙 GLM-5.2
  * 🌙 DeepSeek-V4-Pro
  * Kimi-K3 (multi-host recipes)

 | [Multi-Host Serving](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)  |  
|  How to enable`--load-format runai_streamer` (from `gs://`), `--enable-ep-weight-filter`, `--safetensors-load-strategy prefetch`, `--model-loader-extra-config '{"memory_limit": ...}'`  |  
| **SparseCore offload**  |  `USE_MOE_SPARSE_CORE=1` (default), `ONEHOT_MOE_PERMUTE_THRESHOLD`  | 
  * Every MoE recipe
  * 🌙 Sparse MLA top-k on DeepSeek-V4

 | [Parallelism](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)  |  
|  How to enable`USE_MOE_SPARSE_CORE=1` (default), `ONEHOT_MOE_PERMUTE_THRESHOLD`  |  
| **Profiling & observability**  |  `--profiler-config.profiler torch` with `--profile-result-dir`; `USE_PHASED_PROFILER=1`; Python / host / device tracer levels; vLLM Prometheus metrics (local and external prefix-cache hit counters)  | 
  * 📝 `examples/tpu_profiling.py`
  * 📝 `examples/run_profiling_suite.sh`

 | [Profiling](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/)  |  
|  How to enable`--profiler-config.profiler torch` with `--profile-result-dir`; `USE_PHASED_PROFILER=1`; Python / host / device tracer levels; vLLM Prometheus metrics (local and external prefix-cache hit counters) |  
See the [Environment Variables Reference](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/) for the full list of tuning knobs behind these features.
[**Reach the right audience** on a privacy-first ad network only for software devs:**EthicalAds**](https://server.ethicalads.io/proxy/click/8176/01a17840-4c1d-7f02-ae98-1b21ea1b8b33/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)
