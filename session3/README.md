# Meeting Management CLI - Session 3: Functions and Modularization

A Python CLI application for managing meetings with refactored service architecture using uv.

## Quick Start

```bash
# Install and sync dependencies
uv sync

# Create a meeting
uv run python -m app.cli create-meeting --title "Planning" --date "2026-03-15" --owner "rodrigo"

# List all meetings
uv run python -m app.cli list-meetings

# Add an action item to a meeting
uv run python -m app.cli add-action-item <meeting_id> "Task description" "Owner" "2026-03-20"
```

## Architecture

### Service Layer
- **`app/services/meeting_service.py`** - Business logic
  - `create_meeting(title, date, owner)` - Creates meeting with auto-generated UUID
  - `list_meetings()` - Returns all meetings

### CLI Layer
- **`app/cli.py`** - Command handlers
  - Calls service functions
  - Formats and displays output

### Data Layer
- **`app/services/memory_store.py`** - Persistence
  - `_load_meetings()` - Loads from `meetings.json`
  - `_save_meetings()` - Persists to `meetings.json`

### Models
- **`app/domain/models.py`** - Data models
  - `Meeting` - ID, title, date, owner, participants, action_items
  - `ActionItem` - Description, owner, due_date, status

## Key Features

- **Separation of Concerns** - Business logic in service, CLI handles I/O
- **Auto-generated IDs** - UUID for every new meeting
- **Persistent Storage** - Meetings saved to JSON file
- **No Code Duplication** - Single source of truth in services

## Project Structure

```
session3/
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py
│   └── services/
│       ├── __init__.py
│       ├── meeting_service.py
│       └── memory_store.py
├── pyproject.toml
└── meetings.json (auto-generated)
```
