from shapes import Triangle, Square, Circle
from renderers import RasterRenderer, VectorRenderer


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(141)
    circle.draw()

    square = Square(raster, 5)
    square.draw()
    square.resize(7)
    square.draw()

    triangle = Triangle(raster, 5)
    triangle.draw()
    triangle.resize(11)
    triangle.draw()
