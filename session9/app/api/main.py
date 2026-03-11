from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi import Request
from app.api.schemas import MeetingCreate, MeetingRead
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.post("/meetings", response_model=MeetingRead, status_code=201)
async def create_meeting(meeting: MeetingCreate):
    data = meeting.dict()
    return data
