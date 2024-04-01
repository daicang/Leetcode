

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        prev = prices[0]
        profit = 0
        for p in prices:
            if p > prev:
                profit += p-prev
            prev = p
        return profit