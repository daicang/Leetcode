
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        count = 0

        while fast.next:
            if count == n:
                fast = fast.next
                slow = slow.next
            else:
                fast = fast.next
                count += 1

        if count < n:
            return head.next
        slow.next = slow.next.next
        return head
