'''
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

 Notice

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Example
For L=[232, 124, 456], k=7, return 114.
'''


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def woodCut(self, L, k):
        # write your code here
        if L is None:
            return 0
        if k is 0:
            return 0

        start = 0
        end = 0
        for l in L:
            end = max(end, l)

        while start + 1 < end:
            mid = start + int((end - start) / 2)
            num = 0
            if mid == 0:
                return mid
            for l in L:
                num += int(l / mid)
            if num >= k:
                start = mid
            else:
                end = mid

        num = 0
        for l in L:
            num += int(l / end)
        if num >= k:
            return end
        return start
