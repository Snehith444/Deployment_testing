from dataclasses import dataclass
from uuid import UUID

@dataclass
class Note:
    id: UUID
    title: str
    content: str
    archived: bool = False
