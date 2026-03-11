from pydantic import BaseModel, Field, validator
from typing import List, Optional

class MeetingCreate(BaseModel):
    title: str = Field(..., min_length=3)
    date: str
    owner: str
    participants: Optional[List[str]] = None

    @validator('participants', always=True)
    def participants_not_empty(cls, v):
        if v is not None and len(v) == 0:
            raise ValueError('participants list must not be empty')
        return v

class MeetingRead(BaseModel):
    title: str
    date: str
    owner: str
    participants: Optional[List[str]] = None
