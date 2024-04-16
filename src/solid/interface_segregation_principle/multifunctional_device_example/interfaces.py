from abc import ABCMeta, abstractmethod


class Printer(metaclass=ABCMeta):
    @abstractmethod
    def print(self, document): pass


class Scanner(metaclass=ABCMeta):
    @abstractmethod
    def scan(self, document): pass
