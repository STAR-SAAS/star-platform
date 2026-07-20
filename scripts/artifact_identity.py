from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "build/bootstrap-manifest.json"
if not TARGET.is_file():
    raise SystemExit("build output missing")
print("artifact_identity_sha256=" + sha256(TARGET.read_bytes()).hexdigest())
