'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.
'''


class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        if A is None and B is None:
            return None
        if len(A) == 0 and len(B) == 0:
            return None

        total = len(A) + len(B)
        if total % 2 == 0:
            k = int(total / 2)
            return (self.findKth(A, 0, B, 0, k + 1) + self.findKth(A, 0, B, 0, k)) / 2.0
        else:
            k = int(total / 2)
            return self.findKth(A, 0, B, 0, k + 1)

    def findKth(self, A, startA, B, startB, k):
        if len(A) == startA:
            return B[startB + k - 1]
        if len(B) == startB:
            return A[startA + k - 1]
        if k == 1:
            return min(A[startA], B[startB])

        halfK = int(k / 2)
        if len(A) < startA + halfK:
            startB += halfK
        elif len(B) < startB + halfK:
            startA += halfK
        elif A[startA + halfK - 1] > B[startB + halfK - 1]:
            startB += halfK
        else:
            startA += halfK

        return self.findKth(A, startA, B, startB, k - halfK)










