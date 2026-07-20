import json
import tomllib
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class RepositoryContractTest(unittest.TestCase):
    def test_approved_json_is_synthetic(self) -> None:
        config = json.loads((ROOT / "config/examples/bootstrap.example.json").read_text(encoding="utf-8"))
        fixture = json.loads((ROOT / "tests/fixtures/synthetic/bootstrap_fixture.json").read_text(encoding="utf-8"))
        self.assertTrue(config["synthetic_data_only"])
        self.assertEqual(config["external_secret_reference"], "NOT_CONFIGURED")
        self.assertTrue(fixture["synthetic_data"])
        self.assertFalse(fixture["contains_customer_data"])
        self.assertFalse(fixture["contains_kyc_data"])
        self.assertFalse(fixture["contains_payment_data"])
    def test_no_third_party_dependencies_declared(self) -> None:
        data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertNotIn("dependencies", data["project"])
        self.assertEqual(data["project"]["requires-python"], ">=3.12,<3.13")
        self.assertFalse(data["tool"]["star_platform"]["third_party_dependencies"])
if __name__ == "__main__":
    unittest.main()
