from datetime import date
from typing import Optional
from pydantic import BaseModel


class ActionItem(BaseModel):
    id: str
    meeting_id: str
    title: str
    owner: str
    due_date: date
    done: bool = False
