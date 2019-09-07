class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0

            hl = check(node.left)
            if hl == -1:
                return -1

            hr = check(node.right)
            if hr == -1:
                return -1

            if abs(hl-hr) > 1:
                return -1

            return max(hl, hr) + 1

        return check(root) == -1
