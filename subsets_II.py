'''
Given a list of numbers that may has duplicate numbers, return all possible subsets

 Notice

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    '''
    def subsetsWithDup(self, S):
        # write your code here
        if S is None or len(S) == 0:
            return []

        self.result = []
        self.dfsSearch(sorted(S), [], 0)
        return self.result

    #recurision : dfs for each child do dfs
    #return: index == len(S) no child, visit it self but not recursion any more
    #recursion reduce： increase index
    def dfsSearch(self, S, nums, index):
        #visit itself
        self.result.append(nums)

        #recusion
        for i in range(index, len(S)):
            if i != index and S[i] == S[i - 1]:
                continue
            self.dfsSearch(S, nums + [S[i]], i + 1)
    '''
    '''
    #bfs
    def subsetsWithDup(self, S):
        if S is None or len(S) == 0:
            return []

        result = []
        q = []
        result.append([])
        q.append((0, []))
        S = sorted(S)
        while len(q) != 0:
            index, nums = q.pop()
            for i in range(index, len(S)):
                if i != index and S[i] == S[i-1]:
                    continue
                result.append(nums + [S[i]])
                q.append((i + 1, nums + [S[i]]))
        return result
    '''

    # 2nd time dfs
    def subsetsWithDup(self, S):
        if S is None or len(S) == 0:
            return []
        self.S = sorted(S)
        self.result = []
        self.dfs(0, [])
        return self.result

    def dfs(self, index, nums):
        self.result.append(nums)

        for i in range(index, len(self.S)):
            if i == index or self.S[i] != self.S[i - 1]:
                self.dfs(i + 1, nums + [self.S[i]])
