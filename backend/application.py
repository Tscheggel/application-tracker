from dataclasses import dataclass, field
from datetime import date
from enum import Enum
import uuid

class Status(Enum):
    APPLIED = "beworben"
    REJECTED = "abgelehnt"
    INTERVIEW = "gespräch"

@dataclass
class Application:
    name: str
    company: str
    applied_at: date
    status: Status
    link: str | None = None
    notes: str | None = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        self.status = Status(self.status)

        if isinstance(self.applied_at, str):
            self.applied_at = date.fromisoformat(self.applied_at)

