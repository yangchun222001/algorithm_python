'''
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return [-1, -1]
        if target is None:
            return [-1, -1]

        start = 0
        end = len(A) - 1
        # find first
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

        start = 0
        end = len(A) - 1
        # find first
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        last = -1
        if A[end] == target:
            last = end
        elif A[start] == target:
            last = start

        return [first, last]
