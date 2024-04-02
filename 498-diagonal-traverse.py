
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        prints = []
        row_order = 1 # 0 for low->high, 1 for high->low

        for s in range(rows+cols-1):
            if row_order == 0:
                for row in range(rows):
                    col = s - row
                    if col < 0:
                        break
                    if col < cols:
                        prints.append(mat[row][col])
            else:
                for row in range(rows-1, -1, -1):
                    col = s - row
                    if col == cols:
                        break
                    if 0 <= col:
                        prints.append(mat[row][col])

            row_order ^= 1

        return prints
