import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", "__pycache__", "build"}
PRIVATE_KEY_MARKER = "-----BEGIN " + "PRIVATE KEY-----"
TOKEN_PREFIX = "g" + "h" + "p" + "_"
ACCESS_PREFIX = "A" + "K" + "I" + "A"
PATTERNS = [re.compile(re.escape(PRIVATE_KEY_MARKER)), re.compile(re.escape(TOKEN_PREFIX) + r"[A-Za-z0-9_]{20,}"), re.compile(re.escape(ACCESS_PREFIX) + r"[0-9A-Z]{16}"), re.compile(r"(?i)(?:password|secret|token|api[_-]?key)\s*[:=]\s*[\"'][^\"']{8,}[\"']")]
def main() -> None:
    findings = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in PATTERNS:
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)}:{pattern.pattern}")
    if findings:
        raise SystemExit("secret check failed: " + ", ".join(findings))
    print("secret check passed: no live credential patterns detected")
if __name__ == "__main__":
    main()
