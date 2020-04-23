# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        node = root
        while node:
            if node.right:
                stack.append(node.right)
            result.append(node.val)
            if node.left:
                node = node.left
            elif stack:
                node = stack.pop()
            else:
                break
        return result