# Complete Reference Compendium: `legacy_docs` (4 Resources)

## `legacy_01_manage_tpus_legacy_api` — Manage TPU resources (legacy Cloud TPU API)
- **URL**: https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm
- **Description**: Legacy stop/delete cleanup reference; retain only for existing Cloud TPU API resources.
- **Dedicated Skill**: `skills/catalog/legacy_docs/legacy_01_manage_tpus_legacy_api/SKILL.md`
- **OKF Entity**: `okf/entities/legacy_docs/legacy_01_manage_tpus_legacy_api.okf.json`
- **Markdown Source**: `markdown/legacy_docs/legacy_01_manage_tpus_legacy_api.md`

### Sections (64) & Code Examples (26)
- Manage TPU resources
- Prerequisites
- Connect to a Cloud TPU
- gcloud
- Console
- List Cloud TPU resources
- gcloud
- Console
- Java
- Node.js
- Python
- TODO(developer): Update and un-comment below lines
- project_id = "your-project-id"
- zone = "us-central1-b"
- Example response:

## `legacy_02_run_calculation_jax_legacy` — Run JAX on a Cloud TPU VM — legacy API
- **URL**: https://docs.cloud.google.com/tpu/docs/run-calculation-jax
- **Description**: Older Cloud TPU API quickstart; use the Compute Engine quickstart for new provisioning.
- **Dedicated Skill**: `skills/catalog/legacy_docs/legacy_02_run_calculation_jax_legacy/SKILL.md`
- **OKF Entity**: `okf/entities/legacy_docs/legacy_02_run_calculation_jax_legacy.okf.json`
- **Markdown Source**: `markdown/legacy_docs/legacy_02_run_calculation_jax_legacy.md`

### Sections (16) & Code Examples (17)
- Run a calculation on a Cloud TPU VM using JAX
- Before you begin
- Required roles
- Create a Cloud TPU VM using `gcloud`
- Environment variable descriptions
- Connect to your Cloud TPU VM
- Install JAX on your Cloud TPU VM
- System check
- Perform a calculation
- Exit the Python interpreter
- Running JAX code on a TPU VM
- Clean up
- Performance notes
- Padding
- bfloat16 dtype

## `legacy_03_hf_training_scripts_legacy` — Hugging Face training scripts — legacy TPU instructions
- **URL**: https://huggingface.co/docs/transformers/run_scripts
- **Description**: The TPU section uses PyTorch/XLA and xla_spawn.py; do not treat it as the current TorchTPU setup.
- **Dedicated Skill**: `skills/catalog/legacy_docs/legacy_03_hf_training_scripts_legacy/SKILL.md`
- **OKF Entity**: `okf/entities/legacy_docs/legacy_03_hf_training_scripts_legacy.okf.json`
- **Markdown Source**: `markdown/legacy_docs/legacy_03_hf_training_scripts_legacy.md`

### Sections (11) & Code Examples (19)
- Hugging Face Transformers Training Scripts (Legacy PyTorch/XLA & `xla_spawn.py` Guide)
- Train with a script
- Setup
- Run a script
- Distributed training and mixed precision
- Run a script on a TPU
- Run a script with 🤗 Accelerate
- Use a custom dataset
- Test a script
- Resume training from checkpoint
- Share your model

## `legacy_04_pytorch_xla_legacy_notice` — PyTorch/XLA documentation (legacy notice)
- **URL**: https://docs.pytorch.org/xla/master/index.html
- **Description**: Retain only for migrating existing code: the documentation now labels PyTorch/XLA deprecated and replaced by TorchTPU.
- **Dedicated Skill**: `skills/catalog/legacy_docs/legacy_04_pytorch_xla_legacy_notice/SKILL.md`
- **OKF Entity**: `okf/entities/legacy_docs/legacy_04_pytorch_xla_legacy_notice.okf.json`
- **Markdown Source**: `markdown/legacy_docs/legacy_04_pytorch_xla_legacy_notice.md`

### Sections (30) & Code Examples (11)
- PyTorch/XLA Documentation (Legacy Deprecation Notice)
- Official Deprecation Notice (`https://docs.pytorch.org/xla/master/index.html`)
- Key Migration Differences (PyTorch/XLA -> TorchTPU)
- Legacy PyTorch/XLA Repository Reference (`pytorch/xla`)
- PyTorch/XLA
- Installation
- TPU
- - for venv
- python3.11 -m venv py311
- - for conda
- conda create -n py311 python=3.11
- Optional: if you're using custom kernels, install pallas dependencies
- Edit `cp310-cp310` to fit your desired Python version as needed
- C++11 ABI builds
- Github Doc Map
