from i_shape import IShape


class DrawingSystem:
    """A system to draw all shapes following the IShape interface"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: IShape):
        """Add a shape to the drawing system"""
        self.shapes.append(shape)

    def draw_all_shapes(self):
        """Draw the shapes"""
        for shape in self.shapes:
            shape.draw()
