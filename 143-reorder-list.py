
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        count = 0
        stack = []

        while p:
            stack.append(p)
            count += 1
            p = p.next

        p = head
        for _ in range(count // 2):
            tail = stack.pop()
            next_p = p.next
            p.next = tail
            tail.next = next_p
            p = next_p

        p.next = None  # remove loop
