'''
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].
'''


class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        if A is None or len(A) == 0:
            return -1
        if target is None:
            return -1
        if k is None:
            return -1
        if k == 0:
            return []

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        result = []
        k = min(k, len(A))

        while len(result) < k:
            if start < 0:
                result.append(A[end])
                end += 1
            elif end >= len(A):
                result.append(A[start])
                start -= 1
            elif abs(A[start] - target) <= abs(A[end] - target):
                result.append(A[start])
                start -= 1
            else:
                result.append(A[end])
                end += 1

        return result


