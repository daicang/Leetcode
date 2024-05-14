
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            q = [(r, c)]
            while q:
                r, c = q.pop()
                if grid[r][c] == '0':
                    continue
                grid[r][c] = '0'
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)

        return count
