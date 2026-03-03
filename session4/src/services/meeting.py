from data.models import Meeting
from services import database

def create(title : str,owner : str,date : str):
    if not title or not owner or not date:
        raise ValueError("Title, owner and date are required fields")
    
    new_meeting = Meeting(
        title=title,
        owner=owner,
        date=date
    )
    database.create(meeting=new_meeting)

def list():
    ...