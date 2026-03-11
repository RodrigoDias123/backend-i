import json
import uuid
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ActionItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    completed: bool = False


class Meeting(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    date: str
    owner: str
    action_items: List[ActionItem] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return self.model_dump()

    @classmethod
    def from_dict(cls, data: dict) -> "Meeting":
        return cls(**data)
