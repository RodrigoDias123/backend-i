import uuid
from typing import List
from app.domain.models import Meeting
from app.services.memory_store import meetings, _save_meetings


def create_meeting(title: str, date: str, owner: str) -> Meeting:
    """Create a new meeting with auto-generated UUID"""
    meeting_id = str(uuid.uuid4())[:8]
    
    new_meeting = Meeting(
        id=meeting_id,
        title=title,
        date=date,
        owner=owner
    )
    
    meetings.append(new_meeting)
    _save_meetings(meetings)
    
    return new_meeting


def list_meetings() -> List[Meeting]:
    """List all meetings"""
    return meetings
