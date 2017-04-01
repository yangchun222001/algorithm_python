'''
Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

Example
    1             1
   / \           / \
  2   2   and   2   2
 /             /
4             4
are identical.

    1             1
   / \           / \
  2   3   and   2   3
 /               \
4                 4
are not identical.
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # Write your code here
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False

        leftleft = self.isIdentical(a.left, b.left)
        rightright = self.isIdentical(a.right, b.right)

        if a.val != b.val:
            return False
        if leftleft and rightright:
            return True

        return False