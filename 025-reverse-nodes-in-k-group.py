# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        # start->n1->..->prev_end->end
        # Reverse [n1, .. end] to start->end->..->n1
        h = ListNode(0)
        h.next = head
        start = end = h

        while True:
            for i in range(k):
                end = end.next
                if not end:
                    return h.next
                if i == 0:
                    n1 = end
                if i == k-2:
                    prev_end = end

            while start.next != end:
                # start->end->n1->..->prev_end
                start.next = end
                prev_end.next = end.next
                end.next = n1

                start = end
                end = prev_end

                # Find new node prev to end
                prev_end = start
                while prev_end.next != end:
                    prev_end = prev_end.next

            start = end = n1


