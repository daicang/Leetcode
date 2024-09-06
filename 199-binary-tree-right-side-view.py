# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        vals = []

        def traverse(node, lv):
            if lv == len(vals):
                vals.append(node.val)
            if node.right:
                traverse(node.right, lv+1)
            if node.left:
                traverse(node.left, lv+1)

        traverse(root, 0)
        return vals
