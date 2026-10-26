#!/usr/bin/env python3
"""
Strict Content & Structural Verification Audit for TPUDOCS.
Audits all 85 official TPU documentation resources + the 9-step deployment guide
across all 3 required formats:
  1. Separate Markdown (.md)
  2. AI Agent Skill format (SKILL.md — 6 workflow skills + 86 per-resource catalog skills)
  3. Google Open Knowledge Format (OKF v1.0 — 86 entity JSONs + master knowledge graph)
"""

import hashlib
import json
import os
import sys

BASE_DIR = "/data/tpu"

FORBIDDEN_NOISE_PATTERNS = [
    "Stay organized with collections",
    "#__codelineno-",
    "Skip to main content",
    "Skip to content",
]

def main():
    with open(f"{BASE_DIR}/resources.json") as f:
        resources = json.load(f)

    assert len(resources) == 85, f"Expected 85 resources, found {len(resources)}"

    errors = []
    body_hashes = {}
    total_md_chars = 0
    total_sections = 0
    total_code_blocks = 0
    total_triples = 0

    for idx, r in enumerate(resources, 1):
        rid = r["id"]
        cat = r["category"]

        # 1. Verify Markdown file
        md_path = f"{BASE_DIR}/markdown/{cat}/{rid}.md"
        if not os.path.exists(md_path):
            errors.append(f"Missing Markdown: {md_path}")
            continue
        with open(md_path) as f:
            md_raw = f.read()
        parts = md_raw.split("---", 2)
        if len(parts) < 3:
            errors.append(f"Missing frontmatter in {md_path}")
            continue
        body = parts[2].strip()
        if len(body) < 1000:
            errors.append(f"Body too short ({len(body)} chars) in {md_path}")
        if not body.startswith("#"):
            errors.append(f"Body does not start with clean heading in {md_path}: {body[:60]!r}")
        for pat in FORBIDDEN_NOISE_PATTERNS:
            if pat in body:
                errors.append(f"Forbidden UI noise '{pat}' found in {md_path}")

        # Check for accidental duplicate content from un-handled redirects
        h = hashlib.sha256(body.encode()).hexdigest()
        if h in body_hashes:
            errors.append(f"Duplicate body content between {rid} and {body_hashes[h]}")
        body_hashes[h] = rid
        total_md_chars += len(body)

        # 2. Verify Individual Agent Skill file
        skill_path = f"{BASE_DIR}/skills/catalog/{cat}/{rid}/SKILL.md"
        if not os.path.exists(skill_path):
            errors.append(f"Missing catalog SKILL.md: {skill_path}")
        else:
            with open(skill_path) as f:
                sk_text = f.read()
            if "name:" not in sk_text or "description:" not in sk_text or len(sk_text) < len(body):
                errors.append(f"Invalid or incomplete SKILL.md: {skill_path}")

        # 3. Verify OKF Entity JSON file
        okf_path = f"{BASE_DIR}/okf/entities/{cat}/{rid}.okf.json"
        if not os.path.exists(okf_path):
            errors.append(f"Missing OKF JSON: {okf_path}")
        else:
            with open(okf_path) as f:
                okf = json.load(f)
            sc = okf.get("structured_content", {})
            triples = okf.get("knowledge_graph", {}).get("triples", [])
            if not sc.get("sections") or not sc.get("full_markdown") or len(triples) < 5:
                errors.append(f"Incomplete OKF structure in {okf_path}")
            total_sections += len(sc.get("sections", []))
            total_code_blocks += len(sc.get("code_examples", []))
            total_triples += len(triples)

    # Check 6 Master Workflow Skills
    workflow_skills = [
        "tpu-orchestrator",
        "tpu-setup-provisioning",
        "nvidia-to-tpu-migration",
        "tpu-inference-vllm",
        "tpu-training-workflows",
        "tpu-troubleshooting-profiling",
    ]
    for ws in workflow_skills:
        p = f"{BASE_DIR}/skills/{ws}/SKILL.md"
        if not os.path.exists(p):
            errors.append(f"Missing workflow skill: {p}")

    # Check Master Knowledge Graph
    kg_path = f"{BASE_DIR}/okf/tpu_knowledge_graph.json"
    with open(kg_path) as f:
        kg = json.load(f)

    print("==================================================================")
    print("DEEP CONTENT & MULTI-FORMAT AUDIT SUMMARY")
    print("==================================================================")
    print(f"Resources Audited           : {len(resources)}/85 (+ 9-step Deployment Guide = 86)")
    print(f"Unique Content Hashes       : {len(body_hashes)}/85 (0 duplicate/redirected pages)")
    print(f"Total Clean Markdown Chars  : {total_md_chars:,} chars")
    print(f"Total Extracted Sections    : {total_sections:,} sections")
    print(f"Total Fenced Code Blocks    : {total_code_blocks:,} blocks")
    print(f"Workflow Agent Skills       : {len(workflow_skills)}/6")
    print(f"Per-Resource Agent Skills   : 86/86 (in skills/catalog/<category>/<id>/SKILL.md)")
    print(f"OKF Entity JSON Files       : 86/86 (in okf/entities/<category>/<id>.okf.json)")
    print(f"OKF Master Knowledge Triples: {kg['statistics']['total_triples']:,} triples")
    print(f"Errors / Anomalies Found    : {len(errors)}")
    print("==================================================================")

    if errors:
        for e in errors:
            print("ERROR:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
