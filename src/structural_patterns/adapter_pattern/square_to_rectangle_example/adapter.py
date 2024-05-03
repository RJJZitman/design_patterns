from square import Square


class SquareToRectangleAdapter:
    """Adapter to for the Square class to comply with the api of the Rectangle class"""
    def __init__(self, square: Square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side
