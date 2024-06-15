from game import Game
from goblins import Goblin, GoblinKing

if __name__ == "__main__":
    gob_game = Game()

    gob_1 = Goblin(game=gob_game)
    print(f"goblin 1 on its own stats: {gob_1}")

    gob_2 = Goblin(game=gob_game)
    print(f"goblin 1 with single comrad stats: {gob_1}")

    gob_3 = Goblin(game=gob_game)
    print(f"goblin 1 with 2 comrads stats: {gob_1}")

    gob_king = GoblinKing(game=gob_game)
    print(f"goblin 1 with 2 comrads and a king stats: {gob_1}")
    print(f"goblin king with 3 comrads stats: {gob_king}")
