'''
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Example
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.
'''


class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
        if target is None:
            return 0

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        first = -1
        if A[start] == target:
            first = start
        elif A[end] == target:
            first = end

        end = len(A) - 1
        start = first
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        last = -2
        if A[end] == target:
            last = end
        elif A[start] == target:
            last = start

        return last - first + 1