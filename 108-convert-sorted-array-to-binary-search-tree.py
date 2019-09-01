# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """


        def helper(begin, end):
            if begin > end:
                return None

            middle = (begin+end) / 2

            node = TreeNode(nums[middle])
            node.left = helper(begin, middle-1)
            node.right = helper(middle+1, end)

            return node

        return helper(0, len(nums)-1)

