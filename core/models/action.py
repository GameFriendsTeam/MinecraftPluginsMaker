class Action:
    def __init__(self, action_type="", params=None):
        self.action_type = action_type  # например "send_message"
        self.params = params or {}      # параметры действия
