# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow = head
        fast = head

        while slow and fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if slow == fast:
                break

        if not slow or not fast:
            return None

        p1 = head
        p2 = slow

        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

n4 = ListNode(-4)
n3 = ListNode(0)
n2 = ListNode(2)
n1 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

s = Solution()

n = s.detectCycle(n1)
print n.val

