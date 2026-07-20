from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "README.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md", ".gitignore",
    ".github/CODEOWNERS", ".github/pull_request_template.md", ".github/workflows/bootstrap-checks.yml",
    "docs/architecture/README.md", "docs/adr/README.md", "docs/adr/ADR-TEMPLATE.md",
    "docs/rfc/README.md", "docs/rfc/RFC-TEMPLATE.md", "docs/standards/MODULE_ADMISSION.md",
    "docs/standards/DEPENDENCY_POLICY.md", "docs/operations/BOOTSTRAP_RECOVERY.md",
    "docs/operations/EVIDENCE_RETENTION.md", "foundation/README.md", "platform/README.md",
    "contracts/README.md", "config/examples/README.md", "config/examples/bootstrap.example.json",
    "tests/fixtures/README.md", "tests/fixtures/synthetic/bootstrap_fixture.json", "pyproject.toml",
    "scripts/build.py", "scripts/test.py", "scripts/check.py", "scripts/clean.py",
    "scripts/artifact_identity.py", "scripts/check_repository_contract.py", "scripts/check_secrets.py",
    "scripts/check_synthetic_data.py", "tests/test_repository_contract.py",
}
IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache", "build"}
def main() -> None:
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and not any(part in IGNORED_PARTS for part in p.parts)}
    missing = sorted(EXPECTED - actual)
    extra = sorted(actual - EXPECTED)
    if missing or extra:
        raise SystemExit(f"repository contract failed; missing={missing}; extra={extra}")
    print(f"repository contract passed: {len(actual)} paths")
if __name__ == "__main__":
    main()
