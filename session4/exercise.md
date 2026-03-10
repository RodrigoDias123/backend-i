# Session 4 | JSON/CSV Persistence - Exercise

## Exercise
Persist and reload `Meeting` with participants.

## Requirements
1. Implement JSON persistence to save meetings to disk
2. Load meetings from JSON file on startup
3. Include participants list in the meeting model
4. Ensure data survives between CLI executions

## Expected Behavior
```bash
# First run
python app/cli.py create-meeting --title "Planning" --date "2026-03-15" --owner "Jorge" --participants "Alice,Bob"

# Second run (in new terminal)
python app/cli.py list-meetings
# Should show the previously created meeting
```

## Files to Create/Modify
- `app/storage/json_repository.py` - Create with:
  - `save_meetings(items: list[Meeting])`
  - `load_meetings() -> list[Meeting]`
- `app/domain/models.py` - Add `participants` field to `Meeting`
- `app/services/memory_store.py` - Load from JSON on startup
- `app/cli.py` - Update to accept `--participants`

## Data File
- `data/meetings.json` - Will store all meetings

## Success Criteria
- Meetings are saved to JSON after creation
- Meetings are loaded from JSON on startup
- Participants list persists correctly
- Data format is readable (pretty-printed JSON)
- Empty participants list works correctly
