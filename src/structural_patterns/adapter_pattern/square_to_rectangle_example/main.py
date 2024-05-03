from square import Square
from api import calculate_area
from adapter import SquareToRectangleAdapter


if __name__ == "__main__":
    square = Square(side=11)

    # Note that the linter breaks on the type checking due to the type hints.
    # This is expected and (for this illustrative example) accepted behaviour for fully tested Adapters
    area = calculate_area(rc=SquareToRectangleAdapter(square=square))
    print(f"The area of my Rectangle is: {area}")
