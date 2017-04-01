'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Notice

You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
'''


class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    def mergeSortedArray(self, A, m, B, n):
        if m == 0 and n == 0:
            return []

        index = m + n
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            index -= 1
            if A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1

        if j < 0:
            return A[:m + n]

        for i in range(index):
            A[i] = B[i]
        return A[:m + n]





