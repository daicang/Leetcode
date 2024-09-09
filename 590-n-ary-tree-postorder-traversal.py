class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def traverse(node, l):
            if not node:
                return
            for ch in node.children:
                traverse(ch, l)
            l.append(node.val)
            return

        l = []
        traverse(root, l)
        return l
