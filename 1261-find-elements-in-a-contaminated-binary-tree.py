# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

        def recorver(node, val):
            if not node:
                return
            node.val = val+1
            recorver(node.left, 2*val+1)
            recorver(node.right, 2*val+2)

        recorver(root, 0)


    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        # print '\nfinding %s' % target

        target += 1  # See https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/discuss/431229/Python-Special-Way-for-find()-without-HashSet-O(1)-Space-O(logn)-Time

        if target < 1:
            return False

        tmp = target
        total_bits = 0
        while tmp:
            total_bits += 1
            tmp >>= 1

        level = 1
        curr = self.root
        while curr:
            # print curr.val
            if curr.val == target:
                return True
            if curr.val > target:
                return False

            curr_shift = total_bits - 1 - level
            # print 'shift: %s' % curr_shift
            mask = 1 << curr_shift
            level += 1

            if (target & mask) == 0:
                # print 'left'
                curr = curr.left
            else:
                # print 'right'
                curr = curr.right

        return False

print 'case 1'

tree = TreeNode(-1)
tree.right = TreeNode(-1)

s = FindElements(tree)

for val in (1, 2):
    print s.find(val)

print '\ncase 2'

tree = TreeNode(-1)
tree.left = TreeNode(-1)
tree.right = TreeNode(-1)
tree.left.left = TreeNode(-1)
tree.left.right = TreeNode(-1)

s = FindElements(tree)

for val in (1, 3, 5):
    print s.find(val)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)