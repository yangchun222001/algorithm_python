'''

Given a list of numbers, return all possible permutations.

 Notice

You can assume that there is no duplicate numbers in the list.

Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    '''
    def permute(self, nums):
        # write your code here
        if nums is None or nums is []:
            return []
        self.result = []
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, S):
        if len(nums) == len(S):
            self.result.append(S)
            return

        j = len(S)
        for i in range(len(nums)):
            if j == 0 or nums[i] not in S:
                self.dfs(nums, S + [nums[i]])
            if nums[i] in S:
                j -= 1
    '''
    '''
    public void dfs(Vertex u) {
        u.visit();
        u.visited = true;
        for (each vertex v such that (u, v) is an edge in E) {
            if (!v.visited) {
                dfs(v);
            }
        }
    }

    public void bfs(Vertex u) {
        for (each vertex v in V) {              // O(|V|) time
            v.visited = false;
        }
        u.visit(null);                // Do some unspecified thing to u
        u.visited = true;             // Mark the vertex u visited
        q = new Queue();              // New queue...
        q.enqueue(u);                 // ...initially containing u
        while (q is not empty) {      // With adjacency list, O(|E|) time
            v = q.dequeue();
            for (each vertex w such that (v, w) is an edge in E) {
                if (!w.visited) {
                    w.visit(v);        // Do some unspecified thing to w
                    w.visited = true;       // Mark the vertex w visited
                    q.enqueue(w);
                }
            }
        }                                  public class Vertex {
    }
    '''
    '''
    #no recursion
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return []

        result = []
        q = []
        q.append([])
        nums = sorted(nums)

        while len(q) != 0:
            lst = q.pop()
            j = len(nums)
            for i in range(len(nums)):
                if j != 0 and nums[i] in lst:
                    j -= 1
                    continue
                new_lst = lst + [nums[i]]
                if len(new_lst) == len(nums):
                    result.append(new_lst)
                    continue
                q.append(new_lst)
        return result
    '''
    '''
    #2nd dfs
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return []
        result = []
        self.dfs([], nums, result)
        return result

    def dfs(self, node, options, result):
        if len(options) == 0:
            result.append(node)

        for i in range(len(options)):
            child = node + [options[i]]
            self.dfs(child, options[:i] + options[i + 1:], result)
    '''

    # 2nd bfs
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return []
        result = []
        self.bfs(nums, result)
        return result

    def bfs(self, nums, result):
        lst = [([], nums)]
        while len(lst) != 0:
            node, options = lst.pop()
            if len(nums) == 0:
                result.append(node)
                continue
            for i in range(len(options)):
                child = node + [options[i]]
                lst.append((node, options[:i] + options[i + 1:]))
