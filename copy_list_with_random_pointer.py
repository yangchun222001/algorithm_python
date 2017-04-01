'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''


# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None

        mapping = {None: None}
        curt = head
        while curt is not None:
            curt2 = RandomListNode(curt.label)
            mapping[curt] = curt2
            curt = curt.next
        curt = head
        while curt is not None:
            curt2 = mapping[curt]
            curt2.next = mapping[curt.next]
            curt2.random = mapping[curt.random]
            curt = curt.next
        return mapping[head]