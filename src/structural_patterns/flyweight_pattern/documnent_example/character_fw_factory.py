from typing import Dict


class CharacterFlyweight:
    def __init__(self, char: str):
        self.char = char

    def render(self, font_size: int):
        print(f'Rendering character {self.char} at font size {font_size}')


class CharacterFlyweightFactory:
    _flyweights: Dict[str, CharacterFlyweight] = {}

    @staticmethod
    def get_flyweight(char: str) -> CharacterFlyweight:
        if char not in CharacterFlyweightFactory._flyweights:
            CharacterFlyweightFactory._flyweights[char] = CharacterFlyweight(char)
        return CharacterFlyweightFactory._flyweights[char]
