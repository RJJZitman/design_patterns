from abc import ABCMeta, abstractmethod

from specifications import Specification


class FilterInterface(metaclass=ABCMeta):
    """Interface for filters"""

    @staticmethod
    @abstractmethod
    def filter(items: list[any], spec: Specification) -> any:
        pass


class FilterSpec(FilterInterface):
    @staticmethod
    def filter(items: list[any], spec: Specification) -> any:
        """Filter items on provided specification"""
        for item in items:
            if spec.is_satisfied(item):
                yield item
