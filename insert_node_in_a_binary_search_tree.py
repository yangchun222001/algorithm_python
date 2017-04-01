'''
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

 Notice

You can assume there is no duplicate values in this tree + node.

Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \
  3             3   6
'''


#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        self.helper(root, node)
        return root

    def helper(self, root, node):
        if root is None:
            return

        if node.val < root.val and root.left is None:
            root.left = node
            return
        if node.val < root.val:
            self.helper(root.left, node)
        if node.val > root.val and root.right is None:
            root.right = node
            return
        if node.val > root.val:
            self.helper(root.right, node)

