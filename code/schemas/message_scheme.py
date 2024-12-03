from datetime import datetime
from dataclasses import dataclass

@dataclass
class MessageScheme:
    text: str
    timestamp: datetime