# Session 3 | Functions and Modularization - Exercise

## Exercise
Refactor `create-meeting` to call `create_meeting(...)` service.

## Requirements
1. Move all business logic (meeting creation, storage) from CLI to a dedicated service
2. CLI handler should only call the service and format the response
3. Service should handle ID generation and storage
4. Implement `list_meetings` service function

## Expected Behavior
```
python app/cli.py create-meeting --title "Planning" --date "2026-03-15" --owner "Jorge"
```

Output should show the created meeting ID.

## Files to Create/Modify
- `app/services/meeting_service.py` - Create this with:
  - `create_meeting(title, date, owner) -> Meeting`
  - `list_meetings() -> list[Meeting]`
- `app/cli.py` - Update commands to use services

## Success Criteria
- Business logic is separated from CLI handlers
- Meeting creation uses UUID for IDs
- Meetings persist in memory during execution
- No logic duplication between CLI and services
- Both create and list commands work seamlessly
