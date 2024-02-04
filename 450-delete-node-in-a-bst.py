# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        fake_root = TreeNode(0)
        fake_root.left = root

        parent = fake_root
        node = root
        go_left = True

        while True:
            if node is None:
                # Not found
                return root
            if key < node.val:
                parent = node
                node = node.left
                go_left = True
            elif key > node.val:
                parent = node
                node = node.right
                go_left = False
            else:
                break

        # Now node.val == key
        if node.left is None:
            if go_left:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None:
            if go_left:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            # node has both lchild and rchild
            # find minimal node in right child
            if not node.right.left:
                # The minimal node is the right child
                node.right.left = node.left
                if go_left:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else:
                # The minimal node is the leftmost node in right subtree
                rmin_parent = node.right
                rmin = rmin_parent.left
                while rmin.left:
                    rmin_parent = rmin
                    rmin = rmin.left

                rmin_parent.left = rmin.right
                rmin.right = node.right
                rmin.left = node.left
                if go_left:
                    parent.left = rmin
                else:
                    parent.right = rmin

        return fake_root.left
