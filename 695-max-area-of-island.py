
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = [(r, c)]
            area = 0
            while q:
                r, c = q.pop()
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                area += 1
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area