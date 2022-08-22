
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def count(node):
            if node.left and node.right:
                l_uni, l_count = count(node.left)
                r_uni, r_count = count(node.right)
                if l_uni and r_uni:
                    if node.val == node.left.val and node.val == node.right.val:
                        return True, l_count + r_count + 1
                return False, l_count + r_count

            elif node.left:
                l_uni, l_count = count(node.left)
                if l_uni and node.val == node.left.val:
                    return True, l_count + 1
                return False, l_count

            elif node.right:
                r_uni, r_count = count(node.right)
                if r_uni and node.val == node.right.val:
                    return True, r_count + 1
                return False, r_count

            else:
                return True, 1

        return count(root)[1]
