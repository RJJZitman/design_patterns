from abc import ABCMeta, abstractmethod


class IShape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass
