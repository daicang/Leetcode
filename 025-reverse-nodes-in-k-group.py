
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(left_b, right_b):
            # left_b -> n1 .. -> nn -> right_b
            # left_b -> n1 .. <- nn -> right_b
            # left_b -> nn .. -> n1 -> right_b
            prev = left_b
            curr = left_b.next

            while curr != right_b:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            left_b.next.next = right_b
            left_b.next = prev

        count = 0
        phead = ListNode()
        phead.next = head
        curr_node = head
        left_b = phead

        while curr_node:
            count += 1
            next_node = curr_node.next
            if count == k:
                # reset counter
                count = 0
                # new left boundry is n1
                new_left_b = left_b.next
                # reverse n1 .. nn
                reverse(left_b, curr_node.next)
                left_b = new_left_b

            curr_node = next_node

        return phead.next
