from PySide6.QtWidgets import (
    QMainWindow, QPushButton, QWidget,
    QVBoxLayout, QMessageBox
)
from ui.project_wizard import ProjectWizard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minecraft Plugins Maker (MPM)")
        self.resize(800, 600)

        layout = QVBoxLayout()

        btn_new = QPushButton("Создать проект")
        btn_new.clicked.connect(self.create_project)

        layout.addWidget(btn_new)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_project(self):
        wizard = ProjectWizard(self)
        wizard.project_created.connect(self.on_project_created)
        wizard.exec()

    def on_project_created(self, name, path):
        QMessageBox.information(
            self,
            "Проект создан",
            f"Проект '{name}' успешно создан!\n\nПуть:\n{path}"
        )
