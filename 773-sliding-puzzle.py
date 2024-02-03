
from typing import List

from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = set()
        q = deque()

        l = board[0] + board[1]
        q.append((l, 0))

        def switch(l, x, y):
            nl = l[:]
            nl[x], nl[y] = nl[y], nl[x]
            return nl

        while q:
            l, step = q.popleft()
            if tuple(l) in visited:
                continue
            if l == [1,2,3,4,5,0]:
                return step
            visited.add(tuple(l))
            step += 1
            if l[0] == 0:
                q.append((switch(l, 0, 1), step))
                q.append((switch(l, 0, 3), step))
            elif l[1] == 0:
                q.append((switch(l, 0, 1), step))
                q.append((switch(l, 1, 2), step))
                q.append((switch(l, 1, 4), step))
            elif l[2] == 0:
                q.append((switch(l, 1, 2), step))
                q.append((switch(l, 2, 5), step))
            elif l[3] == 0:
                q.append((switch(l, 3, 0), step))
                q.append((switch(l, 3, 4), step))
            elif l[4] == 0:
                q.append((switch(l, 4, 3), step))
                q.append((switch(l, 4, 5), step))
                q.append((switch(l, 4, 1), step))
            else:
                q.append((switch(l, 4, 5), step))
                q.append((switch(l, 5, 2), step))

        return -1
