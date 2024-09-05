class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxpath = 0

        def traverse(node):
            # return llen, rlen of zpath
            # llen = rpath of left child + 1
            # rlen = lpath of right child + 1
            # maxpath = max(maxpath, llen, rlen)
            if not node:
                return 0, 0

            llen, rlen = 0, 0
            if node.left:
                llen = traverse(node.left)[1] + 1
            if node.right:
                rlen = traverse(node.right)[0] + 1

            self.maxpath = max(self.maxpath, llen, rlen)
            return llen, rlen

        traverse(root)
        return self.maxpath