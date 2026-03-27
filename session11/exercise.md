# Session 11 | Notes, Decisions, and Action Items - Exercise

## Exercise
Implement `POST /meetings/{id}/action-items`.

## Requirements
1. Create Pydantic schema for ActionItem (input/output)
2. Implement POST endpoint to create action items linked to a meeting
3. Validate:
   - Meeting exists (404 if not)
   - Description is not empty
   - Owner is not empty
   - Due date is valid (YYYY-MM-DD)
4. Return 201 with created action item

## Expected Behavior
```bash
# Create action item for existing meeting
curl -X POST http://127.0.0.1:8000/meetings/abc-123/action-items \
  -H "content-type: application/json" \
  -d '{"description": "Update API docs", "owner": "Jorge", "due_date": "2026-03-20"}'
# Returns 201 with created action item

# Meeting not found
curl -X POST http://127.0.0.1:8000/meetings/invalid-id/action-items \
  -H "content-type: application/json" \
  -d '{"description": "Task", "owner": "Jorge", "due_date": "2026-03-20"}'
# Returns 404: Meeting not found

# Invalid data
curl -X POST http://127.0.0.1:8000/meetings/abc-123/action-items \
  -H "content-type: application/json" \
  -d '{"description": "", "owner": "Jorge", "due_date": "2026-03-20"}'
# Returns 422: Description must not be empty
```

## Files to Create/Modify
- `app/api/schemas.py` - Add ActionItem schemas
- `app/api/routers/action_items.py` - Create router for action items
- `app/api/main.py` - Include action items router

## Success Criteria
- Action items are created and linked to meetings
- All validations work (description, owner, due_date)
- Returns 404 when meeting doesn't exist
- Returns 201 with created action item
- Action items persist with the meeting
