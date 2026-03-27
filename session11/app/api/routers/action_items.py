import uuid
from fastapi import APIRouter, HTTPException
from app.api.schemas import ActionItemInput, ActionItemOutput

router = APIRouter()

# In-memory store: meeting_id -> list of action items
# Meetings store is shared via app state set in main.py
meetings_store: dict[str, dict] = {}
action_items_store: dict[str, list[dict]] = {}


@router.post("/meetings/{meeting_id}/action-items", status_code=201, response_model=ActionItemOutput)
def create_action_item(meeting_id: str, body: ActionItemInput):
    if meeting_id not in meetings_store:
        raise HTTPException(status_code=404, detail="Meeting not found")

    item = {
        "id": str(uuid.uuid4()),
        "meeting_id": meeting_id,
        "description": body.description,
        "owner": body.owner,
        "due_date": body.due_date,
    }

    action_items_store.setdefault(meeting_id, []).append(item)

    return item
