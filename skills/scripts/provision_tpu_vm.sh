#!/usr/bin/env bash
# Provision a Google Cloud TPU VM via Compute Engine
set -euo pipefail

ZONE="${1:-us-central2-b}"
NAME="${2:-tpu-v6e-node}"
ACCELERATOR_TYPE="${3:-v6e-4}"
RUNTIME_VERSION="${4:-v2-alpha-tpuv6e}"

echo ">>> Creating Cloud TPU VM: ${NAME} in zone ${ZONE}..."
echo ">>> Type: ${ACCELERATOR_TYPE}, Runtime: ${RUNTIME_VERSION}"

gcloud compute tpus tpu-vm create "${NAME}" \
  --zone="${ZONE}" \
  --accelerator-type="${ACCELERATOR_TYPE}" \
  --version="${RUNTIME_VERSION}"

echo ">>> TPU VM ${NAME} created successfully."
echo ">>> Connect with: gcloud compute tpus tpu-vm ssh ${NAME} --zone=${ZONE}"
