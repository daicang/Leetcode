# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def iter(node):
            if node == None: return [0, 0]
            l = iter(node.left)
            r = iter(node.right)
            return [max(l[0], l[1]) + max(r[0], r[1]), # current node unavailable
                    node.val + l[0] + r[0]] # current node available
        r = iter(root)
        return max(r[0], r[1])

# My first version, TLE
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def iter(node, avai):
            if node == None: return 0
            if avai == 0: return iter(node.left, 1) + iter(node.right, 1)
            return max(iter(node.left, 1) + iter(node.right, 1),
                       node.val + iter(node.left, 0) + iter(node.right, 0))
        return iter(root, 1)
