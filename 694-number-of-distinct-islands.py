
from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = set()

        def bfs(r, c):
            signature = []
            q = [(r, c)]
            ir, ic = r, c
            while q:
                r, c = q.pop()
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                signature.append((r-ir, c-ic))
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))

            islands.add(tuple(signature))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)

        return len(islands)
