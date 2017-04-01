'''
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.
'''


class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        if A is None or len(A) == 0:
            return -1
        if target is None:
            return -1

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1