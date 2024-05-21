from random import randint


class RowGenerator:
    """Generates a row of a given size to construct the square"""
    @staticmethod
    def generate(count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    """constructs a list of all rows, columns and diagonals"""
    @staticmethod
    def split(array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        # get rows
        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
                result.append(the_row)

        # get cols
        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
                result.append(the_col)

        diag1 = []
        diag2 = []
        # get diagonals
        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                    r2 = row_count - r - 1
                    if c == r2:
                        diag2.append(array[r][c])
        result.append(diag1)
        result.append(diag2)
        return result


class Verifier:
    """Verifies if the sum of all rows, cols and diagonals is the same"""
    @staticmethod
    def verify(arrays):
        first = sum(arrays[0])
        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False
        return True
