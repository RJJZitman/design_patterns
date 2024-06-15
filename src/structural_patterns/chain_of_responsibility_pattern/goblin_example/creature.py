from abc import ABCMeta, abstractmethod


class Creature(metaclass=ABCMeta):

    @property
    @abstractmethod
    def attack(self):
        ...

    @property
    @abstractmethod
    def defense(self):
        ...
