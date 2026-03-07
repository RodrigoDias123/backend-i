from datetime import datetime
from fastapi import FastAPI
from api.models import  Meeting, MeetingRequest, MeetingResponse

api = FastAPI()

@api.get("/",response_model=list[Meeting])
def list_meetings(title:str="",owner:str="",date:datetime | None = None)-> list[Meeting]:
    return []
    

@api.post("/", response_model= MeetingResponse)
def create_meetings(meeting:MeetingRequest):
    ... 

@api.get("/{meeting_id}",response_model= Meeting)
def get_meeting(meting_id: str):
    ...