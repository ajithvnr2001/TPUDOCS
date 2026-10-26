---
name: tpu-inference-vllm
description: Expert AI Agent Skill for deploying high-throughput LLM serving endpoints on Cloud TPUs using vLLM-TorchTPU, compilation cache optimization, and Hugging Face integration.
---

# TPU High-Throughput Inference with vLLM-TorchTPU

This skill provides complete operational recipes for deploying open weights LLMs (Llama 3, Gemma, Mistral, Qwen) on Cloud TPUs with high throughput and low latency.

---

## 1. Engine Selection: vLLM-TorchTPU vs vLLM-TPU

| Feature | `vLLM-TorchTPU` (Recommended) | `vLLM-TPU` (JAX Backend) |
| :--- | :--- | :--- |
| **Backend** | Native PyTorch + TorchTPU | JAX / Flax / Pallas |
| **Installation** | `pip install vllm-torchtpu` | `pip install vllm-tpu` |
| **Hardware Fit** | Recommended on **TPU7x (Ironwood)**, Experimental on v6e/v5e | Strong on v5e, v6e |
| **PyTorch Ecosystem** | 100% PyTorch native model definition | Converts models into JAX compute graphs |
| **Warning** | **DO NOT mix dependencies** of both engines in the same virtualenv! |

---

## 2. Production Deployment Recipe

### Step 1: Virtual Environment Setup (Python 3.12 Required)
```bash
python3.12 -m venv ~/.venv-vllm-tpu
source ~/.venv-vllm-tpu/bin/activate
pip install --upgrade pip
pip install --extra-index-url https://download.pytorch.org/whl/cpu vllm-torchtpu
```

### Step 2: Configure Cache Paths
Initial execution compiles TPU execution graphs via XLA / PJRT. Without disk caching, every restart causes a full recompilation cycle:

```bash
mkdir -p /data/tpu_cache/tier3 /data/tpu_cache/vllm
export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/data/tpu_cache/tier3"
export VLLM_CACHE_ROOT="/data/tpu_cache/vllm"
export HF_HUB_ENABLE_HF_TRANSFER=1
```

### Step 3: Authenticate Hugging Face CLI
For gated model weights (Meta Llama 3 / 3.2):
```bash
# Accept terms on huggingface.co/meta-llama/Llama-3.2-1B-Instruct first!
hf auth login
```

### Step 4: Start OpenAI-Compatible Inference Server
```bash
vllm serve meta-llama/Llama-3.2-1B-Instruct \
  --tensor-parallel-size 1 \
  --max-model-len 4096 \
  --port 8000
```

---

## 3. Client Query Verification

Test the live endpoint with `curl`:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.2-1B-Instruct",
    "messages": [
      {"role": "user", "content": "Explain what a Cloud TPU is in three concise bullet points."}
    ],
    "max_tokens": 150,
    "temperature": 0.0
  }'
```

---

## 4. Scaling on GKE with Ray Serve / KubeRay

For production clusters with multi-host slices:
- Deploy using Google Cloud GKE reference architecture:
  `accelerated-platforms/docs/platforms/gke/base/use-cases/inference-ref-arch/online-inference-tpu/vllm-with-hf-model.md`
- Utilize Ray Serve to orchestrate tensor-parallel workers across TPU chip topologies.
