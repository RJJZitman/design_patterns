from abc import ABCMeta, abstractmethod


class IShape(metaclass=ABCMeta):
    """Interface for Shapes that should be drawn"""
    @abstractmethod
    def draw(self):
        pass
