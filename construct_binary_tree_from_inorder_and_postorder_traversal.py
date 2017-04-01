'''
Given inorder and postorder traversal of a tree, construct the binary tree.

 Notice

You may assume that duplicates do not exist in the tree.

Example
Given inorder [1,2,3] and postorder [1,3,2], return a tree:

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
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """

    def buildTree(self, inorder, postorder):
        # write your code here
        if postorder is None or inorder is None:
            return None
        if len(postorder) == 0 or len(inorder) == 0:
            return None

        val = postorder.pop()
        index = inorder.index(val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]

        left_postorder = postorder[:index]
        right_postorder = postorder[index:]

        node = TreeNode(val)
        left = self.buildTree(left_inorder, left_postorder)
        right = self.buildTree(right_inorder, right_postorder)
        node.left = left
        node.right = right

        return node