# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        memo = {}
        ret = []

        def stringify(node):
            if not node:
                return ''
            s = '%s(%s,%s)' % (node.val, stringify(node.left), stringify(node.right))
            if s not in memo:
                memo[s] = 1
            else:
                memo[s] += 1
                if memo[s] == 2:
                    ret.append(node)
            return s

        stringify(root)
        return ret
