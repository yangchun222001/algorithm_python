'''
Reverse a linked list from position m to n.

 Notice

Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
'''
#Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        if head is None:
            return None

        dummy = ListNode(None, head)
        nodeM = self.findNode(dummy, m)
        nodeN = self.findNode(head, n)

        start = nodeM.next
        nxt = nodeN.next
        nodeN.next = None

        self.reverse(start)
        nodeM.next = nodeN
        start.next = nxt
        return dummy.next

    def reverse(self, head):
        if head is None:
            return None
        if head.next is None:
            return head

        pre = head
        cur = head.next

        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        head.next = None
        return pre

    def findNode(self, head, m):
        if head is None:
            return None

        temp = head
        for i in range(1, m):
            if temp is None:
                return None
            temp = temp.next
        return temp
