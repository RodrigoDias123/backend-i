import click
import json
import logging
import sys
import os

# Add the parent directory to the path so imports work correctly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.meeting_service import MeetingService
from app.services.report_service import ReportService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@click.group()
def cli():
    """Meeting CLI - Manage meetings with persistence."""
    pass


@cli.command()
@click.option("--title", required=True, help="Meeting title")
@click.option("--date", required=True, help="Meeting date (YYYY-MM-DD)")
@click.option("--owner", required=True, help="Meeting owner")
def create_meeting(title: str, date: str, owner: str):
    """Create a new meeting."""
    try:
        meeting = MeetingService.create_meeting(title, date, owner)
        click.echo(
            json.dumps({
                "status": "success",
                "message": "Meeting created",
                "meeting": meeting.to_dict()
            }, indent=2)
        )
    except Exception as e:
        click.echo(
            json.dumps({
                "status": "error",
                "message": str(e)
            }, indent=2),
            err=True
        )
        raise SystemExit(1)


@cli.command()
def list_meetings():
    """List all meetings."""
    try:
        meetings = MeetingService.list_meetings()
        click.echo(
            json.dumps({
                "status": "success",
                "meetings": [m.to_dict() for m in meetings]
            }, indent=2)
        )
    except Exception as e:
        click.echo(
            json.dumps({
                "status": "error",
                "message": str(e)
            }, indent=2),
            err=True
        )
        raise SystemExit(1)


@cli.command()
@click.option("--id", "meeting_id", required=True, help="Meeting ID")
def show_meeting(meeting_id: str):
    """Show a specific meeting."""
    try:
        meeting = MeetingService.get_meeting(meeting_id)
        if meeting:
            click.echo(
                json.dumps({
                    "status": "success",
                    "meeting": meeting.to_dict()
                }, indent=2)
            )
        else:
            click.echo(
                json.dumps({
                    "status": "error",
                    "message": f"Meeting with id {meeting_id} not found"
                }, indent=2),
                err=True
            )
            raise SystemExit(1)
    except Exception as e:
        click.echo(
            json.dumps({
                "status": "error",
                "message": str(e)
            }, indent=2),
            err=True
        )
        raise SystemExit(1)


@cli.command()
@click.option("--id", "meeting_id", required=True, help="Meeting ID")
def delete_meeting(meeting_id: str):
    """Delete a meeting."""
    try:
        deleted = MeetingService.delete_meeting(meeting_id)
        if deleted:
            click.echo(
                json.dumps({
                    "status": "success",
                    "message": f"Meeting {meeting_id} deleted"
                }, indent=2)
            )
        else:
            click.echo(
                json.dumps({
                    "status": "error",
                    "message": f"Meeting with id {meeting_id} not found"
                }, indent=2),
                err=True
            )
            raise SystemExit(1)
    except Exception as e:
        click.echo(
            json.dumps({
                "status": "error",
                "message": str(e)
            }, indent=2),
            err=True
        )
        raise SystemExit(1)


@cli.command()
def summary():
    """Show summary report."""
    try:
        meetings = MeetingService.list_meetings()
        summary_data = ReportService.summary(meetings)
        click.echo(json.dumps(summary_data, indent=2))
    except Exception as e:
        click.echo(
            json.dumps({
                "status": "error",
                "message": str(e)
            }, indent=2),
            err=True
        )
        raise SystemExit(1)


if __name__ == "__main__":
    cli()
