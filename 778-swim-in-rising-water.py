
import heapq

from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        t = 0

        heapq.heappush(heap, (grid[0][0], 0, 0))
        grid[0][0] = -1  # visited

        while heap:
            h, i, j = heapq.heappop(heap)
            t = max(t, h)
            if i == n-1 and j == n-1:
                return t
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] != -1:
                    heapq.heappush(heap, (grid[x][y], x, y))
                    grid[x][y] = -1

        return -1
