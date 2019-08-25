# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def gen_tree(begin, end):
            if begin > end:
                return [None]

            result = []
            for i in range(begin, end+1):
                left_trees = gen_tree(begin, i-1)
                right_trees = gen_tree(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            return result

        return gen_tree(1, n)

