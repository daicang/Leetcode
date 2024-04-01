# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        change_p1 = change_p2 = False

        while p1 and p2:
            if p1 == p2:
                return p1

            if p1.next:
                p1 = p1.next
            elif change_p1 is False:
                p1 = headB
                change_p1 = True
            else:
                break

            if p2.next:
                p2 = p2.next
            elif change_p2 is False:
                p2 = headA
                change_p2 = True
            else:
                break

        return None
