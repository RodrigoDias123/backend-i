# Session 11 | Notes, Decisions, and Action Items


REST API built with FastAPI and Python 3.14.

## Setup

```bash
uv sync
```

## Run

```bash
uv run uvicorn app.api.main:app --reload
```

## Endpoints

### POST /meetings/{id}/action-items

Creates an action item linked to a meeting.

**Body**
```json
{
  "description": "Update API docs",
  "owner": "Jorge",
  "due_date": "2026-03-20"
}
```

**Responses**
- `201` — Action item created
- `404` — Meeting not found
- `422` — Validation error (empty description, empty owner, invalid date)

**Examples**
```bash
# Create action item
curl -X POST http://127.0.0.1:8000/meetings/abc-123/action-items \
  -H "content-type: application/json" \
  -d '{"description": "Update API docs", "owner": "Jorge", "due_date": "2026-03-20"}'

# Meeting not found
curl -X POST http://127.0.0.1:8000/meetings/invalid-id/action-items \
  -H "content-type: application/json" \
  -d '{"description": "Task", "owner": "Jorge", "due_date": "2026-03-20"}'

# Invalid data
curl -X POST http://127.0.0.1:8000/meetings/abc-123/action-items \
  -H "content-type: application/json" \
  -d '{"description": "", "owner": "Jorge", "due_date": "2026-03-20"}'
```

## Project Structure

```
app/
  api/
    main.py          # FastAPI app
    schemas.py       # Pydantic schemas
    routers/
      action_items.py  # POST /meetings/{id}/action-items
```
