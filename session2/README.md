# Meeting Management CLI - Session 2: Data Modeling

A Python CLI application for managing meetings and action items using dataclasses and in-memory storage with uv.

## Quick Start

```bash
# Install and sync dependencies
uv sync

# List all meetings
uv run python -m app.cli list-meetings

# Create a meeting
uv run python -m app.cli create-meeting "meet-001" "Q1 Planning" "2026-03-15" "rodrigo"

# Add an action item to a meeting
uv run python -m app.cli add-action-item "meet-001" "Write proposal" "rodrigo" "2026-03-15"
```

## Features

- **Meeting Model**: ID, title, date, owner, participants, and action items
- **ActionItem Model**: Description, owner, due date, and status tracking
- **Persistent Storage**: Meetings saved to `meetings.json` on each operation
- **CLI Commands**: Create meetings, list meetings, and manage action items
- **Data Modeling**: Pythonic dataclasses with proper type hints

## Commands

### List Meetings
```bash
uv run python -m app.cli list-meetings
```

Output:
```
Meetings:
  [1] Sprint Planning | 2026-03-15 | Jorge
  [2] Retro | 2026-03-20 | Alice
Total: 2 meetings
```

### Create Meeting
```bash
uv run python -m app.cli create-meeting <id> <title> <date> <owner>
```

Example:
```bash
uv run python -m app.cli create-meeting "meet-001" "Q1 Planning" "2026-03-15" "Alice"
```

### Add Action Item
```bash
uv run python -m app.cli add-action-item <meeting_id> <description> <owner> <due_date>
```

Example:
```bash
uv run python -m app.cli add-action-item "meet-001" "Write proposal" "Alice" "2026-03-15"
```

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── cli.py                      # CLI commands and handlers
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py              # ActionItem and Meeting dataclasses
│   └── services/
│       ├── __init__.py
│       └── memory_store.py        # Global meetings list with persistence
├── meetings.json                   # Persistent storage
├── exercise.md                     # Exercise requirements
├── pyproject.toml                  # Project config (uv managed)
├── uv.lock                         # Dependency lock file
└── README.md
```

## Data Models

### Meeting
```python
@dataclass
class Meeting:
    id: str
    title: str
    date: str
    owner: str
    participants: List[str] = field(default_factory=list)
    action_items: List[ActionItem] = field(default_factory=list)
```

### ActionItem
```python
@dataclass
class ActionItem:
    description: str
    owner: str
    due_date: str
    status: str = "open"  # open, in_progress, done
```

## Requirements

- Python 3.10+
- uv (package manager)

