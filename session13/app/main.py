from datetime import date
from typing import Annotated

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()


class MeetingCreate(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    date: date
    owner: str


class Meeting(MeetingCreate):
    id: int


@app.post("/meetings", response_model=Meeting, status_code=status.HTTP_201_CREATED)
def create_meeting(payload: MeetingCreate) -> Meeting:
    return Meeting(id=1, **payload.model_dump())
