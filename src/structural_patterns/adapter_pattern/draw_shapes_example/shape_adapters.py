from i_shape import IShape
from shapes_api import Rectangle, Circle, Triangle


class RectangleAdapter(IShape):
    def __init__(self, rectangle: Rectangle):
        self.rectangle = rectangle

    def draw(self):
        self.rectangle.draw_rectangle()


class CircleAdapter(IShape):
    def __init__(self, circle: Circle):
        self.circle = circle

    def draw(self):
        self.circle.draw_circle()


class TriangleAdapter(IShape):
    def __init__(self, triangle: Triangle):
        self.triangle = triangle

    def draw(self):
        self.triangle.draw_triangle()
