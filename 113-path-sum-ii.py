# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        paths = []

        def backtrack(node, remains, path):
            if node is None:
                return
            remains -= node.val

            if node.left is None and node.right is None:
                if remains == 0:
                    paths.append(path+[node.val])
                return

            if node.left:
                path.append(node.val)
                backtrack(node.left, remains, path)
                path.pop()

            if node.right:
                path.append(node.val)
                backtrack(node.right, remains, path)
                path.pop()

        backtrack(root, sum, [])

        return paths

