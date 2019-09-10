class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        curr_lv_head = root

        while curr_lv_head:
            next_lv_head = next_lv_tail = None
            curr = curr_lv_head
            while curr:
                if curr.left:
                    if next_lv_head is None:
                        next_lv_head = next_lv_tail = curr.left
                    else:
                        next_lv_tail.next = curr.left
                        next_lv_tail = curr.left

                if curr.right:
                    if next_lv_head is None:
                        next_lv_head = next_lv_tail = curr.right
                    else:
                        next_lv_tail.next = curr.right
                        next_lv_tail = curr.right

                curr = curr.next

            curr_lv_head = next_lv_head

        return root