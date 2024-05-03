from square import Square
from api import calculate_area
from adapter import SquareToRectangleAdapter


if __name__ == "__main__":
    square = Square(side=11)

    area = calculate_area(rc=SquareToRectangleAdapter(square=square))
    print(area)
