'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

The array may contain duplicates.

Example
Given [4,4,5,6,7,0,1,2] return 0.
'''


class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        if num is None or len(num) == 0:
            return 0
        start = 0
        end = len(num) - 1

        while start + 1 < end:
            mid = start + int((end - start) / 2)

            if num[mid] > num[end]:
                start = mid
                continue
            if num[start] == num[end]:
                end -= 1
                continue
            end = mid

        return min(num[start], num[end])