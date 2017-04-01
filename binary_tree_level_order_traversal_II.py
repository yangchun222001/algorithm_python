'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
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
    @return: buttom-up level order in a list of lists of integers
    """

    def levelOrderBottom(self, root):
        # write your code here
        if root is None:
            return []

        lst = [root]
        level_lst = []
        result = []
        level_result = []

        while len(lst) != 0:
            node = lst.pop(0)
            level_result.append(node.val)

            if node.left is not None:
                level_lst.append(node.left)
            if node.right is not None:
                level_lst.append(node.right)

            if len(lst) != 0:
                continue
            lst = level_lst
            level_lst = []
            result.insert(0, level_result)
            level_result = []

        return result

