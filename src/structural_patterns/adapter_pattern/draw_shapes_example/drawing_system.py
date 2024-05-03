from i_shape import IShape


class DrawingSystem:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: IShape):
        self.shapes.append(shape)

    def draw_all_shapes(self):
        for shape in self.shapes:
            shape.draw()
