

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
            if node is None:
                return

            n1 = traverse(node.left)
            n2 = traverse(node.right)

            match_self = True
            if node.val == p.val:
                self.found_p = True
            elif node.val == q.val:
                self.found_q = True
            else:
                match_self = False

            if n1 and n2:
                # current node is LCA
                return node

            elif match_self:
                if n1 or n2:
                    # current node is LCA
                    return node
                return node

            else:
                return n1 or n2

        node = traverse(root)
        if self.found_p and self.found_q:
            return node

        return None
