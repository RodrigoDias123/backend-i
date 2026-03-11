# Meeting Management CLI

A command-line application for managing meetings with structured logging.

## ✅ Implemented Requirements

1. ✅ Logging system configured with timestamp, level, and message
2. ✅ INFO logs for:
   - Meeting creation (title, date, owner)
   - Meeting list requests
   - Persistence operations (save/load)
3. ✅ WARNING logs for validation errors
4. ✅ Logging level set to INFO
5. ✅ Format: `TIMESTAMP LEVEL MODULE - MESSAGE`

## 🚀 How to Use

### Create a Meeting
```bash
uv run app/cli.py create-meeting --title "Planning" --date "2026-03-15" --owner "rodrigo"
```

### List All Meetings
```bash
uv run app/cli.py list-meetings
```

## 📝 Example Output

### Valid Meeting Creation
```
2026-03-09 23:58:24,897 INFO app.storage.json_repository - File data/meetings.json does not exist, returning empty list
2026-03-09 23:58:24,898 INFO app.services.meeting_service - Creating meeting with title='Team Meeting', date='2026-03-25', owner='Rodrigo'
2026-03-09 23:58:24,898 INFO app.storage.json_repository - Saved 1 meetings to data/meetings.json
Meeting created: Meeting(title='Team Meeting', date='2026-03-25', owner='Rodrigo')
```

### Validation Error (Empty Title)
```
2026-03-09 23:58:30,716 INFO app.storage.json_repository - Loaded 1 meetings from data/meetings.json
2026-03-09 23:58:30,716 WARNING app.core.validators - Validation error: Title cannot be empty
Error: Title cannot be empty
```

### Validation Error (Invalid Date Format)
```
2026-03-09 23:58:35,080 WARNING app.core.validators - Validation error: Date must be in YYYY-MM-DD format, got 'invalid-date'
Error: Date must be in YYYY-MM-DD format, got 'invalid-date'
```

### List Meetings
```
2026-03-09 23:58:48,823 INFO app.storage.json_repository - Loaded 1 meetings from data/meetings.json
2026-03-09 23:58:48,823 INFO app.services.meeting_service - Meetings list is requested
Meeting(title='Team Meeting', date='2026-03-25', owner='Rodrigo')
```

## 📁 Project Structure

```
app/
├── __init__.py
├── cli.py                          # CLI entry point
├── core/
│   ├── __init__.py
│   ├── logging_config.py           # Logging system configuration
│   └── validators.py               # Data validation with WARNING logs
├── services/
│   ├── __init__.py
│   └── meeting_service.py          # Meeting management service
└── storage/
    ├── __init__.py
    └── json_repository.py          # JSON persistence

data/
└── meetings.json                   # Meetings storage file
```

## 🔧 Technologies

- **Python 3.14+**
- **uv** - Package manager
- **logging** - Python standard logging module

## ✔️ Validation

The application validates meeting data and logs warnings for validation errors:

- **Title**: Cannot be empty, max 100 characters
- **Date**: Must be in YYYY-MM-DD format, year between 2000-2100
- **Owner**: Cannot be empty, max 50 characters

Each validation error is logged as a WARNING before raising an exception.

## 💾 Data Persistence

Data is stored in `data/meetings.json` in JSON format. The application automatically creates the directory and file if they don't exist.
