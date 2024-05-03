from drawing_system import DrawingSystem
from shapes_api import Rectangle, Circle, Triangle
from shape_adapters import RectangleAdapter, CircleAdapter, TriangleAdapter


def main():
    rectangle = Rectangle(width=11, height=7)
    circle = Circle(radius=11)
    triangle = Triangle(base=7, height=11)

    rectangle_shape = RectangleAdapter(rectangle)
    circle_shape = CircleAdapter(circle)
    triangle_shape = TriangleAdapter(triangle)

    drawing_system = DrawingSystem()
    drawing_system.add_shape(rectangle_shape)
    drawing_system.add_shape(circle_shape)
    drawing_system.add_shape(triangle_shape)

    drawing_system.draw_all_shapes()


if __name__ == "__main__":
    main()
