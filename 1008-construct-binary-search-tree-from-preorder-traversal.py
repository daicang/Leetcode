# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            curr = TreeNode(val)
            parent = stack[-1]

            if val < parent.val:
                print 'set %s.left to %s' % (parent.val, val)
                parent.left = curr
            else:
                for idx, node in enumerate(stack):
                    if node.val < val:
                        stack = stack[:idx]
                        print 'set %s.right to %s' % (node.val, val)
                        node.right = curr
                        break

            stack.append(curr)

        return root

s = Solution()
s.bstFromPreorder([8,5,1,7,10,12])
