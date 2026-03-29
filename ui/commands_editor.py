from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout, QLineEdit, QLabel
from core.models.command import Command

class CommandsEditor(QWidget):
    def __init__(self, project):
        super().__init__()
        self.project = project

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Команды"))
        self.list = QListWidget()
        layout.addWidget(self.list)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Имя команды (без /)")

        self.desc_edit = QLineEdit()
        self.desc_edit.setPlaceholderText("Описание команды")

        layout.addWidget(self.name_edit)
        layout.addWidget(self.desc_edit)

        btn_layout = QHBoxLayout()

        btn_add = QPushButton("Добавить")
        btn_add.clicked.connect(self.add_command)

        btn_delete = QPushButton("Удалить")
        btn_delete.clicked.connect(self.delete_command)

        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_delete)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.refresh()

    def refresh(self):
        self.list.clear()
        for c in self.project.commands:
            self.list.addItem(f"/{c.name} — {c.description}")

    def add_command(self):
        name = self.name_edit.text().strip()
        desc = self.desc_edit.text().strip()

        if not name:
            return

        self.project.commands.append(Command(name, desc))
        self.name_edit.clear()
        self.desc_edit.clear()
        self.refresh()

    def delete_command(self):
        row = self.list.currentRow()
        if row >= 0:
            del self.project.commands[row]
            self.refresh()
