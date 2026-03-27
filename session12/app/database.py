from datetime import date
from app.models import ActionItem

# In-memory store keyed by meeting_id
DB: dict[str, list[ActionItem]] = {
    "abc-123": [
        ActionItem(id="1", meeting_id="abc-123", title="Write report", owner="Jorge", due_date=date(2026, 4, 1)),
        ActionItem(id="2", meeting_id="abc-123", title="Review PR", owner="Ana", due_date=date(2026, 3, 20)),
        ActionItem(id="3", meeting_id="abc-123", title="Deploy service", owner="Jorge", due_date=date(2026, 3, 25)),
    ]
}
