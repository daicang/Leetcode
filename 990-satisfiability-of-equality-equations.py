
from typing import List


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while i != root:
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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        eqs = []
        ues = []

        for eq in equations:
            i = ord(eq[0]) - ord('a')
            j = ord(eq[3]) - ord('a')
            if eq[1] == '=':
                eqs.append((i, j))
            else:
                ues.append((i, j))

        for i, j in eqs:
            uf.union(i, j)
        for i, j in ues:
            if uf.find(i) == uf.find(j):
                return False
        return True