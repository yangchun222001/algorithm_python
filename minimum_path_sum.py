'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

 Notice

You can only move either down or right at any point in time.


'''


class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        mp = {(0, 0): grid[0][0]}
        for i in range(1, m):
            mp[(i, 0)] = mp[(i - 1, 0)] + grid[i][0]
        for j in range(1, n):
            mp[(0, j)] = mp[(0, j - 1)] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                mp[(i, j)] = min(mp[(i - 1, j)], mp[(i, j - 1)]) + grid[i][j]

        return mp[(m - 1, n - 1)]