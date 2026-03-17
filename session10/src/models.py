from pydantic import BaseModel, Field


class MeetingCreate(BaseModel):
    title: str = Field(..., min_length=3, example="Sprint planning")
    content: str = Field(
        ...,
        min_length=10,
        example="Falamos sobre prioridades da sprint, riscos e distribuicao de tarefas.",
    )


class Meeting(BaseModel):
    id: int
    title: str
    content: str
    summary: str
  