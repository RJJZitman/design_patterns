from shape import Rectangle, Square


if __name__ == "__main__":
    width, height = 2, 3
    rectangle = Rectangle(width=width, height=height)
    print(f'Expected an area of {width * height}, got {rectangle.area()}')

    rectangle.width = 6
    expected = width * height
    print(f'Expected an area of {rectangle.width * height}, got {rectangle.area()}')

    size = 5
    square = Square(size=size)
    print(f'Expected an area of {size**2}, got {square.area()}')
    square.size = 11
    print(f'Expected an area of {square.size**2}, got {square.area()}')
