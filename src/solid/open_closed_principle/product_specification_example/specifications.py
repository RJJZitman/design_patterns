from abc import ABCMeta, abstractmethod


class Specification(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        """Allows for combining the '&' (ampersand) operator to combine specification requirements"""
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size
