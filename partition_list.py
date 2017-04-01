'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
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
    @param x: an integer
    @return: a ListNode 
    """

    def partition(self, head, x):
        # write your code here
        if head is None:
            return head

        leftDummy, rightDummy = ListNode(None), ListNode(None)
        left, right = leftDummy, rightDummy

        cur = head
        while cur is not None:
            if cur.val < x:
                left.next = cur
                cur = cur.next
                left = left.next
                left.next = None
            else:
                right.next = cur
                cur = cur.next
                right = right.next
                right.next = None
        left.next = rightDummy.next
        return leftDummy.next
