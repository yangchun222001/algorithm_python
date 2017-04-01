'''

Given a set of distinct integers, return all possible subsets.

 Notice

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Have you met this question in a real interview? Yes
Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    '''
    #dfs
    def subsets(self, S):
        # write your code here
        if S is None or len(S) == 0:
            return []
        self.result = []
        self.search(sorted(S), [], 0)
        return self.result

    #recursion define: find all subsets after i
    #recursion return: if index equals the lenght of S
    #recursion reduction: index increase
    def search(self, S, nums, index):
        self.result.append(nums)

        for i in range(index, len(S)):
            self.search(S, nums + [S[i]], i + 1)
    '''
    '''
    #bit manipulation
    def subsets(self, S):
        len_s = len(S)
        result = []
        S = sorted(S)
        for i in range(1 << len_s):
            nums = []
            for j in range(len_s):
                if (i & (1 << j)) != 0:
                    nums.append(S[j])
            result.append(nums)
        return result
    '''
    '''
    #bfs
    def subsets(self, S):
        q = []
        result = []
        result.append([])
        q.append((0,[]))
        S = sorted(S)
        while len(q) != 0:
            index, nums = q.pop()
            for i in range(index, len(S)):
                result.append(nums + [S[i]])
                q.append((i + 1, nums + [S[i]]))
        return result
    '''
    '''
    #2nd time dfs
    def subsets(self, S):
        if S is None or len(S) == 0:
            return []

        result = []
        self.dfs(sorted(S), 0, [], result)
        return result

    def dfs(self, S, index, nums, result):
        #visit(自己）
        result.append(nums)

        #对每一个孩子
        for i in range(index, len(S)):
            #每一个孩子再迭代，所以是新数组，孩子嘛，又不是自己
            self.dfs(S, i + 1, nums + [S[i]], result)
    '''

    # 2nd time bfs
    def subsets(self, S):
        if S is None or len(S) == 0:
            return []

        result = []
        self.bfs(sorted(S), 0, result)
        return result

    def bfs(self, S, index, result):
        lst = [([], index)]

        while len(lst) != 0:
            # 取node
            nums, index = lst.pop(0)
            # visit(node)
            result.append(nums)
            # 放自己的孩子进list (自己的孩子嘛，所以肯定建一个新的）
            for i in range(index, len(S)):
                # 放进result里面的都是新的
                lst.append((nums + [S[i]], i + 1))