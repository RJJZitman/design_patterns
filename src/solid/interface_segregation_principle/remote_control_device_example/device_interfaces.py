from abc import ABCMeta, abstractmethod


class Powerable(metaclass=ABCMeta):
    """Interface for devices that can be turned on and off"""

    def __enter__(self):
        """Context manager to allow proper device usage"""
        self.turn_on()
        return self

    def __exit__(self, *args, **kwargs):
        """Context manager to allow proper device usage"""
        self.turn_off()

    @abstractmethod
    def turn_on(self):
        """Turns on the device"""
        pass

    @abstractmethod
    def turn_off(self):
        """Turns off the device"""
        pass


class ChannelChangeable(Powerable, metaclass=ABCMeta):
    """Interface for Powerable devices that can switch between channels"""
    @abstractmethod
    def change_channel(self, channel: int):
        """Change the channel on which the device currently operates"""
        pass


class VolumeControllable(Powerable, metaclass=ABCMeta):
    """Interface for Powerable devices that can adjust volume levels"""
    @abstractmethod
    def adjust_volume(self, volume: int):
        """Change the volume which the device currently produces"""
        pass
