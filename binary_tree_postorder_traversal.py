'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].
'''


#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    '''
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        self.postOrder(root, result)
        return result

    def postOrder(self, root, result):
        if root is None:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.val)
    '''

    def postorderTraversal(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while len(stack) != 0:
            node = stack.pop()
            if isinstance(node, int):
                result.append(node)
                continue
            stack.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result
