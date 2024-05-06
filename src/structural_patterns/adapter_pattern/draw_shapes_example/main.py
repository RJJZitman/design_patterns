from drawing_system import DrawingSystem
from shapes_api import Rectangle, Circle, Triangle
from shape_adapters import RectangleAdapter, CircleAdapter, TriangleAdapter


def main():
    # create the shapes by using the foreign apis
    rectangle = Rectangle(width=11, height=7)
    circle = Circle(radius=11)
    triangle = Triangle(base=7, height=11)

    # utilise the adapters to make the shapes comply with the IShape interface
    rectangle_shape = RectangleAdapter(rectangle=rectangle)
    circle_shape = CircleAdapter(circle)
    triangle_shape = TriangleAdapter(triangle)

    # set up the drawing system
    drawing_system = DrawingSystem()
    drawing_system.add_shape(rectangle_shape)
    drawing_system.add_shape(circle_shape)
    drawing_system.add_shape(triangle_shape)

    # draw all shapes
    drawing_system.draw_all_shapes()


if __name__ == "__main__":
    main()
