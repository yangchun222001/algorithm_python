'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

 Notice

m and n will be at most 100.

Example
Given m = 3 and n = 3, return 6.
Given m = 4 and n = 5, return 35.


'''


class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        if m == 0 or n == 0:
            return 0

        mp = {}
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    mp[(i, j)] = 1
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]

        return mp[(m - 1, n - 1)]