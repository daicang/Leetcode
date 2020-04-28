# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        n_origin = root
        n_copied = TreeNode(root.val)

        while n_origin.left:
            new_node = TreeNode(n_origin.left.val)
            new_node.left = n_origin.right
            new_node.right = n_copied
            n_copied = new_node
            n_origin = n_origin.left

        return n_copied

