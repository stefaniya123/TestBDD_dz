# factories/note_factory.py
import random
import string

class NoteFactory:
    @staticmethod
    def create_valid_note(title=None, content=None):
        if title is None:
            title = "Note " + ''.join(random.choices(string.ascii_letters, k=6))
        if content is None:
            content = "Content of " + title
        return {"title": title, "content": content}

    @staticmethod
    def create_invalid_note(missing_field="title"):
        note = {"title": "Valid Title", "content": "Valid Content"}
        if missing_field in note:
            del note[missing_field]
        return note