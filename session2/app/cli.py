import argparse
import sys
from app.domain.models import ActionItem, Meeting
from app.services.memory_store import meetings, _save_meetings


def list_meetings():
    """List all meetings with readable formatting"""
    if not meetings:
        print("No meetings found.")
        return
    
    print("Meetings:")
    for meeting in meetings:
        print(f"  [{meeting.id}] {meeting.title} | {meeting.date} | {meeting.owner}")
    
    print(f"Total: {len(meetings)} meetings")


def create_meeting(meeting_id: str, title: str, date: str, owner: str):
    """Create a new meeting"""
    new_meeting = Meeting(
        id=meeting_id,
        title=title,
        date=date,
        owner=owner
    )
    meetings.append(new_meeting)
    _save_meetings(meetings)
    print(f"✓ Meeting created: [{new_meeting.id}] {new_meeting.title} | {new_meeting.date} | {new_meeting.owner}")


def add_action_item(meeting_id: str, description: str, item_owner: str, due_date: str):
    """Add an action item to a meeting"""
    for meeting in meetings:
        if meeting.id == meeting_id:
            action_item = ActionItem(
                description=description,
                owner=item_owner,
                due_date=due_date
            )
            meeting.action_items.append(action_item)
            _save_meetings(meetings)
            print(f"✓ Action item added to meeting [{meeting_id}]: {description}")
            return
    print(f"Error: Meeting [{meeting_id}] not found", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Meeting Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # list-meetings command
    subparsers.add_parser("list-meetings", help="List all meetings")
    
    # create-meeting command
    create_parser = subparsers.add_parser("create-meeting", help="Create a new meeting")
    create_parser.add_argument("id", help="Meeting ID")
    create_parser.add_argument("title", help="Meeting title")
    create_parser.add_argument("date", help="Meeting date (YYYY-MM-DD)")
    create_parser.add_argument("owner", help="Meeting owner")
    
    # add-action-item command
    action_parser = subparsers.add_parser("add-action-item", help="Add an action item to a meeting")
    action_parser.add_argument("meeting_id", help="Meeting ID")
    action_parser.add_argument("description", help="Action item description")
    action_parser.add_argument("owner", help="Action item owner")
    action_parser.add_argument("due_date", help="Due date (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    if args.command == "list-meetings":
        list_meetings()
    elif args.command == "create-meeting":
        create_meeting(args.id, args.title, args.date, args.owner)
    elif args.command == "add-action-item":
        add_action_item(args.meeting_id, args.description, args.owner, args.due_date)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
