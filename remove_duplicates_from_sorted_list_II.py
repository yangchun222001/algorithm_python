'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.


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
    @param head: A ListNode
    @return: A ListNode
    """

    def deleteDuplicates(self, head):
        # since the structure changes so use dummy node
        if head is None:
            return None

        dummy = ListNode(None, head)
        pre, cur = dummy, head

        while cur is not None and cur.next is not None:
            if cur.val != cur.next.val:
                pre = pre.next
                cur = cur.next
                continue

            value = cur.val
            while cur is not None and cur.val == value:
                cur = cur.next
            pre.next = cur
        return dummy.next









