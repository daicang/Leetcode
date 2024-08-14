# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        mid = n // 2
        phead = ListNode()
        phead.next = head

        prev = phead

        while mid:
            prev = prev.next
            mid -= 1

        prev.next = prev.next.next

        return phead.next
