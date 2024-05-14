
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        count = 0

        def bfs(r, c):
            q = [(r, c)]
            is_sub = 1
            while q:
                r, c = q.pop()
                if grid2[r][c] == 0:
                    continue
                grid2[r][c] = 0
                if grid1[r][c] == 0:
                    is_sub = 0
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1:
                        q.append((nr, nc))

            return is_sub

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    count += bfs(r, c)

        return count
