# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        p = head
        h = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l))

        while h:
            _, i, node = heapq.heappop(h)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        p.next = None

        return head.next
