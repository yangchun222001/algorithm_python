'''
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

 Notice

Assume two nodes are exist in tree.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None
        if A is None:
            return B
        if B is None:
            return A

        node, hasA, hasB = self.helper(root, A, B)
        if hasA and hasB:
            return node
        return None

    def helper(self, root, A, B):
        if root is None:
            return None, False, False

        node, leftA, leftB = self.helper(root.left, A, B)
        if leftA and leftB:
            return node, True, True
        node, rightA, rightB = self.helper(root.right, A, B)
        if rightA and rightB:
            return node, True, True

        hasA = False
        hasB = False
        if leftA or rightA or root.val == A.val:
            hasA = True
        if leftB or rightB or root.val == B.val:
            hasB = True
        return root, hasA, hasB
