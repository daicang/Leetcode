# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        head = TreeNode(0)
        head.left = root
        remove_mark = -1

        def traverse(node) -> int:
            if node is None:
                return remove_mark
            if traverse(node.left) == traverse(node.right) == remove_mark:
                if node.val == target:
                    node.val = remove_mark
            return node.val

        traverse(head.left)

        def remove(node):
            if node.left:
                if node.left.val == remove_mark:
                    node.left = None
                else:
                    remove(node.left)
            if node.right:
                if node.right.val == remove_mark:
                    node.right = None
                else:
                    remove(node.right)

        remove(head.left)

        return head.left

