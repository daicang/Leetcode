# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minimal = root.val
        ret = None
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left:
                if curr.left.val == minimal:
                    queue.append(curr.left)
                else:
                    if ret is None:
                        ret = curr.left.val
                    else:
                        ret = min(ret, curr.left.val)

                if curr.right.val == minimal:
                    queue.append(curr.right)
                else:
                    if ret is None:
                        ret = curr.right.val
                    else:
                        ret = min(ret, curr.right.val)
        return ret if ret is not None else -1
