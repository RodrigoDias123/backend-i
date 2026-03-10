import json
import os
from typing import List
from app.domain.models import Meeting, ActionItem


def _load_meetings() -> List[Meeting]:
    """Load meetings from JSON file"""
    if not os.path.exists("meetings.json"):
        return []
    
    try:
        with open("meetings.json", "r") as f:
            data = json.load(f)
        
        loaded_meetings = []
        for meeting_data in data:
            action_items = [
                ActionItem(
                    description=item["description"],
                    owner=item["owner"],
                    due_date=item["due_date"],
                    status=item.get("status", "open")
                )
                for item in meeting_data.get("action_items", [])
            ]
            
            meeting = Meeting(
                id=meeting_data["id"],
                title=meeting_data["title"],
                date=meeting_data["date"],
                owner=meeting_data["owner"],
                participants=meeting_data.get("participants", []),
                action_items=action_items
            )
            loaded_meetings.append(meeting)
        
        return loaded_meetings
    except (json.JSONDecodeError, KeyError):
        return []


def _save_meetings(meetings_list: List[Meeting]) -> None:
    """Save meetings to JSON file"""
    data = []
    for meeting in meetings_list:
        data.append({
            "id": meeting.id,
            "title": meeting.title,
            "date": meeting.date,
            "owner": meeting.owner,
            "participants": meeting.participants,
            "action_items": [
                {
                    "description": item.description,
                    "owner": item.owner,
                    "due_date": item.due_date,
                    "status": item.status
                }
                for item in meeting.action_items
            ]
        })
    
    with open("meetings.json", "w") as f:
        json.dump(data, f, indent=2)


# Initialize meetings list from file
meetings: List[Meeting] = _load_meetings()
