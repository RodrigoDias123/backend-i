"""Validators for meeting data."""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_meeting_data(title: str, date: str, owner: str) -> None:
    """Validate meeting data.
    
    Args:
        title: Meeting title
        date: Date in YYYY-MM-DD format
        owner: Meeting owner name
        
    Raises:
        ValidationError: If validation fails
    """
    errors = []
    
    if not title or not title.strip():
        error_msg = "Title cannot be empty"
        logger.warning(f"Validation error: {error_msg}")
        errors.append(error_msg)
    elif len(title) > 100:
        error_msg = "Title must be 100 characters or less"
        logger.warning(f"Validation error: {error_msg}")
        errors.append(error_msg)
    
    if not date or not date.strip():
        error_msg = "Date cannot be empty"
        logger.warning(f"Validation error: {error_msg}")
        errors.append(error_msg)
    else:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            if parsed_date.year < 2000 or parsed_date.year > 2100:
                error_msg = "Date year must be between 2000 and 2100"
                logger.warning(f"Validation error: {error_msg}")
                errors.append(error_msg)
        except ValueError:
            error_msg = f"Date must be in YYYY-MM-DD format, got '{date}'"
            logger.warning(f"Validation error: {error_msg}")
            errors.append(error_msg)
    
    if not owner or not owner.strip():
        error_msg = "Owner cannot be empty"
        logger.warning(f"Validation error: {error_msg}")
        errors.append(error_msg)
    elif len(owner) > 50:
        error_msg = "Owner name must be 50 characters or less"
        logger.warning(f"Validation error: {error_msg}")
        errors.append(error_msg)
    
    if errors:
        raise ValidationError("; ".join(errors))
