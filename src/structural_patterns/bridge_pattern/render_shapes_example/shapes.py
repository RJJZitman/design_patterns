from abc import ABCMeta, abstractmethod

from renderers import Renderer


class Shape(metaclass=ABCMeta):
    """Interface for shapes that should be rendered"""
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass


class Triangle(Shape):
    """Triangle shape"""
    def __init__(self, renderer: Renderer, height):
        super().__init__(renderer, name=Triangle.__name__)
        self.height = height

    def draw(self):
        self.renderer.render_triangle(self.height)

    def resize(self, factor):
        self.height *= factor


class Square(Shape):
    """Square shape"""
    def __init__(self, renderer, side):
        super().__init__(renderer=renderer, name=Square.__name__)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor


class Circle(Shape):
    """Circle shape"""
    def __init__(self, renderer: Renderer, radius):
        super().__init__(renderer, name=Circle.__name__)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor
