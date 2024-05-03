class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


def calculate_area(rc: Rectangle):
    return rc.width * rc.height
