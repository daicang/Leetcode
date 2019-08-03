# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        l = 0
        p = head
        while p is not None:
            l += 1
            tail = p
            p = p.next

        k = k % l
        if k == 0:
            return head

        new_tail = head
        for _ in range(l-k-1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head

