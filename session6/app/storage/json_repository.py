"""JSON storage repository for meetings."""

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class JsonRepository:
    """Repository for persisting meetings to JSON."""
    
    def __init__(self, file_path: str = "data/meetings.json"):
        self.file_path = Path(file_path)
    
    def save(self, data: list[dict[str, Any]]) -> None:
        """Save meetings to JSON file."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.file_path, 'w') as f:
            json.dump(data, f)
        
        logger.info(f"Saved {len(data)} meetings to {self.file_path}")
    
    def load(self) -> list[dict[str, Any]]:
        """Load meetings from JSON file."""
        if not self.file_path.exists():
            logger.info(f"File {self.file_path} does not exist, returning empty list")
            return []
        
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        
        logger.info(f"Loaded {len(data)} meetings from {self.file_path}")
        return data
