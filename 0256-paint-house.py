

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        last_cost = costs[0]

        for i, cost in enumerate(costs):
            if i > 0:
                c0 = cost[0] + min(last_cost[1], last_cost[2])
                c1 = cost[1] + min(last_cost[0], last_cost[2])
                c2 = cost[2] + min(last_cost[0], last_cost[1])
                last_cost = [c0, c1, c2]

        return min(last_cost)

s = Solution()

inputs = [
    [[17,2,17],[16,16,5],[14,3,19]],
    [[7,6,2]],
]

for i in inputs:
    print(s.minCost(i))
