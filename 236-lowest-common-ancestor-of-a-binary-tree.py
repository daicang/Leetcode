# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found_p = self.found_q = False

        def traverse(node):
            if not node:
                return None

            n1 = traverse(node.left)
            n2 = traverse(node.right)

            if n1 and n2:
                # node is LCA
                return node

            found_current = True
            if node.val == p.val:
                self.found_p = True
            elif node.val == q.val:
                self.found_q = True
            else:
                found_current = False

            if found_current:
                return node

            return n1 or n2

        node = traverse(root)
        if self.found_p and self.found_q:
            return node
        return None
