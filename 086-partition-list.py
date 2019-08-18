# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before_head = before_tail = ListNode(None)
        after_head = after_tail = ListNode(None)

        curr = head
        while curr:
            if curr.val < x:
                before_tail.next = curr
                before_tail = before_tail.next
            else:
                after_tail.next = curr
                after_tail = after_tail.next
            curr = curr.next

        before_tail.next = after_head.next
        after_tail.next = None
        return before_head.next


