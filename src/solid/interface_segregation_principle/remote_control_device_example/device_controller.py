from abc import ABCMeta, abstractmethod

from device_interfaces import Powerable


class Command(metaclass=ABCMeta):
    """Interface for command structuring"""
    @abstractmethod
    def execute(self, on: any):
        """Executes a command"""
        pass


class RemoteControl:
    """Implements the execution orchestration of the commands"""
    def __init__(self, device: Powerable):
        self.device = device

    def __enter__(self):
        """Implements the context managers of the object"""
        self.device.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        """Implements the context managers of the object"""
        self.device.__exit__()

    def operate(self, commands: list[Command]):
        """Executes a list of commands"""
        for command in commands:
            command.execute(self.device)


class MethodCommand(Command):
    """Class to execute commands on a object"""
    def __init__(self, method: str, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def execute(self, on: any):
        """Executes the command on the object"""
        getattr(on, self.method)(*self.args, **self.kwargs)