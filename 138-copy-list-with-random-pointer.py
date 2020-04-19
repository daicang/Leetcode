
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copied_head = Node(head.val)
        node_map = {head: copied_head}
        targets = [head]

        while targets:
            curr = targets.pop()
            copied = node_map[curr]
            if curr.next:
                if curr.next not in node_map:
                    node_map[curr.next] = Node(curr.next.val)
                    targets.append(curr.next)
                copied.next = node_map[curr.next]
            if curr.random:
                if curr.random not in node_map:
                    node_map[curr.random] = Node(curr.random.val)
                    targets.append(curr.random)
                copied.random = node_map[curr.random]

        return copied_head




