# Session 14 | API Checkpoint

Minimal FastAPI project built with `uv` for the Session 14 checkpoint.

## Requirements Covered
- Quality checklist created in `CHECKLIST.md`
- API reviewed and 2 gaps identified
- Both gaps fixed in the API implementation
- Tests added and passing

## Identified Gaps
1. Missing consistent error response schema for `404`, `422`, and `500`
2. Missing endpoint descriptions and documented error responses in OpenAPI

## Stack
- Python
- FastAPI
- pytest
- uv

## Setup
```bash
uv sync
```

## Run
```bash
uv run uvicorn app.main:app --reload
```

Docs available at:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/openapi.json`

## Test
```bash
uv run pytest
```

## API Endpoints
- `GET /items` list items with `search`, `skip`, and `limit`
- `POST /items` create an item
- `GET /items/{item_id}` get one item
- `PUT /items/{item_id}` update an item
- `DELETE /items/{item_id}` delete an item

## Notes
- Error responses use a shared schema with `error`, `message`, and `details`
- Validation errors include field-level details
- OpenAPI includes endpoint summaries, descriptions, and error responses