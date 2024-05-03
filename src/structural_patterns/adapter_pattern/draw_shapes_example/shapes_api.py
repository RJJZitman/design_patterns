class Rectangle:
    """Api for rectangles"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_rectangle(self):
        print(f"Drawing a rectangle with width: {self.width} and height: {self.height}")


class Circle:
    """Api for circles"""
    def __init__(self, radius):
        self.radius = radius

    def draw_circle(self):
        print(f"Drawing a circle with radius: {self.radius}")


class Triangle:
    """Api for triangles"""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw_triangle(self):
        print(f"Drawing a triangle with base: {self.base} and height: {self.height}")
