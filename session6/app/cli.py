"""CLI for managing meetings."""

import sys
import argparse
from app.core.logging_config import configure_logging
from app.services.meeting_service import MeetingService
from app.storage.json_repository import JsonRepository
from app.core.validators import ValidationError


def main():
    """Main CLI entry point."""
    configure_logging()
    
    parser = argparse.ArgumentParser(description="Meeting management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    create_parser = subparsers.add_parser("create-meeting", help="Create a new meeting")
    create_parser.add_argument("--title", required=True, help="Title of the meeting")
    create_parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    create_parser.add_argument("--owner", required=True, help="Owner of the meeting")
    
    list_parser = subparsers.add_parser("list-meetings", help="List all meetings")
    
    args = parser.parse_args()
    
    repository = JsonRepository()
    service = MeetingService(repository)
    
    if args.command == "create-meeting":
        try:
            meeting = service.create_meeting(
                title=args.title,
                date=args.date,
                owner=args.owner
            )
            print(f"Meeting created: {meeting}")
        except ValidationError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == "list-meetings":
        meetings = service.list_meetings()
        if meetings:
            for meeting in meetings:
                print(meeting)
        else:
            print("No meetings found")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
