from fastapi.testclient import TestClient


def test_create_meeting_success(client: TestClient, valid_payload: dict[str, str]) -> None:
    response = client.post("/meetings", json=valid_payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == valid_payload["title"]
    assert body["date"] == valid_payload["date"]
    assert body["owner"] == valid_payload["owner"]


def test_create_meeting_missing_title(client: TestClient) -> None:
    response = client.post(
        "/meetings",
        json={
            "date": "2026-03-15",
            "owner": "Jorge",
        },
    )

    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any(error["loc"][-1] == "title" for error in errors)


def test_create_meeting_title_too_short(client: TestClient) -> None:
    response = client.post(
        "/meetings",
        json={
            "title": "OK",
            "date": "2026-03-15",
            "owner": "Jorge",
        },
    )

    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any(error["loc"][-1] == "title" for error in errors)
