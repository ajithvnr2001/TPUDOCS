# TPU Hardware Matrix & Architecture Reference

## 1. Cloud TPU Generations Comparison

| Generation | Code Name | Node/Chip Configs | HBM Memory per Chip | Interconnect | Supported Frameworks | Primary Workload | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TPU v4** | *Pecan* | v4-8 to v4-4096 | 32 GB HBM2 | 3D Torus ICI | PyTorch, JAX, TF | Large-scale LLM Training | Active |
| **TPU v5e** | *ViperLite* | v5litepod-1, 4, 8 to 256 | 16 GB HBM2 | 2D Torus ICI | PyTorch, JAX, TF | Cost-optimized Training & Serving | Active |
| **TPU v5p** | *Viper* | v5p-8 to v5p-8960 | 95 GB HBM3 | 3D Torus ICI | PyTorch, JAX, TF | Frontier Pre-training | Active |
| **TPU v6e** | *Trillium* | v6e-1, 4, 8 to 256 | 32 GB HBM3 | 2D/3D Torus ICI | TorchTPU, JAX | Cost-efficiency Inference & Fine-tuning | Recommended Current |
| **TPU7x** | *Ironwood* | Modular Pod Slices | High Bandwidth HBM | Next-Gen ICI | TorchTPU, JAX (**NO TensorFlow!**) | Ultra-fast LLM Inference & Training | Latest Generation |

> [!IMPORTANT]
> **TPU7x Ironwood Compatibility Alert**: TPU7x supports PyTorch (via TorchTPU) and JAX. It **does NOT support TensorFlow**. Attempting to deploy `tf.distribute.TPUStrategy` on TPU7x will fail.

---

## 2. Memory & Precision Matrix

| Architecture | MXU Precision Support | Vector Processing Unit (VPU) | Memory Bandwidth | Sparsity / SparseCore |
| :--- | :--- | :--- | :--- | :--- |
| **v5e** | bfloat16, int8 | FP32, bfloat16, int32 | ~819 GB/s per chip | SparseCore for recommendation models |
| **v6e (Trillium)** | bfloat16, int8, FP8 (E4M3, E5M2) | FP32, bfloat16, FP8, int32 | ~1.6 TB/s per chip | 2x Matrix Unit compute vs v5e |
| **TPU7x (Ironwood)** | bfloat16, FP8, int8, int4 | Optimized vectorized SIMD | Scaled Multi-TB/s | Specialized low-latency communication engines |

---

## 3. Quota & Consumption Models

- **On-Demand**: Full price, guaranteed availability during run, suitable for mission-critical serving.
- **Spot VMs**: Up to 60-70% discount compared to on-demand, subject to preemption. Ideal for fault-tolerant training checkpoints or test clusters.
- **Reservations**: Fixed commitment for dedicated capacity (1-year or 3-year commitments).
- **Flex-start**: Dynamic scheduling mode with deferred start windows for cost optimization.
