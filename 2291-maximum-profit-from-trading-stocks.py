class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # backpack
        # time: O(n*budget)
        # space: O(budget)
        n = len(present)
        dp = [0] * (budget+1)
        for i in range(n):
            value = future[i] - present[i]
            for spending in range(budget, present[i]-1, -1):
                dp[spending] = max(dp[spending], dp[spending-present[i]]+value)

        return dp[-1]
