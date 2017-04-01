'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example
Given a binary tree as follow:

  1
 / \ 
2   3
   / \
  4   5
The minimum depth is 2.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0

        depth, end = self.helper(root)
        return depth

    def helper(self, root):
        if root is None:
            return 0, False
        if root.left is None and root.right is None:
            return 1, True

        ldepth, leftEnd = self.helper(root.left)
        rdepth, rightEnd = self.helper(root.right)
        if leftEnd and rightEnd:
            return min(ldepth, rdepth) + 1, True
        if leftEnd:
            return ldepth + 1, True
        if rightEnd:
            return rdepth + 1, True




