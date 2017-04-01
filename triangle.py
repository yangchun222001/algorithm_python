'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

 Notice

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Example
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''


class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """

    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0:
            return 0

        m = len(triangle)
        result = [[triangle[0][0]]]

        for i in range(1, m):
            result.append([result[i - 1][0] + triangle[i][0]])

        for i in range(1, m):
            n = len(triangle[i])
            for j in range(1, n - 1):
                result[i].append(min(result[i - 1][j - 1], result[i - 1][j]) + triangle[i][j])
            result[i].append(result[i - 1][n - 2] + triangle[i][n - 1])

        n = len(triangle[m - 1])
        res = result[m - 1][0]
        for j in range(1, n):
            res = min(res, result[m - 1][j])
        return res
