class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxlv = 0
        maxs = -inf

        lv = 0
        nodes = [root]
        while nodes:
            lv += 1
            nxnodes = []
            s = 0
            for node in nodes:
                s += node.val
                if node.left:
                    nxnodes.append(node.left)
                if node.right:
                    nxnodes.append(node.right)
            if s > maxs:
                maxs = s
                maxlv = lv
            nodes = nxnodes

        return maxlv
