# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        import sys
        maxsum = [-sys.maxint]

        def try_update_max(val):
            maxsum[0] = max(maxsum[0], val)

        def solve(node):
            if node.left == node.right == None:
                try_update_max(node.val)
                return node.val

            if not node.left:
                rval = solve(node.right)
                try_update_max(max(rval, rval+node.val, node.val))
                return max(rval+node.val, node.val)

            if not node.right:
                lval = solve(node.left)
                try_update_max(max(lval, lval+node.val, node.val))
                return max(lval+node.val, node.val)

            lval = solve(node.left)
            rval = solve(node.right)

            try_update_max(max(lval, rval, lval+node.val, rval+node.val, lval+rval+node.val, node.val))
            return max(lval, rval, 0) + node.val

        solve(root)
        return maxsum[0]

