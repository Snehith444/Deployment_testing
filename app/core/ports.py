from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from app.core.models import Note

class NoteRepository(ABC):

    @abstractmethod
    def save(self, note: Note) -> Note:
        pass

    @abstractmethod
    def get(self, note_id: UUID) -> Note | None:
        pass

    @abstractmethod
    def delete(self, note_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[Note]:
        pass
