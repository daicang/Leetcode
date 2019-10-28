# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curr = root
        if root:
            self.has_next = True
        else:
            self.has_next = False

    def _morris_traversal_next(self):
        while self.curr.left:
            left = self.curr.left
            # Find rightmost node in left subtree
            while left.right:
                left = left.right
            # Set curr as its next node
            left.right = self.curr

            left = self.curr.left
            self.curr.left = None
            self.curr = left

        # Now curr.left is None
        next_node = self.curr
        self.curr = self.curr.right
        if self.curr is None:
            self.has_next = False
        return next_node

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self._morris_traversal_next()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.has_next



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()