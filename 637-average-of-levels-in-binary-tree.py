# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        avgs = []
        lv = [root]
        while lv:
            s = 0
            next_lv = []
            for node in lv:
                s += node.val
                if node.left:
                    next_lv.append(node.left)
                if node.right:
                    next_lv.append(node.right)
            avgs.append(s/len(lv))
            lv = next_lv
        return avgs
