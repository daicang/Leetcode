from typing import Optional
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth_iter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
                continue
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return max_depth



    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
