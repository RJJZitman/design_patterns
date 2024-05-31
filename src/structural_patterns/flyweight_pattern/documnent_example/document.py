from character_fw_factory import CharacterFlyweightFactory


class Document:
    def __init__(self):
        self.characters = []
        self.font_sizes = []

    def add_character(self, char: str, font_size: int):
        flyweight = CharacterFlyweightFactory.get_flyweight(char)
        self.characters.append(flyweight)
        self.font_sizes.append(font_size)

    def render(self):
        for i, char in enumerate(self.characters):
            char.render(self.font_sizes[i])