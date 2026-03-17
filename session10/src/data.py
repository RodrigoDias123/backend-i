from models import Meeting


meetings_store: dict[int, Meeting] = {}
next_meeting_id = 1