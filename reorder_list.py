'''
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Example
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.
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
    @return: nothing
    """

    def reorderList(self, head):
        # write your code here
        if head is None:
            return None
        mid = self.findMiddle(head)
        right = mid.next
        mid.next = None
        right = self.reverse(right)
        return self.merge(head, right)

    def findMiddle(self, head):
        if head is None:
            return None
        fast, slow = head.next, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        if head is None:
            return None

        prev, curt = None, head
        while curt is not None:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev

    def merge(self, list1, list2):
        dummy = ListNode(None)
        curt = dummy
        count = 0
        while list1 is not None and list2 is not None:
            if count % 2 == 0:
                curt.next = list1
                list1 = list1.next
            else:
                curt.next = list2
                list2 = list2.next
            count += 1
            curt = curt.next
        if list1 is not None:
            curt.next = list1
        if list2 is not None:
            curt.next = list2
        return dummy.next



