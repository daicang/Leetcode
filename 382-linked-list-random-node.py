import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # Reservoir sampling
        ret = self.head
        node = self.head
        i = 1
        while node.next:
            i += 1
            node = node.next
            # Take 1/i chance to keep node i
            if random.randint(0, i-1) == 0:
                ret = node
        return ret



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
