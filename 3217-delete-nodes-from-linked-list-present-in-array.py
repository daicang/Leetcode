# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        phead = ListNode()
        phead.next = head
        prev = phead
        while prev.next:
            node = prev.next
            if node.val in nums:
                prev.next = node.next
            else:
                prev = prev.next
        return phead.next
