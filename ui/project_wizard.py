from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QPushButton,
    QLabel, QComboBox, QFileDialog
)
from PySide6.QtCore import Signal
from core.models.project import Project
from core.generator import Generator
import os


class ProjectWizard(QDialog):
    project_created = Signal(str, str)  # имя проекта, путь

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Создание проекта")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.path_edit = QLineEdit()
        self.platform_box = QComboBox()
        self.platform_box.addItems(["paper", "levilamina"])

        btn_path = QPushButton("Выбрать папку")
        btn_path.clicked.connect(self.choose_path)

        btn_create = QPushButton("Создать")
        btn_create.clicked.connect(self.create_project)

        layout.addWidget(QLabel("Имя проекта"))
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Путь"))
        layout.addWidget(self.path_edit)
        layout.addWidget(btn_path)

        layout.addWidget(QLabel("Платформа"))
        layout.addWidget(self.platform_box)

        layout.addWidget(btn_create)

        self.setLayout(layout)

    def choose_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if folder:
            self.path_edit.setText(folder)

    def create_project(self):
        name = self.name_edit.text()
        base_path = self.path_edit.text()
        platform = self.platform_box.currentText()

        if not name or not base_path:
            return  # можно добавить QMessageBox

        path = os.path.join(base_path, name)
        os.makedirs(path, exist_ok=True)

        project = Project(name=name, platform=platform, path=path)
        Generator().generate(project)

        # 🔥 ВАЖНО: сообщаем главному окну, что проект создан
        self.project_created.emit(name, path)

        self.accept()
