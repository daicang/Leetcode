
from typing import List

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[i] != root:
            parent = self.parent[i]
            self.parent[i] = root
            i = parent
        return root

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            self.parent[ri] = rj
            self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for p1, p2 in edges:
            uf.union(p1, p2)

        return uf.count


s = Solution()

inputs = [
    (5, [[0,1],[0,2],[2,3],[2,4]]),
]

for i in inputs:
    print(s.countComponents(*i))
