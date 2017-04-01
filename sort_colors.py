'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

 Notice

You are not suppose to use the library's sort function for this problem. 
You should do it in-place (sort numbers in the original array).

Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].
'''


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        r = 0
        b = len(nums) - 1
        i = 1

        while i < b:
            while nums[r] == 0:
                r += 1
            while nums[b] == 2:
                b -= 1
            if r > i:
                i = r
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1
            if nums[i] == 2:
                nums[b], nums[i] = nums[i], nums[b]
                b -= 1

        if nums[i] == 0:
            nums[r], nums[i] = nums[i], nums[r]


