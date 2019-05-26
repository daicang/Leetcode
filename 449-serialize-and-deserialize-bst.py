# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        stack = [root]
        parts = []
        while stack:
            curr = stack.pop()
            if curr is None:
                parts.append(')')
            else:
                parts.append('%s(' % curr.val)
                stack.append(None)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return ''.join(parts)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        num = ''
        stack = []
        for char in data:
            if char == '(':
                curr = TreeNode(int(num))
                num = ''
                if stack:
                    parent = stack[-1]
                    if curr.val < parent.val:
                        parent.left = curr
                    else:
                        parent.right = curr
                else:
                    root = curr

                stack.append(curr)
            elif char == ')':
                stack.pop()
            else:
                num += char
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))