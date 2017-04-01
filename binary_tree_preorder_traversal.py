'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].
'''

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    '''
    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []

        result = [root.val]

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        if left is not None:
            result.extend(left)
        if right is not None:
            result.extend(right)

        return result
    '''

    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) != 0:
            node = stack.pop()
            if isinstance(node, int):
                result.append(node)
                continue
            if node is None:
                continue
            stack.extend([node.right, node.left, node.val])
        return result
