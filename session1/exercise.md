# Session 1 | Python Setup + First CLI - Exercise

## Exercise
Create `create-meeting --title --date --owner` and print a summary in the terminal.

## Requirements
1. Create a CLI command that accepts three arguments: `--title`, `--date`, and `--owner`
2. Display a summary of the created meeting in a user-friendly format

## Expected Output Example
```
python app/cli.py create-meeting --title "Sprint Planning" --date "2026-03-15" --owner "Jorge"
```

Should output something like:
```
Meeting Summary:
  Title: Sprint Planning
  Date: 2026-03-15
  Owner: Jorge
  Status: Successfully created!
```

## Files to Create/Modify
- `app/cli.py` - Update the `create_meeting` command

## Success Criteria
- Command accepts all three parameters
- Summary is displayed after creation
- Output is clear and readable
