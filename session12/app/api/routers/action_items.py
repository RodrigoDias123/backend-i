from typing import Annotated, Optional
from fastapi import APIRouter, HTTPException, Query
from app.database import DB
from app.models import ActionItem

router = APIRouter(prefix="/meetings", tags=["action-items"])


@router.get("/{meeting_id}/action-items")
def list_action_items(
    meeting_id: str,
    owner: Annotated[Optional[str], Query(description="Filter by owner")] = None,
    limit: Annotated[int, Query(gt=0, le=100, description="Max items to return")] = 20,
    offset: Annotated[int, Query(ge=0, description="Number of items to skip")] = 0,
) -> dict:
    items = DB.get(meeting_id)
    if items is None:
        raise HTTPException(status_code=404, detail="Meeting not found")

    if owner is not None:
        items = [item for item in items if item.owner == owner]

    items = sorted(items, key=lambda i: i.due_date)

    total = len(items)
    page = items[offset : offset + limit]

    return {"total": total, "items": [item.model_dump() for item in page]}
