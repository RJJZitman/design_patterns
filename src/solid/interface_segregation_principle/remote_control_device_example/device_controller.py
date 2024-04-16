from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, device):
        pass


class DeviceMethodCommand(Command):
    def __init__(self, method, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def execute(self, device):
        getattr(device, self.method)(*self.args, **self.kwargs)


class RemoteControlDevice:
    def __init__(self, device):
        self.device = device

    def __enter__(self):
        self.device.turn_on()
        return self

    def __exit__(self, *args, **kwargs):
        self.device.turn_off()

    def operate(self, commands):
        for command in commands:
            command.execute(self.device)
