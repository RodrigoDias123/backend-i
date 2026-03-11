from fastapi import FastAPI, HTTPException

app = FastAPI()

db_meetings = {
    "abc-123": {"id": "abc-123", "title": "Planning", "date": "2026-03-15", "owner": "Jorge"}
}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/meetings/{meeting_id}")
def get_meeting(meeting_id: str):
    meeting = db_meetings.get(meeting_id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting
