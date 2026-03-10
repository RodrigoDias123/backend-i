import json
from pathlib import Path
from app.domain.models import Meeting


class JsonRepository:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

    def save_meetings(self, items: list[Meeting]) -> None:
        data = [meeting.to_dict() for meeting in items]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def load_meetings(self) -> list[Meeting]:
        if not self.filepath.exists():
            return []
        
        with open(self.filepath, "r") as f:
            data = json.load(f)
        
        return [Meeting.from_dict(item) for item in data]
