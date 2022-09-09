
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # from low to high
        predecessor = deque()
        # from low to high
        successor = deque()
        stack = []
        node = root

        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                # Pop stack and
                node = stack.pop()
                if node.val < target:
                    predecessor.append(node.val)
                    if len(predecessor) > k:
                        predecessor.popleft()
                else:
                    successor.append(node.val)
                    if len(successor) == k:
                        break
                node = node.right
            else:
                break

        # print(predecessor, successor)

        # def traverse(node):
        #     if node.left:
        #         traverse(node.left)

        #     if node.val < target:
        #         predecessor.append(node.val)
        #         if len(predecessor) > k:
        #             predecessor.popleft()
        #     else:
        #         successor.append(node.val)
        #         if len(successor) == k:
        #             return

        #     if node.right:
        #         traverse(node.right)

        # traverse(root)

        closest = []
        pi = len(predecessor)-1
        si = 0

        while len(closest) < k:
            if pi < 0:
                closest.append(successor[si])
                si += 1
            elif si >= len(successor):
                closest.append(predecessor[pi])
                pi -= 1
            elif target - predecessor[pi] < successor[si] - target:
                closest.append(predecessor[pi])
                pi -= 1
            else:
                closest.append(successor[si])
                si += 1

        return closest
