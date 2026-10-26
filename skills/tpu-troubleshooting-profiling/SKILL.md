---
name: tpu-troubleshooting-profiling
description: Expert AI Agent Skill for profiling, performance optimization with XProf, health monitoring, and resolving dynamic shape recompilations on Google Cloud TPUs.
---

# TPU Troubleshooting, Health Monitoring & XProf Profiling Skill

This skill provides diagnostic protocols for monitoring TPU node health, debugging out-of-memory (OOM) errors, tracking compilation overhead, and capturing execution traces using Google Cloud Profiler (XProf).

---

## 1. Cloud TPU Health & Monitoring

Google Cloud TPU provides native Cloud Monitoring metrics under the namespace `tpu.googleapis.com`:

### Key Metrics to Monitor
- `tpu.googleapis.com/accelerator/duty_cycle`: Percentage of time Matrix Units (MXUs) are executing instructions. Values below 30% indicate data starvation or input pipelining bottlenecks.
- `tpu.googleapis.com/accelerator/memory_used`: Real-time High Bandwidth Memory (HBM) utilization.
- `tpu.googleapis.com/accelerator/network_transmit_bytes_rate`: Interconnect (ICI) bandwidth utilization across TPU pod slices.

### Inspect Instance Health via gcloud
```bash
# Check if TPU VM has encountered unhealthy hardware states
gcloud compute tpus tpu-vm describe my-tpu-v6e \
  --zone=us-central2-b \
  --format="yaml(state,health,healthDescription)"
```

---

## 2. Profiling with XProf (Cloud TPU Profiler)

XProf captures detailed trace viewers displaying host CPU activity, PJRT thread orchestration, XLA HLO module execution, and TPU MXU/VPU hardware execution intervals.

### Capturing Trace in TorchTPU
```python
import torch
import torch_tpu

# Profile with standard PyTorch profiler hooked into XProf
with torch.profiler.profile(
    activities=[
        torch.profiler.ProfilerActivity.CPU,
        torch.profiler.ProfilerActivity.TPU,
    ],
    schedule=torch.profiler.schedule(wait=1, warmup=2, active=3, repeat=1),
    on_trace_ready=torch.profiler.tensorboard_trace_handler('/data/tpu_logs/xprof_trace')
) as prof:
    for step, batch in enumerate(dataloader):
        outputs = model(batch)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        prof.step()
```

### Visualizing in TensorBoard
```bash
tensorboard --logdir=/data/tpu_logs/xprof_trace --port=6006
```

---

## 3. Resolving Dynamic Shapes & Repeated Recompilation

### Symptom: High Step Latency or Compilation Hanging
If each forward pass takes several seconds, TorchTPU or XLA is likely recompiling the computational graph for every novel tensor shape.

### Remediation Checklist:
1. **Pad Inputs to Fixed Bucket Sizes**:
   ```python
   # Pad sequence lengths to powers of 2 or predefined buckets (e.g., 128, 512, 1024, 2048)
   def pad_to_bucket(tokens, buckets=[128, 256, 512, 1024, 2048]):
       length = len(tokens)
       bucket = next(b for b in buckets if b >= length)
       return torch.nn.functional.pad(tokens, (0, bucket - length))
   ```
2. **Verify Persistent Compilation Cache**:
   Check that `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` points to a non-volatile disk.
3. **Avoid Non-Contiguous Views**:
   Complex stride manipulations in PyTorch can force physical layout copies on TPUs. Use `tensor.contiguous()` judiciously.

---

## 4. OOM (Out of Memory) Recovery Protocol

1. **Reduce Batch Size**: Scale down `per_device_batch_size`.
2. **Enable Activation Checkpointing (Gradient Checkpointing)**: Trades compute for memory by recalculating intermediate activations during the backward pass.
3. **Switch to bfloat16 or FP8**: Halves activation and weight footprint compared to FP32.
4. **Increase Parallelism**: Scale from Tensor Parallelism (TP=1) to TP=2, 4, or 8 across available TPU chips.
