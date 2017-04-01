'''
Given preorder and inorder traversal of a tree, construct the binary tree.

 Notice

You may assume that duplicates do not exist in the tree.

Example
Given in-order [1,2,3] and pre-order [2,1,3], return a tree:

  2
 / \
1   3
'''

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """

    def buildTree(self, preorder, inorder):
        # write your code here
        if preorder is None or inorder is None:
            return None
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        val = preorder.pop(0)
        index = inorder.index(val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]

        node = TreeNode(val)
        left = self.buildTree(preorder, left_inorder)
        right = self.buildTree(preorder, right_inorder)
        node.left = left
        node.right = right

        return node
