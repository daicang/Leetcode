# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def solve(node, skip):
            if not node:
                return 0
            if skip:
                return max(solve(node.left, False), solve(node.left, True)) + max(solve(node.right, False), solve(node.right, True))
            # must skip next level
            return node.val + solve(node.left, True) + solve(node.right, True)

        return max(solve(root, True), solve(root, False))
