"""Test for items endpoints."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_and_get_item() -> None:
    """Test creating and retrieving an item."""
    # Create item
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "Test Description"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "Test Description"
    item_id = data["id"]

    # Get item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == data


def test_list_items() -> None:
    """Test listing items."""
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_item() -> None:
    """Test updating an item."""
    # Create item
    response = client.post(
        "/api/v1/items",
        json={"name": "Original", "description": "Original Description"},
    )
    assert response.status_code == 201
    item_id = response.json()["id"]

    # Update item
    response = client.put(
        f"/api/v1/items/{item_id}",
        json={"name": "Updated", "description": "Updated Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated"
    assert data["description"] == "Updated Description"


def test_delete_item() -> None:
    """Test deleting an item."""
    # Create item
    response = client.post(
        "/api/v1/items",
        json={"name": "To Delete", "description": "Will be deleted"},
    )
    assert response.status_code == 201
    item_id = response.json()["id"]

    # Delete item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204

    # Verify deletion
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 404


def test_get_nonexistent_item() -> None:
    """Test getting a nonexistent item."""
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404
