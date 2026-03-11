
# Session 8 | FastAPI Meetings API

## Description
This project implements a simple API using FastAPI to manage meetings, as required by Session 8 exercise.

## Endpoints

- `GET /health` — Application health check. Returns `{ "status": "ok" }`.
- `GET /meetings/{meeting_id}` — Returns meeting data by ID or 404 if not found.

## How to run

1. Install dependencies using [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install fastapi uvicorn
   ```
2. Create the virtual environment (if it doesn't exist yet):
   ```bash
   uv venv
   ```
3. Start the server:
   ```bash
   uvicorn app.api.main:app --reload
   ```

## Usage examples

```bash
# Health check
curl http://127.0.0.1:8000/health

# Get existing meeting
curl http://127.0.0.1:8000/meetings/abc-123

# Get non-existent meeting
curl http://127.0.0.1:8000/meetings/invalid-id
```

## Structure
- `app/api/main.py` — Main API code
- `app/api/__init__.py` — Empty init file
- `app/api/routers/` — Directory reserved for future routes




