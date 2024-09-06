class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c0, c1 = 0, 0

        i = 2
        while i <= len(cost):
            c0, c1 = c1, min(c0+cost[i-2], c1+cost[i-1])
            i += 1

        return c1