
from typing import List
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        @cache
        def solve(row, col):
            val = grid[row][col]
            if row == 0 and col == 0:
                return val
            if row == 0:
                return val + solve(row, col-1)
            if col == 0:
                return val + solve(row-1, col)

            return val + min(solve(row-1, col), solve(row, col-1))

        rows = len(grid)
        cols = len(grid[0])

        return solve(rows-1, cols-1)
