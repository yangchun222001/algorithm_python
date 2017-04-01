'''
Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

Example
Given binary search tree:

    5
   / \
  3   6
 / \
2   4
Remove 3, you can either return:

    5
   / \
  2   6
   \
    4
or

    5
   / \
  4   6
 /
2
'''


#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return None

        node = root
        father = None
        while node is not None and node.val != value:
            father = node
            if node.val > value:
                node = node.left
            else:
                node = node.right

        if node is None:
            return root

        if node.left is None and node.right is None:
            # position = 'leaf'
            if father is None:
                return None
            self.changeChild(father, value, None)
            return root

        elif node.left is not None and node.right is not None:
            # position = 'hasboth'
            replace = node.left
            rfather = node
            while replace.right is not None:
                rfather = replace
                replace = replace.right
            node.val = replace.val
            if rfather is node:
                rfather.left = replace.left
            else:
                rfather.right = replace.left
            return root

        elif node.left is None:
            # position = 'hasright'
            if father is None:
                return node.right
            self.changeChild(father, value, node.right)
            return root

        else:
            # node.right is None:
            # position = 'hasleft'
            if father is None:
                return node.left
            self.changeChild(father, value, node.left)
            return root
        return root

    def changeChild(self, father, value, node):
        if father.left is not None and father.left.val == value:
            father.left = node
        if father.right is not None and father.right.val == value:
            father.right = node










