# Session 12 — Filters, Sorting, and Pagination


FastAPI project implementing filters, sorting, and pagination for action items.

## Setup

```bash
uv sync
```

## Run

```bash
uv run uvicorn app.main:app --reload
```

## Endpoints

### List action items for a meeting

```
GET /meetings/{meeting_id}/action-items
```

**Query parameters:**

| Parameter | Type   | Default | Description                        |
|-----------|--------|---------|------------------------------------|
| `owner`   | string | —       | Filter by owner name (optional)    |
| `limit`   | int    | 20      | Max items to return (1–100)        |
| `offset`  | int    | 0       | Number of items to skip (≥ 0)      |

Results are sorted by `due_date` ascending. Response includes `total` (after filtering) and `items` (paginated).

**Examples:**

```bash
# All action items for a meeting
curl "http://127.0.0.1:8000/meetings/abc-123/action-items"

# Filter by owner
curl "http://127.0.0.1:8000/meetings/abc-123/action-items?owner=Jorge"

# Pagination
curl "http://127.0.0.1:8000/meetings/abc-123/action-items?limit=10&offset=0"

# Combined
curl "http://127.0.0.1:8000/meetings/abc-123/action-items?owner=Jorge&limit=5&offset=0"
```

**Response format:**

```json
{
  "total": 2,
  "items": [
    {
      "id": "3",
      "meeting_id": "abc-123",
      "title": "Deploy service",
      "owner": "Jorge",
      "due_date": "2026-03-25",
      "done": false
    }
  ]
}
```
