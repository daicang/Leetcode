# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        last_node = head
        curr_node = head.next

        while curr_node is not None:
            if curr_node.val == last_node.val:
                last_node.next = curr_node.next
            else:
                last_node = curr_node
            curr_node = curr_node.next

        return head


