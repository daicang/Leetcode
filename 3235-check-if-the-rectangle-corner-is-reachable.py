
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[i] != root:
            j = self.parent[i]
            self.parent[i] = root
            i = j
        return root

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        self.parent[ri] = rj

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        n = len(circles)
        uf = UnionFind(n+2)  # n for bottom/right, n+1 for top/left

        for i in range(n):
            x, y, r = circles[i]
            # check if outside rect
            if x-r >= xCorner or x+r <= 0 or y-r >= yCorner or y+r <= 0:
                continue

            if x+r >= xCorner or y-r <= 0:
                # bottom/right border
                uf.union(i, n)

            if y+r >= yCorner or x-r <= 0:
                # top/left border
                uf.union(i, n+1)

            for j in range(i):
                x2, y2, r2 = circles[j]
                if (x-x2) ** 2 + (y-y2) ** 2 <= (r+r2) ** 2:
                    uf.union(i, j)

        if uf.find(n) == uf.find(n+1):
            return False
        return True
