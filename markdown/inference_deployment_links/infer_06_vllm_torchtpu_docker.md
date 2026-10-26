---
id: "infer_06_vllm_torchtpu_docker"
title: "vLLM-TorchTPU Docker guide"
url: "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/"
category: "Inference deployment links"
description: "Container images and build targets for TPU inference; distinguish runtime images from CI-only images."
crawled_at: "2026-10-26T12:47:33.598610+00:00"
crawler_engine: "Crawl4AI"
---

[ Skip to content ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#docker-images)
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU")
vLLM TorchTPU 
Docker Guide 
[ ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/?q= "Share")
Type to start searching
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
[ ![vLLM logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/vllm-logo-only-light.png) + ![PyTorch logo](https://vllm-torchtpu.readthedocs.io/en/latest/assets/logos/pytorch-icon-fullcolor.png) ](https://vllm-torchtpu.readthedocs.io/en/latest/ "vLLM TorchTPU") vLLM TorchTPU 
[ GitHub 
  * 113
  * 28

](https://github.com/vllm-project/vllm-torchtpu "Go to repository")
  * [ Home  ](https://vllm-torchtpu.readthedocs.io/en/latest/)
  * Getting Started  Getting Started 
    * [ Cloud TPU Setup  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/tpu_setup/)
    * [ Installation  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/installation/)
    * [ Quickstart  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/)
    * Docker Guide  [ Docker Guide  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/) Table of contents 
      * [ Pre-built Images on Docker Hub  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#pre-built-images-on-docker-hub)
        * [ Release Images (--target prod)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#release-images-target-prod)
        * [ Nightly Images (--target dev)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#nightly-images-target-dev)
        * [ Running the Container on a Cloud TPU VM  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#running-the-container-on-a-cloud-tpu-vm)
      * [ Image targets  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#image-targets)
        * [ ci:latest  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#cilatest)
        * [ dev:latest  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#devlatest)
        * [ prod:latest  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#prodlatest)
      * [ vllm-router  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#vllm-router)
      * [ Useful build arguments  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#useful-build-arguments)
  * User Guide  User Guide 
    * [ Supported Models & Features  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/supported_models/)
    * [ Parallelism & Scaling  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/parallelism/)
    * [ Multi-Host Serving  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/multihost/)
    * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/disaggregated_serving/)
    * [ Quantization  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/quantization/)
    * [ Speculative Decoding  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/speculative_decoding/)
    * [ Compilation & Warmup Cache  ](https://vllm-torchtpu.readthedocs.io/en/latest/user_guide/compilation_cache/)
    * Code Examples  Code Examples 
      * [ Offline Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_inference/)
      * [ Multi Modal Inference  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/multi_modal_inference/)
      * [ Offline LoRA  ](https://vllm-torchtpu.readthedocs.io/en/latest/api_and_code_examples/offline_lora_inference/)
  * Deployment & Recipes  Deployment & Recipes 
    * [ TPU v7x (Ironwood) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v7x_recipes/)
    * [ TPU v6e (Trillium) Recipes  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/v6e_recipes/)
    * [ Kubernetes & GKE  ](https://vllm-torchtpu.readthedocs.io/en/latest/deployment/kubernetes/)
  * Developer Guide  Developer Guide 
    * [ Contributing  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/contributing/)
    * [ Coding Guidance  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/coding_guidance/)
    * [ Optimization Best Practices  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/optimization_best_practices/)
    * [ TPU Patch Mechanism  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/tpu_patch_mechanism/)
    * [ Type Checking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/type_checking/)
    * [ Testing & CI  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/testing_and_ci/)
    * [ Benchmarking  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/benchmarking/)
    * [ Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/)
Profiling 
      * [ Offline (tpu_profiling.py)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/offline/)
      * [ Server-side Capture  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/server/)
      * [ Phased Profiling  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/phased/)
      * [ Disaggregated Serving (P/D)  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/disaggregated/)
      * [ Output Layout  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/output/)
      * [ Viewing Traces  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/viewing/)
      * [ Troubleshooting  ](https://vllm-torchtpu.readthedocs.io/en/latest/developers_guide/profiling/troubleshooting/)
  * Reference  Reference 
    * [ Environment Variables  ](https://vllm-torchtpu.readthedocs.io/en/latest/reference/env_vars/)
  * [ Roadmap  ](https://vllm-torchtpu.readthedocs.io/en/latest/roadmap/)


Table of contents 
  * [ Pre-built Images on Docker Hub  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#pre-built-images-on-docker-hub)
    * [ Release Images (--target prod)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#release-images-target-prod)
    * [ Nightly Images (--target dev)  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#nightly-images-target-dev)
    * [ Running the Container on a Cloud TPU VM  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#running-the-container-on-a-cloud-tpu-vm)
  * [ Image targets  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#image-targets)
    * [ ci:latest  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#cilatest)
    * [ dev:latest  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#devlatest)
    * [ prod:latest  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#prodlatest)
  * [ vllm-router  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#vllm-router)
  * [ Useful build arguments  ](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#useful-build-arguments)


[ ](https://github.com/vllm-project/vllm-torchtpu/edit/main/docs/getting_started/docker.md "Edit this page")
# Docker images[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#docker-images "Permanent link")
This folder contains the Dockerfile used to build the main image variants for vllm-torchtpu.
## Pre-built Images on Docker Hub[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#pre-built-images-on-docker-hub "Permanent link")
Official pre-built `vllm-torchtpu` Docker images are publicly available on Docker Hub at [`vllm/vllm-torchtpu`](https://hub.docker.com/r/vllm/vllm-torchtpu/tags). No registry authentication is required.  
| Docker Hub Tag  | Dockerfile Stage  | Installed Dependencies  | Intended Use  |  
| --- | --- | --- | --- |  
|  `vllm/vllm-torchtpu:latest`  
`vllm/vllm-torchtpu:vX.Y.Z`  | `--target prod`  | Runtime only (`--group vllm` + `vllm-torchtpu`)  | Production serving and inference  |  
|  `vllm/vllm-torchtpu:nightly`  
`vllm/vllm-torchtpu:nightly-YYYYMMDD-<commit>-<vllm>`  | `--target dev`  | Runtime + test & benchmark tools (`--group vllm --group test --extra benchmarking`, editable install)  | Local development, running `pytest`, type checking, and benchmarking  |  
Note
Release images (`:latest`, `:vX.Y.Z`) are built from `--target prod` and do **not** include test or benchmarking dependencies. For development, testing, or running `tools/typecheck_full.sh`, use `vllm/vllm-torchtpu:nightly` (`--target dev`). The intermediate `--target ci` base stage (which does not install `vllm-torchtpu` itself) is not published to Docker Hub; build it locally with `./docker/build_image.sh --target ci` if needed.
### Release Images (`--target prod`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#release-images-target-prod "Permanent link")
Release images are built from the `--target prod` Dockerfile stage and contain a standard runtime installation of `vllm` and `vllm-torchtpu`.
  * **Latest Stable Release** (`:latest`):

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-0-1)docker pull vllm/vllm-torchtpu:latest

```

  * **Pinned Version Release** (`:vX.Y.Z`, e.g., `v0.29.0`):

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-1-1)docker pull vllm/vllm-torchtpu:v0.29.0

```

### Nightly Images (`--target dev`)[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#nightly-images-target-dev "Permanent link")
Nightly images are built automatically every night from the `main` branch (`--target dev` stage, which includes the repository source, `--group test` dependencies, and `--extra benchmarking` tools):
  * **Latest Nightly Build** (`:nightly`):

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-2-1)docker pull vllm/vllm-torchtpu:nightly

```

  * **Date- and Commit-Pinned Nightly Tags** (`:nightly-YYYYMMDD-<commit>-<vllm-version>`):

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-3-1)docker pull vllm/vllm-torchtpu:nightly-20261019-88534b8-v0.31.0

```

Browse all available release and nightly tags at [`https://hub.docker.com/r/vllm/vllm-torchtpu/tags`](https://hub.docker.com/r/vllm/vllm-torchtpu/tags).
### Running the Container on a Cloud TPU VM[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#running-the-container-on-a-cloud-tpu-vm "Permanent link")
Include `--privileged`, `--net=host`, and `--shm-size 150gb` so the container can access the `/dev/vfio/*` TPU devices and shared host memory:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-1)sudo docker run -it --rm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-2)  --name $USER-vllm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-3)  --privileged \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-4)  --net=host \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-5)  -v /dev/shm:/dev/shm \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-6)  --shm-size 150gb \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-7)  -p 8000:8000 \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-8)  --entrypoint /bin/bash \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-4-9)  vllm/vllm-torchtpu:latest

```

## Image targets[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#image-targets "Permanent link")
###  `ci:latest`[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#cilatest "Permanent link")
CI image target built from `--target ci`.
Use this image for CI and test infrastructure. It includes extra tooling on top of the base runtime, such as:
  * `git`
  * `google-cloud-cli`
  * `gcsfuse`
  * `lsof`
  * `psmisc` / `fuser`


Note
This image does not install the `vllm-torchtpu` project itself, only the dependencies and tools needed for CI.
Example build using the standard helper script:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-5-1)./docker/build_image.sh --target ci -t ci:latest

```

###  `dev:latest`[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#devlatest "Permanent link")
Developer image target built from `--target dev`.
This image is based on the `ci` variant, copies the repository into the image, and installs the project in editable mode with the `vllm`/`test` dependency groups and the `benchmarking` extra:
  * dependencies: `--group vllm --group test --extra benchmarking`
  * intended for local development, debugging, and running tests


Example build using the standard helper script:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-6-1)./docker/build_image.sh --target dev -t dev:latest

```

###  `prod:latest`[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#prodlatest "Permanent link")
Production image target built from `--target prod`.
This image is intended for regular runtime usage. It performs a standard install of the project and is the best target for production-style execution.
Example build using the standard helper script:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-7-1)./docker/build_image.sh --target prod -t prod:latest

```

## vllm-router[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#vllm-router "Permanent link")
The `ci` and `dev` targets carry [vllm-router](https://github.com/vllm-project/router) at `/usr/local/bin/vllm-router`, built from the commit in the `VLLM_ROUTER_COMMIT` build arg. The disaggregated benchmark clients start it in prefill/decode mode when a serve config sets `AGENTX_PROXY=router`; the default stays the toy proxy in `examples/disagg`.
## Useful build arguments[¶](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#useful-build-arguments "Permanent link")
The Dockerfile also supports a few build arguments that may be useful in advanced workflows:
  * `VLLM_SOURCE`: when set, installs `vllm` from the copied local source tree


Example using the helper script with build arguments:

```
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-8-1)./docker/build_image.sh \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-8-2)  --target prod \
[](https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/docker/#__codelineno-8-3)  -t prod:latest

```

Back to top 
Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)