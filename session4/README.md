# Meetings App - JSON/CSV Persistence

A CLI application for managing meetings with persistent JSON storage.

## Features

- ✅ Create meetings with participants
- ✅ List all saved meetings
- ✅ JSON persistence between sessions
- ✅ Pretty-printed data format
- ✅ Optional participants list support

## Project Structure

```
.
├── app/
│   ├── cli.py                    # CLI commands
│   ├── domain/
│   │   └── models.py             # Meeting dataclass
│   ├── services/
│   │   └── memory_store.py        # Business logic & persistence
│   └── storage/
│       └── json_repository.py    # JSON file operations
├── data/
│   └── meetings.json             # Data storage file
├── pyproject.toml                # Project config & dependencies
└── README.md
```

## Installation

Using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Usage

### Create a Meeting

```bash
uv run python -m app.cli create-meeting \
  --title "Planning" \
  --date "2026-03-15" \
  --owner "Jorge" \
  --participants "Alice,Bob"
```

**Without participants:**

```bash
uv run python -m app.cli create-meeting \
  --title "Standup" \
  --date "2026-03-10" \
  --owner "Pedro"
```

### List All Meetings

```bash
uv run python -m app.cli list-meetings
```

Output:

```
1. Planning
   Owner: Jorge
   Date: 2026-03-15
   Participants: Alice, Bob
   Created: 2026-03-09T23:45:42.403981

2. Standup
   Owner: Pedro
   Date: 2026-03-10
   Created: 2026-03-09T23:46:07.336913
```

## Data Storage

Meetings are stored in `data/meetings.json` with the following format:

```json
[
  {
    "title": "Planning",
    "date": "2026-03-15",
    "owner": "Jorge",
    "participants": ["Alice", "Bob"],
    "created_at": "2026-03-09T23:45:42.403981"
  }
]
```

## Implementation Details

- **Models** (`app/domain/models.py`): `Meeting` dataclass with `title`, `date`, `owner`, `participants`, and `created_at`
- **Repository** (`app/storage/json_repository.py`): Handles JSON file I/O and serialization
- **Store** (`app/services/memory_store.py`): In-memory list loaded from JSON on startup, persisted after each operation
- **CLI** (`app/cli.py`): Click-based command interface with two commands: `create-meeting` and `list-meetings`

## Requirements

- Python 3.11+
- Click 8.0+

## Notes

- Data persists between CLI executions
- Empty participants list is supported
- Meetings are loaded from JSON on application startup
- All changes are automatically saved to `data/meetings.json`
