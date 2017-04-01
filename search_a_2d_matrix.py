'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
'''


class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    '''
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return False
        if target is None:
            return False

        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        end = rows * columns - 1

        while start + 1 < end:
            mid = start + int((end - start) / 2)

            row = int(mid / columns)
            col = mid % columns

            if matrix[row][col] >= target:
                end = mid
            else:
                start = mid

        indexes = [start, end]

        for index in indexes:
            row = int(index / columns)
            col = index % columns

            if matrix[row][col] == target:
                return True

        return False
    '''

    def searchMatrix(self, matrix, target):
        # edge case:
        # 1. matrix is None or target is None
        # 2. len(matrix) = 0

        if matrix is None or target is None:
            return False
        if len(matrix) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start + 1 < end:
            mid = start + int((end - start) / 2)
            midM, midN = self.getRowAndCol(mid, n)

            if matrix[midM][midN] >= target:
                end = mid
            else:
                start = mid

        indexes = [start, end]
        for index in indexes:
            row, col = self.getRowAndCol(index, n)
            if matrix[row][col] == target:
                return True
        return False

    def getRowAndCol(self, index, cols):
        return int(index / cols), index % cols

