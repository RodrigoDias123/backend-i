# Meeting CLI


A command-line interface (CLI) for managing meetings with JSON persistence, built with Python, Click, and Pydantic. All dependencies are managed with [uv](https://github.com/astral-sh/uv).

## Features
- Create, list, show, and delete meetings
- JSON persistence between executions
- Summary report of meetings and action items
- Error handling and logging for all operations

## Setup

1. **Install [uv](https://github.com/astral-sh/uv) if not already installed:**
   ```bash
   pip install uv
   ```
2. **Install dependencies:**
   ```bash
   uv sync
   ```

## Usage

All commands are run from the project root:

### Create a meeting
```bash
uv run python app/cli.py create-meeting --title "Sprint" --date "2026-03-15" --owner "rodrigo"
```

### List all meetings
```bash
uv run python app/cli.py list-meetings
```

### Show a specific meeting
```bash
uv run python app/cli.py show-meeting --id "<meeting-id>"
```

### Delete a meeting
```bash
uv run python app/cli.py delete-meeting --id "<meeting-id>"
```

### Show summary
```bash
uv run python app/cli.py summary
# Output: {"meetings": 2, "action_items": 5}
```

## Data Persistence
- All meetings are stored in `meetings.json` in the project root.

## Project Structure
```
app/
  cli.py                # CLI entrypoint
  models.py             # Pydantic models
  services/
    meeting_service.py  # CRUD and persistence logic
    report_service.py   # Summary report logic
pyproject.toml          # Project dependencies
meetings.json           # Data file (auto-created)
```

## License
MIT
