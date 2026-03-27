# Session 13 | API Testing - Exercise

## Exercise
Write 3 tests for `POST /meetings` (success + 2 errors).

## Requirements
1. Use pytest and TestClient from FastAPI
2. Test successful meeting creation (201)
3. Test missing required field validation (422)
4. Test invalid title length (422)
5. All tests should be independent and reusable

## Expected Tests
```python
def test_create_meeting_success() -> None:
    # Valid payload returns 201 with meeting data
    
def test_create_meeting_missing_title() -> None:
    # Missing title returns 422
    
def test_create_meeting_title_too_short() -> None:
    # Title shorter than minimum returns 422
```

## Test Cases to Implement
1. **Success**: Create meeting with valid data
   - Payload: {"title": "Planning", "date": "2026-03-15", "owner": "Jorge"}
   - Expect: 201 status, meeting has id, title, date, owner
   
2. **Error - Missing Title**: 
   - Payload: {"date": "2026-03-15", "owner": "Jorge"}
   - Expect: 422 status, error on title field
   
3. **Error - Title Too Short**:
   - Payload: {"title": "OK", "date": "2026-03-15", "owner": "Jorge"}
   - Expect: 422 status, error on title field

## Files to Create/Modify
- `tests/test_meetings.py` - Implement 3 test functions
- `conftest.py` - Optional: Create fixtures for reusable test data

## Success Criteria
- All 3 tests pass
- Tests use TestClient from FastAPI
- Tests check correct status codes and response data
- Each test is independent and can run in any order
- Response data is validated properly
