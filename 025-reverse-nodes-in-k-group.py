from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        def reverse(begin, end):
            # -> begin -> .. -> end ->
            # -> end   -> .. -> begin ->
            prev = begin
            node = begin.next

            while node:
                next_node = node.next
                node.next = prev
                if node == end:
                    return
                prev = node
                node = next_node

        counter = 0
        phead = ListNode()
        phead.next = head

        prev = phead
        begin = head
        node = head

        while node:
            counter += 1
            next_node = node.next

            if counter == k:
                counter = 0
                reverse(begin, node)
                # prev -> [node -> begin] -> next_node
                prev.next = node
                begin.next = next_node

                prev = begin
                node = next_node
            else:
                # prev -> node -> next_node
                node = next_node

        return phead.next


    def reverseKGroup0(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        def reverse(head, tail):
            # head -> node .. -> tail ->
            # tail -> node .. -> head ->
            # returns tail as new head
            prev = head
            node = prev.next
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                if node == tail:
                    break
                node = next_node

        phead = ListNode()
        phead.next = head
        counter = 0
        node = head
        start = head
        before_start = phead

        while node:
            counter += 1
            if counter == k:
                # reverse [start .. node]
                # to: before_start [node .. start] next_node
                next_node = node.next
                reverse(start, node)

                before_start.next = node
                start.next = next_node

                before_start = start
                start = next_node

                node = next_node
                counter = 0
            else:
                node = node.next

        return phead.next
