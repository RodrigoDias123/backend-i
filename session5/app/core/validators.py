"""Validation functions for action items."""

from datetime import datetime
from .errors import ValidationError


def validate_owner(owner: str | None) -> None:
    """Validate that owner is provided."""
    if not owner:
        raise ValidationError("Validation error: 'owner' is required")


def validate_due_date(due_date: str | None) -> None:
    """Validate due date format and presence."""
    if not due_date:
        raise ValidationError("Validation error: 'due_date' is required")
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValidationError("Validation error: Date must be YYYY-MM-DD")


def validate_action_item(description: str, owner: str | None, due_date: str | None) -> None:
    """Validate all action item fields."""
    validate_owner(owner)
    validate_due_date(due_date)
