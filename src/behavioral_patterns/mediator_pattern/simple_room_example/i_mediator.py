from abc import ABC, abstractmethod

from i_participants import IParticipant


class IMediator(ABC):
    @abstractmethod
    def join(self, participant: IParticipant):
        ...

    @abstractmethod
    def broadcast(self, sender: IParticipant, message: str):
        ...
