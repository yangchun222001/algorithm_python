'''
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

 Notice

The array may contains multiple peeks, find any of them.

Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)
'''


class Solution:
    # @param A: An integers list.
    # @return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] > A[end]:
            return start
        return end