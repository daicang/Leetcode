# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder:
            return None

        val = postorder[-1]
        node = TreeNode(val)

        i = 0
        for i, v in enumerate(inorder):
            if v == val:
                break

        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return node
