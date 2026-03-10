"""Service for managing action items."""

from app.core.validators import validate_action_item
from app.core.errors import ValidationError


class ActionItem:
    """Represents an action item."""
    
    def __init__(self, description: str, owner: str, due_date: str):
        self.description = description
        self.owner = owner
        self.due_date = due_date
    
    def __repr__(self):
        return f"ActionItem(description={self.description!r}, owner={self.owner!r}, due_date={self.due_date!r})"


def create_action_item(description: str, owner: str | None, due_date: str | None) -> ActionItem:
    """Create an action item with validation."""
    validate_action_item(description, owner, due_date)
    return ActionItem(description, owner, due_date)
