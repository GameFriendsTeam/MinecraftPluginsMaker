from core.platforms.paper import PaperGenerator
from core.platforms.levilamina import LeviLaminaGenerator

class Generator:
    def generate(self, project):
        if project.platform == "paper":
            PaperGenerator().generate(project)
        elif project.platform == "levilamina":
            LeviLaminaGenerator().generate(project)
        else:
            raise ValueError("Unknown platform: " + project.platform)
