# Session 2 | Data Modeling - Exercise

## Exercise
Implement `list-meetings` with readable output.

## Requirements
1. Create a command that lists all created meetings
2. Display each meeting with clear formatting
3. Show: ID, Title, Date, Owner for each meeting
4. Handle empty meetings list gracefully

## Expected Output Example
```
python app/cli.py list-meetings
```

Should output:
```
Meetings:
  [1] Sprint Planning | 2026-03-15 | Jorge
  [2] Retro | 2026-03-20 | Alice
Total: 2 meetings
```

Or if no meetings:
```
No meetings found.
```

## Files to Create/Modify
- `app/domain/models.py` - Ensure `Meeting` dataclass exists
- `app/services/memory_store.py` - Keep in-memory storage
- `app/cli.py` - Add `list-meetings` command

## Success Criteria
- Command displays all meetings in readable format
- Each meeting shows ID, title, date, and owner
- Handles empty state gracefully
