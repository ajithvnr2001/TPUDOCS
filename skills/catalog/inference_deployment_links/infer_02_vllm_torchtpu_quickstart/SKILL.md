---
name: infer-02-vllm-torchtpu-quickstart
description: "vLLM-TorchTPU quickstart \u2014 Ready-to-run online serving, offline inference, and multimodal examples for PyTorch-native TPU serving."
source_url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/"
category: "inference_deployment_links"
---

# Agent Skill: vLLM-TorchTPU quickstart

- **Official Source**: [https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/)
- **Category**: `inference_deployment_links`
- **Resource ID**: `infer_02_vllm_torchtpu_quickstart`
- **When to Activate**: Ready-to-run online serving, offline inference, and multimodal examples for PyTorch-native TPU serving.

## Document Sections

- **Quickstart**
  - **1. Online Serving (`vllm serve`)**
    - **Single-Chip (`TP=1`)**
    - **8-Device TPU Host (`TP=8` + Expert Parallelism)**
  - **2. Offline Batch Inference (`vllm.LLM`)**
- **SPDX-FileCopyrightText: Copyright contributors to the vLLM project**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
  - **3. Multimodal Vision-Language Inference**
- **SPDX-FileCopyrightText: Copyright contributors to the vLLM project**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **Currently Qwen2.5-VL is the only supported multi-modal**
- **Qwen2.5-VL**
  - **4. Multi-LoRA Inference**
- **SPDX-FileCopyrightText: Copyright contributors to the vLLM project**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**

## Key CLI Commands & Invocations

```bash
vllm serve meta-llama/Llama-3.2-1B-Instruct \
vllm serve Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \
curl http://localhost:8000/v1/chat/completions \
python examples/offline_inference.py \
python examples/multi_modal_inference.py \
python examples/offline_lora_inference.py \
```

## Complete Technical Reference

# Quickstart
Once you have [provisioned a Cloud TPU VM](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/) and [installed `vllm-torchtpu`](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/), you can run online OpenAI-compatible serving or offline batch inference.
* * *
## 1. Online Serving (`vllm serve`)
Start an OpenAI-compatible HTTP server using `vllm serve`:
### Single-Chip (`TP=1`)

```
vllm serve meta-llama/Llama-3.2-1B-Instruct \
  --tensor-parallel-size 1 \
  --max-model-len 4096 \
  --port 8000

```

### 8-Device TPU Host (`TP=8` + Expert Parallelism)

```
vllm serve Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --kv-cache-dtype fp8 \
  --max-model-len 16384 \
  --max-num-batched-tokens 8192 \
  --async-scheduling \
  --port 8000

```

Once the server logs `Application startup complete`, query the `/v1/chat/completions` endpoint from another terminal:

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.2-1B-Instruct",
    "messages": [
      {"role": "user", "content": "Explain how Tensor Processing Units accelerate matrix multiplication."}
    ],
    "max_tokens": 128,
    "temperature": 0.0
  }'

```

Tip
**Persisting Compilation Caches Across Restarts** : The first startup compiles XLA/Pallas graphs for the configured token shapes. Set `VLLM_XLA_CACHE_PATH` to persist compiled artifacts across runs—see [Compilation & Warmup Cache](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/).
* * *
## 2. Offline Batch Inference (`vllm.LLM`)
Run offline batch generation directly from Python using `vllm.LLM`:

```
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The capital of France is",
    "The future of AI hardware is",
]

sampling_params = SamplingParams(temperature=0.0, max_tokens=64)
llm = LLM(
    model="meta-llama/Llama-3.2-1B-Instruct",
    tensor_parallel_size=1,
    max_model_len=1024,
)

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    print(f"Prompt: {output.prompt!r}")
    print(f"Generated: {output.outputs[0].text!r}\n")

```

Or run the repository's CLI example script directly:

```
python examples/offline_inference.py \
  --model meta-llama/Llama-3.2-1B-Instruct \
  --tensor-parallel-size 1 \
  --max-model-len 1024

```

Full Source: `examples/offline_inference.py`

```
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json

from vllm import LLM, EngineArgs
from vllm.utils.argparse_utils import FlexibleArgumentParser

from vllm_torchtpu.logger import init_logger

logger = init_logger(__name__)


def create_parser():
    parser = FlexibleArgumentParser()
    # Add engine args
    EngineArgs.add_cli_args(parser)
    parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")
    parser.set_defaults(max_model_len=1024)

    # Add sampling params
    sampling_group = parser.add_argument_group("Sampling parameters")
    sampling_group.add_argument(
        "--prompt",
        type=str,
        nargs="+",
        default=None,
        help="Custom prompt(s) for offline inference.",
    )
    sampling_group.add_argument("--max-tokens", type=int)
    sampling_group.add_argument("--temperature", type=float, default=0.0)
    sampling_group.add_argument("--top-p", type=float)
    sampling_group.add_argument("--top-k", type=int)

    # Chat params
    chat_group = parser.add_argument_group("Chat parameters")
    chat_group.add_argument(
        "--use-chat-template",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Apply the model's chat template via LLM.chat instead of sending "
        "raw prompts to LLM.generate. Defaults to True when the tokenizer "
        "defines a chat template.",
    )
    # A few models (like Qwen3.5) can use this to disable thinking using,
    # `--chat-template-kwargs='{"enable_thinking": false}'`
    chat_group.add_argument("--chat-template-kwargs", type=json.loads, default={})

    return parser


def main(args: dict):
    # Pop arguments not used by LLM
    custom_prompts = args.pop("prompt")
    max_tokens = args.pop("max_tokens")
    temperature = args.pop("temperature")
    top_p = args.pop("top_p")
    top_k = args.pop("top_k")

    use_chat_template = args.pop("use_chat_template")
    chat_template_kwargs = args.pop("chat_template_kwargs")
    # Safeguard in case the user doesn't provide use_chat_template
    if use_chat_template is None and chat_template_kwargs != {}:
        use_chat_template = True

    # Create an LLM
    llm = LLM(**args)
    if use_chat_template is None:
        use_chat_template = bool(getattr(llm.get_tokenizer(), "chat_template", None))

    # Create a sampling params object
    sampling_params = llm.get_default_sampling_params()
    sampling_params.temperature = 0.0
    if max_tokens is not None:
        sampling_params.max_tokens = max_tokens
    if temperature is not None:
        sampling_params.temperature = temperature
    if top_p is not None:
        sampling_params.top_p = top_p
    if top_k is not None:
        sampling_params.top_k = top_k

    # Generate texts from the prompts. The output is a list of RequestOutput
    # objects that contain the prompt, generated text, and other information.
    prompts = custom_prompts or [
        "Hello, my name is",
        "The capital of France is",
        "The colors of the rainbow are",
        "The future of AI is",
        "The president of the United States is",
        "How many players are on a standard soccer team on the field at one time?",
        "In Greek mythology, who is the god of the sea?",
        "In what year did the Titanic sink?",
        "In which museum is the Mona Lisa displayed?",
        "Mount Everest is located in which mountain range?",
        "What ancient empire was ruled by Julius Caesar?",
        "What are the four fundamental forces of nature?",
        'What does "CPU" stand for?',
        'What does "HTML" stand for?',
        "What is the capital of Australia?",
        "What is the chemical symbol for gold?",
        "What is the currency of Switzerland?",
        "What is the distance from the Earth to the Sun called?",
        "What is the freezing point of water in Celsius?",
        "What is the hardest known natural substance on Earth?",
        "What is the largest planet in our solar system?",
        "What is the longest river in the world?",
        "What is the main function of the kidneys in the human body?",
        "What is the main ingredient in guacamole?",
        "What is the most spoken language in the world by number of native speakers?",
        "What is the process by which plants use sunlight to create food?",
        "Which country is known as the Land of the Rising Sun?",
        "Who developed the theory of general relativity?",
        'Who directed the original "Star Wars" trilogy?',
        "Who is credited with inventing the telephone?",
        "Who painted the ceiling of the Sistine Chapel?",
        "Who was the first female Prime Minister of the United Kingdom?",
        "Who was the first person to walk on the moon?",
        "Who wrote the American Declaration of Independence?",
        'Who wrote the novel "Pride and Prejudice"?',
    ]

    torch_profiler_dir = llm.llm_engine.vllm_config.profiler_config.torch_profiler_dir
    if torch_profiler_dir is not None:
        llm.start_profile()
    if use_chat_template:
        logger.info(
            "Using LLM chat API for inference with extra chat kwargs: %s",
            chat_template_kwargs,
        )
        conversations = [[{"role": "user", "content": prompt}] for prompt in prompts]
        outputs = llm.chat(
            messages=conversations,
            sampling_params=sampling_params,
            chat_template_kwargs=chat_template_kwargs,
        )
    else:
        logger.info("Using LLM generate API for inference")
        outputs = llm.generate(prompts, sampling_params)
    if torch_profiler_dir is not None:
        llm.stop_profile()

    # Print the outputs.
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)


if __name__ == "__main__":
    parser = create_parser()
    args: dict = vars(parser.parse_args())

    main(args)

```

* * *
## 3. Multimodal Vision-Language Inference
`vllm-torchtpu` supports vision-language models such as `Qwen/Qwen2.5-VL-3B-Instruct` and `Qwen/Qwen3.5-397B-A17B`:

```
python examples/multi_modal_inference.py \
  --model Qwen/Qwen2.5-VL-3B-Instruct \
  --tensor-parallel-size 1 \
  --num-prompts 1

```

Full Source: `examples/multi_modal_inference.py`

```
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This example shows how to use vLLM for running offline inference with
the correct prompt format on vision language models for text generation.

For most models, the prompt format should follow corresponding examples
on HuggingFace model repository.

Example Command:
python examples/multi_modal_inference.py \
  --model Qwen/Qwen2.5-VL-3B-Instruct \
  --tensor-parallel-size 1 \
  --num-prompts 1
"""

from contextlib import contextmanager
from dataclasses import asdict
from typing import NamedTuple

from vllm import LLM, EngineArgs, SamplingParams
from vllm.assets.image import ImageAsset
from vllm.multimodal.image import convert_image_mode
from vllm.utils.argparse_utils import FlexibleArgumentParser


class ModelRequestData(NamedTuple):
    engine_args: EngineArgs
    prompts: list[str]
    stop_token_ids: list[int] | None = None


# Currently Qwen2.5-VL is the only supported multi-modal
# Qwen2.5-VL
def run_qwen2_5_vl(questions: list[str], modality: str, args) -> ModelRequestData:
    engine_args = EngineArgs(
        model=args.model,
        max_model_len=args.max_model_len,
        tensor_parallel_size=args.tensor_parallel_size,
        gpu_memory_utilization=args.gpu_memory_utilization,
        max_num_seqs=5,
        mm_processor_kwargs={
            "min_pixels": 28 * 28,
            "max_pixels": 1280 * 28 * 28,
            "fps": 1,
        },
        limit_mm_per_prompt={modality: 1},
    )

    if modality == "image":
        placeholder = "<|image_pad|>"
    elif modality == "video":
        placeholder = "<|video_pad|>"

    prompts = [
        (
            "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
            f"<|im_start|>user\n<|vision_start|>{placeholder}<|vision_end|>"
            f"{question}<|im_end|>\n"
            "<|im_start|>assistant\n"
        )
        for question in questions
    ]

    return ModelRequestData(
        engine_args=engine_args,
        prompts=prompts,
    )


model_example_map = {
    "qwen2_5_vl": run_qwen2_5_vl,
}


def get_multi_modal_input(args):
    """
    return {
        "data": image or video,
        "question": question,
    }
    """
    if args.modality == "image":
        # Input image and question
        image = convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB")
        img_questions = [
            "What is the content of this image?",
            "Describe the content of this image in detail.",
            "What's in the image?",
            "Where is this image taken?",
        ]

        return {
            "data": image,
            "questions": img_questions,
        }

    # NOTE: not used for now, saved for future reference
    # if args.modality == "video":
    #     # Input video and question
    #     video = VideoAsset(name="baby_reading",
    #                        num_frames=args.num_frames).np_ndarrays
    #     metadata = VideoAsset(name="baby_reading",
    #                           num_frames=args.num_frames).metadata
    #     vid_questions = ["Why is this video funny?"]

    #     return {
    #         "data": video,
    #         "questions": vid_questions,
    #     }

    msg = f"Modality {args.modality} is not supported."
    raise ValueError(msg)


@contextmanager
def time_counter(enable: bool):
    if enable:
        import time

        start_time = time.time()
        yield
        elapsed_time = time.time() - start_time
        print("-" * 50)
        print("-- generate time = {}".format(elapsed_time))
        print("-" * 50)
    else:
        yield


def parse_args():
    parser = FlexibleArgumentParser(
        description="Demo on using vLLM for offline inference with "
        "vision language models for text generation"
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default="Qwen/Qwen2.5-VL-3B-Instruct",
        help="Huggingface model name.",
    )
    parser.add_argument(
        "--tensor-parallel-size",
        "-tp",
        type=int,
        default=1,
        help="Tensor parallelism degree",
    )

    # TODO: Currently it needs much more space for intermidiate tensors
    parser.add_argument(
        "--gpu-memory-utilization",
        type=float,
        default=0.5,
        help="GPU memory utilization",
    )

    parser.add_argument(
        "--max-model-len",
        type=int,
        default=4096,
        help="Maximum sequence length of the model.",
    )
    parser.add_argument(
        "--num-prompts", type=int, default=4, help="Number of prompts to run."
    )

    # NOTE: Currently, only image modality is supported
    parser.add_argument(
        "--modality",
        type=str,
        default="image",
        choices=["image", "video"],
        help="Modality of the input.",
    )

    # NOTE: For video. Not used for now
    parser.add_argument(
        "--num-frames",
        type=int,
        default=16,
        help="Number of frames to extract from the video.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Set the seed when initializing `vllm.LLM`.",
    )
    parser.add_argument(
        "--disable-mm-preprocessor-cache",
        action="store_true",
        help="If True, disables caching of multi-modal preprocessor/mapper.",
    )

    parser.add_argument(
        "--time-generate",
        action="store_true",
        help="If True, then print the total generate() call time",
    )

    parser.add_argument(
        "--use-same-prompt-per-request",
        action="store_false",
        dest="use_different_prompt_per_request",
        help="If set, use the same prompt for all requests. By default, "
        "different prompts are used for each request.",
    )
    return parser.parse_args()


def main(args):
    modality = args.modality
    mm_input = get_multi_modal_input(args)
    data = mm_input["data"]
    questions = mm_input["questions"]

    # NOTE: Currently, only Qwen2.5-VL is supported. If later we want to support a model
    # with new chat template, we may need to change this
    req_data = model_example_map["qwen2_5_vl"](questions, modality, args)

    # Disable other modalities to save memory
    # Initial all modalities to be 0s and add the specifc modality limit
    # later accordingly
    default_limits = {"image": 0, "video": 0, "audio": 0}
    req_data.engine_args.limit_mm_per_prompt = default_limits | dict(
        req_data.engine_args.limit_mm_per_prompt or {}
    )

    engine_args = asdict(req_data.engine_args) | {
        "seed": args.seed,
        "disable_mm_preprocessor_cache": args.disable_mm_preprocessor_cache,
    }
    llm = LLM(**engine_args)

    # Don't want to check the flag multiple times, so just hijack `prompts`.
    prompts = (
        req_data.prompts
        if args.use_different_prompt_per_request
        else [req_data.prompts[0]]
    )

    # We set temperature to 0.2 so that outputs can be different
    # even when all prompts are identical when running batch inference.
    sampling_params = SamplingParams(
        temperature=0.2, max_tokens=64, stop_token_ids=req_data.stop_token_ids
    )

    assert args.num_prompts > 0
    if args.num_prompts == 1:
        # Single inference
        inputs = {
            "prompt": prompts[0],
            "multi_modal_data": {modality: data},
        }
    else:
        # Batch inference
        # Use the same image for all prompts
        inputs = [
            {
                "prompt": prompts[i % len(prompts)],
                "multi_modal_data": {modality: data},
            }
            for i in range(args.num_prompts)
        ]

    with time_counter(args.time_generate):
        outputs = llm.generate(
            inputs,
            sampling_params=sampling_params,
        )

    print("-" * 50)
    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)
        print("-" * 50)


if __name__ == "__main__":
    args = parse_args()
    main(args)

```

* * *
## 4. Multi-LoRA Inference
Run offline inference with LoRA adapters enabled:

```
python examples/offline_lora_inference.py \
  --model Qwen/Qwen2.5-3B-Instruct \
  --enable-lora \
  --max-lora-rank 8

```

Full Source: `examples/offline_lora_inference.py`

```
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

from vllm import LLM, EngineArgs
from vllm.lora.request import LoRARequest
from vllm.utils.argparse_utils import FlexibleArgumentParser


def create_parser():
    parser = FlexibleArgumentParser()
    # Add engine args
    EngineArgs.add_cli_args(parser)
    parser.set_defaults(model="Qwen/Qwen2.5-3B-Instruct")
    parser.set_defaults(max_model_len=256)
    parser.set_defaults(max_num_seqs=8)
    parser.set_defaults(enable_lora=True)
    parser.set_defaults(max_lora_rank=8)

    # Add sampling params
    sampling_group = parser.add_argument_group("Sampling parameters")
    sampling_group.add_argument("--max-tokens", type=int, default=16)
    sampling_group.add_argument("--temperature", type=float, default=0)
    sampling_group.add_argument("--top-p", type=float)
    sampling_group.add_argument("--top-k", type=int)
    return parser


def main(args: dict):
    # Pop arguments not used by LLM
    max_tokens = args.pop("max_tokens")
    temperature = args.pop("temperature")
    top_p = args.pop("top_p")
    top_k = args.pop("top_k")

    # Create an LLM
    llm = LLM(**args)

    # Create a sampling params object
    sampling_params = llm.get_default_sampling_params()
    if max_tokens is not None:
        sampling_params.max_tokens = max_tokens
    if temperature is not None:
        sampling_params.temperature = temperature
    if top_p is not None:
        sampling_params.top_p = top_p
    if top_k is not None:
        sampling_params.top_k = top_k

    prompt = "What is 1+1? \n"
    lora_request = LoRARequest(
        "lora_adapter_3",
        3,
        "Username6568/Qwen2.5-3B-Instruct-1_plus_1_equals_3_adapter",
    )

    if llm.llm_engine.vllm_config.profiler_config.torch_profiler_dir is not None:
        llm.start_profile()
    start = time.perf_counter()
    outputs = llm.generate(
        prompt, sampling_params=sampling_params, lora_request=lora_request
    )
    if llm.llm_engine.vllm_config.profiler_config.torch_profiler_dir is not None:
        llm.stop_profile()

    # Print the outputs.
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)
    end = time.perf_counter()
    print(f"total time: {end - start} [secs].")


if __name__ == "__main__":
    parser = create_parser()
    args: dict = vars(parser.parse_args())

    main(args)

```
