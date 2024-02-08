

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        ret = []
        for _ in range(rows):
            ret.append([False] * cols)

        visited = []
        for _ in range(rows):
            visited.append([False] * cols)

        def dp(x, y):
            if mat[x][y] == 0:
                return 0

            if ret[x][y] != False:
                return ret[x][y]

            min_dist = float('inf')
            visited[x][y] = True

            for nx, ny in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
                if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] == False:
                    ret[nx][ny] = dp(nx, ny)
                    min_dist = min(min_dist, ret[nx][ny]+1)

            visited[x][y] = False

            return min_dist

        for r in range(rows):
            for c in range(cols):
                ret[r][c] = dp(r, c)

        return ret


data = [
    [[0,0,0],[0,1,0],[1,1,1]],
    [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]],
]

s = Solution()

for d in data:
    print(s.updateMatrix(d))
