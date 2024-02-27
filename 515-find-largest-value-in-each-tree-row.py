

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        q = [root]

        while q:
            nq = []
            largest = None
            for node in q:
                if largest is None or node.val > largest:
                    largest = node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            ret.append(largest)
            q = nq

        return ret