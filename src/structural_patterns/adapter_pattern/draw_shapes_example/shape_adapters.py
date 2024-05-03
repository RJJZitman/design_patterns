from i_shape import IShape
from shapes_api import Rectangle, Circle, Triangle


class RectangleAdapter(IShape):
    """Adapter to make the Rectangle api comply with native IShape interface"""
    def __init__(self, rectangle: Rectangle):
        self.rectangle = rectangle

    def draw(self):
        self.rectangle.draw_rectangle()


class CircleAdapter(IShape):
    """Adapter to make the Circle api comply with native IShape interface"""
    def __init__(self, circle: Circle):
        self.circle = circle

    def draw(self):
        self.circle.draw_circle()


class TriangleAdapter(IShape):
    """Adapter to make the Triangle api comply with native IShape interface"""
    def __init__(self, triangle: Triangle):
        self.triangle = triangle

    def draw(self):
        self.triangle.draw_triangle()
