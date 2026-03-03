import typer
from services import meeting


cli = typer.Typer()

@cli.command()
def create(
    title: str,
    owner: str,
    date: str
)->None:
    
    meeting.create(title,owner,date)



@cli.command()
def list() -> None : 
    ...


if __name__ == "__main__":
    cli()