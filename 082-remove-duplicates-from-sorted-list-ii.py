# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        fake_head = ListNode(None)
        fake_head.next = head

        last_node = fake_head
        curr_node = fake_head.next
        duplicate_val = None

        while curr_node:
            if curr_node and curr_node.next and curr_node.val == curr_node.next.val:
                # Update deplicate_val
                duplicate_val = curr_node.val

            if curr_node.val == duplicate_val:
                last_node.next = curr_node.next
                curr_node = curr_node.next
            else:
                last_node = curr_node
                curr_node = curr_node.next

        return fake_head.next