import click
from app.services.memory_store import MemoryStore


store = MemoryStore()


@click.group()
def cli():
    """Meeting management CLI"""
    pass


@cli.command()
@click.option("--title", required=True, help="Meeting title")
@click.option("--date", required=True, help="Meeting date (YYYY-MM-DD)")
@click.option("--owner", required=True, help="Meeting owner name")
@click.option("--participants", default="", help="Comma-separated list of participants")
def create_meeting(title: str, date: str, owner: str, participants: str):
    """Create a new meeting"""
    participants_list = [p.strip() for p in participants.split(",") if p.strip()]
    
    meeting = store.create_meeting(
        title=title,
        date=date,
        owner=owner,
        participants=participants_list,
    )
    
    click.echo(f"✓ Meeting '{title}' created successfully")
    click.echo(f"  Owner: {owner}")
    click.echo(f"  Date: {date}")
    if participants_list:
        click.echo(f"  Participants: {', '.join(participants_list)}")


@cli.command()
def list_meetings():
    """List all meetings"""
    meetings = store.list_meetings()
    
    if not meetings:
        click.echo("No meetings found")
        return
    
    for i, meeting in enumerate(meetings, 1):
        click.echo(f"\n{i}. {meeting.title}")
        click.echo(f"   Owner: {meeting.owner}")
        click.echo(f"   Date: {meeting.date}")
        if meeting.participants:
            click.echo(f"   Participants: {', '.join(meeting.participants)}")
        click.echo(f"   Created: {meeting.created_at}")


if __name__ == "__main__":
    cli()
