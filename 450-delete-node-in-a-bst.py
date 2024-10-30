# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.left:
                # pick largest element in left branch
                node = root.left
                parent = None
                while node.right:
                    parent = node
                    node = node.right
                node.right = root.right
                if parent:
                    parent.right = node.left
                    node.left = root.left
                return node
            return root.right

        if root.val > key:
            # search left branch
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
