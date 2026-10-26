---
id: "infer_14_vllm_tpu_recommended_models"
title: "vLLM TPU recommended models"
url: "https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/"
category: "Inference deployment links"
description: "Model and feature validation matrix; check release and nightly support before deploying."
crawled_at: "2026-10-26T12:47:44.915019+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#recommended-models)
[ ![vLLM logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/vllm-logo-only-light.png) + ![JAX logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/jax-logo.svg) ](https://docs.vllm.ai/projects/tpu/en/latest/ "vLLM JAX")
vLLM JAX 
Recommended Models 
[ ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/?q= "Share")
Type to start searching
[ GitHub 
  * v0.32.0
  * 467
  * 349

](https://github.com/vllm-project/tpu-inference "Go to repository")
[ ![vLLM logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/vllm-logo-only-light.png) + ![JAX logo](https://docs.vllm.ai/projects/tpu/en/latest/assets/logos/jax-logo.svg) ](https://docs.vllm.ai/projects/tpu/en/latest/ "vLLM JAX") vLLM JAX 
[ GitHub 
  * v0.32.0
  * 467
  * 349

](https://github.com/vllm-project/tpu-inference "Go to repository")
  * [ Home  ](https://docs.vllm.ai/projects/tpu/en/latest/)
  * Getting Started  Getting Started 
    * [ TPU Setup  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/tpu_setup/)
    * [ Installation  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/)
    * [ Quickstart  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/)
  * Features & Usage  Features & Usage 
    * Recommended Models  [ Recommended Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/) Table of contents 
      * [ Recommended Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#recommended-models_1)
        * [ Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#models)
        * [ Embedding Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#embedding-models)
    * [ Feature Matrix  ](https://docs.vllm.ai/projects/tpu/en/latest/features/)
    * Deployment Recipes  Deployment Recipes 
      * [ v7x Recipes (Ironwood)  ](https://docs.vllm.ai/projects/tpu/en/latest/deployment_guides/ironwood/)
      * [ v6e Recipes (Trillium)  ](https://docs.vllm.ai/projects/tpu/en/latest/deployment_guides/trillium/)
    * Code Examples  Code Examples 
      * [ Multi Modal Inference  ](https://docs.vllm.ai/projects/tpu/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://docs.vllm.ai/projects/tpu/en/latest/api_and_code_examples/offline_lora_inference/)
    * [ Out-of-Tree Usage  ](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/out-of-tree/)
  * Developers Guides  Developers Guides 
    * [ Contributing to vLLM JAX  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/contributing/)
    * [ Adding a New Model to CI  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/buildkite/)
    * [ JAX Model Development  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/jax_model_development/)
    * [ Torchax Model Development  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/torchax_model_development/)
    * [ Profiling  ](https://docs.vllm.ai/projects/tpu/en/latest/developers_guide/profiling/)


Table of contents 
  * [ Recommended Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#recommended-models_1)
    * [ Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#models)
    * [ Embedding Models  ](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#embedding-models)


[ ](https://github.com/vllm-project/tpu-inference/edit/main/docs/recommended_models.md "Edit this page")
# Recommended Models[¶](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#recommended-models "Permanent link")
Although vLLM JAX’s new unified backend makes out-of-the-box high performance serving possible with any model supported in vLLM, the reality is that we're still in the process of implementing a few core components. For this reason, until we land more capabilities, we recommend starting from this list of stress tested models and features below.
We are still landing components in vllm-jax that will improve performance for larger scale, higher complexity models (XL MoE, +vision encoders, MLA, etc.).
If you’d like us to prioritize something specific, please submit a GitHub feature request [here](https://github.com/vllm-project/tpu-inference/issues/new/choose).
**🚦 _Status Legend_ **
>   * ✅ **Passing:** Tested and works as expected. Ready for use.
>   * ❌ **Failing:** Known to be broken or not functional. Help is wanted to fix this!
>   * 🧪 **Experimental:** Works, but unoptimized or pending community validation.
>   * 📝 **Planned:** Not yet implemented, but on the official roadmap.
>   * ⛔️ **Unplanned:** There is no benefit to adding this.
>   * ❓ **Untested:** The functionality exists but has not been recently or thoroughly verified.
> 

## Recommended Models[¶](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#recommended-models_1 "Permanent link")
These tables show the models currently tested for accuracy and performance.
### Models[¶](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#models "Permanent link")
[Release](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#release)[Nightly](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#nightly)  
| Model  | Type  | Unit Test  | Correctness Test  | Performance Test  |  
| --- | --- | --- | --- | --- |  
| [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)  | Multimodal  | ✅  | ✅  | ✅  |  
| [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)  | Multimodal  | ✅  | ✅  | ✅  |  
| [google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)  | Multimodal  | ✅  | ✅  | ✅  |  
| [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)  | Multimodal  | ✅  | ✅  | ✅  |  
| [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it)  | Text  | ✅  | ✅  | ✅  |  
| [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)  | Text  | ✅  | ✅  | ✅  |  
| [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B)  | Embedding  | ✅  | ✅  | ❓  |  
| [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)  | Multimodal  | ✅  | ✅  | ❓  |  
| [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)  | Text  | ✅  | ✅  | ❓  |  
| [moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)  | Text  | ✅  | ✅  | ❓  |  
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)  | Text  | ✅  | ✅  | ❓  |  
| [deepseek-ai/DeepSeek-OCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR)  | Multimodal  | ❓  | ❓  | ❓  |  
| [meta-llama/Llama-4-Maverick-17B-128E-Instruct/multimodal](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/multimodal)  | Multimodal  | ❓  | ❓  | ❓  |  
| [Qwen/Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct)  | Multimodal  | ❓  | ❓  | ❓  |  
| [Qwen/Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)  | Multimodal  | ❓  | ❓  | ❓  |  
| [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)  | Multimodal  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-Math-V2](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2)  | Text  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1)  | Text  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2)  | Text  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-V3.2-Speciale](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale)  | Text  | ❓  | ❓  | ❓  |  
| [MiniMaxAI/MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)  | Text  | ❓  | ❓  | ❓  |  
| [mistralai/Mistral-Small-4-119B-2603/text-only](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/text-only)  | Text  | ❓  | ❓  | ❓  |  
| [moonshotai/Kimi-K2-Thinking](https://huggingface.co/moonshotai/Kimi-K2-Thinking)  | Text  | ❓  | ❓  | ❓  |  
| [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)  | Text  | ❓  | ❓  | ❓  |  
| [zai-org/GLM-5](https://huggingface.co/zai-org/GLM-5)  | Text  | ❓  | ❓  | ❓  |  
| Model  | Type  | Unit Test  | Correctness Test  | Performance Test  |  
| --- | --- | --- | --- | --- |  
| [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)  | Multimodal  | ✅  | ✅  | ✅  |  
| [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)  | Multimodal  | ✅  | ✅  | ✅  |  
| [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it)  | Text  | ✅  | ✅  | ✅  |  
| [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)  | Text  | ✅  | ✅  | ✅  |  
| [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)  | Text  | ✅  | ✅  | ✅  |  
| [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)  | Multimodal  | ✅  | ✅  | ❌  |  
| [Qwen/Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B)  | Embedding  | ✅  | ✅  | ❓  |  
| [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)  | Text  | ✅  | ✅  | ❓  |  
| [moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)  | Text  | ✅  | ✅  | ❓  |  
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)  | Text  | ✅  | ✅  | ❓  |  
| [google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)  | Multimodal  | ✅  | ❌  | ❓  |  
| [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)  | Multimodal  | ✅  | ❌  | ❓  |  
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)  | Text  | ❌  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-OCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR)  | Multimodal  | ❓  | ❓  | ❓  |  
| [Qwen/Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct)  | Multimodal  | ❓  | ❓  | ❓  |  
| [Qwen/Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)  | Multimodal  | ❓  | ❓  | ❓  |  
| [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)  | Multimodal  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-Math-V2](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2)  | Text  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1)  | Text  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2)  | Text  | ❓  | ❓  | ❓  |  
| [deepseek-ai/DeepSeek-V3.2-Speciale](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale)  | Text  | ❓  | ❓  | ❓  |  
| [MiniMaxAI/MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)  | Text  | ❓  | ❓  | ❓  |  
| [moonshotai/Kimi-K2-Thinking](https://huggingface.co/moonshotai/Kimi-K2-Thinking)  | Text  | ❓  | ❓  | ❓  |  
| [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)  | Text  | ❓  | ❓  | ❓  |  
| [zai-org/GLM-5](https://huggingface.co/zai-org/GLM-5)  | Text  | ❓  | ❓  | ❓  |  
### Embedding Models[¶](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#embedding-models "Permanent link")
[v7x](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#v7x)[v6e](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models/#v6e)  
| Model  | Type  | UnitTest  | Accuracy/Correctness  | Benchmark  |  
| --- | --- | --- | --- | --- |  
| Qwen/Qwen3-Embedding-8B  | Embedding  | ✅ Passing  | ✅ Passing  | ❓ Untested  |  
| Qwen/Qwen2.5-VL-7B-Instruct  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-Omni-30B-A3B-Instruct  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Qwen/Qwen3-VL-8B-Instruct  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Qwen/Qwen3.5-9B  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-OCR  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| google/gemma-4-26B-A4B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| google/gemma-4-31B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| google/gemma-4-E2B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| google/gemma-4-E4B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| meta-llama/Llama-4-Maverick-17B-128E-Instruct/multimodal  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| MiniMaxAI/MiniMax-M2.5  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Qwen/Qwen3-30B-A3B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-32B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-4B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-Coder-480B-A35B-Instruct  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3.5-397B-A17B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| deepseek-ai/DeepSeek-Math-V2  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-R1  | Text  | ✅ Passing  | ✅ Passing  | ❓ Untested  |  
| deepseek-ai/DeepSeek-V3.1  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-V3.2  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-V3.2-Speciale  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| google/gemma-3-27b-it  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| meta-llama/Llama-3.1-8B-Instruct  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| meta-llama/Llama-3.3-70B-Instruct  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| mistralai/Mistral-Small-4-119B-2603/text-only  | Text  | ❓ Untested  | ✅ Passing  | ❓ Untested  |  
| moonshotai/Kimi-K2-Thinking  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| moonshotai/Kimi-K2.6  | Text  | ✅ Passing  | ✅ Passing  | ❓ Untested  |  
| openai/gpt-oss-120b  | Text  | ✅ Passing  | ✅ Passing  | ❓ Untested  |  
| openai/gpt-oss-20b  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| zai-org/GLM-5  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Model  | Type  | UnitTest  | Accuracy/Correctness  | Benchmark  |  
| --- | --- | --- | --- | --- |  
| Qwen/Qwen3-Embedding-8B  | Embedding  | ✅ Passing  | ✅ Passing  | ❓ Untested  |  
| Qwen/Qwen2.5-VL-7B-Instruct  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-Omni-30B-A3B-Instruct  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Qwen/Qwen3-VL-8B-Instruct  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Qwen/Qwen3.5-9B  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-OCR  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| google/gemma-4-26B-A4B-it  | Multimodal  | not enough HBM  | not enough HBM  | not enough HBM  |  
| google/gemma-4-31B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | not enough HBM  |  
| google/gemma-4-E2B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| google/gemma-4-E4B-it  | Multimodal  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| meta-llama/Llama-4-Maverick-17B-128E-Instruct/multimodal  | Multimodal  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| MiniMaxAI/MiniMax-M2.5  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| Qwen/Qwen3-30B-A3B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-32B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-4B  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| Qwen/Qwen3-Coder-480B-A35B-Instruct  | Text  | not enough HBM  | not enough HBM  | not enough HBM  |  
| Qwen/Qwen3.5-397B-A17B  | Text  | not enough HBM  | not enough HBM  | not enough HBM  |  
| deepseek-ai/DeepSeek-Math-V2  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-R1  | Text  | not enough HBM  | not enough HBM  | ❓ Untested  |  
| deepseek-ai/DeepSeek-V3.1  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-V3.2  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| deepseek-ai/DeepSeek-V3.2-Speciale  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| google/gemma-3-27b-it  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| meta-llama/Llama-3.1-8B-Instruct  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| meta-llama/Llama-3.3-70B-Instruct  | Text  | ✅ Passing  | ✅ Passing  | ✅ Passing  |  
| mistralai/Mistral-Small-4-119B-2603/text-only  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| moonshotai/Kimi-K2-Thinking  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| moonshotai/Kimi-K2.6  | Text  | not enough HBM  | not enough HBM  | ❓ Untested  |  
| openai/gpt-oss-120b  | Text  | not enough HBM  | not enough HBM  | ❓ Untested  |  
| openai/gpt-oss-20b  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
| zai-org/GLM-5  | Text  | ❓ Untested  | ❓ Untested  | ❓ Untested  |  
Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)