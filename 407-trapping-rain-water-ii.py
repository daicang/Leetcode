
import heapq

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0

        rows = len(heightMap)
        cols = len(heightMap[0])

        if rows < 3 or cols < 3:
            return 0

        heap = []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    # Mark as visited
                    heightMap[r][c] = -1

        level = 0
        water = 0

        while heap:
            height, r, c = heapq.heappop(heap)
            level = max(level, height)

            for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 < i < rows and 0 < j < cols:
                    h = heightMap[i][j]
                    if h != -1:
                        heapq.heappush(heap, (h, i, j))
                        if h < level:
                            water += level - h
                        heightMap[i][j] = -1

        return water