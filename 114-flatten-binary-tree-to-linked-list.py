class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return []

        def preorder(node, last):
            left = node.left
            right = node.right

            if last:
                last.left = None
                last.right = node

            last = node

            if left:
                last = preorder(left, last)

            if right:
                last = preorder(right, last)

            return last

        preorder(root, None)

