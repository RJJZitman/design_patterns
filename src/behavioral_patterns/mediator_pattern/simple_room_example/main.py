from mediators import AdditionRoom
from participants import Participant


if __name__ == "__main__":
    game = AdditionRoom()

    p1 = Participant(mediator=game)
    p2 = Participant(mediator=game)

    print(p1.value, p2.value)

    p1.say(value=3)
    print(p1.value, p2.value)
    p2.say(value=1)
    print(p1.value, p2.value)
