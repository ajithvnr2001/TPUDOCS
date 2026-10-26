#!/usr/bin/env python3
"""
Builds true end-to-end AI Agent Skills (/data/tpu/skills/) and
Google Open Knowledge Format (OKF v1.0) (/data/tpu/okf/) from all 85 cleaned
official TPU documents + the 9-step NVIDIA-to-TPU deployment guide.
"""

import json
import os
import re
from datetime import datetime, timezone

BASE_DIR = "/data/tpu"

TPU_HARDWARE_ENTITIES = [
    ("TPU7x", "Ironwood", "Google Cloud 7th-gen TPU (Ironwood) for large-scale training and inference; supports PyTorch and JAX"),
    ("v6e", "Trillium", "Google Cloud 6th-gen TPU (Trillium) with 2x MXU performance and 32GB HBM per chip"),
    ("v5p", "TPU v5p", "High-performance 5th-gen TPU pod architecture for large-scale training"),
    ("v5e", "TPU v5e", "Cost-efficient 5th-gen TPU (`v5litepod`) for training and inference"),
    ("v4", "TPU v4", "4th-gen Cloud TPU pod architecture"),
]

FRAMEWORK_ENTITIES = [
    ("TorchTPU", "torch_tpu", "Native PyTorch backend for Cloud TPU replacing deprecated PyTorch/XLA"),
    ("vLLM-TorchTPU", "vllm-torchtpu", "PyTorch-native vLLM plugin for LLM serving on Cloud TPU via TorchTPU"),
    ("vLLM-TPU", "vllm-tpu", "JAX-backed vLLM plugin for TPU serving"),
    ("SGLang-TorchTPU", "sglang-torchtpu", "SGLang inference engine backend for Cloud TPU via TorchTPU"),
    ("JAX", "jax", "High-performance numerical computing and ML framework with native XLA/TPU support"),
    ("MaxText", "maxtext", "Google AI-Hypercomputer flagship JAX LLM training and fine-tuning framework"),
    ("MaxDiffusion", "maxdiffusion", "Google AI-Hypercomputer JAX diffusion model training and serving framework"),
    ("TorchTitan", "torchtitan", "PyTorch native distributed pre-training framework with TorchTPU support"),
    ("Pallas", "jax.experimental.pallas", "JAX kernel language for writing custom Mosaic TPU kernels"),
    ("Tokamax", "tokamax", "OpenXLA custom kernel library and autotuner for TPU and GPU"),
    ("TPUStrategy", "tf.distribute.TPUStrategy", "TensorFlow synchronous distributed training strategy for TPUs"),
    ("KubeRay", "kuberay", "Kubernetes operator for deploying distributed Ray clusters on GKE with TPUs"),
    ("XProf", "xprof", "Performance profiling tool for TPU workloads in PyTorch, JAX, and TensorFlow"),
]

def parse_markdown_structure(md_body):
    """Extracts sections, code blocks, CLI commands, env vars, tables, and assertions from Markdown."""
    sections = []
    current_heading = "Overview"
    current_level = 1
    current_lines = []

    for line in md_body.splitlines():
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            if current_lines or sections:
                sections.append({
                    "heading": current_heading,
                    "level": current_level,
                    "content": "\n".join(current_lines).strip()
                })
            current_level = len(m.group(1))
            current_heading = m.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_lines or not sections:
        sections.append({
            "heading": current_heading,
            "level": current_level,
            "content": "\n".join(current_lines).strip()
        })

    # Extract fenced code blocks
    code_blocks = []
    for m in re.finditer(r"```([a-zA-Z0-9_-]*)\n(.*?)```", md_body, re.S):
        lang = m.group(1).strip() or "text"
        code = m.group(2).strip()
        if code:
            code_blocks.append({"language": lang, "code": code})

    # Extract CLI commands (gcloud, kubectl, pip, uv, vllm, python, ray, docker, huggingface-cli, hf)
    cli_commands = []
    cmd_pattern = re.compile(r"^\s*(\$?\s*(?:gcloud|kubectl|pip|pip3|uv|vllm|python|python3|torchrun|ray|docker|huggingface-cli|hf|export|curl|git|bash)\b[^\n]*)", re.M)
    for cb in code_blocks:
        for cm in cmd_pattern.finditer(cb["code"]):
            cmd = cm.group(1).lstrip("$ ").strip()
            if cmd and cmd not in cli_commands:
                cli_commands.append(cmd)

    # Extract environment variables
    env_vars = sorted(set(re.findall(r"\b([A-Z][A-Z0-9_]{2,})=", md_body)))
    env_vars = [e for e in env_vars if any(k in e for k in ("TPU", "XLA", "VLLM", "TORCH", "JAX", "HF", "RAY", "GKE", "ZONE", "PROJECT", "MODEL", "CACHE", "RANK", "LOCAL", "MASTER", "PJRT"))]

    # Extract markdown tables
    tables = []
    lines = md_body.splitlines()
    i = 0
    while i < len(lines):
        if "|" in lines[i] and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?---", lines[i + 1]):
            headers = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and "|" in lines[i]:
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(row)
                i += 1
            tables.append({"headers": headers, "rows": rows[:50]})
        else:
            i += 1

    return {
        "sections": sections,
        "code_blocks": code_blocks,
        "cli_commands": cli_commands[:50],
        "environment_variables": env_vars[:50],
        "tables": tables[:20],
    }

def extract_semantic_triples(r, parsed, md_body):
    rid = f"tpu_doc:{r['id']}"
    triples = [
        {"subject": rid, "predicate": "rdf:type", "object": "okf:TechnicalDocumentation"},
        {"subject": rid, "predicate": "schema:name", "object": r["name"]},
        {"subject": rid, "predicate": "schema:url", "object": r["url"]},
        {"subject": rid, "predicate": "schema:category", "object": r["category"]},
        {"subject": rid, "predicate": "schema:description", "object": r["description"]},
    ]
    lower_body = md_body.lower()
    for hw_code, hw_name, _ in TPU_HARDWARE_ENTITIES:
        if hw_code.lower() in lower_body or hw_name.lower() in lower_body:
            triples.append({
                "subject": rid,
                "predicate": "okf:documentsHardware",
                "object": f"tpu_hw:{hw_code}"
            })
    for fw_name, fw_token, _ in FRAMEWORK_ENTITIES:
        if fw_name.lower() in lower_body or fw_token.lower() in lower_body:
            triples.append({
                "subject": rid,
                "predicate": "okf:documentsFramework",
                "object": f"tpu_fw:{fw_name}"
            })
    for sec in parsed["sections"][:25]:
        if sec["heading"] and sec["heading"] != "Overview":
            triples.append({
                "subject": rid,
                "predicate": "okf:hasSection",
                "object": sec["heading"]
            })
    for env in parsed["environment_variables"][:15]:
        triples.append({
            "subject": rid,
            "predicate": "okf:configuresEnvironmentVariable",
            "object": env
        })
    return triples

def build_okf_entity(r, md_body):
    parsed = parse_markdown_structure(md_body)
    triples = extract_semantic_triples(r, parsed, md_body)
    word_count = len(md_body.split())

    # Generate QA pairs from top sections
    qa_pairs = [
        {
            "question": f"What is covered in '{r['name']}' ({r['url']})?",
            "answer": r["description"]
        }
    ]
    for sec in parsed["sections"]:
        if sec["content"] and len(sec["content"]) > 60 and len(qa_pairs) < 10:
            qa_pairs.append({
                "question": f"How does '{r['name']}' handle: {sec['heading']}?",
                "answer": sec["content"][:1200]
            })

    return {
        "@context": {
            "@vocab": "https://schema.org/",
            "okf": "https://developers.google.com/open-knowledge-format/v1#",
            "tpu_doc": "https://github.com/ajithvnr2001/TPUDOCS/okf/doc#",
            "tpu_hw": "https://github.com/ajithvnr2001/TPUDOCS/okf/hardware#",
            "tpu_fw": "https://github.com/ajithvnr2001/TPUDOCS/okf/framework#"
        },
        "@type": "okf:KnowledgeDocument",
        "@id": f"tpu_doc:{r['id']}",
        "okf_version": "1.0",
        "metadata": {
            "id": r["id"],
            "name": r["name"],
            "url": r["url"],
            "category": r["category"],
            "description": r["description"],
            "char_count": len(md_body),
            "word_count": word_count,
            "section_count": len(parsed["sections"]),
            "code_block_count": len(parsed["code_blocks"]),
            "table_count": len(parsed["tables"]),
            "cli_command_count": len(parsed["cli_commands"]),
            "indexed_at": datetime.now(timezone.utc).isoformat()
        },
        "knowledge_graph": {
            "triples": triples
        },
        "structured_content": {
            "summary": r["description"],
            "sections": parsed["sections"],
            "code_examples": parsed["code_blocks"],
            "cli_commands": parsed["cli_commands"],
            "environment_variables": parsed["environment_variables"],
            "tables": parsed["tables"],
            "qa_pairs": qa_pairs,
            "full_markdown": md_body
        }
    }

def build_individual_skill_md(r, parsed, md_body):
    skill_name = r["id"].replace("_", "-")
    cmds_md = ""
    if parsed["cli_commands"]:
        cmds_md = "## Key CLI Commands & Invocations\n\n```bash\n" + "\n".join(parsed["cli_commands"][:15]) + "\n```\n\n"
    envs_md = ""
    if parsed["environment_variables"]:
        envs_md = "## Key Environment Variables\n\n" + "\n".join(f"- `{ev}`" for ev in parsed["environment_variables"][:20]) + "\n\n"
    toc_md = "## Document Sections\n\n" + "\n".join(
        f"{'  ' * max(0, s['level'] - 1)}- **{s['heading']}**" for s in parsed["sections"] if s["heading"]
    ) + "\n\n"

    return (
        "---\n"
        f"name: {skill_name}\n"
        f"description: {json.dumps(r['name'] + ' — ' + r['description'])}\n"
        f"source_url: {json.dumps(r['url'])}\n"
        f"category: {json.dumps(r['category'])}\n"
        "---\n\n"
        f"# Agent Skill: {r['name']}\n\n"
        f"- **Official Source**: [{r['url']}]({r['url']})\n"
        f"- **Category**: `{r['category']}`\n"
        f"- **Resource ID**: `{r['id']}`\n"
        f"- **When to Activate**: {r['description']}\n\n"
        + toc_md
        + cmds_md
        + envs_md
        + "## Complete Technical Reference\n\n"
        + md_body.strip()
        + "\n"
    )

def main():
    with open(f"{BASE_DIR}/resources.json") as f:
        resources = json.load(f)

    master_entities = []
    master_triples = []

    # Add canonical hardware and framework nodes to master knowledge graph
    for hw_code, hw_name, hw_desc in TPU_HARDWARE_ENTITIES:
        master_entities.append({
            "@id": f"tpu_hw:{hw_code}",
            "@type": "okf:HardwareAccelerator",
            "name": hw_name,
            "code": hw_code,
            "description": hw_desc
        })
    for fw_name, fw_token, fw_desc in FRAMEWORK_ENTITIES:
        master_entities.append({
            "@id": f"tpu_fw:{fw_name}",
            "@type": "okf:SoftwareFramework",
            "name": fw_name,
            "package": fw_token,
            "description": fw_desc
        })

    cat_docs = {}

    for idx, r in enumerate(resources, 1):
        rid = r["id"]
        cat = r["category"]
        md_path = f"{BASE_DIR}/markdown/{cat}/{rid}.md"
        with open(md_path) as f:
            raw = f.read()
        parts = raw.split("---", 2)
        md_body = parts[2].strip() if len(parts) == 3 else raw.strip()

        # 1. Build OKF entity file
        okf_obj = build_okf_entity(r, md_body)
        okf_dir = f"{BASE_DIR}/okf/entities/{cat}"
        os.makedirs(okf_dir, exist_ok=True)
        okf_path = f"{okf_dir}/{rid}.okf.json"
        with open(okf_path, "w") as f:
            json.dump(okf_obj, f, indent=2)

        master_entities.append({
            "@id": okf_obj["@id"],
            "@type": okf_obj["@type"],
            "metadata": okf_obj["metadata"],
            "sections": [s["heading"] for s in okf_obj["structured_content"]["sections"]],
            "cli_commands": okf_obj["structured_content"]["cli_commands"],
            "environment_variables": okf_obj["structured_content"]["environment_variables"],
            "entity_file": f"okf/entities/{cat}/{rid}.okf.json"
        })
        master_triples.extend(okf_obj["knowledge_graph"]["triples"])

        # 2. Build Individual AI Agent Skill file under /data/tpu/skills/catalog/<cat>/<rid>/SKILL.md
        parsed = parse_markdown_structure(md_body)
        skill_md = build_individual_skill_md(r, parsed, md_body)
        skill_dir = f"{BASE_DIR}/skills/catalog/{cat}/{rid}"
        os.makedirs(skill_dir, exist_ok=True)
        with open(f"{skill_dir}/SKILL.md", "w") as f:
            f.write(skill_md)

        cat_docs.setdefault(cat, []).append((r, parsed, md_body))

    # Also build OKF and Skill for the 9-step NVIDIA-to-TPU practical deployment guide
    with open(f"{BASE_DIR}/DEPLOYMENT_GUIDE.md") as f:
        deploy_md = f.read().strip()
    deploy_r = {
        "id": "deploy_00_nvidia_to_tpu_9step_guide",
        "name": "Practical 9-Step NVIDIA-to-TPU Deployment & vLLM-TorchTPU Serving Guide",
        "url": "https://vllm-torchtpu.readthedocs.io/en/latest/getting_started/quickstart/",
        "category": "nvidia_to_tpu_migration_docs",
        "description": "End-to-end 9-step runbook for migrating from NVIDIA CUDA to Cloud TPU v6e: project/IAM setup, TPU VM creation, Python 3.12 venv, TorchTPU smoke test, vLLM-TorchTPU installation, Hugging Face auth, Llama-3.2-1B serving, OpenAI API test, and VM cleanup."
    }
    deploy_okf = build_okf_entity(deploy_r, deploy_md)
    with open(f"{BASE_DIR}/okf/entities/nvidia_to_tpu_migration_docs/deploy_00_nvidia_to_tpu_9step_guide.okf.json", "w") as f:
        json.dump(deploy_okf, f, indent=2)
    deploy_parsed = parse_markdown_structure(deploy_md)
    deploy_skill_dir = f"{BASE_DIR}/skills/catalog/nvidia_to_tpu_migration_docs/deploy_00_nvidia_to_tpu_9step_guide"
    os.makedirs(deploy_skill_dir, exist_ok=True)
    with open(f"{deploy_skill_dir}/SKILL.md", "w") as f:
        f.write(build_individual_skill_md(deploy_r, deploy_parsed, deploy_md))

    # Write Master OKF Knowledge Graph
    master_kg = {
        "@context": {
            "@vocab": "https://schema.org/",
            "okf": "https://developers.google.com/open-knowledge-format/v1#",
            "tpu_doc": "https://github.com/ajithvnr2001/TPUDOCS/okf/doc#",
            "tpu_hw": "https://github.com/ajithvnr2001/TPUDOCS/okf/hardware#",
            "tpu_fw": "https://github.com/ajithvnr2001/TPUDOCS/okf/framework#"
        },
        "@type": "okf:KnowledgeGraph",
        "okf_version": "1.0",
        "title": "Official Google Cloud TPU Knowledge Graph (85 Resources + 9-Step Deployment Runbook)",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "statistics": {
            "total_documents": len(resources) + 1,
            "total_entities": len(master_entities) + 1,
            "total_triples": len(master_triples) + len(deploy_okf["knowledge_graph"]["triples"])
        },
        "entities": master_entities,
        "triples": master_triples + deploy_okf["knowledge_graph"]["triples"]
    }
    with open(f"{BASE_DIR}/okf/tpu_knowledge_graph.json", "w") as f:
        json.dump(master_kg, f, indent=2)

    # Write Category Compendium References inside /data/tpu/skills/references/
    os.makedirs(f"{BASE_DIR}/skills/references", exist_ok=True)
    for cat, items in cat_docs.items():
        compendium_lines = [f"# Complete Reference Compendium: `{cat}` ({len(items)} Resources)\n"]
        for r, parsed, md_body in items:
            compendium_lines.append(
                f"## `{r['id']}` — {r['name']}\n"
                f"- **URL**: {r['url']}\n"
                f"- **Description**: {r['description']}\n"
                f"- **Dedicated Skill**: `skills/catalog/{cat}/{r['id']}/SKILL.md`\n"
                f"- **OKF Entity**: `okf/entities/{cat}/{r['id']}.okf.json`\n"
                f"- **Markdown Source**: `markdown/{cat}/{r['id']}.md`\n\n"
                f"### Sections ({len(parsed['sections'])}) & Code Examples ({len(parsed['code_blocks'])})\n"
                + "\n".join(f"- {s['heading']}" for s in parsed["sections"][:15])
                + "\n"
            )
        with open(f"{BASE_DIR}/skills/references/{cat}_compendium.md", "w") as f:
            f.write("\n".join(compendium_lines))

    print(f"Successfully generated {len(resources)+1} OKF entities, {len(resources)+1} individual Agent Skills, and master Knowledge Graph ({master_kg['statistics']['total_triples']} triples).")

if __name__ == "__main__":
    main()
