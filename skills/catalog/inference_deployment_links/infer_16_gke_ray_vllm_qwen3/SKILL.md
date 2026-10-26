---
name: infer-16-gke-ray-vllm-qwen3
description: "Google Kubernetes Engine Ray + vLLM TPU Qwen3 sample \u2014 Official GKE production-oriented tutorial/sample using Ray Serve and vLLM-TPU to deploy an ungated small model on a TPU v6e slice."
source_url: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve"
category: "inference_deployment_links"
---

# Agent Skill: Google Kubernetes Engine Ray + vLLM TPU Qwen3 sample

- **Official Source**: [https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve)
- **Category**: `inference_deployment_links`
- **Resource ID**: `infer_16_gke_ray_vllm_qwen3`
- **When to Activate**: Official GKE production-oriented tutorial/sample using Ray Serve and vLLM-TPU to deploy an ungated small model on a TPU v6e slice.

## Document Sections

- **Serve Qwen3 on GKE with Ray, vLLM, and TPU v6e (`ai-ml/gke-ray/tpu/get-started/serve`)**
- **Serve Qwen3-4B on a TPU slice with Ray Serve and vLLM**
  - **Prerequisites**
  - **About the base image**
  - **Deploy**
- **-> Running**
  - **Send a request**
  - **Watch it run: Ray Dashboard + Grafana**
- **Ray Dashboard, Serve tab + Cluster tab (live TPU utilization / HBM)**
- **open http://localhost:8265**
- **Grafana, the Ray "Serve LLM" dashboard is auto-loaded**
- **open http://localhost:3000  (default login admin / prom-operator)**
  - **How it works**
  - **Clean up**
  - **Next**
  - **File: `Dockerfile`**
- **Copyright 2026 Google LLC**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **Ray Serve LLM on TPU image.**
- **The vllm-tpu nightly ships protobuf 7, which is too new for Ray Serve (it**
- **removed FieldDescriptor.label in protobuf 6) and breaks deployment. Pin**
- **protobuf to 5.x, and drop grpcio-status to 1.70 to stay consistent. This is**
- **the smallest change that makes ray.serve.llm work on the current image.**
- **haproxy powers Ray Serve's high-throughput ingress (RAY_SERVE_ENABLE_HA_PROXY).**
- **The base image does not ship it.**
  - **File: `cloudbuild.yaml`**
- **Copyright 2026 Google LLC**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **Builds the Ray Serve LLM on TPU image (vllm-tpu base, protobuf and grpcio pins).**
- **Run with**
- **gcloud builds submit --config cloudbuild.yaml \**
- **--substitutions=_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1 .**
  - **File: `predict.py`**
- **Copyright 2026 Google LLC**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **[START gke_ai_ml_gke_ray_tpu_get_started_serve_predict]**
- **Match the model_id served by serve_qwen3_tpu.py (overridable via MODEL_ID).**
- **[END gke_ai_ml_gke_ray_tpu_get_started_serve_predict]**
  - **File: `ray-service.qwen3-tpu-v6e.yaml`**
- **Copyright 2026 Google LLC**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **[START gke_ai_ml_gke_ray_tpu_get_started_serve_rayservice]**
- **[END gke_ai_ml_gke_ray_tpu_get_started_serve_rayservice]**
  - **File: `serve_qwen3_tpu.py`**
- **Copyright 2026 Google LLC**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **[START gke_ai_ml_gke_ray_tpu_get_started_serve_qwen3_tpu]**
- **[END gke_ai_ml_gke_ray_tpu_get_started_serve_qwen3_tpu]**

## Key CLI Commands & Invocations

```bash
gcloud builds submit --config cloudbuild.yaml \
export KSA_NAME=ray-tpu-sa
export SERVE_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1
kubectl create configmap qwen3-serve-code --from-file=serve_qwen3_tpu.py
kubectl get rayservice qwen3-serve -o jsonpath='{.status.serviceStatus}{"\n"}'
kubectl port-forward svc/qwen3-serve-serve-svc 8000:8000 &
python predict.py "In one sentence, what is a TPU slice?"
curl http://localhost:8000/v1/chat/completions \
kubectl port-forward svc/qwen3-serve-head-svc 8265:8265
kubectl -n prometheus-system port-forward svc/prometheus-stack-grafana 3000:80
kubectl delete rayservice qwen3-serve
kubectl delete configmap qwen3-serve-code
kubectl port-forward svc/qwen3-serve-serve-svc 8000:8000
python predict.py "What is a TPU slice?"
```

## Key Environment Variables

- `JAX_PLATFORMS`
- `MODEL_IMPL_TYPE`

## Complete Technical Reference

# Serve Qwen3 on GKE with Ray, vLLM, and TPU v6e (`ai-ml/gke-ray/tpu/get-started/serve`)


# Serve Qwen3-4B on a TPU slice with Ray Serve and vLLM

Deploy
[`Qwen/Qwen3-4B-Instruct-2507`](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
(a small, text-only LLM, Apache-2.0) on a Cloud TPU v6e slice using Ray Serve and
vLLM. One config field, `accelerator_config.topology`, gang-schedules every vLLM
worker onto one TPU slice so they share the high-speed interconnect (ICI).

The sample assumes a GKE cluster with the Ray Operator add-on; see the top-level
get-started README for cluster setup.

## Prerequisites

Before you deploy, make sure you have:

- A GKE cluster with the Ray Operator add-on and a **TPU v6e** node pool
  (`2x4`, single host, 8 chips, `ct6e-standard-8t`). See [`../cluster/`](../cluster/).
- A Kubernetes ServiceAccount (`ray-tpu-sa`) with access to your model cache bucket.
- A serve image built from `Dockerfile` (vLLM-TPU nightly + a `protobuf<6` pin
  that `ray.serve.llm` needs). Build it with `cloudbuild.yaml`:
  ```bash
  gcloud builds submit --config cloudbuild.yaml \
    --substitutions=_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1 .
  ```
- `kubectl`, `envsubst`.

> Note:
> Qwen3-4B serves on vLLM-TPU's **JAX-native** (`flax_nnx`) path. It's in the
> architecture registry (`tpu_inference/models/jax/qwen3.py`), so there's no
> torchax fallback. Set `JAX_PLATFORMS=tpu,cpu` (not `tpu` alone): the weight
> loader stages through the CPU backend, so a `tpu`-only value crashes with
> `Unknown backend cpu`.

## About the base image

The image is a pinned nightly, `vllm/vllm-tpu:nightly-20260701-6af3d12-9969466`,
the first to bundle Ray 2.56, vLLM, and `ray.serve.llm` on TPU.

Nightly tags can be pruned from Docker Hub over time. For a durable setup,
mirror this image to your own Artifact Registry and reference that instead.

In the image, the pin locks the validated stack, and `Dockerfile` adds the
`protobuf<6` fix and `haproxy` for the high-throughput ingress with Ray Serve.
You enable high-throughput serving (Ray 2.56+) with env vars on the head and
worker:

- `RAY_SERVE_ENABLE_HA_PROXY` puts an HAProxy load balancer in front of each
  pod's Serve proxy.
- `RAY_SERVE_THROUGHPUT_OPTIMIZED` turns on throughput optimizations, including
  direct gRPC data-plane traffic between Serve replicas.
- `RAY_SERVE_LLM_ENABLE_DIRECT_STREAMING` streams requests and responses
  straight to the backend instead of through the ingress.
- `VLLM_USE_RAY_V2_EXECUTOR_BACKEND` runs vLLM on the Ray V2 executor backend.

These help most under high load with multiple replicas. See the
[KubeRay high-throughput guide](https://docs.ray.io/en/master/cluster/kubernetes/user-guides/kuberay-serve-high-throughput.html).

## Deploy

`serve_qwen3_tpu.py` is mounted into the pods from a ConfigMap. Create it, then
render the manifest (image + service account) and apply it:

```bash
export KSA_NAME=ray-tpu-sa
export SERVE_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1

kubectl create configmap qwen3-serve-code --from-file=serve_qwen3_tpu.py
envsubst < ray-service.qwen3-tpu-v6e.yaml | kubectl apply -f -
```

Wait for the service to become ready:

```bash
kubectl get rayservice qwen3-serve -o jsonpath='{.status.serviceStatus}{"\n"}'
# -> Running
```

You should see one head pod and one TPU worker pod; it holds all 8 chips of the slice.

## Send a request

Port-forward the serve endpoint, then use the included `predict.py` (an
OpenAI-client script) or a raw curl.

```bash
kubectl port-forward svc/qwen3-serve-serve-svc 8000:8000 &
```

With the script (`pip install openai` first):

```bash
python predict.py "In one sentence, what is a TPU slice?"
```

Or with curl:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-4B-Instruct-2507",
    "messages": [{"role": "user", "content": "In one sentence, what is a TPU slice?"}]
  }'
```

## Watch it run: Ray Dashboard + Grafana

The cluster ships with the Ray Dashboard and a Grafana stack (from
[`../cluster/`](../cluster/)). While the model serves:

```bash
# Ray Dashboard, Serve tab + Cluster tab (live TPU utilization / HBM)
kubectl port-forward svc/qwen3-serve-head-svc 8265:8265
#   open http://localhost:8265

# Grafana, the Ray "Serve LLM" dashboard is auto-loaded
kubectl -n prometheus-system port-forward svc/prometheus-stack-grafana 3000:80
#   open http://localhost:3000  (default login admin / prom-operator)
```

See [cluster/monitoring](../cluster/#monitoring) for the full metrics walkthrough.

## How it works

Looking at the serving module:

- `serve_qwen3_tpu.py` builds an OpenAI-compatible app with `build_openai_app`.
  The key line is `accelerator_config={"kind": "tpu", "topology": "2x4"}`: with a
  topology set, Ray Serve defers placement to the replica, which reserves a whole
  slice via a `SlicePlacementGroup`. Drop it and a multi-host model can fragment
  across slices and hang in `DEPLOYING`.
- `tensor_parallel_size` (8) equals the chip count of the `2x4` topology.
- The pods run a vLLM-TPU image with one dependency pin (see `Dockerfile`):
  `ray.serve.llm` needs `protobuf<6`, which the base nightly ships too new.

## Clean up

```bash
kubectl delete rayservice qwen3-serve
kubectl delete configmap qwen3-serve-code
```

## Next

- **[data](../data/)**. Prepare a DPO dataset and batch-predict with Ray Data.
- **[train](../train/)**. DPO fine-tune Qwen3-4B on a TPU slice with JaxTrainer.
- **[cluster/monitoring](../cluster/#monitoring)**. TPU metrics in the Ray Dashboard and Grafana.

## File: `Dockerfile`

```dockerfile
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Ray Serve LLM on TPU image.
#
# The vllm-tpu nightly ships protobuf 7, which is too new for Ray Serve (it
# removed FieldDescriptor.label in protobuf 6) and breaks deployment. Pin
# protobuf to 5.x, and drop grpcio-status to 1.70 to stay consistent. This is
# the smallest change that makes ray.serve.llm work on the current image.
ARG BASE_IMAGE=docker.io/vllm/vllm-tpu:nightly-20260701-6af3d12-9969466
FROM ${BASE_IMAGE}

# haproxy powers Ray Serve's high-throughput ingress (RAY_SERVE_ENABLE_HA_PROXY).
# The base image does not ship it.
RUN apt-get update \
    && apt-get install -y --no-install-recommends haproxy \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "protobuf==5.29.6" "grpcio-status==1.70.0"
```

## File: `cloudbuild.yaml`

```yaml
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Builds the Ray Serve LLM on TPU image (vllm-tpu base, protobuf and grpcio pins).
# Run with
#   gcloud builds submit --config cloudbuild.yaml \
#     --substitutions=_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1 .
substitutions:
  _IMAGE: "REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1"
steps:
  - name: gcr.io/cloud-builders/docker
    args: ["build", "-t", "${_IMAGE}", "-f", "Dockerfile", "."]
images:
  - "${_IMAGE}"
options:
  machineType: E2_HIGHCPU_8
```

## File: `predict.py`

```python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gke_ai_ml_gke_ray_tpu_get_started_serve_predict]
"""Send a prediction to the Qwen3-4B-Instruct-2507 Ray Serve endpoint.

Ray Serve exposes an OpenAI-compatible API, so you can use the openai client.
First port-forward the serve service:

    kubectl port-forward svc/qwen3-serve-serve-svc 8000:8000

Then:

    python predict.py "What is a TPU slice?"

Qwen3-4B-Instruct-2507 is a text-only model, so this client sends text prompts.
Install the client with:  pip install openai
"""
import argparse
import os

from openai import OpenAI

# Match the model_id served by serve_qwen3_tpu.py (overridable via MODEL_ID).
MODEL_ID = os.environ.get("MODEL_ID", "Qwen/Qwen3-4B-Instruct-2507")


def main() -> None:
    """Sends one prompt to the serve endpoint and prints the reply."""
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Text prompt to send to the model")
    parser.add_argument("--base-url", default="http://localhost:8000/v1")
    parser.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args()

    # Ray Serve doesn't require a real key. Any non-empty string works.
    client = OpenAI(base_url=args.base_url, api_key="not-needed")

    resp = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": args.prompt}],
        max_tokens=args.max_tokens,
    )
    print(resp.choices[0].message.content)


if __name__ == "__main__":
    main()
# [END gke_ai_ml_gke_ray_tpu_get_started_serve_predict]
```

## File: `ray-service.qwen3-tpu-v6e.yaml`

```yaml
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gke_ai_ml_gke_ray_tpu_get_started_serve_rayservice]
apiVersion: ray.io/v1
kind: RayService
metadata:
  name: qwen3-serve
spec:
  serveConfigV2: |
    http_options:
      host: 0.0.0.0
      port: 8000
    applications:
      - name: llm
        import_path: serve_qwen3_tpu:deployment
        runtime_env:
          env_vars:
            PYTHONPATH: "/home/ray/app"
            MODEL_ID: "Qwen/Qwen3-4B-Instruct-2507"
            ACCELERATOR_TYPE: "TPU-V6E"
            TPU_TOPOLOGY: "2x4"
            TENSOR_PARALLEL_SIZE: "8"
            VLLM_XLA_CACHE_PATH: "/tmp/vllm_xla_cache"
  rayClusterConfig:
    headGroupSpec:
      rayStartParams: {}
      template:
        spec:
          serviceAccountName: ${KSA_NAME}
          containers:
          - name: ray-head
            image: ${SERVE_IMAGE}
            imagePullPolicy: IfNotPresent
            ports:
            - {containerPort: 6379, name: gcs}
            - {containerPort: 8265, name: dashboard}
            - {containerPort: 10001, name: client}
            - {containerPort: 8000, name: serve}
            - {containerPort: 8080, name: metrics}
            env:
            # Wire the Ray dashboard's Metrics tab to the cluster's Prometheus and
            # Grafana. Without these, the time-series charts stay empty.
            # HOST vars are in-cluster service DNS (the head talks to them).
            - name: RAY_PROMETHEUS_HOST
              value: "http://prometheus-stack-kube-prom-prometheus.prometheus-system.svc:9090"
            - name: RAY_GRAFANA_HOST
              value: "http://prometheus-stack-grafana.prometheus-system.svc:80"
            # Datasource name must match the Grafana Prometheus datasource
            # (kube-prometheus-stack names it "Prometheus").
            - name: RAY_PROMETHEUS_NAME
              value: "Prometheus"
            # IFRAME host is what the browser loads the embedded panels from. Point it at
            # your Grafana URL (localhost:3000 when you port-forward Grafana to 3000).
            - name: RAY_GRAFANA_IFRAME_HOST
              value: "http://localhost:3000"
            # Ray Serve high-throughput ingress (Ray 2.56+). Needs haproxy in the
            # image (see Dockerfile). Set on head and worker.
            - name: RAY_SERVE_ENABLE_HA_PROXY
              value: "1"
            - name: RAY_SERVE_THROUGHPUT_OPTIMIZED
              value: "1"
            - name: RAY_SERVE_LLM_ENABLE_DIRECT_STREAMING
              value: "1"
            - name: VLLM_USE_RAY_V2_EXECUTOR_BACKEND
              value: "1"
            resources:
              limits: {cpu: "4", memory: 16Gi}
              requests: {cpu: "4", memory: 16Gi}
            volumeMounts:
            - name: app-code
              mountPath: /home/ray/app
          volumes:
          - name: app-code
            configMap:
              name: qwen3-serve-code
    workerGroupSpecs:
    - groupName: tpu-group
      replicas: 1
      minReplicas: 1
      maxReplicas: 1
      numOfHosts: 1
      rayStartParams: {}
      template:
        spec:
          serviceAccountName: ${KSA_NAME}
          containers:
          - name: ray-worker
            image: ${SERVE_IMAGE}
            imagePullPolicy: IfNotPresent
            resources:
              limits: {google.com/tpu: "8", cpu: "24", memory: 200Gi}
              requests: {google.com/tpu: "8", cpu: "24", memory: 200Gi}
            env:
            - name: JAX_PLATFORMS
              value: "tpu,cpu"
            - name: ENABLE_PJRT_COMPATIBILITY
              value: "true"
            # Ray Serve high-throughput ingress (Ray 2.56+). Needs haproxy in the
            # image (see Dockerfile). Set on head and worker.
            - name: RAY_SERVE_ENABLE_HA_PROXY
              value: "1"
            - name: RAY_SERVE_THROUGHPUT_OPTIMIZED
              value: "1"
            - name: RAY_SERVE_LLM_ENABLE_DIRECT_STREAMING
              value: "1"
            - name: VLLM_USE_RAY_V2_EXECUTOR_BACKEND
              value: "1"
            volumeMounts:
            - name: app-code
              mountPath: /home/ray/app
          volumes:
          - name: app-code
            configMap:
              name: qwen3-serve-code
          nodeSelector:
            cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
            cloud.google.com/gke-tpu-topology: 2x4
# [END gke_ai_ml_gke_ray_tpu_get_started_serve_rayservice]
```

## File: `serve_qwen3_tpu.py`

```python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gke_ai_ml_gke_ray_tpu_get_started_serve_qwen3_tpu]
"""Serve Qwen3-4B-Instruct-2507 on a Cloud TPU slice with Ray Serve + vLLM.

Qwen3 (`Qwen3ForCausalLM`) is in vLLM-TPU's JAX-native architecture registry
(`tpu_inference/models/jax/qwen3.py`), so it serves on the default `flax_nnx`
path: no `MODEL_IMPL_TYPE=vllm` / torchax fallback, and `JAX_PLATFORMS=tpu` is
enough (no CPU-backend workaround). It's a small (4B), text-only, ungated model,
which keeps this get-started sample simple. One `accelerator_config.topology`
field gang-schedules the workers onto a single slice.
"""
import os

from ray.serve.llm import LLMConfig, LLMServingArgs, build_openai_app

MODEL_ID = os.environ.get("MODEL_ID", "Qwen/Qwen3-4B-Instruct-2507")
MODEL_SOURCE = os.environ.get("MODEL_SOURCE", MODEL_ID)

ACCELERATOR_TYPE = os.environ.get("ACCELERATOR_TYPE", "TPU-V6E")
TPU_TOPOLOGY = os.environ.get("TPU_TOPOLOGY", "2x4")
TENSOR_PARALLEL_SIZE = int(os.environ.get("TENSOR_PARALLEL_SIZE", "8"))
MAX_MODEL_LEN = int(os.environ.get("MAX_MODEL_LEN", "8192"))

llm_config = LLMConfig(
    model_loading_config={"model_id": MODEL_ID, "model_source": MODEL_SOURCE},
    accelerator_type=ACCELERATOR_TYPE,
    accelerator_config={"kind": "tpu", "topology": TPU_TOPOLOGY},
    engine_kwargs={
        "tensor_parallel_size": TENSOR_PARALLEL_SIZE,
        "max_model_len": MAX_MODEL_LEN,
        "distributed_executor_backend": "ray",
    },
)

deployment = build_openai_app(LLMServingArgs(llm_configs=[llm_config]))
# [END gke_ai_ml_gke_ray_tpu_get_started_serve_qwen3_tpu]
```
