import typer
from app.services.list_meetings import list_meetings
from app.services.memory_store import meetings
from app.domain.models import Meeting, ActionItem

app = typer.Typer(help="Gestão de Reuniões")

def _seed_demo_data() -> None:
    meetings.clear()

    reuniao_1 = Meeting(
        id="R001",
        title="Planeamento da Sprint",
        date="2026-02-26",
        owner="Rodrigo",
        participants=["Ana", "Bruno"],
        action_items=[
            ActionItem(
                description="Preparar backlog",
                owner="Ana",
                due_date="2026-02-28",
                status="open",
            ),
            ActionItem(
                description="Rever estimativas",
                owner="Bruno",
                due_date="2026-03-01",
                status="done",
            ),
        ],
    )

    reuniao_2 = Meeting(
        id="R002",
        title="Revisão de Produto",
        date="2026-03-02",
        owner="Carla",
        participants=["Diego", "Elisa", "Fábio"],
        action_items=[
            ActionItem(
                description="Consolidar feedback do cliente",
                owner="Elisa",
                due_date="2026-03-05",
                status="open",
            )
        ],
    )

    reuniao_3 = Meeting(
        id="R003",
        title="Retrospectiva da Equipa",
        date="2026-03-04",
        owner="Marina",
        participants=["Ana", "Carla", "Diego"],
    )

    meetings.extend([reuniao_1, reuniao_2, reuniao_3])


@app.command()
def demo():
    _seed_demo_data()
    typer.echo("3 reuniões de exemplo criadas.")

@app.command()
def listar():
    if not meetings:
        _seed_demo_data()
        typer.echo("Memória vazia: carregadas 3 reuniões de exemplo.")
    list_meetings()

if __name__ == "__main__":
    app()
