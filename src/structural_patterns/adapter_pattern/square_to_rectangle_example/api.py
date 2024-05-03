class Rectangle:
    """Rectangle class to work with the 'calculate area' function"""
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


def calculate_area(rc: Rectangle):
    """Calculates the area of a Rectangle"""
    return rc.width * rc.height
