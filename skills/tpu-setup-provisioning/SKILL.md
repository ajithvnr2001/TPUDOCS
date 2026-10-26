---
name: tpu-setup-provisioning
description: Expert AI Agent Skill for provisioning, sizing, quota management, and Cloud Storage integration for Google Cloud TPUs (v5e, v6e Trillium, and TPU7x Ironwood) via Compute Engine.
---

# TPU Setup & Provisioning Skill

This skill provides step-by-step instructions for selecting TPU topologies, requesting quota, managing Spot VMs, creating Compute Engine instances, and connecting cloud storage.

---

## 1. Prerequisites Checklist

Before executing any provisioning commands, ensure the following steps are complete in your GCP project:

1. **Enable Google Cloud APIs**:
   ```bash
   gcloud services enable compute.googleapis.com tpu.googleapis.com storage.googleapis.com
   ```
2. **Assign Required IAM Roles**:
   - `roles/tpu.admin` or `roles/compute.admin` (Provisioning)
   - `roles/storage.objectViewer` or `roles/storage.admin` (Bucket access)
   - `roles/monitoring.metricWriter` and `roles/logging.logWriter` (Diagnostics)
3. **Check Quota Availability**:
   - Quota metric names for TPU v6e: `tpu.googleapis.com/v6e_tpus`
   - Quota metric names for TPU7x: `tpu.googleapis.com/tpu7x_chips`
   - Region/zone availability: `us-central2-b`, `europe-west4-a`, `asia-southeast1-b`

---

## 2. Provisioning Commands (Compute Engine Modern Path)

> [!CAUTION]
> Do NOT use legacy `gcloud compute tpus create` without `--zone` or using the older Cloud TPU API. The modern approach creates TPU VMs inside Compute Engine.

### A. On-Demand Single-Host TPU VM (e.g., v6e-4)
```bash
gcloud compute tpus tpu-vm create my-tpu-v6e \
  --zone=us-central2-b \
  --accelerator-type=v6e-4 \
  --version=v2-alpha-tpuv6e
```

### B. Spot (Preemptible) TPU VM for Maximum Cost Savings
```bash
gcloud compute tpus tpu-vm create my-tpu-spot \
  --zone=us-central2-b \
  --accelerator-type=v6e-4 \
  --version=v2-alpha-tpuv6e \
  --spot
```

### C. Connect to the TPU VM
```bash
gcloud compute tpus tpu-vm ssh my-tpu-v6e --zone=us-central2-b
```

---

## 3. High Performance Storage Mounting

TPUs process massive data throughput. Local SSDs or Cloud Storage FUSE mounts must be tuned:

```bash
# Install gcsfuse if needed
gcloud storage buckets create gs://my-tpu-data-bucket --location=us-central2

# Mount bucket on TPU VM with high-throughput flags
mkdir -p /mnt/gcs_data
gcsfuse --implicit-dirs \
  --file-cache:max-size-mb=100000 \
  --stat-cache-ttl=1h \
  my-tpu-data-bucket /mnt/gcs_data
```

---

## 4. Teardown & Resource Cleanup

To prevent runaway billing after experiments:

```bash
gcloud compute tpus tpu-vm delete my-tpu-v6e --zone=us-central2-b --quiet
```
