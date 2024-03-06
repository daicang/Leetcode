

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def find_subtree(node, q):
            if not node:
                return False
            if node.val == q.val:
                return True
            return find_subtree(node.left, q) or find_subtree(node.right, q)

        # find down
        if find_subtree(p.left, q) or find_subtree(p.right, q):
            return p

        # find up
        while p.parent:
            parent = p.parent
            if parent.val == q.val:
                return parent

            other_branch = parent.left
            if parent.left == p:
                other_branch = parent.right

            if find_subtree(other_branch, q):
                return parent

            p = p.parent
