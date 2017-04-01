'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [1,3,2].
'''


#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    '''
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root is None:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

        return
    '''

    def inorderTraversal(self, root):
        if root is None:
            return []

        lst = [root]
        result = []

        while len(lst) != 0:
            node = lst.pop()
            if isinstance(node, int):
                result.append(node)
                continue
            if node.right is not None:
                lst.append(node.right)
            lst.append(node.val)
            if node.left is not None:
                lst.append(node.left)

        return result