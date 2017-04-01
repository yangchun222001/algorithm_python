'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:

[
  [3],
  [20,9],
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
    @return: A list of list of integer include
             the zig zag level order traversal of its nodes' values
    """

    def zigzagLevelOrder(self, root):
        # write your code here
        if root is None:
            return []

        lst = [root]
        lst_temp = []
        result = []
        result_temp = []
        count = 0

        while len(lst) != 0:
            node = lst.pop(0)

            if count % 2 == 0:
                result_temp.append(node.val)
            else:
                result_temp.insert(0, node.val)

            if node.left is not None:
                lst_temp.append(node.left)
            if node.right is not None:
                lst_temp.append(node.right)

            if len(lst) != 0:
                continue
            result.append(result_temp)
            result_temp = []
            lst = lst_temp
            lst_temp = []
            count += 1

        return result


