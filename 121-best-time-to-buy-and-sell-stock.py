
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # monotonic stack
        stack = []
        max_profit = 0

        for p in prices:
            while stack and stack[-1] >= p:
                stack.pop()
            stack.append(p)
            max_profit = max(max_profit, p-stack[0])

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        size = len(prices)
        min_before = [prices[0]] * size
        max_after = [prices[-1]] * size

        for idx, p in enumerate(prices):
            if idx > 0:
                min_before[idx] = min(min_before[idx-1], p)

        for idx in range(size-2, -1, -1):
            max_after[idx] = max(max_after[idx+1], prices[idx])

        maxp = 0
        for i in range(size):
            maxp = max(maxp, max_after[i]-min_before[i])

        return maxp


s = Solution()

data = [
    [7,1,5,3,6,4], # 5
    [7,6,4,3,1], # 0
]

for d in data:
    print(s.maxProfit(d))
