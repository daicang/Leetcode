
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head

        def traverse(node):
            if node is None:
                return True
            if traverse(node.next) is False:
                return False
            # when returning from the call stack
            # it is like postorder, node is called in reverse order
            if node.val != self.left.val:
                return False
            self.left = self.left.next
            return True

        return traverse(head)
