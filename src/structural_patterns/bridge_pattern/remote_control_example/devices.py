from abc import ABCMeta, abstractmethod


class Device(metaclass=ABCMeta):

    @property
    @abstractmethod
    def is_on(self):
        pass

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


class TV(Device):
    def __init__(self):
        self._channel = 0
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on

    @property
    def channel(self):
        return self._channel

    def power_on(self):
        self._is_on = True
        print("TV is ON")

    def power_off(self):
        self._is_on = False
        print("TV is OFF")

    def set_channel(self, channel):
        if self._is_on:
            self._channel = channel
            print(f"Channel set to {channel}")


class Radio(Device):
    def __init__(self):
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on

    def power_on(self):
        self._is_on = True
        print("Radio is ON")

    def power_off(self):
        self._is_on = False
        print("Radio is OFF")

    def set_channel(self, channel):
        if self._is_on:
            print(f"Radio frequency set to {channel} MHz")
