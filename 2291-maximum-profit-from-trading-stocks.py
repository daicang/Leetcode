class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # backpack
        # time: O(n*budget)
        # space: O(budget)
        profits = [0] * (budget+1)
        for cost, price in zip(present, future):
            profit = price - cost
            for p in range(budget, cost-1, -1):
                profits[p] = max(profits[p], profits[p-cost]+profit)
        return profits[-1]
