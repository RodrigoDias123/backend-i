# Session 9 | Pydantic and Contracts - Exercise

## Exercise
Validate minimum `title` length and non-empty participants list.

## Requirements
1. Create Pydantic schemas for Meeting input/output
2. Validate title has minimum length (e.g., 3 characters)
3. Validate participants list is not empty (when provided)
4. Return 422 error with field details for invalid input

## Expected Behavior
```bash
# Valid request
curl -X POST http://127.0.0.1:8000/meetings \
  -H "content-type: application/json" \
  -d '{"title": "Planning Meeting", "date": "2026-03-15", "owner": "Jorge", "participants": ["Alice", "Bob"]}'
# Returns 201 with created meeting

# Invalid: title too short
curl -X POST http://127.0.0.1:8000/meetings \
  -H "content-type: application/json" \
  -d '{"title": "Ok", "date": "2026-03-15", "owner": "Jorge"}'
# Returns 422: Field validation error for title

# Invalid: empty participants
curl -X POST http://127.0.0.1:8000/meetings \
  -H "content-type: application/json" \
  -d '{"title": "Planning", "date": "2026-03-15", "owner": "Jorge", "participants": []}'
# Returns 422: Field validation error for participants
```

## Files to Create/Modify
- `app/api/schemas.py` - Create with:
  - `MeetingCreate(BaseModel)` - Input validation schema
  - `MeetingRead(BaseModel)` - Output schema
  - Use `Field()` for constraints
- `app/api/main.py` - Update POST endpoint to use schemas

## Success Criteria
- Title minimum length is enforced
- Empty participants list is rejected
- Invalid requests return 422 with clear field errors
- Valid requests return 201 with created meeting
- Schema is used for both input/output validation
