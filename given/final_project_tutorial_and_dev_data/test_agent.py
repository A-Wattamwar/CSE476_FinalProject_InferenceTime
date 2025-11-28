#!/usr/bin/env python3
import sys
import json
import random
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "agent"))
from agent import solve

with open("cse476_final_project_dev_data.json") as f:
    data = json.load(f)

domains = {}
for item in data:
    domain = item["domain"]
    if domain not in domains:
        domains[domain] = []
    domains[domain].append(item)

samples = []
for domain in sorted(domains.keys()):
    samples.extend(random.sample(domains[domain], min(2, len(domains[domain]))))

for item in samples:
    expected = item["output"]
    got = solve(item["input"])
    print(f"Expected: {expected}")
    print(f"Got: {got}")
    print()