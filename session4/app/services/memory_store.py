from app.domain.models import Meeting
from app.storage.json_repository import JsonRepository


class MemoryStore:
    def __init__(self, storage_path: str = "data/meetings.json"):
        self.repository = JsonRepository(storage_path)
        self.meetings: list[Meeting] = self.repository.load_meetings()

    def create_meeting(
        self,
        title: str,
        date: str,
        owner: str,
        participants: list[str] = None,
    ) -> Meeting:
        if participants is None:
            participants = []
        
        meeting = Meeting(
            title=title,
            date=date,
            owner=owner,
            participants=participants,
        )
        self.meetings.append(meeting)
        self.repository.save_meetings(self.meetings)
        return meeting

    def list_meetings(self) -> list[Meeting]:
        return self.meetings

    def get_meeting(self, title: str) -> Meeting | None:
        for meeting in self.meetings:
            if meeting.title == title:
                return meeting
        return None
