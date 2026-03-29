class Event:
    def __init__(self, event_type=""):
        self.event_type = event_type  # например "PlayerJoin"
        self.actions = []             # список Action
