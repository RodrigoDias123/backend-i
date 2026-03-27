import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def valid_payload() -> dict[str, str]:
    return {
        "title": "Planning",
        "date": "2026-03-15",
        "owner": "Jorge",
    }
