# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.new_node = TreeNode(val)

        if val > root.val:
            self.new_node.left = root
            return self.new_node

        if root.right is None:
            root.right = self.new_node
            return root

        if val < root.right.val:
            self.insertIntoMaxTree(root=root.right, val=val)
            return root

        # val > root.right.val:
        self.new_node.left = root.right
        root.right = self.new_node
        return root
