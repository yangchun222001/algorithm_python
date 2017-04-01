'''
Follow up for Search in Rotated Sorted Array:

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Example
Given [1, 1, 0, 1, 1, 1] and target = 0, return true.
Given [1, 1, 1, 1, 1, 1] and target = 0, return false.
'''


class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """

    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return False
        if target is None:
            return False

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] == target or A[start] == target or A[end] == target:
                return True
            if A[mid] > A[end]:
                if A[end] > target:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[end]:
                if A[mid] < target:
                    start = mid
                else:
                    end = mid
            else:
                start += 1

        return A[start] == target or A[end] == target
