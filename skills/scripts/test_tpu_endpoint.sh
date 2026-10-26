#!/usr/bin/env bash
# Test the local vLLM-TorchTPU OpenAI-compatible inference endpoint
set -euo pipefail

PORT="${1:-8000}"
MODEL="${2:-meta-llama/Llama-3.2-1B-Instruct}"
PROMPT="${3:-Explain the architectural advantages of Google Cloud TPU v6e Trillium.}"

echo ">>> Sending test completion request to http://localhost:${PORT}/v1/chat/completions..."
curl -s "http://localhost:${PORT}/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"${PROMPT}\"}
    ],
    \"max_tokens\": 150,
    \"temperature\": 0.0
  }" | jq . || cat
echo ""
