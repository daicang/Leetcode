# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        c1 = [root]
        h = 0

        while c1:
            h += 1
            c2 = []
            for node in c1:
                if (not node.left) and (not node.right):
                    return h

                if node.left:
                    c2.append(node.left)
                if node.right:
                    c2.append(node.right)

            c1 = c2
