---
id: "infer_02_vllm_torchtpu_quickstart"
title: "vLLM-TorchTPU quickstart"
url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/"
category: "Inference deployment links"
description: "Ready-to-run online serving, offline inference, and multimodal examples for PyTorch-native TPU serving."
crawled_at: "2026-10-26T12:47:23.294732+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#quickstart)
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU")
vLLM TorchTPU 
Quickstart 
[ ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/?q= "Share")
Type to start searching
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU") vLLM TorchTPU 
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
  * [ Home  ](https://vllm-torchtpu.readthedocs.io/en/latest/)
  * Getting Started  Getting Started 
    * [ Cloud TPU Setup  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/)
    * [ Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/)
    * Quickstart  [ Quickstart  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/) Table of contents 
      * [ 1. Online Serving (vllm serve)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#1-online-serving-vllm-serve)
        * [ Single-Chip (TP=1)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#single-chip-tp1)
        * [ 8-Device TPU Host (TP=8 + Expert Parallelism)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#8-device-tpu-host-tp8-expert-parallelism)
      * [ 2. Offline Batch Inference (vllm.LLM)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#2-offline-batch-inference-vllmllm)
      * [ 3. Multimodal Vision-Language Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#3-multimodal-vision-language-inference)
      * [ 4. Multi-LoRA Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#4-multi-lora-inference)
    * [ Docker Guide  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/)
  * User Guide  User Guide 
    * [ Supported Models & Features  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/)
    * [ Parallelism & Scaling  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)
    * [ Multi-Host Serving  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)
    * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/disaggregated_serving/)
    * [ Quantization  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/quantization/)
    * [ Speculative Decoding  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/speculative_decoding/)
    * [ Compilation & Warmup Cache  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/)
    * Code Examples  Code Examples 
      * [ Offline Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_inference/)
      * [ Multi Modal Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_lora_inference/)
  * Deployment & Recipes  Deployment & Recipes 
    * [ TPU v7x (Ironwood) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/)
    * [ TPU v6e (Trillium) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v6e_recipes/)
    * [ Kubernetes & GKE  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/kubernetes/)
  * Developer Guide  Developer Guide 
    * [ Contributing  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/contributing/)
    * [ Coding Guidance  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/coding_guidance/)
    * [ Optimization Best Practices  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/optimization_best_practices/)
    * [ TPU Patch Mechanism  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/tpu_patch_mechanism/)
    * [ Type Checking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/type_checking/)
    * [ Testing & CI  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/testing_and_ci/)
    * [ Benchmarking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/benchmarking/)
    * [ Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/)
Profiling 
      * [ Offline (tpu_profiling.py)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/offline/)
      * [ Server-side Capture  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/server/)
      * [ Phased Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/phased/)
      * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/disaggregated/)
      * [ Output Layout  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/output/)
      * [ Viewing Traces  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/viewing/)
      * [ Troubleshooting  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/troubleshooting/)
  * Reference  Reference 
    * [ Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/)
  * [ Roadmap  ](https://vllm-torchtpu.readthedocs.io/en/latest/roadmap/)


Table of contents 
  * [ 1. Online Serving (vllm serve)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#1-online-serving-vllm-serve)
    * [ Single-Chip (TP=1)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#single-chip-tp1)
    * [ 8-Device TPU Host (TP=8 + Expert Parallelism)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#8-device-tpu-host-tp8-expert-parallelism)
  * [ 2. Offline Batch Inference (vllm.LLM)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#2-offline-batch-inference-vllmllm)
  * [ 3. Multimodal Vision-Language Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#3-multimodal-vision-language-inference)
  * [ 4. Multi-LoRA Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#4-multi-lora-inference)


[ ](https://github.com/vllm-project/vllm-torchtpu/edit/main/docs/getting_started/quickstart.md "Edit this page")
# Quickstart[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#quickstart "Permanent link")
Once you have [provisioned a Cloud TPU VM](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/) and [installed `vllm-torchtpu`](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/), you can run online OpenAI-compatible serving or offline batch inference.
* * *
## 1. Online Serving (`vllm serve`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#1-online-serving-vllm-serve "Permanent link")
Start an OpenAI-compatible HTTP server using `vllm serve`:
### Single-Chip (`TP=1`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#single-chip-tp1 "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-0-1)vllm serve meta-llama/Llama-3.2-1B-Instruct \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-0-2)  --tensor-parallel-size 1 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-0-3)  --max-model-len 4096 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-0-4)  --port 8000

```

### 8-Device TPU Host (`TP=8` + Expert Parallelism)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#8-device-tpu-host-tp8-expert-parallelism "Permanent link")

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-1)vllm serve Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-2)  --tensor-parallel-size 8 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-3)  --enable-expert-parallel \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-4)  --kv-cache-dtype fp8 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-5)  --max-model-len 16384 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-6)  --max-num-batched-tokens 8192 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-7)  --async-scheduling \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-1-8)  --port 8000

```

Once the server logs `Application startup complete`, query the `/v1/chat/completions` endpoint from another terminal:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-1)curl http://localhost:8000/v1/chat/completions \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-2)  -H "Content-Type: application/json" \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-3)  -d '{
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-4)    "model": "meta-llama/Llama-3.2-1B-Instruct",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-5)    "messages": [
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-6)      {"role": "user", "content": "Explain how Tensor Processing Units accelerate matrix multiplication."}
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-7)    ],
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-8)    "max_tokens": 128,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-9)    "temperature": 0.0
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-2-10)  }'

```

Tip
**Persisting Compilation Caches Across Restarts** : The first startup compiles XLA/Pallas graphs for the configured token shapes. Set `VLLM_XLA_CACHE_PATH` to persist compiled artifacts across runs—see [Compilation & Warmup Cache](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/).
* * *
## 2. Offline Batch Inference (`vllm.LLM`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#2-offline-batch-inference-vllmllm "Permanent link")
Run offline batch generation directly from Python using `vllm.LLM`:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-1)from vllm import LLM, SamplingParams
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-2)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-3)prompts = [
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-4)    "Hello, my name is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-5)    "The capital of France is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-6)    "The future of AI hardware is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-7)]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-8)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-9)sampling_params = SamplingParams(temperature=0.0, max_tokens=64)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-10)llm = LLM(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-11)    model="meta-llama/Llama-3.2-1B-Instruct",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-12)    tensor_parallel_size=1,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-13)    max_model_len=1024,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-14))
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-15)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-16)outputs = llm.generate(prompts, sampling_params)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-17)for output in outputs:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-18)    print(f"Prompt: {output.prompt!r}")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-3-19)    print(f"Generated: {output.outputs[0].text!r}\n")

```

Or run the repository's CLI example script directly:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-4-1)python examples/offline_inference.py \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-4-2)  --model meta-llama/Llama-3.2-1B-Instruct \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-4-3)  --tensor-parallel-size 1 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-4-4)  --max-model-len 1024

```

Full Source: `examples/offline_inference.py`

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-1)# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-2)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-3)# Licensed under the Apache License, Version 2.0 (the "License");
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-4)# you may not use this file except in compliance with the License.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-5)# You may obtain a copy of the License at
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-6)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-7)#     http://www.apache.org/licenses/LICENSE-2.0
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-8)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-9)# Unless required by applicable law or agreed to in writing, software
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-10)# distributed under the License is distributed on an "AS IS" BASIS,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-11)# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-12)# See the License for the specific language governing permissions and
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-13)# limitations under the License.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-14)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-15)import argparse
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-16)import json
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-17)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-18)from vllm import LLM, EngineArgs
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-19)from vllm.utils.argparse_utils import FlexibleArgumentParser
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-20)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-21)from vllm_torchtpu.logger import init_logger
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-22)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-23)logger = init_logger(__name__)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-24)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-25)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-26)def create_parser():
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-27)    parser = FlexibleArgumentParser()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-28)    # Add engine args
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-29)    EngineArgs.add_cli_args(parser)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-30)    parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-31)    parser.set_defaults(max_model_len=1024)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-32)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-33)    # Add sampling params
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-34)    sampling_group = parser.add_argument_group("Sampling parameters")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-35)    sampling_group.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-36)        "--prompt",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-37)        type=str,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-38)        nargs="+",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-39)        default=None,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-40)        help="Custom prompt(s) for offline inference.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-41)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-42)    sampling_group.add_argument("--max-tokens", type=int)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-43)    sampling_group.add_argument("--temperature", type=float, default=0.0)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-44)    sampling_group.add_argument("--top-p", type=float)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-45)    sampling_group.add_argument("--top-k", type=int)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-46)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-47)    # Chat params
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-48)    chat_group = parser.add_argument_group("Chat parameters")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-49)    chat_group.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-50)        "--use-chat-template",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-51)        action=argparse.BooleanOptionalAction,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-52)        default=None,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-53)        help="Apply the model's chat template via LLM.chat instead of sending "
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-54)        "raw prompts to LLM.generate. Defaults to True when the tokenizer "
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-55)        "defines a chat template.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-56)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-57)    # A few models (like Qwen3.5) can use this to disable thinking using,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-58)    # `--chat-template-kwargs='{"enable_thinking": false}'`
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-59)    chat_group.add_argument("--chat-template-kwargs", type=json.loads, default={})
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-60)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-61)    return parser
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-62)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-63)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-64)def main(args: dict):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-65)    # Pop arguments not used by LLM
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-66)    custom_prompts = args.pop("prompt")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-67)    max_tokens = args.pop("max_tokens")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-68)    temperature = args.pop("temperature")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-69)    top_p = args.pop("top_p")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-70)    top_k = args.pop("top_k")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-71)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-72)    use_chat_template = args.pop("use_chat_template")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-73)    chat_template_kwargs = args.pop("chat_template_kwargs")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-74)    # Safeguard in case the user doesn't provide use_chat_template
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-75)    if use_chat_template is None and chat_template_kwargs != {}:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-76)        use_chat_template = True
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-77)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-78)    # Create an LLM
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-79)    llm = LLM(**args)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-80)    if use_chat_template is None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-81)        use_chat_template = bool(getattr(llm.get_tokenizer(), "chat_template", None))
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-82)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-83)    # Create a sampling params object
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-84)    sampling_params = llm.get_default_sampling_params()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-85)    sampling_params.temperature = 0.0
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-86)    if max_tokens is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-87)        sampling_params.max_tokens = max_tokens
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-88)    if temperature is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-89)        sampling_params.temperature = temperature
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-90)    if top_p is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-91)        sampling_params.top_p = top_p
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-92)    if top_k is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-93)        sampling_params.top_k = top_k
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-94)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-95)    # Generate texts from the prompts. The output is a list of RequestOutput
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-96)    # objects that contain the prompt, generated text, and other information.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-97)    prompts = custom_prompts or [
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-98)        "Hello, my name is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-99)        "The capital of France is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-100)        "The colors of the rainbow are",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-101)        "The future of AI is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-102)        "The president of the United States is",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-103)        "How many players are on a standard soccer team on the field at one time?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-104)        "In Greek mythology, who is the god of the sea?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-105)        "In what year did the Titanic sink?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-106)        "In which museum is the Mona Lisa displayed?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-107)        "Mount Everest is located in which mountain range?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-108)        "What ancient empire was ruled by Julius Caesar?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-109)        "What are the four fundamental forces of nature?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-110)        'What does "CPU" stand for?',
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-111)        'What does "HTML" stand for?',
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-112)        "What is the capital of Australia?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-113)        "What is the chemical symbol for gold?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-114)        "What is the currency of Switzerland?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-115)        "What is the distance from the Earth to the Sun called?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-116)        "What is the freezing point of water in Celsius?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-117)        "What is the hardest known natural substance on Earth?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-118)        "What is the largest planet in our solar system?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-119)        "What is the longest river in the world?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-120)        "What is the main function of the kidneys in the human body?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-121)        "What is the main ingredient in guacamole?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-122)        "What is the most spoken language in the world by number of native speakers?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-123)        "What is the process by which plants use sunlight to create food?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-124)        "Which country is known as the Land of the Rising Sun?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-125)        "Who developed the theory of general relativity?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-126)        'Who directed the original "Star Wars" trilogy?',
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-127)        "Who is credited with inventing the telephone?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-128)        "Who painted the ceiling of the Sistine Chapel?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-129)        "Who was the first female Prime Minister of the United Kingdom?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-130)        "Who was the first person to walk on the moon?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-131)        "Who wrote the American Declaration of Independence?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-132)        'Who wrote the novel "Pride and Prejudice"?',
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-133)    ]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-134)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-135)    torch_profiler_dir = llm.llm_engine.vllm_config.profiler_config.torch_profiler_dir
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-136)    if torch_profiler_dir is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-137)        llm.start_profile()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-138)    if use_chat_template:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-139)        logger.info(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-140)            "Using LLM chat API for inference with extra chat kwargs: %s",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-141)            chat_template_kwargs,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-142)        )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-143)        conversations = [[{"role": "user", "content": prompt}] for prompt in prompts]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-144)        outputs = llm.chat(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-145)            messages=conversations,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-146)            sampling_params=sampling_params,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-147)            chat_template_kwargs=chat_template_kwargs,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-148)        )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-149)    else:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-150)        logger.info("Using LLM generate API for inference")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-151)        outputs = llm.generate(prompts, sampling_params)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-152)    if torch_profiler_dir is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-153)        llm.stop_profile()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-154)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-155)    # Print the outputs.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-156)    print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-157)    for output in outputs:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-158)        prompt = output.prompt
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-159)        generated_text = output.outputs[0].text
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-160)        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-161)        print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-162)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-163)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-164)if __name__ == "__main__":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-165)    parser = create_parser()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-166)    args: dict = vars(parser.parse_args())
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-167)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-5-168)    main(args)

```

* * *
## 3. Multimodal Vision-Language Inference[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#3-multimodal-vision-language-inference "Permanent link")
`vllm-torchtpu` supports vision-language models such as `Qwen/Qwen2.5-VL-3B-Instruct` and `Qwen/Qwen3.5-397B-A17B`:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-6-1)python examples/multi_modal_inference.py \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-6-2)  --model Qwen/Qwen2.5-VL-3B-Instruct \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-6-3)  --tensor-parallel-size 1 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-6-4)  --num-prompts 1

```

Full Source: `examples/multi_modal_inference.py`

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-1)# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-2)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-3)# Licensed under the Apache License, Version 2.0 (the "License");
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-4)# you may not use this file except in compliance with the License.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-5)# You may obtain a copy of the License at
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-6)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-7)#     http://www.apache.org/licenses/LICENSE-2.0
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-8)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-9)# Unless required by applicable law or agreed to in writing, software
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-10)# distributed under the License is distributed on an "AS IS" BASIS,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-11)# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-12)# See the License for the specific language governing permissions and
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-13)# limitations under the License.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-14)"""
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-15)This example shows how to use vLLM for running offline inference with
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-16)the correct prompt format on vision language models for text generation.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-17)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-18)For most models, the prompt format should follow corresponding examples
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-19)on HuggingFace model repository.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-20)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-21)Example Command:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-22)python examples/multi_modal_inference.py \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-23)  --model Qwen/Qwen2.5-VL-3B-Instruct \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-24)  --tensor-parallel-size 1 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-25)  --num-prompts 1
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-26)"""
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-27)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-28)from contextlib import contextmanager
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-29)from dataclasses import asdict
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-30)from typing import NamedTuple
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-31)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-32)from vllm import LLM, EngineArgs, SamplingParams
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-33)from vllm.assets.image import ImageAsset
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-34)from vllm.multimodal.image import convert_image_mode
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-35)from vllm.utils.argparse_utils import FlexibleArgumentParser
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-36)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-37)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-38)class ModelRequestData(NamedTuple):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-39)    engine_args: EngineArgs
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-40)    prompts: list[str]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-41)    stop_token_ids: list[int] | None = None
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-42)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-43)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-44)# Currently Qwen2.5-VL is the only supported multi-modal
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-45)# Qwen2.5-VL
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-46)def run_qwen2_5_vl(questions: list[str], modality: str, args) -> ModelRequestData:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-47)    engine_args = EngineArgs(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-48)        model=args.model,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-49)        max_model_len=args.max_model_len,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-50)        tensor_parallel_size=args.tensor_parallel_size,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-51)        gpu_memory_utilization=args.gpu_memory_utilization,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-52)        max_num_seqs=5,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-53)        mm_processor_kwargs={
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-54)            "min_pixels": 28 * 28,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-55)            "max_pixels": 1280 * 28 * 28,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-56)            "fps": 1,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-57)        },
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-58)        limit_mm_per_prompt={modality: 1},
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-59)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-60)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-61)    if modality == "image":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-62)        placeholder = "<|image_pad|>"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-63)    elif modality == "video":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-64)        placeholder = "<|video_pad|>"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-65)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-66)    prompts = [
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-67)        (
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-68)            "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-69)            f"<|im_start|>user\n<|vision_start|>{placeholder}<|vision_end|>"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-70)            f"{question}<|im_end|>\n"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-71)            "<|im_start|>assistant\n"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-72)        )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-73)        for question in questions
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-74)    ]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-75)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-76)    return ModelRequestData(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-77)        engine_args=engine_args,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-78)        prompts=prompts,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-79)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-80)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-81)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-82)model_example_map = {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-83)    "qwen2_5_vl": run_qwen2_5_vl,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-84)}
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-85)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-86)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-87)def get_multi_modal_input(args):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-88)    """
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-89)    return {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-90)        "data": image or video,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-91)        "question": question,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-92)    }
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-93)    """
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-94)    if args.modality == "image":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-95)        # Input image and question
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-96)        image = convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-97)        img_questions = [
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-98)            "What is the content of this image?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-99)            "Describe the content of this image in detail.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-100)            "What's in the image?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-101)            "Where is this image taken?",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-102)        ]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-103)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-104)        return {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-105)            "data": image,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-106)            "questions": img_questions,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-107)        }
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-108)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-109)    # NOTE: not used for now, saved for future reference
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-110)    # if args.modality == "video":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-111)    #     # Input video and question
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-112)    #     video = VideoAsset(name="baby_reading",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-113)    #                        num_frames=args.num_frames).np_ndarrays
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-114)    #     metadata = VideoAsset(name="baby_reading",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-115)    #                           num_frames=args.num_frames).metadata
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-116)    #     vid_questions = ["Why is this video funny?"]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-117)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-118)    #     return {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-119)    #         "data": video,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-120)    #         "questions": vid_questions,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-121)    #     }
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-122)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-123)    msg = f"Modality {args.modality} is not supported."
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-124)    raise ValueError(msg)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-125)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-126)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-127)@contextmanager
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-128)def time_counter(enable: bool):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-129)    if enable:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-130)        import time
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-131)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-132)        start_time = time.time()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-133)        yield
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-134)        elapsed_time = time.time() - start_time
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-135)        print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-136)        print("-- generate time = {}".format(elapsed_time))
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-137)        print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-138)    else:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-139)        yield
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-140)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-141)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-142)def parse_args():
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-143)    parser = FlexibleArgumentParser(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-144)        description="Demo on using vLLM for offline inference with "
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-145)        "vision language models for text generation"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-146)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-147)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-148)        "--model",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-149)        "-m",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-150)        type=str,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-151)        default="Qwen/Qwen2.5-VL-3B-Instruct",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-152)        help="Huggingface model name.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-153)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-154)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-155)        "--tensor-parallel-size",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-156)        "-tp",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-157)        type=int,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-158)        default=1,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-159)        help="Tensor parallelism degree",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-160)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-161)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-162)    # TODO: Currently it needs much more space for intermidiate tensors
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-163)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-164)        "--gpu-memory-utilization",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-165)        type=float,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-166)        default=0.5,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-167)        help="GPU memory utilization",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-168)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-169)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-170)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-171)        "--max-model-len",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-172)        type=int,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-173)        default=4096,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-174)        help="Maximum sequence length of the model.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-175)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-176)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-177)        "--num-prompts", type=int, default=4, help="Number of prompts to run."
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-178)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-179)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-180)    # NOTE: Currently, only image modality is supported
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-181)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-182)        "--modality",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-183)        type=str,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-184)        default="image",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-185)        choices=["image", "video"],
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-186)        help="Modality of the input.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-187)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-188)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-189)    # NOTE: For video. Not used for now
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-190)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-191)        "--num-frames",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-192)        type=int,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-193)        default=16,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-194)        help="Number of frames to extract from the video.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-195)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-196)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-197)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-198)        "--seed",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-199)        type=int,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-200)        default=None,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-201)        help="Set the seed when initializing `vllm.LLM`.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-202)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-203)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-204)        "--disable-mm-preprocessor-cache",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-205)        action="store_true",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-206)        help="If True, disables caching of multi-modal preprocessor/mapper.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-207)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-208)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-209)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-210)        "--time-generate",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-211)        action="store_true",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-212)        help="If True, then print the total generate() call time",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-213)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-214)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-215)    parser.add_argument(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-216)        "--use-same-prompt-per-request",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-217)        action="store_false",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-218)        dest="use_different_prompt_per_request",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-219)        help="If set, use the same prompt for all requests. By default, "
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-220)        "different prompts are used for each request.",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-221)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-222)    return parser.parse_args()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-223)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-224)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-225)def main(args):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-226)    modality = args.modality
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-227)    mm_input = get_multi_modal_input(args)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-228)    data = mm_input["data"]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-229)    questions = mm_input["questions"]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-230)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-231)    # NOTE: Currently, only Qwen2.5-VL is supported. If later we want to support a model
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-232)    # with new chat template, we may need to change this
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-233)    req_data = model_example_map["qwen2_5_vl"](questions, modality, args)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-234)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-235)    # Disable other modalities to save memory
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-236)    # Initial all modalities to be 0s and add the specifc modality limit
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-237)    # later accordingly
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-238)    default_limits = {"image": 0, "video": 0, "audio": 0}
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-239)    req_data.engine_args.limit_mm_per_prompt = default_limits | dict(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-240)        req_data.engine_args.limit_mm_per_prompt or {}
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-241)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-242)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-243)    engine_args = asdict(req_data.engine_args) | {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-244)        "seed": args.seed,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-245)        "disable_mm_preprocessor_cache": args.disable_mm_preprocessor_cache,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-246)    }
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-247)    llm = LLM(**engine_args)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-248)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-249)    # Don't want to check the flag multiple times, so just hijack `prompts`.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-250)    prompts = (
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-251)        req_data.prompts
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-252)        if args.use_different_prompt_per_request
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-253)        else [req_data.prompts[0]]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-254)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-255)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-256)    # We set temperature to 0.2 so that outputs can be different
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-257)    # even when all prompts are identical when running batch inference.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-258)    sampling_params = SamplingParams(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-259)        temperature=0.2, max_tokens=64, stop_token_ids=req_data.stop_token_ids
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-260)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-261)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-262)    assert args.num_prompts > 0
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-263)    if args.num_prompts == 1:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-264)        # Single inference
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-265)        inputs = {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-266)            "prompt": prompts[0],
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-267)            "multi_modal_data": {modality: data},
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-268)        }
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-269)    else:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-270)        # Batch inference
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-271)        # Use the same image for all prompts
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-272)        inputs = [
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-273)            {
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-274)                "prompt": prompts[i % len(prompts)],
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-275)                "multi_modal_data": {modality: data},
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-276)            }
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-277)            for i in range(args.num_prompts)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-278)        ]
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-279)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-280)    with time_counter(args.time_generate):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-281)        outputs = llm.generate(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-282)            inputs,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-283)            sampling_params=sampling_params,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-284)        )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-285)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-286)    print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-287)    for o in outputs:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-288)        generated_text = o.outputs[0].text
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-289)        print(generated_text)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-290)        print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-291)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-292)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-293)if __name__ == "__main__":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-294)    args = parse_args()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-7-295)    main(args)

```

* * *
## 4. Multi-LoRA Inference[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#4-multi-lora-inference "Permanent link")
Run offline inference with LoRA adapters enabled:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-8-1)python examples/offline_lora_inference.py \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-8-2)  --model Qwen/Qwen2.5-3B-Instruct \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-8-3)  --enable-lora \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-8-4)  --max-lora-rank 8

```

Full Source: `examples/offline_lora_inference.py`

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-1)# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-2)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-3)# Licensed under the Apache License, Version 2.0 (the "License");
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-4)# you may not use this file except in compliance with the License.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-5)# You may obtain a copy of the License at
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-6)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-7)#     http://www.apache.org/licenses/LICENSE-2.0
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-8)#
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-9)# Unless required by applicable law or agreed to in writing, software
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-10)# distributed under the License is distributed on an "AS IS" BASIS,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-11)# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-12)# See the License for the specific language governing permissions and
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-13)# limitations under the License.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-14)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-15)import time
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-16)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-17)from vllm import LLM, EngineArgs
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-18)from vllm.lora.request import LoRARequest
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-19)from vllm.utils.argparse_utils import FlexibleArgumentParser
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-20)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-21)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-22)def create_parser():
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-23)    parser = FlexibleArgumentParser()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-24)    # Add engine args
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-25)    EngineArgs.add_cli_args(parser)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-26)    parser.set_defaults(model="Qwen/Qwen2.5-3B-Instruct")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-27)    parser.set_defaults(max_model_len=256)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-28)    parser.set_defaults(max_num_seqs=8)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-29)    parser.set_defaults(enable_lora=True)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-30)    parser.set_defaults(max_lora_rank=8)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-31)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-32)    # Add sampling params
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-33)    sampling_group = parser.add_argument_group("Sampling parameters")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-34)    sampling_group.add_argument("--max-tokens", type=int, default=16)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-35)    sampling_group.add_argument("--temperature", type=float, default=0)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-36)    sampling_group.add_argument("--top-p", type=float)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-37)    sampling_group.add_argument("--top-k", type=int)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-38)    return parser
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-39)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-40)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-41)def main(args: dict):
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-42)    # Pop arguments not used by LLM
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-43)    max_tokens = args.pop("max_tokens")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-44)    temperature = args.pop("temperature")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-45)    top_p = args.pop("top_p")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-46)    top_k = args.pop("top_k")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-47)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-48)    # Create an LLM
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-49)    llm = LLM(**args)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-51)    # Create a sampling params object
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-52)    sampling_params = llm.get_default_sampling_params()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-53)    if max_tokens is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-54)        sampling_params.max_tokens = max_tokens
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-55)    if temperature is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-56)        sampling_params.temperature = temperature
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-57)    if top_p is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-58)        sampling_params.top_p = top_p
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-59)    if top_k is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-60)        sampling_params.top_k = top_k
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-61)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-62)    prompt = "What is 1+1? \n"
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-63)    lora_request = LoRARequest(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-64)        "lora_adapter_3",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-65)        3,
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-66)        "Username6568/Qwen2.5-3B-Instruct-1_plus_1_equals_3_adapter",
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-67)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-68)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-69)    if llm.llm_engine.vllm_config.profiler_config.torch_profiler_dir is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-70)        llm.start_profile()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-71)    start = time.perf_counter()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-72)    outputs = llm.generate(
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-73)        prompt, sampling_params=sampling_params, lora_request=lora_request
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-74)    )
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-75)    if llm.llm_engine.vllm_config.profiler_config.torch_profiler_dir is not None:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-76)        llm.stop_profile()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-77)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-78)    # Print the outputs.
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-79)    print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-80)    for output in outputs:
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-81)        prompt = output.prompt
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-82)        generated_text = output.outputs[0].text
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-83)        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-84)        print("-" * 50)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-85)    end = time.perf_counter()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-86)    print(f"total time: {end - start} [secs].")
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-87)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-88)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-89)if __name__ == "__main__":
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-90)    parser = create_parser()
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-91)    args: dict = vars(parser.parse_args())
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-92)
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/#__codelineno-9-93)    main(args)

```

Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)