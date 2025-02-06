class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_dist = inf

        def traverse(node):
            lbound = rbound = node.val
            if node.left:
                lbound, r = traverse(node.left)
                self.min_dist = min(self.min_dist, node.val-r)
            if node.right:
                l, rbound = traverse(node.right)
                self.min_dist = min(self.min_dist, l-node.val)
            return lbound, rbound

        traverse(root)
        return self.min_dist
