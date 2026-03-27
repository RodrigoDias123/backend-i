from fastapi.testclient import TestClient

from app.api.store import store
from app.main import app

client = TestClient(app)


def setup_function() -> None:
    store._items.clear()
    store._ids = iter(range(1, 10_000))


def test_crud_operations_work_end_to_end() -> None:
    create_response = client.post(
        "/items",
        json={"name": "Notebook", "description": "Paper notes"},
    )

    assert create_response.status_code == 201
    created = create_response.json()
    assert created["name"] == "Notebook"

    get_response = client.get(f"/items/{created['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["description"] == "Paper notes"

    update_response = client.put(f"/items/{created['id']}", json={"description": "Updated"})
    assert update_response.status_code == 200
    assert update_response.json()["description"] == "Updated"

    list_response = client.get("/items", params={"search": "note", "skip": 0, "limit": 10})
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    delete_response = client.delete(f"/items/{created['id']}")
    assert delete_response.status_code == 204


def test_not_found_errors_use_consistent_schema() -> None:
    response = client.get("/items/999")

    assert response.status_code == 404
    assert response.json() == {
        "error": "http_error",
        "message": "Item 999 not found.",
        "details": [],
    }


def test_validation_errors_include_field_details() -> None:
    response = client.post("/items", json={"name": ""})

    assert response.status_code == 422
    body = response.json()
    assert body["error"] == "validation_error"
    assert body["message"] == "Request validation failed."
    assert {detail["field"] for detail in body["details"]} == {"name"}


def test_openapi_documents_descriptions_and_error_responses() -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    post_operation = schema["paths"]["/items"]["post"]

    assert post_operation["summary"] == "Create item"
    assert post_operation["description"] == "Create a new item from the provided payload."
    assert post_operation["responses"]["404"]["description"] == "Requested resource was not found."