from typing import List
from data import meetings_store, next_meeting_id
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from models import Meeting, MeetingCreate
from client import summarize_with_ollama



api = FastAPI(
    title="Meetings API",
    description="Cria e consulta meetings com resumo gerado pelo Ollama.",
    version="1.0.0",
)


@api.get("/doc", include_in_schema=False)
def doc_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@api.post("/meetings", response_model=Meeting, summary="Criar meeting")
def create_meeting(payload: MeetingCreate) -> Meeting:
    global next_meeting_id

    summary = summarize_with_ollama(payload.content)
    
    meeting = Meeting(
        id=next_meeting_id,
        title=payload.title,
        content=payload.content,
        summary=summary,
    )

    meetings_store[next_meeting_id] = meeting
    next_meeting_id += 1
    return meeting


@api.get("/meetings", response_model=List[Meeting], summary="Listar meetings")
def list_meetings() -> List[Meeting]:
    return list(meetings_store.values())


@api.get("/meetings/{meeting_id}", response_model=Meeting, summary="Buscar meeting por ID")
def get_meeting_by_id(meeting_id: int) -> Meeting:
    meeting = meetings_store.get(meeting_id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting nao encontrada.")
    return meeting



