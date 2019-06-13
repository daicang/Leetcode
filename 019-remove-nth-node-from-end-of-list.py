# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pslow = head
        pfast = head
        delta = 0

        while pfast.next != None:
            if delta == n:
                pfast = pfast.next
                pslow = pslow.next
            elif delta < n:
                pfast = pfast.next
                delta += 1
        if delta < n:
            # head is to remove
            return head.next
        pslow.next = pslow.next.next
        return head
