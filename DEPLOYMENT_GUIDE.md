# Practical Guide: Deploying NVIDIA Workloads to Google Cloud TPUs

This guide provides the authoritative step-by-step instructions for porting and deploying machine learning workloads—originally developed for NVIDIA CUDA GPUs—onto Google Cloud TPUs.

---

## 1. Workload Strategy & Framework Paradigm
- **Migrate the workload, not NVIDIA hardware**: These instructions specifically target Google Cloud TPUs.
- **PyTorch Strategy**: For existing PyTorch code, start with **TorchTPU**. Google officially recommends TorchTPU instead of the deprecated PyTorch/XLA path for all new PyTorch TPU workloads.
- **LLM Serving Strategy**: For PyTorch-based LLM serving, use **vLLM-TorchTPU** (the native PyTorch out-of-tree plugin) or vLLM-TPU (JAX-native). Do not mix their dependencies.

---

## 2. Provisioning a Compatible Cloud TPU VM
1. Enable billing and the required Google Cloud APIs (`compute.googleapis.com`, `tpu.googleapis.com`).
2. Obtain TPU quota in your chosen region/zone (e.g., `us-central2-b`).
3. Follow the Compute Engine TPU quickstart to create your TPU VM instance.
4. Start on a single host (e.g. `v6e-4` or `v6e-8`) rather than a multi-host Kubernetes cluster unless you already require container orchestration.
5. **Hardware compatibility checks**:
   - `vLLM-TorchTPU` currently recommends **TPU7x (Ironwood)** and marks `v6e`, `v5e`, and `v5p` experimental.
   - Its installation guide strictly requires **Python 3.12**.

```bash
# Provision a single-host TPU v6e VM via Compute Engine
gcloud compute tpus tpu-vm create tpu-quickstart-node \
  --zone=us-central2-b \
  --accelerator-type=v6e-4 \
  --version=v2-alpha-tpuv6e

# Connect to the instance
gcloud compute tpus tpu-vm ssh tpu-quickstart-node --zone=us-central2-b
```

---

## 3. Custom PyTorch Environment & Hardware Smoke Test
For custom PyTorch training or inference, create a dedicated Python 3.12 environment on the TPU VM:

```bash
# 1. Create and activate virtual environment
python3.12 -m venv .venv-tpu
source .venv-tpu/bin/activate

# 2. Install TorchTPU released package
pip install --upgrade pip
pip install torch_tpu==0.2.0 --extra-index-url https://download.pytorch.org/whl/cpu

# 3. Execute hardware smoke test
python -c 'import torch; import torch_tpu; x = torch.ones((4, 4), device="tpu"); print((x @ x).cpu())'
```
*Note: This confirms hardware access and runtime linkage; it is not deployment of your model.*

---

## 4. Incremental Workload Porting from CUDA to TPU
1. **Device Placement**: Replace `.cuda()` or `.to("cuda")` calls with `.to("tpu")`.
2. **CUDA APIs**: Consult the CUDA-to-TPU API Reference for `torch.cuda` calls:
   - `torch.cuda.device_count()` $\rightarrow$ `torch.tpu.device_count()`
   - `torch.cuda.synchronize()` $\rightarrow$ `torch.tpu.synchronize()`
3. **Distributed Execution**: Use the documented `tpu_dist` backend rather than NCCL:
   ```python
   torch.distributed.init_process_group("tpu_dist")
   ```
4. **CUDA Extensions & Operators**: Review CUDA-only extensions (`.cu` kernels, custom Triton code) instead of assuming a device string replacement is sufficient. Use **Tokamax** for prebuilt high-performance kernels or **Pallas** for custom TPU kernel authoring.
5. **Execution Order**:
   - First verify correctness in **eager mode**.
   - Then evaluate `torch.compile(..., backend="openxla")` with appropriate numerical precision (`bfloat16`).

---

## 5. Deploying LLM Serving with vLLM-TorchTPU
For an OpenAI-compatible LLM inference server, isolate dependencies in a separate Python 3.12 environment:

```bash
# 1. Create and activate serving environment
python3.12 -m venv .venv-vllm-tpu
source .venv-vllm-tpu/bin/activate

# 2. Install native vLLM-TorchTPU package
pip install --upgrade pip
pip install --extra-index-url https://download.pytorch.org/whl/cpu vllm-torchtpu

# 3. Configure compilation and artifact caching
export TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT="/data/tpu_cache/tier3"
export VLLM_CACHE_ROOT="/data/tpu_cache/vllm"
mkdir -p "$TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT" "$VLLM_CACHE_ROOT"

# 4. Hugging Face Authentication (accept model license on HF website first)
hf auth login

# 5. Launch the OpenAI-compatible vLLM serving daemon
vllm serve meta-llama/Llama-3.2-1B-Instruct \
  --tensor-parallel-size 1 \
  --max-model-len 4096 \
  --port 8000
```
> [!IMPORTANT]
> - Obtain access to the Llama model on Hugging Face and accept its license before serving it; authentication does not itself grant gated model access.
> - Do not mix this installation with the separate `vllm-tpu`/JAX backend.

---

## 6. Verification and Endpoint Querying
From a second terminal on the TPU VM (or across a secure VPC network), send a chat completion request:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.2-1B-Instruct",
    "messages": [
      {"role": "user", "content": "Explain what a TPU is."}
    ],
    "max_tokens": 128,
    "temperature": 0.0
  }'
```
*Security note: Keep initial tests private on localhost or behind VPN/IAM proxy before exposing public endpoints.*

---

## 7. Compilation Cache & Scaling Considerations
- **Initial Compilation**: Expect 2–10 minutes of initial graph compilation upon starting a new model or context size.
- **Persistent Cache**: Ensure `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` points to a persistent disk so restarts do not re-trigger graph compilation.
- **Production Scaling**: When moving beyond a single host, use the official GKE reference architecture with Ray Serve or KubeRay.

---

## 8. JAX & TensorFlow Alternatives
- **JAX Workloads**: If your existing codebase uses JAX, install accelerator dependencies via `pip install "jax[tpu]"` and utilize **MaxText** (for LLMs) or **MaxDiffusion** (for image generation) instead of rewriting into PyTorch.
- **TensorFlow / Keras**: Use `tf.distribute.TPUStrategy` on TPU v4 or v5e. **Note: TPU7x (Ironwood) does not support TensorFlow**.

---

## 9. Cleanup & Teardown
Clean up test infrastructure when experimentation concludes to prevent ongoing charges:

```bash
# Delete Compute Engine TPU VM instance
gcloud compute instances delete TPU_NAME --zone=ZONE
# Or via TPU VM management:
gcloud compute tpus tpu-vm delete TPU_NAME --zone=ZONE --quiet
```
*Ensure all model weights, checkpoints, and logs are synced to Google Cloud Storage (`gs://...`) before deletion.*
