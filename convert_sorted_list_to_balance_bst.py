'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Example
               2
1->2->3  =>   / \
             1   3
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        if head is None:
            return None

        pre, mid = self.findMiddle(head)
        if pre is None:
            left = None
        else:
            pre.next = None
            left = self.sortedListToBST(head)
        right = self.sortedListToBST(mid.next)
        mid = TreeNode(mid.val)
        mid.left, mid.right = left, right
        return mid

    def findMiddle(self, head):
        if head is None:
            return None, None

        fast, slow = head.next, head
        pre = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        return pre, slow
