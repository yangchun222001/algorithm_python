'''

Given a list of numbers with duplicate number in it. Find all unique permutations.

Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
'''


class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    '''
    def permuteUnique(self, nums):
        # write your code here
        if nums is None or nums is []:
            return []
        self.result = []
        self.dfs(sorted(nums), [])
        return self.result

    def dfs(self, nums, S):
        if len(nums) == 0:
            self.result.append(S)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[(i + 1):], S + [nums[i]])
    '''

    def permuteUnique(self, nums):
        if nums is None or len(nums) == 0:
            return []

        result = []
        q = []
        nums = sorted(nums)
        q.append((nums[:], []))

        while len(q) != 0:
            available, lst = q.pop()
            for i in range(len(available)):
                if i != 0 and available[i] == available[i - 1]:
                    continue
                new_lst = lst + [available[i]]
                if len(new_lst) == len(nums):
                    result.append(new_lst)
                    continue
                q.append((available[:i] + available[i + 1:], new_lst))
        return result
