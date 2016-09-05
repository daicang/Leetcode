import Queue
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
        q = Queue.Queue()
        q.put(root)
        vals = []

        while not q.empty():
            curr = q.get()
            if curr:
                vals.append(str(curr.val))
                q.put(curr.left)
                q.put(curr.right)
            else:
                vals.append('None')

        return '.'.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split('.')
        if not vals:
            return None

        r = [TreeNode(None), 'l']
        q = Queue.Queue()
        q.put(r)

        for val in vals:
            curr = q.get()
            parent, lr = curr
            if val == 'None':
                if lr == 'l':
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = TreeNode(val)
                if lr == 'l':
                    parent.left = node
                else:
                    parent.right = node
                q.put([node, 'l'])
                q.put([node, 'r'])

        return r[0].left

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
