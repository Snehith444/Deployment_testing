from uuid import uuid4
import pytest
from app.core.services import NoteService
from app.infra.memory_repo import InMemoryNoteRepository
from app.core.excepting import ValidationError, NotFoundError


def setup_service():
    repo = InMemoryNoteRepository()
    return NoteService(repo)

def test_create_note():
    service = setup_service()
    note = service.create_note("My note", "Hello world")

    assert note.id is not None
    assert note.title == "My note"
    assert note.archived is False

def test_update_note():
    service = setup_service()
    note = service.create_note("Old", "Body")

    updated = service.update_note(note.id, "New", "Updated body")
    assert updated.title == "New"

def test_archive_note():
    service = setup_service()
    note = service.create_note("Test", "Body")

    archived = service.archive_note(note.id)
    assert archived.archived is True

def test_search_notes():
    service = setup_service()
    service.create_note("Python", "FastAPI")
    service.create_note("Java", "Spring")

    results = service.search_notes("fastapi")
    assert len(results) == 1



def test_create_note_empty_title():
    service = setup_service()
    with pytest.raises(ValidationError):
        service.create_note("", "content")


def test_create_note_empty_content():
    service = setup_service()
    with pytest.raises(ValidationError):
        service.create_note("title", "")




def test_update_non_existing_note():
    service = setup_service()
    with pytest.raises(NotFoundError):
        service.update_note(uuid4(), "t", "c")

def test_update_note_empty_title():
    service = setup_service()
    note = service.create_note("a", "b")

    with pytest.raises(ValidationError):
        service.update_note(note.id, "", "new")


def test_archive_non_existing_note():
    service = setup_service()
    with pytest.raises(NotFoundError):
        service.archive_note(uuid4())


def test_archive_already_archived_note():
    service = setup_service()
    note = service.create_note("t", "c")
    service.archive_note(note.id)

    archived_again = service.archive_note(note.id)
    assert archived_again.archived is True


def test_delete_non_existing_note_does_not_fail():
    service = setup_service()
    service.delete_note(uuid4())  


def test_list_notes_empty():
    service = setup_service()
    notes = service.list_notes()
    assert notes == []


def test_search_empty_keyword_returns_all():
    service = setup_service()
    service.create_note("Python", "FastAPI")

    results = service.search_notes("")
    assert len(results) == 1

def test_search_case_insensitive():
    service = setup_service()
    service.create_note("Python", "FastAPI")

    results = service.search_notes("fastapi")
    assert len(results) == 1

def test_search_no_match():
    service = setup_service()
    service.create_note("Python", "FastAPI")

    results = service.search_notes("java")
    assert results == []

