'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

 Notice

There is at least one subarray that it's sum equals to zero.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) is None:
            return []

        prefix = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in prefix:
                return [prefix[sum] + 1, i]
            prefix[sum] = i

