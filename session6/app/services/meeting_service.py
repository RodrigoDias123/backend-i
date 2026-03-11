"""Service for managing meetings."""

import logging
from datetime import datetime
from app.core.validators import validate_meeting_data, ValidationError

logger = logging.getLogger(__name__)


class Meeting:
    """Represents a meeting."""
    
    def __init__(self, title: str, date: str, owner: str):
        self.title = title
        self.date = date
        self.owner = owner
    
    def to_dict(self) -> dict:
        """Convert meeting to dictionary."""
        return {
            'title': self.title,
            'date': self.date,
            'owner': self.owner
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Meeting':
        """Create meeting from dictionary."""
        return cls(
            title=data['title'],
            date=data['date'],
            owner=data['owner']
        )
    
    def __repr__(self):
        return f"Meeting(title={self.title!r}, date={self.date!r}, owner={self.owner!r})"


class MeetingService:
    """Service for managing meetings."""
    
    def __init__(self, repository):
        self.repository = repository
        self.meetings = []
        self._load_meetings()
    
    def _load_meetings(self) -> None:
        """Load meetings from repository."""
        data = self.repository.load()
        self.meetings = [Meeting.from_dict(item) for item in data]
    
    def create_meeting(self, title: str, date: str, owner: str) -> Meeting:
        """Create a meeting."""
        validate_meeting_data(title, date, owner)
        
        logger.info(f"Creating meeting with title={title!r}, date={date!r}, owner={owner!r}")
        
        meeting = Meeting(title, date, owner)
        self.meetings.append(meeting)
        self._persist()
        
        return meeting
    
    def list_meetings(self) -> list[Meeting]:
        """List all meetings."""
        logger.info("Meetings list is requested")
        return self.meetings
    
    def _persist(self) -> None:
        """Persist meetings to storage."""
        data = [meeting.to_dict() for meeting in self.meetings]
        self.repository.save(data)
