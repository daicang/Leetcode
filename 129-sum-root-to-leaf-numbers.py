# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        number_sum = [0]

        def traverse(node, path):
            if not node:
                return

            if not node.left and not node.right:
                num = 0
                for n in path:
                    num = 10*num + n
                num = 10*num + node.val
                number_sum[0] += num
                return

            path.append(node.val)
            traverse(node.left, path)
            path.pop()

            path.append(node.val)
            traverse(node.right, path)
            path.pop()

        traverse(root, [])

        return number_sum[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

s = Solution()

print s.sumNumbers(root)

