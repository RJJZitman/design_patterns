from collections.abc import Sequence

from algorithms import SortingAlgorithm, BubbleSort, QuickSort


def sort_numbers(sorting_algorithm: SortingAlgorithm, nums: Sequence[int | float]):
    """Returns the sorted numbers by the given SortingAlgorithm"""
    sorting_algorithm.sort(nums)
    return nums


if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 2, 7, 4, 6]

    # Sort using Bubble Sort
    sorted_numbers = sort_numbers(BubbleSort(), numbers.copy())
    print("Sorted using Bubble Sort:", sorted_numbers)

    # Sort using Quick Sort
    sorted_numbers = sort_numbers(QuickSort(), numbers.copy())
    print("Sorted using Quick Sort:", sorted_numbers)
