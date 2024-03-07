# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        n = len(nodes)
        values = {n.val: True for n in nodes}

        def traverse(node):
            if not node:
                return None, 0

            node_left, count_left = traverse(node.left)
            if count_left == n:
                # LCA is left child
                return node_left, n

            node_right, count_right = traverse(node.right)
            if count_right == n:
                # LCA is right child
                return node_right, n

            count = count_left + count_right
            if node.val in values:
                count += 1

            return node, count

        node, count = traverse(root)
        if count == n:
            return node
        return None
