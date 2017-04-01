'''
Given a linked list, remove the nth node from the end of list and return its head.

 Notice

The minimum number of nodes in list is n.

Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        if head is None or n <= 0:
            return head

        pre, curt, post = self.findNthNodeFromEnd(head, n)

        if curt is None:
            return head
        if pre is None:
            return curt.next
        pre.next = post
        curt.next = None
        return head

    def findNthNodeFromEnd(self, head, n):
        if head is None:
            return None, None, None

        pre, curt, post = head, None, None

        temp = head
        while temp is not None and n >= 0:
            temp = temp.next
            n -= 1

        # curt is head
        if temp is None and n == 0:
            return None, head, head.next

        # lisk len is smaller then n
        if temp is None:
            return None, None, None

        # pre is not None, curt maybe None
        while temp is not None:
            pre = pre.next
            temp = temp.next

        curt = pre.next
        post = curt.next
        return pre, curt, post







