# Session 6 | Debugging and Logging - Exercise

## Exercise
Add `INFO` logs to create/list flow.

## Requirements
1. Configure logging system with timestamp, level, and message
2. Add INFO logs when:
   - A meeting is created (title, date, owner)
   - Meetings list is requested
   - Validation errors occur (WARNING level)
   - Persistence operations happen (save/load)
3. Set logging level to INFO
4. Format: `TIMESTAMP LEVEL MODULE - MESSAGE`

## Expected Behavior
```bash
python app/cli.py create-meeting --title "Planning" --date "2026-03-15" --owner "Jorge"
```

Console output should include something like:
```
2026-03-09 14:30:45,123 INFO app.services.meeting_service - Creating meeting with title='Planning', date='2026-03-15', owner='Jorge'
2026-03-09 14:30:45,150 INFO app.storage.json_repository - Saved 1 meetings to data/meetings.json
```

## Files to Create/Modify
- `app/core/logging_config.py` - Create with `configure_logging()`
- `app/cli.py` - Call `configure_logging()` on startup
- `app/services/meeting_service.py` - Add logging statements
- `app/storage/json_repository.py` - Add logging for save/load

## Success Criteria
- All INFO logs are displayed with proper format
- Each major operation has corresponding log
- Logging is initialized before any business logic
- Module names in logs help with debugging
