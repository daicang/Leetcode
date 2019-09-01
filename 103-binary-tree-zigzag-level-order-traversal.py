# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        c1 = [root]
        c2 = []
        levels = []
        reverse = False

        while c1:
            level = []
            for node in c1:
                level.append(node.val)
                if node.left:
                    c2.append(node.left)
                if node.right:
                    c2.append(node.right)
            if reverse:
                level = level[::-1]
            reverse = not reverse
            levels.append(level)
            c1 = c2
            c2 = []

        return levels

