"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def check(row, col, n):
            v = grid[row][col]
            for r in range(row, row+n):
                for c in range(col, col+n):
                    if grid[r][c] != v:
                        return -1
            return v

        def cblock(row, col, n):
            val = check(row, col, n)
            if val != -1:
                return Node(val, True, None, None, None, None)
            half = n // 2
            return Node(1, False,
                cblock(row, col, half),
                cblock(row, col+half, half),
                cblock(row+half, col, half),
                cblock(row+half, col+half, half))

        return cblock(0, 0, len(grid))
