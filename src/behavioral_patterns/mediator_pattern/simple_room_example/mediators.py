from i_mediator import IMediator
from participants import Participant


class AdditionRoom(IMediator):
    def __init__(self):
        self.participants: list[Participant] = []

    def join(self, participant: Participant):
        self.participants.append(participant)

    def broadcast(self, sender: Participant, message: str):
        for participant in self.participants:
            if participant is sender:
                continue
            participant.receive(value=int(message))
