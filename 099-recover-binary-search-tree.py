# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        curr = root

        last = None
        n1 = n2 = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            # visit
            if n1 is None:
                if last is not None and curr.val < last.val:
                    n1 = last
                    n2 = curr

            else:
                if curr.val < n2.val:
                    n2 = curr

            last = curr
            curr = curr.right

        n1.val, n2.val = n2.val, n1.val
