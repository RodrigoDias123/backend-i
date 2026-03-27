import logging

from fastapi import APIRouter, HTTPException, Query, Response, status

from app.api.schemas import ErrorResponse, Item, ItemCreate, ItemUpdate
from app.api.store import store

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/items", tags=["items"])

ERROR_RESPONSES = {
    404: {"model": ErrorResponse, "description": "Requested resource was not found."},
    422: {"model": ErrorResponse, "description": "Request validation failed."},
    500: {"model": ErrorResponse, "description": "Unexpected server error."},
}


def get_or_404(item_id: int) -> Item:
    item = store.get(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found.")
    return item


@router.get(
    "",
    response_model=list[Item],
    responses=ERROR_RESPONSES,
    summary="List items",
    description="Return items using optional text search and offset pagination.",
)
def list_items(
    search: str | None = Query(default=None, min_length=1, description="Filter by item name or description."),
    skip: int = Query(default=0, ge=0, description="Number of items to skip."),
    limit: int = Query(default=10, ge=1, le=100, description="Maximum number of items to return."),
) -> list[Item]:
    logger.info("Listing items", extra={"search": search, "skip": skip, "limit": limit})
    return store.list(search=search, skip=skip, limit=limit)


@router.post(
    "",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    responses=ERROR_RESPONSES,
    summary="Create item",
    description="Create a new item from the provided payload.",
)
def create_item(payload: ItemCreate) -> Item:
    item = store.create(payload)
    logger.info("Created item", extra={"item_id": item.id})
    return item


@router.get(
    "/{item_id}",
    response_model=Item,
    responses=ERROR_RESPONSES,
    summary="Get item",
    description="Return a single item by its identifier.",
)
def get_item(item_id: int) -> Item:
    return get_or_404(item_id)


@router.put(
    "/{item_id}",
    response_model=Item,
    responses=ERROR_RESPONSES,
    summary="Update item",
    description="Update one or more fields of an existing item.",
)
def update_item(item_id: int, payload: ItemUpdate) -> Item:
    updated = store.update(item_id, payload)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found.")
    logger.info("Updated item", extra={"item_id": item_id})
    return updated


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=ERROR_RESPONSES,
    summary="Delete item",
    description="Delete an existing item by identifier.",
)
def delete_item(item_id: int) -> Response:
    deleted = store.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found.")
    logger.info("Deleted item", extra={"item_id": item_id})
    return Response(status_code=status.HTTP_204_NO_CONTENT)