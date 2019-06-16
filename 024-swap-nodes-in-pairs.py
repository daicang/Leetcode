# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # beat 99% on time, 96% on memory
        if not head:
            return None

        # (start)->n1->(end)
        # Swap n1 with end
        h = ListNode(0)
        h.next = head
        start = end = h

        while True:
            for _ in range(2):
                end = end.next
                if not end:
                    return h.next
            n1 = start.next
            start.next = end
            n1.next = end.next
            end.next = n1

            start = end = n1

