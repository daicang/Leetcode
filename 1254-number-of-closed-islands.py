
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = [(r, c)]
            closed = 1
            while q:
                r, c = q.pop()
                if grid[r][c] == 1:
                    continue
                grid[r][c] = 1  # floodfill
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    closed = 0
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        q.append((nr, nc))

            return closed


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += bfs(r, c)

        return count


data= [
   [[0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0],
    [0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0],
    [0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1],
    [0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1],
    [0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1],
    [1,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1],
    [0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,1],
    [1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0],
    [1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1],
    [1,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1],
    [1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0]],
]

s = Solution()

for d in data:
    print(s.closedIsland(d))
