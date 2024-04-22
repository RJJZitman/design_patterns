from abc import ABCMeta, abstractmethod


class Specification(metaclass=ABCMeta):
    """Interface for specifications that must be satisfied"""
    @abstractmethod
    def is_satisfied(self, item: any) -> bool:
        """Contains logic to validate the item"""
        pass

    def __and__(self, other):
        """Allows for combining the '&' (ampersand) operator to combine specification requirements"""
        return AndSpecification(self, other)


class AndSpecification(Specification):
    """"Specification implementation that allows to bind multiple specifications together that must all be satisfied"""
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item) -> bool:
        """Validates whether all specifications are validated by the given item"""
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class ColorSpecification(Specification):
    """Color specification"""
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item) -> bool:
        """Validate if the defined color matches the color of the item"""
        return item.color == self.color


class SizeSpecification(Specification):
    """Size specification"""
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item) -> bool:
        """Validate if the defined size matches the size of the item"""
        return item.size == self.size
