class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        self.count = 0

        def traverse(node, sums):
            if not node:
                return

            sums.append(0)
            for i, s in enumerate(sums):
                sums[i] = s + node.val
                if sums[i] == target:
                    self.count += 1

            traverse(node.left, sums)
            traverse(node.right, sums)

            # donot use sums = [i-node.val for i in sums] since it would create a new list
            for i, s in enumerate(sums):
                sums[i] -= node.val
            sums.pop()

        traverse(root, [])
        return self.count