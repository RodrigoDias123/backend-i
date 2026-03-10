# Session 5 | Validation and Exceptions - Exercise

## Exercise
Block `ActionItem` creation without `owner` and without `due_date`.

## Requirements
1. Create custom exception classes for validation errors
2. Validate that action items have both owner and due_date
3. Add date format validation (YYYY-MM-DD)
4. Display clear error messages to the user
5. Exit with non-zero code on validation errors

## Expected Behavior
```bash
# Invalid: missing owner
python app/cli.py create-action-item --description "Do something" --due-date "2026-03-15"
# Output: Validation error: 'owner' is required

# Invalid: bad date format
python app/cli.py create-action-item --description "Do something" --owner "Jorge" --due-date "15-03-2026"
# Output: Validation error: Date must be YYYY-MM-DD

# Valid
python app/cli.py create-action-item --description "Do something" --owner "Jorge" --due-date "2026-03-15"
# Output: Action item created successfully
```

## Files to Create/Modify
- `app/core/errors.py` - Define custom exceptions
- `app/core/validators.py` - Implement validation functions
- `app/services/action_item_service.py` - Add validation before creation
- `app/cli.py` - Add error handling for commands

## Success Criteria
- Missing owner raises validation error
- Missing due_date raises validation error
- Invalid date format shows helpful message
- Exit code is non-zero on error
- Valid action items are created successfully
