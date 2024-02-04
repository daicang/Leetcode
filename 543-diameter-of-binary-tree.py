
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestPath(self, root):
        if not root:
            return 0
        len_left = self.longestPath(root.left)
        len_right = self.longestPath(root.right)

        self.diameter = max(self.diameter, len_left+len_right)

        return max(len_left, len_right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.longestPath(root)

        return self.diameter
