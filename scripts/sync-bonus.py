#!/usr/bin/env python3
"""Copy each canonical phase-folder BONUS-*.md over the copies bundled in skills/.

Some skills bundle a BONUS reference so they work outside a ProductOS repo. The phase
folder (define/, design/, develop/, distribute/) holds the canonical copy: edit that one,
then run this from the repo root:  python3 scripts/sync-bonus.py
"""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
PHASES = ["define", "design", "develop", "distribute"]

synced = 0
for name in sorted(os.listdir(SKILLS)):
    folder = os.path.join(SKILLS, name)
    if not os.path.isdir(folder):
        continue
    for f in sorted(os.listdir(folder)):
        if not f.startswith("BONUS-"):
            continue
        for phase in PHASES:
            canon = os.path.join(ROOT, phase, f)
            if os.path.isfile(canon):
                target = os.path.join(folder, f)
                if open(canon, "rb").read() != open(target, "rb").read():
                    shutil.copyfile(canon, target)
                    print(f"synced skills/{name}/{f} from {phase}/{f}")
                    synced += 1
                break
print(f"{synced} file(s) updated")
