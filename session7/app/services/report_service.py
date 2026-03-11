import logging
from typing import List, Dict
from app.models import Meeting

logger = logging.getLogger(__name__)


class ReportService:
    @staticmethod
    def summary(meetings: List[Meeting]) -> Dict:
        """Generate a summary report of meetings and action items."""
        try:
            total_meetings = len(meetings)
            total_action_items = sum(len(m.action_items) for m in meetings)
            
            summary = {
                "meetings": total_meetings,
                "action_items": total_action_items
            }
            
            logger.info(f"Summary generated: {summary}")
            return summary
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            raise
