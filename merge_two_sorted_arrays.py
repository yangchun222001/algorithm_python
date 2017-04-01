'''

Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]
'''


class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        if A is None or len(A) == 0:
            return B
        if B is None or len(B) == 0:
            return A

        c = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] > B[j]:
                c.append(B[j])
                j += 1
                continue
            c.append(A[i])
            i += 1

        if i < len(A):
            c.extend(A[i:])
        if j < len(B):
            c.extend(B[j:])
        return c

