"""CLI for managing action items."""

import sys
import argparse
from app.services.action_item_service import create_action_item
from app.core.errors import ValidationError


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Action item management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Create action-item command
    create_parser = subparsers.add_parser("create-action-item", help="Create a new action item")
    create_parser.add_argument("--description", required=True, help="Description of the action item")
    create_parser.add_argument("--owner", help="Owner of the action item")
    create_parser.add_argument("--due-date", help="Due date in YYYY-MM-DD format")
    
    args = parser.parse_args()
    
    if args.command == "create-action-item":
        try:
            action_item = create_action_item(
                description=args.description,
                owner=args.owner,
                due_date=args.due_date
            )
            print("Action item created successfully")
        except ValidationError as e:
            print(str(e))
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
