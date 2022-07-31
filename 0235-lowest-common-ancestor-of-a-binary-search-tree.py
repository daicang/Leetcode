# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        v1 = p.val
        v2 = q.val

        node = root
        while node:
            if node.val > v1 and node.val > v2:
                node = node.left
            elif node.val < v1 and node.val < v2:
                node = node.right
            else:
                return node
        return None
