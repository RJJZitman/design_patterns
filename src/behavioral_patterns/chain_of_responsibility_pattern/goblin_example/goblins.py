from game import Game
from creature import Creature


class Goblin(Creature):
    def __init__(self, game: Game, attack: int = 1, defense: int = 1):
        self.game = game
        self.game.add_creature(creature=self)

        self.base_attack = attack
        self.base_defense = defense

    def __str__(self):
        return f"defense: {self.defense}, attack: {self.attack}"

    def _king_bonus(self):
        return sum([1 for creature in self.game.creatures if isinstance(creature, GoblinKing)])

    def _goblin_comrade_bonus(self):
        return sum([1 for creature in self.game.creatures if isinstance(creature, Goblin)]) - 1

    @property
    def attack(self):
        return self.base_attack + self._king_bonus()

    @property
    def defense(self):
        return self.base_defense + self._goblin_comrade_bonus()


class GoblinKing(Goblin):
    def __init__(self, game: Game):
        super().__init__(game=game, attack=3, defense=3)

    def _king_bonus(self):
        return 0
