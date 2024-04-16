from abc import ABCMeta, abstractmethod


class SortingAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, nums):
        pass


class BubbleSort(SortingAlgorithm):
    def sort(self, nums):
        # Bubble sort logic
        pass


class QuickSort(SortingAlgorithm):
    def sort(self, nums):
        # Quick sort logic
        pass