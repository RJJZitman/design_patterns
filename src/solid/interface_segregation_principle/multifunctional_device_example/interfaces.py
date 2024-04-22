from abc import ABCMeta, abstractmethod


class Printer(metaclass=ABCMeta):
    """Interface for printers"""
    @abstractmethod
    def print(self, document: str):
        """Print the document content"""
        pass


class Scanner(metaclass=ABCMeta):
    """Interface for scanners"""
    @abstractmethod
    def scan(self, document: str):
        """Scan the document"""
        pass
