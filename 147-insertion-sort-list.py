# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        fake_head = ListNode(0)
        fake_head.next = head
        prev = head

        # start from head.next
        while prev.next:
            if prev.next.val >= prev.val:
                prev = prev.next
                continue

            curr = prev.next
            prev.next = prev.next.next
            node = fake_head
            while node.next.val < curr.val:
                node = node.next
            curr.next = node.next
            node.next = curr

        return fake_head.next

s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

# 4 2 1 3
n4.next = n2
n2.next = n1
n1.next = n3

l = s.insertionSortList(n4)
n = l
while n:
    print(n.val)
    n = n.next

