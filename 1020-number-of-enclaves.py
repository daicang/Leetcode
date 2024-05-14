
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        if rows <= 2 or cols <= 2:
            return 0

        # marker holds those points can be visited from border
        marker = []
        for _ in range(rows):
            marker.append([0] * cols)

        q = []
        # enqueue border nodes
        for r in (0, rows-1):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))

        for c in (0, cols-1):
            for r in range(1, rows-1):
                if grid[r][c] == 1:
                    q.append((r, c))

        # bfs
        while q:
            r, c = q.pop()
            marker[r][c] = 1
            for new_r, new_c in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 < new_r < rows and 0 < new_c < cols:
                    if grid[new_r][new_c] == 1 and marker[new_r][new_c] == 0:
                        q.append((new_r, new_c))

        count = 0
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if grid[r][c] == 1:
                    if marker[r][c] == 0:  # unreachable
                        count += 1

        return count
