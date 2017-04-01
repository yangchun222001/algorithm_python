'''
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].
'''


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []

        sum = 0
        sums = []
        map = {0: -1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == 0:
                return [0, i]
            if sum in map:
                return [map[sum] + 1, i]
            map[sum] = i
            sums.append(sum)

        sums = sorted(sums)
        small = abs(sums[0])
        presum = sums[0]
        pair = [0, 0]
        for i in range(1, len(sums)):
            if abs(sums[i] - presum) < small:
                small = abs(sums[i] - presum)
                index1 = map[sums[i]]
                index2 = map[presum]
                if index1 < index2:
                    pair = [index1 + 1, index2]
                else:
                    pair = [index2 + 1, index1]
            presum = sums[i]

        return pair


        # [6, 2, -6, -3, -2, 5]



