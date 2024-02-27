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
        def traverse(node):
            if node is None:
                return ['#']

            ret = [str(node.val)]
            ret.extend(traverse(node.left))
            ret.extend(traverse(node.right))
            return ret

        return ','.join(traverse(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tokens = []
        for ch in data.split(','):
            if ch == '#':
                tokens.append(None)
            else:
                tokens.append(int(ch))

        def _deserialize(idx):
            if tokens[idx] is None:
                return None, idx+1

            node = TreeNode(tokens[idx])
            node.left, idx = _deserialize(idx+1)
            node.right, idx = _deserialize(idx)
            return node, idx

        return _deserialize(0)[0]


def same_tree(t1, t2):
    if t1 is None or t2 is None:
        return t1 is None and t2 is None
    if t1.val != t2.val:
        return False
    return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)

s = Codec()

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.right.left = TreeNode(4)
node.right.right = TreeNode(5)

data = [
    node,
    None,
]

for d in data:
    print(s.serialize(d))
    assert same_tree(s.deserialize(s.serialize(d)), d)
