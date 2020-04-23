# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        total = 0
        node = head
        stack = []
        while node:
            total += 1
            stack.append(node)
            node = node.next

        node = head
        count = 0
        # total = 4, total/2 = 2
        # 0 1 2 3
        # 0 3 1 2
        # total = 5, total/2 = 2
        # 0 1 2 3 4
        # 0 4 1 3 2
        while count < total // 2:
            tmp = node.next
            node.next = stack.pop()
            node.next.next = tmp
            node = tmp
            count += 1
        node.next = None

