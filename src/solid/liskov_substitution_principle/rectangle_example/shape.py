from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """Interface for shapes"""

    @abstractmethod
    def area(self):
        """Calculate the area of a shape"""
        pass


class Rectangle(Shape):
    """Provides the structure for a rectangle"""
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def __str__(self) -> str:
        """Custom string representation to show the dimensions of the rectangle"""
        return f'Width: {self._width}, Height: {self._height}'

    def area(self) -> float:
        """Calculates the area of the rectangle"""
        return self._width * self._height

    @property
    def width(self) -> float:
        """Getter of the width property"""
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """Setter of the width property"""
        self._width = value

    @property
    def height(self) -> float:
        """Getter of the height property"""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """Setter of the height property"""
        self._height = value


class Square(Shape):
    """Provides the structure for a square"""
    def __init__(self, size: float):
        self._size = size

    def __str__(self) -> str:
        """Custom string representation to show the dimensions of the square"""
        return f'Size: {self._size}'

    def area(self) -> float:
        """Calculates the area of the square"""
        return self._size ** 2

    @property
    def size(self) -> float:
        """Getter of the size property"""
        return self._size

    @size.setter
    def size(self, value: float) -> None:
        """Setter of the size property"""
        self._size = value

    @property
    def width(self) -> float:
        """Getter of the width property"""
        return self._size

    @width.setter
    def width(self, value: float) -> None:
        """Setter of the width property"""
        self._size = value

    @property
    def height(self) -> float:
        """Getter of the height property"""
        return self._size

    @height.setter
    def height(self, value: float) -> None:
        """Setter of the height property"""
        self._size = value
