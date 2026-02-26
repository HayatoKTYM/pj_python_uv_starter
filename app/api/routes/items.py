"""Items CRUD endpoints."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# In-memory storage for demo purposes
items_db: dict[int, dict[str, str | int]] = {}
next_id = 1


class Item(BaseModel):
    """Item model."""

    name: str
    description: str | None = None


class ItemResponse(BaseModel):
    """Item response model."""

    id: int
    name: str
    description: str | None = None


@router.get("/items")
async def list_items() -> list[ItemResponse]:
    """List all items."""
    return [ItemResponse(**item) for item in items_db.values()]


@router.post("/items", status_code=201)
async def create_item(item: Item) -> ItemResponse:
    """Create a new item."""
    global next_id
    item_dict = {"id": next_id, **item.model_dump()}
    items_db[next_id] = item_dict
    response = ItemResponse(**item_dict)
    next_id += 1
    return response


@router.get("/items/{item_id}")
async def get_item(item_id: int) -> ItemResponse:
    """Get an item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(**items_db[item_id])


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item) -> ItemResponse:
    """Update an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item_dict = {"id": item_id, **item.model_dump()}
    items_db[item_id] = item_dict
    return ItemResponse(**item_dict)


@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None:
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
