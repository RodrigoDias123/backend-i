# Session 8 | HTTP/REST + FastAPI - Exercise

## Exercise
Create `GET /meetings/{meeting_id}` endpoint.

## Requirements
1. Set up FastAPI server with basic health check
2. Implement GET endpoint to retrieve a single meeting by ID
3. Return appropriate status codes:
   - 200 for successful retrieval
   - 404 for meeting not found
4. Return meeting data as JSON

## Expected Behavior
```bash
# Start server
uvicorn app.api.main:app --reload

# Health check
curl http://127.0.0.1:8000/health
# {"status": "ok"}

# Get existing meeting (assuming id is "abc-123")
curl http://127.0.0.1:8000/meetings/abc-123
# {"id": "abc-123", "title": "Planning", "date": "2026-03-15", "owner": "Jorge"}

# Get non-existent meeting
curl http://127.0.0.1:8000/meetings/invalid-id
# 404: {"detail": "Meeting not found"}
```

## Files to Create/Modify
- `app/api/__init__.py` - Create empty init file
- `app/api/main.py` - Create FastAPI app with endpoints:
  - `GET /health` - Returns status
  - `GET /meetings/{meeting_id}` - Returns meeting or 404
- `app/api/routers/` - Prepare for future route organization

## Success Criteria
- Health endpoint works and returns 200
- GET /meetings/{id} returns meeting with 200 for valid IDs
- GET /meetings/{id} returns 404 for invalid IDs
- API docs are available at /docs
- All responses are valid JSON
