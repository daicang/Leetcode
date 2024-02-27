

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        rootval = preorder[0]
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        i1 = i2 = 0

        for i in range(1, len(preorder)):
            j = i-1
            counter1[preorder[i]] += 1
            counter2[postorder[j]] += 1

            if counter1 == counter2:
                i1 = i
                i2 = j
                break

        left = self.constructFromPrePost(preorder[1:i1+1], postorder[:i2+1])
        right = self.constructFromPrePost(preorder[i1+1:], postorder[i2+1:-1])

        return TreeNode(rootval, left, right)
