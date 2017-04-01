'''
Given two arrays, write a function to compute their intersection.

 Notice

Each element in the result must be unique.
The result can be in any order.

Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
'''


class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        if nums1 is None or nums2 is None:
            return None

        if len(nums1) == 0 or len(nums2) == 0:
            return []

        return list(set(nums1) & set(nums2))
