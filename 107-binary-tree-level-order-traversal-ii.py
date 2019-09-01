# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        levels = []
        c1 = [root]
        c2 = []

        while c1:
            level = []
            for node in c1:
                level.append(node.val)
                if node.left:
                    c2.append(node.left)
                if node.right:
                    c2.append(node.right)
            levels.append(level)
            c1 = c2
            c2 = []

        levels.reverse()
        return levels





