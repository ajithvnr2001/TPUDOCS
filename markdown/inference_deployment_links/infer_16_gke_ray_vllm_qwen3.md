---
id: "infer_16_gke_ray_vllm_qwen3"
title: "Google Kubernetes Engine Ray + vLLM TPU Qwen3 sample"
url: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve"
category: "Inference deployment links"
description: "Official GKE production-oriented tutorial/sample using Ray Serve and vLLM-TPU to deploy an ungated small model on a TPU v6e slice."
crawled_at: "2026-10-26T12:47:49.299819+00:00"
crawler_engine: "Crawl4AI"
---

[Skip to content](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#start-of-content)
## Navigation Menu
[](https://github.com/)
[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fkubernetes-engine-samples%2Ftree%2Fmain%2Fai-ml%2Fgke-ray%2Ftpu%2Fget-started%2Fserve)
Appearance settings
  * Platform
    * AI CODE CREATION
      * [GitHub CopilotWrite better code with AI](https://github.com/features/copilot)
      * [GitHub Copilot appDirect agents from issue to merge](https://github.com/features/ai/github-app)
      * [MCP RegistryIntegrate external tools](https://github.com/mcp)
    * DEVELOPER WORKFLOWS
      * [ActionsAutomate any workflow](https://github.com/features/actions)
      * [CodespacesInstant dev environments](https://github.com/features/codespaces)
      * [IssuesPlan and track work](https://github.com/features/issues)
      * [Code ReviewManage code changes](https://github.com/features/code-review)
      * [Code QualityEnforce quality at merge](https://github.com/features/code-quality)
    * APPLICATION SECURITY
      * [GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)
      * [Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)
      * [Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)
    * EXPLORE
      * [Why GitHub](https://github.com/why-github)
      * [Documentation](https://docs.github.com)
      * [Blog](https://github.blog)
      * [Changelog](https://github.blog/changelog)
      * [Marketplace](https://github.com/marketplace)
[View all features](https://github.com/features)
  * Solutions
    * BY COMPANY SIZE
      * [Enterprises](https://github.com/enterprise)
      * [Small and medium teams](https://github.com/team)
      * [Startups](https://github.com/enterprise/startups)
      * [Nonprofits](https://github.com/solutions/industry/nonprofits)
    * BY USE CASE
      * [App Modernization](https://github.com/solutions/use-case/app-modernization)
      * [DevSecOps](https://github.com/solutions/use-case/devsecops)
      * [DevOps](https://github.com/solutions/use-case/devops)
      * [CI/CD](https://github.com/solutions/use-case/ci-cd)
      * [View all use cases](https://github.com/solutions/use-case)
    * BY INDUSTRY
      * [Healthcare](https://github.com/solutions/industry/healthcare)
      * [Financial services](https://github.com/solutions/industry/financial-services)
      * [Manufacturing](https://github.com/solutions/industry/manufacturing)
      * [Government](https://github.com/solutions/industry/government)
      * [See all industries](https://github.com/solutions/industry)
[View all solutions](https://github.com/solutions)
  * Resources
    * EXPLORE BY TOPIC
      * [AI](https://github.com/resources/articles?topic=ai)
      * [Software Development](https://github.com/resources/articles?topic=software-development)
      * [DevOps](https://github.com/resources/articles?topic=devops)
      * [Security](https://github.com/resources/articles?topic=security)
      * [View all topics](https://github.com/resources/articles)
    * EXPLORE BY TYPE
      * [Customer stories](https://github.com/customer-stories)
      * [Events & webinars](https://github.com/resources/events)
      * [Ebooks & reports](https://github.com/resources/whitepapers)
      * [Business insights](https://github.com/solutions/executive-insights)
      * [GitHub Skills](https://skills.github.com)
    * SUPPORT & SERVICES
      * [Documentation](https://docs.github.com)
      * [Customer support](https://support.github.com)
      * [Community forum](https://github.com/orgs/community/discussions)
      * [Trust center](https://github.com/trust-center)
      * [Partners](https://github.com/partners)
[View all resources](https://github.com/resources)
  * Open Source
    * COMMUNITY
      * [GitHub SponsorsFund open source developers](https://github.com/open-source/sponsors)
    * PROGRAMS
      * [Security Lab](https://securitylab.github.com)
      * [Maintainer Community](https://maintainers.github.com)
      * [GitHub Stars](https://stars.github.com)
      * [Archive Program](https://archiveprogram.github.com)
    * REPOSITORIES
      * [Topics](https://github.com/topics)
      * [Trending](https://github.com/trending)
      * [Collections](https://github.com/collections)
  * Enterprise
    * ENTERPRISE SOLUTIONS
      * [Enterprise platformAI-powered developer platform](https://github.com/enterprise)
    * AVAILABLE ADD-ONS
      * [GitHub Advanced SecurityEnterprise-grade security features](https://github.com/security/advanced-security)
      * [Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)
      * [Premium SupportEnterprise-grade 24/7 support](https://github.com/enterprise/premium-support)
  * [Pricing](https://github.com/pricing)


Search`/`
[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fkubernetes-engine-samples%2Ftree%2Fmain%2Fai-ml%2Fgke-ray%2Ftpu%2Fget-started%2Fserve)
[Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&source=header-repo&source_repo=GoogleCloudPlatform%2Fkubernetes-engine-samples)
Appearance settings
You signed in with another tab or window. [Reload](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve) to refresh your session. Dismiss alert
{{ message }}
  1. [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
  2. [kubernetes-engine-samples](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples)


## Repository navigation
  * [Code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples)
  * [Issues23 (23)](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/issues)
  * [Pull requests128 (128)](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/pulls)
  * [Discussions](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/discussions)
  * [Actions](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/actions)
  * [Projects](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/projects)
  * [Security and quality](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/security)
  * [Insights](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/pulse)


More items
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples)
## Collapse file tree
## Files
main
Search this repository(forward slash)` forward slash/`
  * .github
  * ai-ml
    * adk-vertex
    * adk-vllm
    * anthropic-agent-sandbox
    * axolotl-multimodal-finetuning-gemma
    * gke-a100-jax
    * gke-model-armor
    * gke-online-serving-single-gpu
    * gke-ray
      * gke-platform
      * kueue-concurrent-admission
      * rayserve
      * raytrain
      * tpu
        * dws
        * get-started
          * cluster
          * data
          * serve
            * Dockerfile
            * README.md
            * cloudbuild.yaml
            * predict.py
            * ray-service.qwen3-tpu-v6e.yaml
            * serve_qwen3_tpu.py
          * train
          * README.md
        * ray-job.tpu-v6e-multihost.yaml
        * ray-job.tpu-v6e-singlehost.yaml
        * tpu_list_devices.py
    * gke-slurm
    * gke-tpu-dynamic-slicing
    * inference-optimized-gateway
    * infw-gw
    * llm-finetuning-gemma
    * llm-multihost-gpus-tensorrt-llm
    * llm-multihost-gpus
    * llm-multihost-tpus-saxml
    * llm-multiple-gpus
    * llm-quantize
    * llm-serving-gemma
    * llm-serving-llama
    * llm-serving-optimum-tpu
    * llm-serving-tpus-jetstream
    * llm-training-jax-tpu-gemma3
    * maxdiffusion-tpu
    * maxtext-rl-on-gke
    * mix-train-and-inference
    * nemo-rl-on-gke
    * notebooks
    * physical-ai-on-gke
    * t5-model-serving
    * verl-on-gke
    * vllm-tpu
  * app-design-center
  * autopilot
  * autoscaling
  * batch
  * cost-optimization
  * databases
  * demos
  * hpc
  * management
  * networking
  * observability
  * quickstarts
  * security
  * service-mesh
  * streaming
  * troubleshooting
  * windows
  * workloads
  * .gitignore
  * LICENSE
  * README.md


## Breadcrumbs
  1. [kubernetes-engine-samples](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main)
  2. /[ai-ml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml)
  3. /[gke-ray](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray)
  4. /[tpu](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu)
  5. /[get-started](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started)


/
# serve
/
Copy path
## Directory actions
## More options
More options
## Directory actions
## More options
More options
## Latest commit
## History
[History](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/commits/main/ai-ml/gke-ray/tpu/get-started/serve)
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/commits/main/ai-ml/gke-ray/tpu/get-started/serve)History
## Breadcrumbs
  1. [kubernetes-engine-samples](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main)
  2. /[ai-ml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml)
  3. /[gke-ray](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray)
  4. /[tpu](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu)
  5. /[get-started](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started)


/
# serve
/
Copy path
Top
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
### parent directory
[..](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started)  |  
| [Dockerfile](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/Dockerfile "Dockerfile")  | [Dockerfile](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/Dockerfile "Dockerfile")  |   |   |  
| [README.md](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/README.md "README.md")  | [README.md](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/README.md "README.md")  |   |   |  
| [cloudbuild.yaml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/cloudbuild.yaml "cloudbuild.yaml")  | [cloudbuild.yaml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/cloudbuild.yaml "cloudbuild.yaml")  |   |   |  
| [predict.py](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/predict.py "predict.py")  | [predict.py](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/predict.py "predict.py")  |   |   |  
| [ray-service.qwen3-tpu-v6e.yaml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/ray-service.qwen3-tpu-v6e.yaml "ray-service.qwen3-tpu-v6e.yaml")  | [ray-service.qwen3-tpu-v6e.yaml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/ray-service.qwen3-tpu-v6e.yaml "ray-service.qwen3-tpu-v6e.yaml")  |   |   |  
| [serve_qwen3_tpu.py](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/serve_qwen3_tpu.py "serve_qwen3_tpu.py")  | [serve_qwen3_tpu.py](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/serve/serve_qwen3_tpu.py "serve_qwen3_tpu.py")  |   |   |  
| View all files |  
## [README.md](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#readme)
Outline
# Serve Qwen3-4B on a TPU slice with Ray Serve and vLLM
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#serve-qwen3-4b-on-a-tpu-slice-with-ray-serve-and-vllm)
Deploy [`Qwen/Qwen3-4B-Instruct-2507`](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) (a small, text-only LLM, Apache-2.0) on a Cloud TPU v6e slice using Ray Serve and vLLM. One config field, `accelerator_config.topology`, gang-schedules every vLLM worker onto one TPU slice so they share the high-speed interconnect (ICI).
The sample assumes a GKE cluster with the Ray Operator add-on; see the top-level get-started README for cluster setup.
## Prerequisites
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#prerequisites)
Before you deploy, make sure you have:
  * A GKE cluster with the Ray Operator add-on and a **TPU v6e** node pool (`2x4`, single host, 8 chips, `ct6e-standard-8t`). See [`../cluster/`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/cluster).
  * A Kubernetes ServiceAccount (`ray-tpu-sa`) with access to your model cache bucket.
  * A serve image built from `Dockerfile` (vLLM-TPU nightly + a `protobuf<6` pin that `ray.serve.llm` needs). Build it with `cloudbuild.yaml`: 

```
gcloud builds submit --config cloudbuild.yaml \
  --substitutions=_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1 .
```

  * `kubectl`, `envsubst`.


> Note: Qwen3-4B serves on vLLM-TPU's **JAX-native** (`flax_nnx`) path. It's in the architecture registry (`tpu_inference/models/jax/qwen3.py`), so there's no torchax fallback. Set `JAX_PLATFORMS=tpu,cpu` (not `tpu` alone): the weight loader stages through the CPU backend, so a `tpu`-only value crashes with `Unknown backend cpu`.
## About the base image
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#about-the-base-image)
The image is a pinned nightly, `vllm/vllm-tpu:nightly-20260701-6af3d12-9969466`, the first to bundle Ray 2.56, vLLM, and `ray.serve.llm` on TPU.
Nightly tags can be pruned from Docker Hub over time. For a durable setup, mirror this image to your own Artifact Registry and reference that instead.
In the image, the pin locks the validated stack, and `Dockerfile` adds the `protobuf<6` fix and `haproxy` for the high-throughput ingress with Ray Serve. You enable high-throughput serving (Ray 2.56+) with env vars on the head and worker:
  * `RAY_SERVE_ENABLE_HA_PROXY` puts an HAProxy load balancer in front of each pod's Serve proxy.
  * `RAY_SERVE_THROUGHPUT_OPTIMIZED` turns on throughput optimizations, including direct gRPC data-plane traffic between Serve replicas.
  * `RAY_SERVE_LLM_ENABLE_DIRECT_STREAMING` streams requests and responses straight to the backend instead of through the ingress.
  * `VLLM_USE_RAY_V2_EXECUTOR_BACKEND` runs vLLM on the Ray V2 executor backend.


These help most under high load with multiple replicas. See the [KubeRay high-throughput guide](https://docs.ray.io/en/master/cluster/kubernetes/user-guides/kuberay-serve-high-throughput.html).
## Deploy
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#deploy)
`serve_qwen3_tpu.py` is mounted into the pods from a ConfigMap. Create it, then render the manifest (image + service account) and apply it:

```
export KSA_NAME=ray-tpu-sa
export SERVE_IMAGE=REGION-docker.pkg.dev/PROJECT_ID/ray-tpu/serve-qwen-tpu:v1

kubectl create configmap qwen3-serve-code --from-file=serve_qwen3_tpu.py
envsubst < ray-service.qwen3-tpu-v6e.yaml | kubectl apply -f -
```

Wait for the service to become ready:

```
kubectl get rayservice qwen3-serve -o jsonpath='{.status.serviceStatus}{"\n"}'
# -> Running
```

You should see one head pod and one TPU worker pod; it holds all 8 chips of the slice.
## Send a request
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#send-a-request)
Port-forward the serve endpoint, then use the included `predict.py` (an OpenAI-client script) or a raw curl.

```
kubectl port-forward svc/qwen3-serve-serve-svc 8000:8000 &
```

With the script (`pip install openai` first):

```
python predict.py "In one sentence, what is a TPU slice?"
```

Or with curl:

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-4B-Instruct-2507",
    "messages": [{"role": "user", "content": "In one sentence, what is a TPU slice?"}]
  }'
```

## Watch it run: Ray Dashboard + Grafana
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#watch-it-run-ray-dashboard--grafana)
The cluster ships with the Ray Dashboard and a Grafana stack (from [`../cluster/`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/cluster)). While the model serves:

```
# Ray Dashboard, Serve tab + Cluster tab (live TPU utilization / HBM)
kubectl port-forward svc/qwen3-serve-head-svc 8265:8265
#   open http://localhost:8265

# Grafana, the Ray "Serve LLM" dashboard is auto-loaded
kubectl -n prometheus-system port-forward svc/prometheus-stack-grafana 3000:80
#   open http://localhost:3000  (default login admin / prom-operator)
```

See [cluster/monitoring](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/cluster/#monitoring) for the full metrics walkthrough.
## How it works
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#how-it-works)
Looking at the serving module:
  * `serve_qwen3_tpu.py` builds an OpenAI-compatible app with `build_openai_app`. The key line is `accelerator_config={"kind": "tpu", "topology": "2x4"}`: with a topology set, Ray Serve defers placement to the replica, which reserves a whole slice via a `SlicePlacementGroup`. Drop it and a multi-host model can fragment across slices and hang in `DEPLOYING`.
  * `tensor_parallel_size` (8) equals the chip count of the `2x4` topology.
  * The pods run a vLLM-TPU image with one dependency pin (see `Dockerfile`): `ray.serve.llm` needs `protobuf<6`, which the base nightly ships too new.


## Clean up
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#clean-up)

```
kubectl delete rayservice qwen3-serve
kubectl delete configmap qwen3-serve-code
```

## Next
[](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/tpu/get-started/serve#next)
  * **[data](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/data)**. Prepare a DPO dataset and batch-predict with Ray Data.
  * **[train](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/train)**. DPO fine-tune Qwen3-4B on a TPU slice with JaxTrainer.
  * **[cluster/monitoring](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/get-started/cluster/#monitoring)**. TPU metrics in the Ray Dashboard and Grafana.


## Footer
[ ](https://github.com) © 2026 GitHub, Inc. 
### Footer navigation
  * [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
  * [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
  * [Security](https://github.com/security)
  * [Status](https://www.githubstatus.com/)
  * [Community](https://github.community/)
  * [Docs](https://docs.github.com/)
  * [Contact](https://support.github.com?tags=dotcom-footer)
  * Manage cookies 
  * Do not share my personal information 


You can’t perform that action at this time.