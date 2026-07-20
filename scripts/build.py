from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)
inputs = [
    ROOT / "config/examples/bootstrap.example.json",
    ROOT / "tests/fixtures/synthetic/bootstrap_fixture.json",
]
manifest = {
    "bounded_bootstrap": True,
    "inputs": [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        for path in inputs
    ],
}
(BUILD / "bootstrap-manifest.json").write_text(
    json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print("build passed: build/bootstrap-manifest.json")
