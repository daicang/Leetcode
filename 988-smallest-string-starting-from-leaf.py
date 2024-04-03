
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        self.smallest_path = None

        def traverse(node, path):
            path.append(node.val)
            if not node.left and not node.right:
                spath = tuple(path[::-1])
                if self.smallest_path is None or spath < self.smallest_path:
                    self.smallest_path = spath

            if node.left:
                traverse(node.left, path)
            if node.right:
                traverse(node.right, path)

            path.pop()

        traverse(root, [])

        return ''.join([chr(ord('a')+i) for i in self.smallest_path])
