
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return

        rows = len(matrix)
        cols = len(matrix[0])
        ret = []

        upper = 0
        lower = rows-1
        left = 0
        right = cols-1

        while len(ret) < rows * cols:
            # 1. Must loop full of first line,
            # Otherwise cannot handle last line/column
            # 2. Must check and update boundry on each iteration
            if upper <= lower:
                for i in range(left, right+1):
                    ret.append(matrix[upper][i])
                upper = upper + 1

            if left <= right:
                for i in range(upper, lower+1):
                    ret.append(matrix[i][right])
                right = right - 1

            if upper <= lower:
                for i in range(right, left-1, -1):
                    ret.append(matrix[lower][i])
                lower = lower - 1

            if left <= right:
                for i in range(lower, upper-1, -1):
                    ret.append(matrix[i][left])
                left = left + 1

        return ret


s = Solution()

data = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
]

for d in data:
    print(s.spiralOrder(d))
