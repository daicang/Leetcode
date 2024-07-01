class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def traverse(node):
            if node is None:
                return 0

            ll = traverse(node.left)
            lr = traverse(node.right)

            val = 1
            ret = 1

            if node.left and node.right and \
                node.val == node.left.val and \
                node.val == node.right.val:
                val = ll + lr + 1  # the path ends in current node
                ret = max(ll, lr) + 1  # path can continue go up
            elif node.left and node.val == node.left.val:
                val = ll + 1
                ret = val
            elif node.right and node.val == node.right.val:
                val = lr + 1
                ret = val

            self.longest_path = max(self.longest_path, val)

            return ret

        traverse(root)
        if self.longest_path == 0:
            return 0
        return self.longest_path - 1