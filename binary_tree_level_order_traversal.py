'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """

    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []

        stack = [root]
        stack_temp = []
        result = []
        temp = []

        while len(stack) != 0:
            node = stack.pop(0)
            temp.append(node.val)
            if node.left is not None:
                stack_temp.append(node.left)
            if node.right is not None:
                stack_temp.append(node.right)
            if len(stack) == 0:
                stack.extend(stack_temp)
                result.append(temp)
                stack_temp = []
                temp = []
        return result


