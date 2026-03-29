from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout, QComboBox, QLabel
from core.models.event import Event

EVENT_TYPES = [
    "PlayerJoin",
    "PlayerQuit",
    "BlockBreak",
    "BlockPlace",
    "PlayerDamage",
    "Tick"
]

class EventsEditor(QWidget):
    def __init__(self, project):
        super().__init__()
        self.project = project

        layout = QVBoxLayout()

        self.list = QListWidget()
        layout.addWidget(QLabel("События"))
        layout.addWidget(self.list)

        btn_layout = QHBoxLayout()

        self.event_box = QComboBox()
        self.event_box.addItems(EVENT_TYPES)

        btn_add = QPushButton("Добавить")
        btn_add.clicked.connect(self.add_event)

        btn_delete = QPushButton("Удалить")
        btn_delete.clicked.connect(self.delete_event)

        btn_layout.addWidget(self.event_box)
        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_delete)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.refresh()

    def refresh(self):
        self.list.clear()
        for e in self.project.events:
            self.list.addItem(e.event_type)

    def add_event(self):
        event_type = self.event_box.currentText()
        self.project.events.append(Event(event_type))
        self.refresh()

    def delete_event(self):
        row = self.list.currentRow()
        if row >= 0:
            del self.project.events[row]
            self.refresh()
