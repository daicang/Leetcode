# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def merge(l1, l2):
            fake_head = ListNode(0)
            node = fake_head
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            if l1:
                node.next = l1
            elif l2:
                node.next = l2
            else:
                node.next = None
            return fake_head.next

        p1 = p2 = head
        while p2 and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        p2 = p1.next
        p1.next = None

        # print(p2.val)
        return merge(self.sortList(head), self.sortList(p2))



s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

# 4 2 1 3
n4.next = n2
n2.next = n1
n1.next = n3

l = s.sortList(n4)
n = l
while n:
    print(n.val)
    n = n.next

