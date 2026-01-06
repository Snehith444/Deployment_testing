import uuid
from uuid import UUID
from typing import List
from app.core.excepting import NotFoundError, ValidationError
from app.core.models import Note
from app.core.ports import NoteRepository



class NoteService:

    def __init__(self, repo: NoteRepository):
        self.repo = repo

 
    def _validate_text(self, value: str, field: str):
        if not value or not value.strip():
            raise ValidationError(f"{field} cannot be empty")


    def create_note(self, title: str, content: str) -> Note:
        self._validate_text(title, "title")
        self._validate_text(content, "content")

        note = Note(
            id=uuid.uuid4(),
            title=title.strip(),
            content=content.strip()
        )
        return self.repo.save(note)

    def update_note(self, note_id: UUID, title: str, content: str) -> Note:
        self._validate_text(title, "title")
        self._validate_text(content, "content")

        note = self.repo.get(note_id)
        if not note:
            raise NotFoundError("Note not found")

        note.title = title.strip()
        note.content = content.strip()
        return self.repo.save(note)

    def archive_note(self, note_id: UUID) -> Note:
        note = self.repo.get(note_id)
        if not note:
            raise NotFoundError("Note not found")

        note.archived = True
        return self.repo.save(note)

    def unarchive_note(self, note_id: UUID) -> Note:
        note = self.repo.get(note_id)
        if not note:
            raise NotFoundError("Note not found")

        note.archived = False
        return self.repo.save(note)

    def delete_note(self, note_id: UUID):
 
        self.repo.delete(note_id)


    def list_notes(self) -> List[Note]:
        return self.repo.list()

    def search_notes(self, keyword: str) -> List[Note]:
        if keyword is None:
            raise ValidationError("keyword is required")

        keyword = keyword.strip().lower()
        if not keyword:
            return self.repo.list()

        return [
            note for note in self.repo.list()
            if keyword in note.title.lower()
            or keyword in note.content.lower()
        ]
