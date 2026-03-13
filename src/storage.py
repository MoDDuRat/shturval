class NoteStorage:
    def __init__(self):
        self.notes = []
        self.id_counter = 1

    def add_note(self, title, body):
        note = {
            "id": self.id_counter,
            "title": title,
            "body": body
        }
        self.notes.append(note)
        print(f"Добавлена заметка {self.id_counter}")
        self.id_counter += 1

    def get_all_notes(self):
        if not self.notes:
            print("Заметок нет")
        else:
            for note in self.notes:
                print(f"{note['id']}. {note['title']} - {note['body']}")

    def remove_note(self, note_id):
        for index, note in enumerate(self.notes):
            if note["id"] == note_id:
                del self.notes[index]
                print(f"Удалена заметка {note_id}")
                return
        print(f"Заметка {note_id} не найдена")