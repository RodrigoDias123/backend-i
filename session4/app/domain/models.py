from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Meeting:
    title: str
    date: str
    owner: str
    participants: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "date": self.date,
            "owner": self.owner,
            "participants": self.participants,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data: dict) -> "Meeting":
        return Meeting(
            title=data["title"],
            date=data["date"],
            owner=data["owner"],
            participants=data.get("participants", []),
            created_at=data.get("created_at", datetime.now().isoformat()),
        )
