from abc import ABCMeta, abstractmethod
from collections.abc import Sequence


class SortingAlgorithm(metaclass=ABCMeta):
    """Interface for sorting algorithms"""
    @abstractmethod
    def sort(self, nums: Sequence[int | float]) -> Sequence[int | float]:
        """Sorts the sequence"""
        pass


class BubbleSort(SortingAlgorithm):
    """Bubble sort algorithm"""
    def sort(self, nums: Sequence[int | float]) -> Sequence[int | float]:
        # Bubble sort logic
        pass


class QuickSort(SortingAlgorithm):
    """Quick sort algorithm"""
    def sort(self, nums: Sequence[int | float]) -> Sequence[int | float]:
        # Quick sort logic
        pass
