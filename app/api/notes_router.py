from fastapi import APIRouter
from uuid import UUID

from app.schemas.notes_schema import NoteCreate, NoteUpdate
from app.core.services import NoteService
from app.infra.memory_repo import InMemoryNoteRepository
from app.api.response import build_response

router = APIRouter(prefix="/notes", tags=["Notes"])

repo = InMemoryNoteRepository()
service = NoteService(repo)


@router.post("/")
def create_note(payload: NoteCreate):
    note = service.create_note(payload.title, payload.content)
    return build_response(
        success=True,
        message="Note created successfully",
        data=note
    )


@router.put("/{note_id}")
def update_note(note_id: UUID, payload: NoteUpdate):
    note = service.update_note(note_id, payload.title, payload.content)
    return build_response(
        success=True,
        message="Note updated successfully",
        data=note
    )


@router.get("/")
def list_notes():
    notes = service.list_notes()
    return build_response(
        success=True,
        message="Notes fetched successfully",
        data=notes
    )


@router.get("/search")
def search_notes(q: str):
    notes = service.search_notes(q)
    return build_response(
        success=True,
        message="Search results fetched",
        data=notes
    )


@router.post("/{note_id}/archive")
def archive(note_id: UUID):
    note = service.archive_note(note_id)
    return build_response(
        success=True,
        message="Note archived successfully",
        data=note
    )


@router.post("/{note_id}/unarchive")
def unarchive(note_id: UUID):
    note = service.unarchive_note(note_id)
    return build_response(
        success=True,
        message="Note unarchived successfully",
        data=note
    )


@router.delete("/{note_id}")
def delete(note_id: UUID):
    service.delete_note(note_id)
    return build_response(
        success=True,
        message="Note deleted successfully",
        data=None
    )
