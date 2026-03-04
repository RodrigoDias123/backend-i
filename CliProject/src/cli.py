from datetime import datetime
import typer
from data import load_birthdays, save_birthdays
from logic import add_friend, calculate_days_until_birthday, filter_upcoming_birthdays, sort_birthdays

app = typer.Typer(help="🎉 Avisador de Aniversários CLI")

@app.command()
def add(name: str, date: str):
    """Adiciona um novo amigo e a sua data de nascimento (AAAA-MM-DD)."""
    try:
        name, valid_date = add_friend(name, date)
        birthdays = load_birthdays()
        birthdays[name] = valid_date
        save_birthdays(birthdays)
        typer.secho(f"✅ {name} adicionado com sucesso! (Data: {valid_date})", fg=typer.colors.GREEN)
    except ValueError as e:
        typer.secho(f"❌ Erro: {e}", fg=typer.colors.RED, bold=True)

@app.command()
def upcoming(days: int = typer.Option(7, "--days", "-d", help="Número de dias para a frente a verificar.")):
    """Mostra quem faz anos nos próximos dias."""
    birthdays = load_birthdays()
    
    if not birthdays:
        typer.secho("Ainda não tens amigos registados. Usa o comando 'add'.", fg=typer.colors.YELLOW)
        return

    upcoming_friends = filter_upcoming_birthdays(birthdays, days)
    
    if not upcoming_friends:
        typer.secho(f"Nenhum amigo faz anos nos próximos {days} dias.", fg=typer.colors.YELLOW)
    else:
        typer.secho(f"🎂 Aniversários nos próximos {days} dias:", fg=typer.colors.CYAN, bold=True)
        for name, birthdate, days_until in upcoming_friends:
            if days_until == 0:
                msg = f"Hoje é o aniversário de {name}! 🎉"
            elif days_until == 1:
                msg = f"{name} faz anos AMANHÃ! ⏰"
            else:
                msg = f"{name} faz anos daqui a {days_until} dias!"
                
            typer.secho(f"  - {msg} ({birthdate})", fg=typer.colors.GREEN)

@app.command(name="list")
def list_all():
    """Lista todos os aniversários guardados, ordenados no ano."""
    birthdays = load_birthdays()
    
    if not birthdays:
        typer.secho("Nenhum amigo encontrado na lista.", fg=typer.colors.YELLOW)
        return

    sorted_birthdays = sort_birthdays(birthdays)
    
    typer.secho("📅 Lista Completa de Aniversários:", fg=typer.colors.CYAN, bold=True)
    for name, birthdate in sorted_birthdays:
        typer.echo(f"  - {name}: {birthdate}")

if __name__ == "__main__":
    app()