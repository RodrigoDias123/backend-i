import json
import logging
import os
from typing import List, Optional
from app.models import Meeting, ActionItem

logger = logging.getLogger(__name__)

DATA_FILE = "meetings.json"


class MeetingService:
    @staticmethod
    def _load_meetings() -> dict:
        """Load meetings from JSON file."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.error(f"Error reading {DATA_FILE}. Starting with empty data.")
                return {"meetings": []}
        return {"meetings": []}

    @staticmethod
    def _save_meetings(data: dict) -> None:
        """Save meetings to JSON file."""
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Meetings saved to {DATA_FILE}")
        except Exception as e:
            logger.error(f"Error saving meetings to {DATA_FILE}: {e}")
            raise

    @staticmethod
    def create_meeting(title: str, date: str, owner: str) -> Meeting:
        """Create a new meeting and persist it."""
        try:
            meeting = Meeting(title=title, date=date, owner=owner)
            data = MeetingService._load_meetings()
            data["meetings"].append(meeting.to_dict())
            MeetingService._save_meetings(data)
            logger.info(f"Meeting created: {meeting.id}")
            return meeting
        except Exception as e:
            logger.error(f"Error creating meeting: {e}")
            raise

    @staticmethod
    def list_meetings() -> List[Meeting]:
        """List all meetings."""
        try:
            data = MeetingService._load_meetings()
            meetings = [Meeting.from_dict(m) for m in data.get("meetings", [])]
            logger.info(f"Listed {len(meetings)} meetings")
            return meetings
        except Exception as e:
            logger.error(f"Error listing meetings: {e}")
            raise

    @staticmethod
    def get_meeting(meeting_id: str) -> Optional[Meeting]:
        """Get a specific meeting by ID."""
        try:
            data = MeetingService._load_meetings()
            for m in data.get("meetings", []):
                if m["id"] == meeting_id:
                    logger.info(f"Meeting retrieved: {meeting_id}")
                    return Meeting.from_dict(m)
            logger.warning(f"Meeting not found: {meeting_id}")
            return None
        except Exception as e:
            logger.error(f"Error getting meeting: {e}")
            raise

    @staticmethod
    def delete_meeting(meeting_id: str) -> bool:
        """Delete a meeting by ID."""
        try:
            data = MeetingService._load_meetings()
            original_count = len(data.get("meetings", []))
            data["meetings"] = [m for m in data.get("meetings", []) if m["id"] != meeting_id]
            
            if len(data["meetings"]) < original_count:
                MeetingService._save_meetings(data)
                logger.info(f"Meeting deleted: {meeting_id}")
                return True
            else:
                logger.warning(f"Meeting not found for deletion: {meeting_id}")
                return False
        except Exception as e:
            logger.error(f"Error deleting meeting: {e}")
            raise
