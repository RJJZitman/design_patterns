from i_mediator import IMediator
from i_participants import IParticipant


class Participant(IParticipant):
    def __init__(self, mediator: IMediator):
        self.value: int = 0
        self.mediator = mediator
        self.mediator.join(participant=self)

    def say(self, value: int):
        self.mediator.broadcast(sender=self, message=str(value))

    def receive(self, value: int):
        self.value += value
