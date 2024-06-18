from abc import ABC, abstractmethod


class IParticipant(ABC):
    @abstractmethod
    def say(self, value: int):
        ...

    @abstractmethod
    def receive(self, value: int):
        ...
