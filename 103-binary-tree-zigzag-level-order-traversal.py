

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        level = [root]
        reverse = False

        while level:
            next_level = []
            level_result = []

            for node in level:
                level_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if reverse:
                level_result.reverse()
            reverse = not reverse
            result.append(level_result)
            level = next_level

        return result
