from core.models.action import Action
from core.models.command import Command
from core.models.event import Event
from core.models.project import Project


def test_action_default_params_are_isolated_between_instances():
    first = Action(action_type="send_message")
    second = Action(action_type="send_message")

    first.params["text"] = "Hello"

    assert second.params == {}


def test_project_event_and_command_lists_start_empty():
    project = Project(name="Demo", platform="paper", path="/tmp/demo")

    assert project.events == []
    assert project.commands == []


def test_event_and_command_action_lists_start_empty():
    event = Event(event_type="PlayerJoin")
    command = Command(name="ping", description="Ping command")

    assert event.actions == []
    assert command.actions == []
