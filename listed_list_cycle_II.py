'''
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Example
Given -21->10->4->5, tail connects to node index 1，return 10
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
    @param head: The first node of the linked list.
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here

        cycle, node = self.isCycle(head)
        if not cycle:
            return None
        cur = head
        while cur != node:
            cur = cur.next
            node = node.next
        return cur

    def isCycle(self, head):
        if head is None:
            return False, None

        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True, slow
        return False, None
