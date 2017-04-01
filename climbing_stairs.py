'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
'''


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 1

        stairs = [1]
        stairs.append(1)
        for i in range(2, n + 1):
            stairs.append(stairs[i - 1] + stairs[i - 2])
        return stairs[n]
