
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):
            if left == right:
                return TreeNode(nums[left])
            if left > right:
                return None

            max_idx = left
            for i in range(left, right+1):
                if nums[i] > nums[max_idx]:
                    max_idx = i

            node = TreeNode(nums[max_idx])
            node.left = build(left, max_idx-1)
            node.right = build(max_idx+1, right)
            return node

        return build(0, len(nums)-1)
