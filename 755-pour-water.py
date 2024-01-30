
from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            pos = k
            level = heights[pos]
            for i in range(pos-1, -1, -1):
                if heights[i] > level:
                    break
                if heights[i] < level:
                    level = heights[i]
                    pos = i
            if pos == k:
                for i in range(pos+1, len(heights)):
                    if heights[i] > level:
                        break
                    if heights[i] < level:
                        level = heights[i]
                        pos = i
            heights[pos] += 1

        return heights


data = [
    (([1,2,3,4,3,2,1,2,3,4,3,2,1], 5, 5), [1,2,3,4,3,4,3,3,3,4,3,2,1]),
]

s = Solution()

for d in data:
    args, result = d
    ans = s.pourWater(*args)
    assert ans == result, (ans, result)
