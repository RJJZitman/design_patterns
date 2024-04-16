from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def change_channel(self, channel):
        pass

    @abstractmethod
    def adjust_volume(self, volume):
        pass


class TV(RemoteControl):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")

    def change_channel(self, channel):
        print(f"TV channel changed to {channel}")

    def adjust_volume(self, volume):
        print(f"TV volume adjusted to {volume}")


class Stereo(RemoteControl):
    def turn_on(self):
        print("Stereo turned on")

    def turn_off(self):
        print("Stereo turned off")

    def change_channel(self, channel):
        pass  # Not applicable to stereo

    def adjust_volume(self, volume):
        print(f"Stereo volume adjusted to {volume}")


class RemoteControlDevice:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()
        self.device.change_channel(5)
        self.device.adjust_volume(20)
        self.device.turn_off()

# break isp by implementing functionalities in the interface that do not necessarily hold for the implementations
