# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        c1 = [root]
        c2 = []
        levles = []

        while c1:
            level = []
            for curr in c1:
                curr = c1.pop()
                level.append(curr.val)
                if curr.left:
                    c2.append(curr.left)
                if curr.right:
                    c2.append(curr.right)
            levles.append(level)
            c1 = c2
            c2 = []

        return levles

