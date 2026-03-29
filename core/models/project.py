class Project:
    def __init__(self, name="", platform="", path=""):
        self.name = name
        self.platform = platform  # "paper" или "levilamina"
        self.path = path

        self.events = []   # список Event
        self.commands = [] # список Command
