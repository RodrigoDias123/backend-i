import typer
from datetime import datetime

app = typer.Typer()

@app.command()
def create_meeting(title: str, owner: str, date: str) -> None:
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d")
        
        typer.echo("--- Meeting Created ---")
        typer.echo(f"Title: {title}")
        typer.echo(f"Owner: {owner}")
        typer.echo(f"Date:  {valid_date.date()}")
        
    except ValueError:
        typer.secho(f"Error: '{date}' is not a valid date. Use YYYY-MM-DD format.", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()