from uuid import UUID
from app.core.models import Note
from app.core.ports import NoteRepository

class InMemoryNoteRepository(NoteRepository):

    def __init__(self):
        self._notes = {}

    def save(self, note: Note) -> Note:
        self._notes[note.id] = note
        return note

    def get(self, note_id: UUID):
        return self._notes.get(note_id)

    def delete(self, note_id: UUID):
        self._notes.pop(note_id, None)

    def list(self):
        return list(self._notes.values())
