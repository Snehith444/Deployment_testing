from fastapi.testclient import TestClient
from app.main import app
from uuid import uuid4

client = TestClient(app)

def test_create_note_api():
    res = client.post("/notes/", json={
        "title": "Test",
        "content": "Body"
    })
    assert res.status_code == 200
    assert res.json()["title"] == "Test"


def test_create_note_missing_fields():
    res = client.post("/notes/", json={})
    assert res.status_code == 422


def test_create_note_empty_title_api():
    res = client.post("/notes/", json={
        "title": "",
        "content": "c"
    })
    assert res.status_code == 400


def test_update_note_invalid_uuid():
    res = client.put("/notes/123", json={
        "title": "t",
        "content": "c"
    })
    assert res.status_code == 422



def test_update_note_not_found():
    res = client.put(f"/notes/{uuid4()}", json={
        "title": "t",
        "content": "c"
    })
    assert res.status_code == 404


def test_archive_note_not_found():
    res = client.post(f"/notes/{uuid4()}/archive")
    assert res.status_code == 404


def test_delete_non_existing_note_api():
    res = client.delete(f"/notes/{uuid4()}")
    assert res.status_code == 200


def test_search_missing_query_param():
    res = client.get("/notes/search")
    assert res.status_code == 422

