'''
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

 Notice

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
'''


#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''

    def serialize(self, root):
        # write your code here
        if root is None:
            return ''

        lst = [root]
        level_lst = []
        result = ''
        level_result = ''

        while len(lst) != 0:
            node = lst.pop(0)
            if node is None:
                level_result += '# '
            else:
                level_result += str(node.val)
                level_result += ' '
                level_lst.append(node.left)
                level_lst.append(node.right)

            if len(lst) != 0:
                continue

            result += level_result
            level_result = ''
            lst = level_lst
            level_lst = []

        return result

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''

    def deserialize(self, data):
        # write your code here
        if data == '':
            return None
        data = data.split(' ')
        val = int(data[0])
        root = TreeNode(val)
        supers = [root]
        children = []
        count = 0

        while len(supers) != 0:
            node = supers.pop(0)
            count += 1
            node.left = self.getNode(data, count)
            count += 1
            node.right = self.getNode(data, count)

            if node.left is not None:
                children.append(node.left)
            if node.right is not None:
                children.append(node.right)

            if len(supers) != 0:
                continue
            supers = children
            children = []
        return root

    def getNode(self, data, count):
        if count >= len(data):
            return None
        val = data[count]
        if val == '#':
            return None
        return TreeNode(int(val))