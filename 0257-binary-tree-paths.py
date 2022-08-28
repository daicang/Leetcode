
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        stack = [[root, [str(root.val)]]]

        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append([node.left, path+[str(node.left.val)]])
            if node.right:
                stack.append([node.right, path+[str(node.right.val)]])
            if node.left == None and node.right == None:
                paths.append('->'.join(path))

        return paths