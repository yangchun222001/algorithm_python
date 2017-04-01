'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST

Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
'''

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    '''
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True

        valid, mx, mn = self.validate(root)
        return valid

    def validate(self, root):
        if root is None:
            return True, None, None

        valid, leftMax, leftMin = self.validate(root.left)
        if not valid:
            return False, 0, 0
        valid, rightMax, rightMin = self.validate(root.right)
        if not valid:
            return False, 0, 0

        if leftMax is None:
            left = True
        else:
            left = leftMax < root.val
        if rightMin is None:
            right = True
        else: 
            right = root.val < rightMin

        if rightMax is None:
            rightMax = root.val
        if leftMin is None:
            leftMin = root.val

        if left and right:
            return True, rightMax, leftMin
        return False, 0, 0
    '''

    def isValidBST(self, root):
        if root is None:
            return True
        isBST, small, big = self.validate(root)
        return isBST

    def validate(self, root):
        if root is None:
            return True, None, None

        left, leftMin, leftMax = self.validate(root.left)
        if not left:
            return False, None, None
        right, rightMin, rightMax = self.validate(root.right)
        if not right:
            return False, None, None

        if (leftMax is None or leftMax < root.val) and (rightMin is None or rightMin > root.val):
            small = None if leftMin is None else root.val
            big = None if rightMax is None else root.val
            return True, small, big
        return False, None, None

