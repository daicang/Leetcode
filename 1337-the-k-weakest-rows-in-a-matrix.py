from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order = []
        rows = len(mat)
        cols = len(mat[0])
        s = set(range(rows))

        for col in range(cols):
            for row in range(rows):
                if row not in s:
                    continue
                if mat[row][col] == 0:
                    order.append(row)
                    if len(order) == k:
                        return order
                    s.remove(row)

        for row in range(rows):
            if row in s:
                order.append(row)
                if len(order) == k:
                    return order

        return order


s = Solution()

data = [
    [[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3],
    [[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2]
]

for d in data:
    print(s.kWeakestRows(*d))

