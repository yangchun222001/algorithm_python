'''
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.

Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
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
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        if root is None:
            return []

        left = self.searchRange(root.left, k1, k2)
        right = self.searchRange(root.right, k1, k2)

        result = []
        result.extend(left)
        if k1 <= root.val <= k2:
            result.append(root.val)
        result.extend(right)
        return result