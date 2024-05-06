from abc import ABCMeta, abstractmethod


class Renderer(metaclass=ABCMeta):
    """Renderer interface"""  # Breaks OCP
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_square(self, side):
        pass

    @abstractmethod
    def render_triangle(self, height):
        pass


class VectorRenderer(Renderer):
    """Renders shapes as vectors"""
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing a square with side {side}')

    def render_triangle(self, height):
        print(f'Drawing a circle of height {height}')


class RasterRenderer(Renderer):
    """Renders shapes as pixels"""
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing pixels for square with side {side}')

    def render_triangle(self, height):
        print(f'Drawing pixels for circle of height {height}')

