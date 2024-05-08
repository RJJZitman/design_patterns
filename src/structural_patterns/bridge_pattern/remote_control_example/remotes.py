from abc import ABCMeta, abstractmethod


class Remote(metaclass=ABCMeta):
    def __init__(self, device):
        self._device = device

    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


class BasicRemote(Remote):
    def __init__(self, device):
        super().__init__(device)

    def power(self) -> None:
        if self._device.is_on:
            self._device.power_off()
        else:
            self._device.power_on()

    def set_channel(self, channel) -> None:
        self._device.set_channel(channel)


class AdvancedRemote(Remote):
    def __init__(self, device):
        super().__init__(device)

    def power(self) -> None:
        if self._device.is_on:
            self._device.power_off()
        else:
            self._device.power_on()

    def set_channel(self, channel) -> None:
        self._device.set_channel(channel)
        print(f"Channel {channel} saved to favorites")
