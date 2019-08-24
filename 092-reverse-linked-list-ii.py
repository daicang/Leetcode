# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        fake_head = ListNode(None)
        fake_head.next = head

        front = fake_head

        for _ in range(1, m):
            front = front.next

        count = n - m
        end = front.next
        while count > 0:
            curr = end.next
            end.next = curr.next
            curr.next = front.next
            front.next = curr

            count -= 1

        return fake_head.next

