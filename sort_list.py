'''
Sort a linked list in O(n log n) time using constant space complexity.

Example
Given 1->3->2->null, sort it to 1->2->3->null.
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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """

    def sortList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        mid = self.findMid(head)
        rightStart = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(rightStart)

        return self.merge(left, right)

    def findMid(self, head):
        if head is None:
            return None
        fast, slow = head.next, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, list1, list2):
        dummy = ListNode(None)
        curt = dummy
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                node = list2
                list2 = list2.next
            else:
                node = list1
                list1 = list1.next
            curt.next = node
            curt = curt.next
        if list1 is not None:
            curt.next = list1
        if list2 is not None:
            curt.next = list2
        return dummy.next


