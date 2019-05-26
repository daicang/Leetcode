# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''

        # Non-recursive

        stack = [root]
        parts = []
        while stack:
            curr = stack.pop()
            if curr is None:
                parts.append('}')
            else:
                parts.append('%s{' % curr.val)
                stack.append(None)
                for child in curr.children[::-1]:
                    stack.append(child)
        return ''.join(parts)

        # recursive

        # parts = []
        # for child in root.children:
        #     parts.append(self.serialize(child))
        # return '%s{%s}' % (root.val, ''.join(parts))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == '':
            return None

        # Non-recursive

        num = ''
        stack = []
        for ch in data:
            if ch == '{':
                curr = Node(int(num), [])
                num = ''
                if not stack:
                    # first element
                    root = curr
                else:
                    stack[-1].children.append(curr)
                stack.append(curr)
            elif ch == '}':
                stack.pop()
            else:
                num += ch

        return root

        # recursive

        # ret = Node(0, [])

        # ret.val = int(data[:idx_left_bracket])
        # data = data[idx_left_bracket+1:]
        # counter = 0
        # start = 0
        # for idx, ch in enumerate(data):
        #     if ch == '{':
        #         counter += 1
        #     elif ch == '}':
        #         counter -= 1
        #         if counter == 0:
        #             # print 'append ', data[start:idx+1]
        #             ret.children.append(self.deserialize(data[start:idx+1]))
        #             start = idx + 1

        # return ret


s = Codec()
s.deserialize('1{3{5{}6{}}2{}4{}}')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))