import glob
import os
import json
import re

with open('/data/tpu/resources.json') as f:
    resources = json.load(f)

print(f"Total target resources in manifest: {len(resources)}")

issues = []
verified = []

for r in resources:
    rid = r['id']
    cat = r['category']
    url = r['url']
    name = r['name']
    
    md_file = f"/data/tpu/markdown/{cat}/{rid}.md"
    okf_file = f"/data/tpu/okf/entities/{cat}/{rid}.okf.json"
    
    if not os.path.exists(md_file):
        issues.append((rid, "Missing markdown file", url))
        continue
    if not os.path.exists(okf_file):
        issues.append((rid, "Missing OKF file", url))
        continue
        
    size = os.path.getsize(md_file)
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    word_count = len(content.split())
    has_code = "```" in content
    headings = len(re.findall(r"^#+\s+", content, re.MULTILINE))
    
    # Check for potential scrape issues
    if "DescriptorFallback" in content or word_count < 100:
        issues.append((rid, f"Low content / fallback: {word_count} words, {size} bytes", url))
    else:
        verified.append({
            "id": rid,
            "name": name,
            "category": cat,
            "size_bytes": size,
            "words": word_count,
            "headings": headings,
            "has_code": has_code
        })

print(f"Successfully verified: {len(verified)} / {len(resources)}")
print(f"Issues found: {len(issues)}")
for iss in issues:
    print(f"  [ISSUE] {iss[0]}: {iss[1]} -> {iss[2]}")

# Show distribution
cats = {}
for v in verified:
    c = v["category"]
    cats[c] = cats.get(c, 0) + 1

print("\nBreakdown by category:")
for c, count in cats.items():
    print(f"  {c}: {count} files")

# Print top 5 largest and 5 smallest
sorted_by_size = sorted(verified, key=lambda x: x["size_bytes"])
print("\nSmallest 5 verified files:")
for x in sorted_by_size[:5]:
    print(f"  {x['id']} ({x['category']}): {x['size_bytes']} bytes, {x['words']} words, {x['headings']} headings, has_code={x['has_code']}")

print("\nLargest 5 verified files:")
for x in sorted_by_size[-5:]:
    print(f"  {x['id']} ({x['category']}): {x['size_bytes']} bytes, {x['words']} words, {x['headings']} headings, has_code={x['has_code']}")
