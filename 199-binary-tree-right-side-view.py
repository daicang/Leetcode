from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        output = []
        if root is None:
            return []

        current_level = [root]
        next_level = []

        while current_level:
            for i, node in enumerate(current_level):
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if i == len(current_level)-1:
                    # Last element
                    output.append(node.val)
            current_level = next_level
            next_level = []

        return output

