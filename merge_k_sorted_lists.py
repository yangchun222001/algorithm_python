'''
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
'''
#-------------version1 divide and conquer---------------
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return None
        return self.mergeHelper(lists, 0, len(lists) - 1)

    def mergeHelper(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = start + int((end - start) / 2)
        left = self.mergeHelper(lists, start, mid)
        right = self.mergeHelper(lists, mid + 1, end)
        return self.merge2Lists(left, right)

'''

'''

#------------version2 priority queue(heap) -------------
import  heapq
class Solution:
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None

        dummy = ListNode(None)
        cur = dummy

        h = []
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(h, (lists[i].val, lists[i]))

        while len(h) != 0:
            val, node = heapq.heappop(h)
            if node.next is not None:
                heapq.heappush(h, (node.next.val, node.next))
            cur.next = node
            cur = node
        return dummy.next
'''


# -------------version3 merge2 --------------------------
class Solution:
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            list = self.merge2Lists(lists.pop(0), lists.pop(0))
            lists.append(list)
        return lists[0]

    def merge2Lists(self, list1, list2):
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





