import os
import pickle

import pytest

from hiddenlayer import HiddenlayerServiceClient


class MaliciousPickle:
    def __reduce__(self):
        return exec, ("import os; os.system('env')",)


@pytest.fixture(scope="session")
def hl_client_saas() -> HiddenlayerServiceClient:
    hl_client_id = os.getenv("HL_CLIENT_ID")
    hl_client_secret = os.getenv("HL_CLIENT_SECRET")

    if not hl_client_id:
        raise RuntimeError("HL_CLIENT_ID env var not set.")

    if not hl_client_secret:
        raise RuntimeError("HL_CLIENT_SECRET env var not set.")

    return HiddenlayerServiceClient(api_id=hl_client_id, api_key=hl_client_secret)


def test_scan_model(tmp_path, hl_client_saas: HiddenlayerServiceClient):
    """Integration test to scan a model"""

    model_path = tmp_path / "model.pkl"
    malicious_model = MaliciousPickle()

    with open(model_path, "wb") as f:
        pickle.dump(malicious_model, f)

    results = hl_client_saas.model_scanner.scan_file(
        model_name="sdk-integration-scan_model", model_path=model_path
    )

    detections = results.detections

    assert detections
    assert detections[0]["severity"] == "MALICIOUS"
    assert "system" in detections[0]["description"]
