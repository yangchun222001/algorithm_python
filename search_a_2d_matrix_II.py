'''
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.

Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.
'''


class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
        if target is None:
            return 0
        total = 0

        startRow = 0
        endRow = len(matrix) - 1
        last = len(matrix[0]) - 1

        start = 0
        end = endRow
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if matrix[mid][0] > target:
                end = mid
            else:
                start = mid
        endRow = end
        if matrix[start][0] >= target:
            endRow = start

        start = 0
        end = endRow
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if matrix[mid][last] > target:
                end = mid
            else:
                start = mid
        startRow = start
        if matrix[end][last] <= target:
            startRow = end

        for i in range(startRow, endRow + 1):
            start = 0
            end = last
            while start + 1 < end:
                mid = start + int((end - start) / 2)
                if matrix[i][mid] > target:
                    end = mid
                else:
                    start = mid
            if matrix[i][start] == target or matrix[i][end] == target:
                total += 1
        return total


