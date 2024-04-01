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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        phead = ListNode()
        phead.next = head
        prev = phead

        # prev -> n1 -> n2
        # swap n1 with n2
        # prev -> n2 -> n1
        while prev:
            n1 = prev.next
            if not n1:
                break
            n2 = n1.next
            if not n2:
                break

            n1.next = n2.next
            n2.next = n1
            prev.next = n2

            prev = n1

        return phead.next
