# Session 7 | CLI Checkpoint - Exercise

## Exercise
Deliver a working CLI with JSON persistence.

## Requirements
1. Implement full CRUD operations for meetings
2. Implement a summary report command
3. All data persists in JSON between executions
4. All commands have proper error handling and logging

## Expected Commands
```bash
# Create a meeting
python app/cli.py create-meeting --title "Sprint" --date "2026-03-15" --owner "Jorge"

# List all meetings
python app/cli.py list-meetings

# Show specific meeting
python app/cli.py show-meeting --id "<meeting-id>"

# Delete a meeting
python app/cli.py delete-meeting --id "<meeting-id>"

# Show summary
python app/cli.py summary
# Output: {"meetings": 2, "action_items": 5}
```

## Files to Create/Modify
- `app/services/meeting_service.py` - Implement:
  - `create_meeting(title, date, owner) -> Meeting`
  - `list_meetings() -> list[Meeting]`
  - `get_meeting(id) -> Meeting`
  - `delete_meeting(id) -> bool`
- `app/services/report_service.py` - Implement:
  - `summary(meetings) -> dict`
- `app/cli.py` - Add all commands above

## Success Criteria
- All CRUD operations work correctly
- JSON persistence works across executions
- Summary includes meeting count and total action items
- All errors are handled gracefully
- Logs track all operations
