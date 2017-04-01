'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Example
Given the below binary tree:

  1
 / \
2   3
return 6.
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

    def maxPathSum(self, root):
        # write your code here
        if root is None:
            return 0

        single, double = self.helper(root)
        return max(single, double)

    def helper(self, root):
        if root is None:
            return None, None

        leftSingle, leftDouble = self.helper(root.left)
        rightSingle, rightDouble = self.helper(root.right)

        if leftSingle is None and rightSingle is None:
            return root.val, root.val

        if leftSingle is None and rightSingle is not None:
            return max(rightSingle, 0) + root.val, max(rightSingle + root.val, rightDouble, root.val)

        if rightSingle is None and leftSingle is not None:
            return max(leftSingle, 0) + root.val, max(leftSingle + root.val, leftDouble, root.val)

        single = max(leftSingle, rightSingle, 0) + root.val
        double = max(leftSingle + rightSingle + root.val, leftDouble, rightDouble, root.val)

        return single, double

