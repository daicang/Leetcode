# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        curr = TreeNode(root.val)
        if not root.children:
            return curr

        last_encoded_child = self.encode(root.children[0])
        curr.left = last_encoded_child

        for child in root.children[1:]:
            this_encoded_child = self.encode(child)
            last_encoded_child.right = this_encoded_child
            last_encoded_child = this_encoded_child

        return curr

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None
        curr = Node(data.val, [])
        child = data.left

        while child:
            curr.children.append(self.decode(child))
            child = child.right
        return curr





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))