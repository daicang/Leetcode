# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if not root:
            return []

        def put(node):
            stack.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        put(root)

        while stack:
            curr = stack.pop()
            if isinstance(curr, int):
                result.append(curr)
            else:
                put(curr)

        return result


s = Solution()


