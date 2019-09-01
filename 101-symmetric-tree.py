# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def same_tree(t1, t2):
            if t1 is None or t2 is None:
                return t1 == t2
            if t1.val != t2.val:
                return False
            return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)

        return same_tree(root.left, root.right)
