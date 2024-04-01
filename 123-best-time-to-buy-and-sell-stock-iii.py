
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = -100000
        sell1 = sell2 = 0

        for p in prices:
            sell2 = max(sell2, p+buy2)
            buy2 = max(buy2, sell1-p)
            sell1 = max(sell1, p+buy1)
            buy1 = max(buy1, -p)

        return sell2


s = Solution()

inputs = [
    [1,2,3,4,5],
    [3,3,5,0,0,3,1,4],
    [1,2,3,4,5]
]

for i in inputs:
    print(s.maxProfit(i))
