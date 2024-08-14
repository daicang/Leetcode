# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()

        odd_head.next = head
        pe = even_head

        p = head
        p_prev = odd_head

        while p and p.next:
            pe.next = p.next
            p.next = p.next.next

            p_prev = p
            p = p.next
            pe = pe.next
            pe.next = None

        if p:
            p.next = even_head.next
        else:
            p_prev.next = even_head.next


        return odd_head.next
