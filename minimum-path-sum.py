from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sums = []
        for _ in range(rows):
            sums.append([None] * cols)

        for row in range(rows):
            for col in range(cols):
                if row == 0:
                    if col == 0:
                        sums[0][0] = grid[0][0]
                    else:
                        sums[0][col] = sums[0][col-1] + grid[0][col]
                else:
                    if col == 0:
                        sums[row][0] = sums[row-1][0] + grid[row][0]
                    else:
                        sums[row][col] = min(sums[row][col-1], sums[row-1][col]) + grid[row][col]

        return sums[-1][-1]


