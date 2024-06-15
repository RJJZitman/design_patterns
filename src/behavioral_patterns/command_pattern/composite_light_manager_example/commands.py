from abc import ABC, abstractmethod

from light import Light


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class CompositeCommand(Command):
    def __init__(self):
        self._commands = []

    def add(self, command: Command):
        self._commands.append(command)

    def remove(self, command: Command):
        self._commands.remove(command)

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        for command in reversed(self._commands):
            command.undo()
