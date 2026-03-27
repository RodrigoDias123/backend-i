# Session 1 - CLI Create Meeting


Exercise implementation with the `create-meeting` command using Typer.

## Requirements

- Python 3
- uv

## Install dependencies

```bash
uv sync
```

## Run

```bash
uv run app/cli.py create-meeting --title "Sprint Planning" --date "2026-03-15" --owner "Jorge"
```

## Expected output

```text
Meeting Summary:
	Title: Sprint Planning
	Date: 2026-03-15
	Owner: Jorge
	Status: Successfully created!
```
