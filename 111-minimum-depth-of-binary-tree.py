
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 1))

        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))



    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        c1 = [root]
        h = 0

        while c1:
            h += 1
            c2 = []
            for node in c1:
                if (not node.left) and (not node.right):
                    return h

                if node.left:
                    c2.append(node.left)
                if node.right:
                    c2.append(node.right)

            c1 = c2
