# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        currs = [h for h in lists if h is not None]

        while currs:
            min_i = 0
            for i, p in enumerate(currs):
                if p.val < currs[min_i].val:
                    min_i = i

            curr.next = currs[min_i]
            curr = curr.next

            if currs[min_i].next:
                currs[min_i] = currs[min_i].next
            else:
                currs.remove(currs[min_i])

        return head.next