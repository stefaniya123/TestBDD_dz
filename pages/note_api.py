# pages/note_api.py
import requests

class NoteAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_note(self, payload):
        return requests.post(f"{self.base_url}/notes", json=payload)

    def get_all_notes(self):
        return requests.get(f"{self.base_url}/notes")

    def get_note_by_id(self, note_id):
        return requests.get(f"{self.base_url}/notes/{note_id}")

    def update_note(self, note_id, payload):
        return requests.put(f"{self.base_url}/notes/{note_id}", json=payload)

    def delete_note(self, note_id):
        return requests.delete(f"{self.base_url}/notes/{note_id}")