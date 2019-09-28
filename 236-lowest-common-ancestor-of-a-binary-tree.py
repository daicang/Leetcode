# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def search(node):
            if not node:
                return None

            l = search(node.left)
            if isinstance(l, TreeNode):
                return l

            r = search(node.right)
            if isinstance(r, TreeNode):
                return r

            if (l, r) in ((1, 2), (2, 1)):
                return node

            if (node == p) and (2 in (l, r)):
                return node

            if (node == q) and (1 in (l, r)):
                return node

            if node == p:
                return 1

            if node == q:
                return 2

            return l or r

        return search(root)

