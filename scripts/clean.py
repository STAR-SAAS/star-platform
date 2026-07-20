from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for relative in ("build",):
    target = ROOT / relative
    if target.exists():
        shutil.rmtree(target)
for cache in ROOT.rglob("__pycache__"):
    shutil.rmtree(cache)
print("clean passed")
