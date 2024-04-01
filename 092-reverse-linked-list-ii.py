# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween_recr(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        count = 0
        phead = ListNode()
        phead.next = head
        p = head

        def reverse(head, tail):
            if head == tail:
                return head
            reverse(head.next, tail)
            head.next.next = head
            head.next = None

        left_node = None
        # next node after right node
        next_node = None
        last_node = phead

        while p:
            count += 1

            if count == left:
                left_node = p
                prev_node = last_node

            elif count == right:
                next_node = p.next
                reverse(left_node, p)
                left_node.next = next_node
                prev_node.next = p

                return phead.next

            last_node = p
            p = p.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # must consider boundry
        if not head or not head.next or left == right:
            return head

        # create pseudo head
        phead = ListNode()
        phead.next = head

        # node before and after boundry
        node_before = phead
        node_after = None

        # boundry nodes
        left_boundry = None
        right_boundry = None

        # previous, current and next node
        prev_node = phead
        curr_node = head
        next_node = None
        count = 0

        while curr_node:
            # save next node at first
            next_node = curr_node.next
            count += 1

            if count < left:
                prev_node = curr_node
                curr_node = next_node

            elif count == left:
                left_boundry = curr_node
                node_before = prev_node
                prev_node = curr_node
                curr_node = next_node

            elif count <= right:
                if count == right:
                    right_boundry = curr_node
                # reverse
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node

            else:
                # count > right
                node_after = curr_node
                break

        # link with node_before and node_after
        node_before.next = right_boundry
        left_boundry.next = node_after

        return phead.next
