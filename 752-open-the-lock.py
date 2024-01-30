
import copy

from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def to_tuple(s):
            return tuple([int(i) for i in s])

        visited = set()
        for d in deadends:
            visited.add(to_tuple(d))

        q = deque()
        q.append((to_tuple('0000'), 0))
        target = to_tuple(target)

        while q:
            l, move = q.popleft()
            if l in visited:
                continue
            visited.add(l)
            if l == target:
                return move
            move += 1
            for i in range(4):
                l1 = list(l)
                l2 = list(l)
                l1[i] = (l1[i]+1)%10
                l2[i] = (l2[i]-1)%10
                for lnew in (l1, l2):
                    lnew = tuple(lnew)
                    q.append((lnew, move))

        return -1

data = [
    [["0201","0101","0102","1212","2002"], "0202"],
]

s = Solution()

for d in data:
    print(s.openLock(*d))