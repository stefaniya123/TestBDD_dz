# features/steps/note_steps.py
from behave import given, when, then
import json
from pages.note_api import NoteAPI
from factories.note_factory import NoteFactory

@given('I have a valid note payload')
def step_impl(context):
    context.payload = NoteFactory.create_valid_note()

@given('I have an invalid note payload missing "{field}"')
def step_impl(context, field):
    context.payload = NoteFactory.create_invalid_note(missing_field=field)

@given('I have created a note')
def step_impl(context):
    api = NoteAPI(context.base_url)
    payload = NoteFactory.create_valid_note()
    response = api.create_note(payload)
    assert response.status_code == 200
    context.created_note = response.json()

@given('I have an updated note payload')
def step_impl(context):
    context.updated_payload = NoteFactory.create_valid_note(title="Updated Title", content="Updated Content")

@when('I send a request to create the note')
def step_impl(context):
    api = NoteAPI(context.base_url)
    context.response = api.create_note(context.payload)

@when('I request all notes')
def step_impl(context):
    api = NoteAPI(context.base_url)
    context.response = api.get_all_notes()

@when('I request the note by its ID')
def step_impl(context):
    api = NoteAPI(context.base_url)
    note_id = context.created_note["id"]
    context.response = api.get_note_by_id(note_id)

@when('I request a note with ID {note_id:d}')
def step_impl(context, note_id):
    api = NoteAPI(context.base_url)
    context.response = api.get_note_by_id(note_id)

@when('I send a request to update the note by its ID')
def step_impl(context):
    api = NoteAPI(context.base_url)
    note_id = context.created_note["id"]
    context.response = api.update_note(note_id, context.updated_payload)

@when('I send a request to update a note with ID {note_id:d}')
def step_impl(context, note_id):
    api = NoteAPI(context.base_url)
    context.response = api.update_note(note_id, context.updated_payload)

@when('I send a request to delete the note by its ID')
def step_impl(context):
    api = NoteAPI(context.base_url)
    note_id = context.created_note["id"]
    context.response = api.delete_note(note_id)

@when('I send a request to delete a note with ID {note_id:d}')
def step_impl(context, note_id):
    api = NoteAPI(context.base_url)
    context.response = api.delete_note(note_id)

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain the correct title and content')
def step_impl(context):
    data = context.response.json()
    assert data["title"] == context.payload["title"]
    assert data["content"] == context.payload["content"]

@then('the response should be an empty list')
def step_impl(context):
    data = context.response.json()
    assert data == []

@then('the response should contain at least one note')
def step_impl(context):
    data = context.response.json()
    assert len(data) >= 1

@then('the response should contain the correct note data')
def step_impl(context):
    data = context.response.json()
    assert data["id"] == context.created_note["id"]
    assert data["title"] == context.created_note["title"]
    assert data["content"] == context.created_note["content"]

@then('the response should contain the updated title and content')
def step_impl(context):
    data = context.response.json()
    assert data["title"] == context.updated_payload["title"]
    assert data["content"] == context.updated_payload["content"]

@then('the response should confirm deletion')
def step_impl(context):
    data = context.response.json()
    assert data["detail"] == "Note deleted"