from datetime import date
from pydantic import BaseModel, field_validator


class ActionItemInput(BaseModel):
    description: str
    owner: str
    due_date: str

    @field_validator("description")
    @classmethod
    def description_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Description must not be empty")
        return v

    @field_validator("owner")
    @classmethod
    def owner_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Owner must not be empty")
        return v

    @field_validator("due_date")
    @classmethod
    def due_date_valid(cls, v: str) -> str:
        try:
            date.fromisoformat(v)
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")
        return v


class ActionItemOutput(BaseModel):
    id: str
    meeting_id: str
    description: str
    owner: str
    due_date: str
