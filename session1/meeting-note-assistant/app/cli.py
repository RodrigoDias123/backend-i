import typer
from datetime import datetime
from app.memory_store import meetings
from app.models import Meeting, ActionItem
import uuid

app = typer.Typer()

@app.command("create")
def create_meeting(title: str, date: str, owner: str) -> None:
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        typer.echo("Erro: Formato de data inválido. Por favor, use o formato YYYY-MM-DD (exemplo: 2023-10-20).")
        raise typer.Exit(code=1)
    
    meeting_id = str(uuid.uuid4())
    meeting = Meeting(id=meeting_id, title=title, date=date, owner=owner)
    meetings.append(meeting)
    typer.echo(f"Meeting '{title}' created with ID: {meeting_id}")

@app.command("add-action")
def add_action_item(meeting_id: str, description: str, owner: str, due_date: str) -> None:
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        typer.echo("Erro: Formato de data inválido. Por favor, use o formato YYYY-MM-DD.")
        raise typer.Exit(code=1)
    
    meeting = next((m for m in meetings if m.id == meeting_id), None)
    if not meeting:
        typer.echo(f"Meeting with ID {meeting_id} not found.")
        raise typer.Exit(code=1)
    
    action_item = ActionItem(description=description, owner=owner, due_date=due_date)
    meeting.action_items.append(action_item)
    typer.echo(f"Action item added to meeting '{meeting.title}'")

if __name__ == "__main__":
    app()