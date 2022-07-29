

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        count = 0

        node = root
        while node:
            count += 1 << level
            node = node.right
            level += 1

        # Now the last level is level, if complete it should have 2^level nodes
        # Binary search to detect the last node

        def left_subtree_full(root, level):
            assert level > 0
            node = root.left
            if not node:
                return False
            level -= 1

            while level > 0:
                if node.right is None:
                    return False
                node = node.right
                level -= 1
            return True

        node = root

        while level > 0:
            if left_subtree_full(node, level):
                node = node.right
                count += 1 << (level-1)
            else:
                node = node.left
            level -= 1

        return count
