'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

 Notice

m and n will be at most 100.

Example
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''


class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mp = {}

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    mp[(i, j)] = 1
                elif i == 0:
                    mp[(i, j)] = 0 if obstacleGrid[i][j] == 1 else mp[(i, j - 1)]
                elif j == 0:
                    mp[(i, j)] = 0 if obstacleGrid[i][j] == 1 else mp[(i - 1, j)]
                else:
                    mp[(i, j)] = 0 if obstacleGrid[i][j] == 1 else mp[(i - 1, j)] + mp[(i, j - 1)]

        return mp[(m - 1, n - 1)]
