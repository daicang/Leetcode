
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_ll(node):
            if not node.next:
                return node
            new_head = reverse_ll(node.next)
            # reverse next element
            node.next.next = node
            # remove loop
            node.next = None
            return new_head

        l1 = reverse_ll(l1)
        l2 = reverse_ll(l2)
        carry = 0
        phead = ListNode()
        prev_node = phead

        while l1 or l2 or carry:
            value = carry
            carry = 0

            if l1:
                value += l1.val
                l1 = l1.next

            if l2:
                value += l2.val
                l2 = l2.next

            if value >= 10:
                carry = value // 10
                value = value % 10

            prev_node.next = ListNode(value)
            prev_node = prev_node.next

        return reverse_ll(phead.next)
