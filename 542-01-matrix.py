

from typing import List
from collections import deque

class Solution:
    def updateMatrix_bfs(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        ret = []
        for _ in range(rows):
            ret.append([None] * cols)

        for x in range(rows):
            for y in range(cols):
                if mat[x][y] == 0:
                    q.append((x, y, 0))

        while q:
            x, y, moves = q.popleft()
            if ret[x][y] != None:
                continue
            ret[x][y] = moves
            moves += 1
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < rows and 0 <= ny < cols and ret[nx][ny] is None:
                    q.append((nx, ny, moves))

        return ret


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        ret = []
        for _ in range(rows):
            ret.append([float('inf')] * cols)

        for x in range(rows):
            for y in range(cols):
                if mat[x][y] == 0:
                    ret[x][y] = 0

        for x in range(rows):
            for y in range(cols):
                if ret[x][y] == 0:
                    continue
                if x-1 >= 0:
                    ret[x][y] = min(ret[x][y], ret[x-1][y]+1)
                if y-1 >= 0:
                    ret[x][y] = min(ret[x][y], ret[x][y-1]+1)

        for x in range(rows-1, -1, -1):
            for y in range(cols-1, -1, -1):
                if ret[x][y] == 0:
                    continue
                if x+1 < rows:
                    ret[x][y] = min(ret[x][y], ret[x+1][y]+1)
                if y+1 < cols:
                    ret[x][y] = min(ret[x][y], ret[x][y+1]+1)

        return ret


data = [
    [[0,0,0],[0,1,0],[1,1,1]],
    [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]],
]

s = Solution()

for d in data:
    print(s.updateMatrix(d))
