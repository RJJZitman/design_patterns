from abc import ABCMeta, abstractmethod


class Powerable(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class ChannelChangeable(Powerable, metaclass=ABCMeta):
    @abstractmethod
    def change_channel(self, channel):
        pass


class VolumeControllable(Powerable, metaclass=ABCMeta):
    @abstractmethod
    def adjust_volume(self, volume):
        pass
