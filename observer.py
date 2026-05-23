from abc import ABC, abstractmethod

class EventListener(ABC):
    
    @abstractmethod
    def update(self, event_type, file):
        pass


class EventManager:
    def __init__(self, operations):
        self.operations = operations
        self.listeners = {}
        for op in operations:
            self.listeners[op] = []

    def subscribe(self, event_type, listener: EventListener):
        users = self.listeners[event_type]
        users.append(listener)

    def unsubscribe(self, event_type, listener):
        users = self.listeners[event_type]
        users.append(listener)

    def notify(self, event_type, file):
        users = self.listeners[event_type]
        [u.update(event_type, file) for u in users]

class Editor:
    events = EventManager(['open', 'save'])
    file = None

    def open_file(self, file):
        self.file = file
        print(f'Opening file: {file}')

    def save_file(self):
        print(f"Editor: Saving file")
        self.events.notify("open", self.file)

class EmailNotificationListener(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, event_type, file):
        print(f"Email to {self.email}: Someone has perform {event_type} on file {file}")

class LogOpenListener(EventListener):
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type, file):
        print(f"Save to log {self.log_file}: SOmeone has performed {event_type} operation on the file {file}")


if __name__ == '__main__':
    editor = Editor()

    email_listener = EmailNotificationListener("test@gmail.com")
    log_listener = LogOpenListener("path/to/log/file.txt")

    editor.events.subscribe("open", log_listener)
    editor.events.subscribe("save", log_listener)
    editor.events.subscribe("save", email_listener)

    editor.open_file("text.file")
    editor.save_file()
