'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0
'''


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    '''
    def searchInsert(self, A, target):
        # write your code here
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

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end + 1
    '''

    def searchInsert(self, A, target):
        # edge case:
        # 1. target < all items in list
        # 2. target > all items in list
        # 3. A is empty return 0
        if A is None or target is None:
            return -1
        if len(A) == 0:
            return 0

        '''
        #solution1 O(n) complexity
        if target in A:
            return A.index(target)
        '''

        # solution2 O(logN) complexity
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        # handle edge case 1
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end

        # handle edge case 2
        return end + 1



