from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        last_row = [None] * cols
        this_row = [None] * cols

        for row in range(rows)[::-1]:
            if row == rows-1:
                # The last row
                for col in range(cols)[::-1]:
                    curr = dungeon[row][col]
                    if col == cols-1:
                        this_row[col] = min(curr, 0)
                    else:
                        this_row[col] = min(this_row[col+1] + curr, 0)
            else:
                for col in range(cols)[::-1]:
                    curr = dungeon[row][col]
                    if col == cols-1:
                        this_row[col] = min(last_row[col] + curr, 0)
                    else:
                        this_row[col] = min(curr + max(last_row[col], this_row[col+1]), 0)

            last_row = this_row
            this_row = [None] * cols

        return -1 * last_row[0] + 1


s = Solution()

data = [
    [[-2,-3,3],[-5,-10,1],[10,30,-5]],  # 7
    [[100]],  # 1
    [[1,-3,3],[0,-2,0],[-3,-3,-3]]  # 3
]

for d in data:
    print(s.calculateMinimumHP(d))