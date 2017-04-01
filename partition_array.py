'''
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

 Notice

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.
'''


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    '''
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if nums is None or len(nums) == 0:
            return 0

        i = 0
        j = len(nums) - 1

        while i < j:
            while i < j and nums[i] < k:
                i += 1
            while i < j and nums[j] >= k:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        if nums[i] < k:
            return i + 1
        return i
    '''

    def partitionArray(self, nums, k):
        # edge case:
        # 1. nums is None or len(nums) = 0
        # 2. [1 2] k = 0 return 0
        # 3. [1 2] k = 3 return 2

        if nums is None or len(nums) == 0:
            return 0

        i = 0
        j = len(nums) - 1

        while i < j:
            while i < j and nums[i] < k:
                i += 1
            while i < j and nums[j] >= k:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        if nums[i] < k:
            return i + 1
        return i