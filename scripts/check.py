from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
commands = [
    [sys.executable, "scripts/check_repository_contract.py"],
    [sys.executable, "scripts/check_secrets.py"],
    [sys.executable, "scripts/check_synthetic_data.py"],
]
for command in commands:
    subprocess.run(command, cwd=ROOT, check=True)
print("check passed")
