from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f'Width: {self._width}, Height: {self._height}'

    def area(self) -> float:
        return self._width * self._height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value


class Square(Shape):
    def __init__(self, size: float):
        self._size = size

    def __str__(self) -> str:
        return f'Size: {self._size}'

    def area(self) -> float:
        return self._size ** 2

    @property
    def size(self) -> float:
        return self._size

    @size.setter
    def size(self, value: float) -> None:
        self._size = value

    @property
    def width(self) -> float:
        return self._size

    @width.setter
    def width(self, value: float) -> None:
        self._size = value

    @property
    def height(self) -> float:
        return self._size

    @height.setter
    def height(self, value: float) -> None:
        self._size = value
