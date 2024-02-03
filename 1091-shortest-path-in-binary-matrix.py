
import heapq
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix_bfs(self, grid: List[List[int]]) -> int:
        q = deque()
        q.append((0, 0, 1))

        if not grid or not grid[0]:
            return 0
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        while q:
            x, y, move = q.popleft()
            if x == rows-1 and y == cols-1:
                return move
            move += 1
            for nx, ny in [(x-1, y-1), (x-1, y), (x-1, y+1),
                            (x, y-1), (x, y+1),
                            (x+1, y-1), (x+1, y), (x+1, y+1)]:
                if 0 <= nx < rows and \
                    0 <= ny < cols and \
                    grid[nx][ny] == 0:
                    grid[nx][ny] = -1
                    q.append((nx, ny, move))

        return -1

    def shortestPathBinaryMatrix_astar(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        visited = set()

        def estimate(x, y):
            return max(rows-x, cols-y)

        q = []
        heapq.heappush(q, (estimate(0, 0)+1, 1, 0, 0))

        while q:
            est, moves, x, y = heapq.heappop(q)
            if (x, y) in visited:
                continue
            if (x, y) == (rows-1, cols-1):
                return moves
            visited.add((x, y))
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 0 and (nx, ny) not in visited:
                        est = moves + estimate(nx, ny) + 1
                        heapq.heappush(q, (est, moves+1, nx, ny))

        return -1