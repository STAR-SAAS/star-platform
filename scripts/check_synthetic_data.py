import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(relative: str) -> dict[str, object]:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))
def main() -> None:
    assert load("config/examples/bootstrap.example.json") == {"environment": "local", "synthetic_data_only": True, "external_secret_reference": "NOT_CONFIGURED", "logging_level": "INFO"}
    assert load("tests/fixtures/synthetic/bootstrap_fixture.json") == {"synthetic_data": True, "fixture_id": "SYNTHETIC-BOOTSTRAP-001", "tenant_id": "TENANT-DEMO-001", "record_type": "repository-bootstrap", "contains_customer_data": False, "contains_kyc_data": False, "contains_payment_data": False}
    print("synthetic-data check passed: approved synthetic configuration and fixture only")
if __name__ == "__main__":
    main()
