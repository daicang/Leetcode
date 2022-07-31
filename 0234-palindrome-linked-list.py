
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        p = head
        count = 0

        while p:
            count += 1
            p = p.next

        stack = []
        p = head

        for i in range(count):
            if i < count // 2:
                stack.append(p.val)
            elif count % 2 == 1 and i == count // 2:
                pass
            else:
                print(stack)
                val = stack.pop()
                if p.val != val:
                    return False
            p = p.next

        return True


# [0,1,2,3] 4->2
# [0,1,2] 3->1
