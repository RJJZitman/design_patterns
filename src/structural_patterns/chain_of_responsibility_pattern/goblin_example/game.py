from creature import Creature


class Game:
    def __init__(self):
        self.creatures: list[Creature] = []

    def add_creature(self, creature: Creature):
        self.creatures.append(creature)
