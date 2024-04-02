
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        # level traverse

        if root.val in (x, y):
            return False

        level = [root.left, root.right]

        while level:
            next_level = []
            found_level = 0

            while level:
                right = level.pop()
                left = level.pop()
                found_pair = 0

                if left:
                    next_level.append(left.left)
                    next_level.append(left.right)
                    if left.val in (x, y):
                        found_level += 1
                        found_pair += 1

                if right:
                    next_level.append(right.left)
                    next_level.append(right.right)
                    if right.val in (x, y):
                        found_level += 1
                        found_pair += 1

                if found_pair == 2:
                    return False
                if found_level == 2:
                    return True

            level = next_level

        return False
