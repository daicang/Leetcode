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
        while True:
            if node is None:
                # Not found
                return root

            if node.val == key:
                break
            if key < node.val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        def update_parent(parent, child, new_child):
            if parent.left == child:
                parent.left = new_child
            else:
                parent.right = new_child

        # Now node.val == key
        if node.left is None or node.right is None:
            update_parent(parent, node, node.left or node.right)

        else:
            # Replace node with minimal node in right child
            if not node.right.left:
                # The minimal node is the right child
                node.right.left = node.left
                update_parent(parent, node, node.right)
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
                update_parent(parent, node, rmin)

        return fake_root.left
