from dataclasses import dataclass
from typer import Typer, echo, style, colors
from datetime import datetime

@dataclass
class Meeting:
    title: str
    owner: str
    date: str

cli = Typer()

@cli.command()
def greettings(name: str, surname: str =""):
    echo(style(f"greetings {name} {surname}", fg=colors.BLUE))

@cli.command()
def goodbye():
    echo(style("bye", fg=colors.YELLOW))

@cli.command()
def create_meeting(meeting: Meeting):
    """
    Create a meeting note
    """
    echo(style(f"""
        ============================
                {meeting.title}
        ============================
        created by {meeting.owner} at {meeting.date}
        """, fg=colors.BRIGHT_CYAN,bold=True))
   


if __name__ == "__main__":
    cli()
