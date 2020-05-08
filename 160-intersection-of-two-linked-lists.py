# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        node_a = headA
        node_b = headB
        count_a = count_b = 0
        while True:
            count_a += 1
            if not node_a.next:
                break
            node_a = node_a.next

        while True:
            count_b += 1
            if not node_b.next:
                break
            node_b = node_b.next

        if node_a != node_b:
            return None

        node_a = headA
        node_b = headB
        if count_a < count_b:
            while count_b > count_a:
                count_b -= 1
                node_b = node_b.next
        else:
            while count_a > count_b:
                count_a -= 1
                node_a = node_a.next

        while True:
            if node_a == node_b:
                return node_a
            node_a = node_a.next
            node_b = node_b.next
