#!/usr/bin/env bash
# Terminate and clean up Google Cloud TPU instance
set -euo pipefail

NAME="${1:-tpu-v6e-node}"
ZONE="${2:-us-central2-b}"

echo ">>> WARNING: Deleting Cloud TPU VM: ${NAME} in zone ${ZONE}..."
echo ">>> Verify that all checkpoints and logs have been synced to Cloud Storage before deleting."

gcloud compute tpus tpu-vm delete "${NAME}" --zone="${ZONE}" --quiet

echo ">>> TPU VM ${NAME} deleted successfully."
