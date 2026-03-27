# Session 12 | Filters, Sorting, and Pagination - Exercise

## Exercise
Add `owner` filter for action items.

## Requirements
1. Add query parameters to list action items by meeting
2. Add `owner` filter to filter action items by owner
3. Implement pagination with `limit` and `offset`
4. Sort results by due_date (ascending)
5. Return total count with paginated results

## Expected Behavior
```bash
# List all action items for a meeting
curl "http://127.0.0.1:8000/meetings/abc-123/action-items"
# Returns: {"total": 3, "items": [...]}

# Filter by owner
curl "http://127.0.0.1:8000/meetings/abc-123/action-items?owner=Jorge"
# Returns only action items owned by Jorge

# Pagination
curl "http://127.0.0.1:8000/meetings/abc-123/action-items?limit=10&offset=0"
# Returns paginated results

# Combined
curl "http://127.0.0.1:8000/meetings/abc-123/action-items?owner=Jorge&limit=5&offset=0"
# Returns paginated action items for Jorge
```

## Files to Create/Modify
- `app/api/routers/action_items.py` - Update GET endpoint with:
  - `owner` query parameter (optional)
  - `limit` query parameter (default 20, max 100)
  - `offset` query parameter (default 0)
- Update response to include total count

## Success Criteria
- Owner filter works correctly
- Pagination works with limit/offset
- Results are sorted by due_date
- Total count is returned
- Query parameters are validated (limit > 0, offset >= 0)
- Combined filters work properly
