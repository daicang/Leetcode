
from typing import List
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        last = costs[0]
        k = len(last)

        for i, current_cost in enumerate(costs):
            if i == 0: continue
            tmp = []
            for color in range(k):
                min_cost = None
                for last_color, last_cost in enumerate(last):
                    if last_color != color:
                        if min_cost is None:
                            min_cost = last_cost
                        else:
                            min_cost = min(min_cost, last_cost)
                tmp.append(min_cost + current_cost[color])
            last = tmp

        return min(last)

s = Solution()

inputs = [
    [[1,5,3],[2,9,4]],
    [[1,3],[2,4]],
]

for i in inputs:
    print(s.minCostII(i))
