# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# In-order traversal by stack
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left

        while True:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            if curr.right:
                stack.append(curr.right)
                curr = curr.right
                while curr.left:
                    stack.append(curr.left)
                    curr = curr.left

