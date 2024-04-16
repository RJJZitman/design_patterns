from abc import ABCMeta, abstractmethod

from specifications import Specification


class FilterInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def filter(items: list[any], spec: Specification):
        pass


class Filter(FilterInterface):
    @staticmethod
    def filter(items: list[any], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item
