
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST_iter(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        froot = TreeNode(val+1)
        froot.left = root

        parent = froot
        node = root
        while node:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        new_node = TreeNode(val)
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        return froot.left
