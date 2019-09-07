# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        level = [root]

        while level:
            children = []
            for node in level:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            for idx, node in enumerate(children):
                if idx == 0:
                    continue
                children[idx-1].next = node

            level = children





