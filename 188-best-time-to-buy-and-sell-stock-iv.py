from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # profit by selling k times
        # suppose no earning by selling k times initially
        sells = [0] * (k+1)

        # profit by buying k times
        buys = [-1000] * (k+1)

        for p in prices:
            for i in range(k, 0, -1):
                # sell at this moment, gain p with buys[i]
                sells[i] = max(sells[i], buys[i]+p)

                # buy at this moment, lose p with sells[i-1]
                buys[i] = max(buys[i], sells[i-1]-p)

        return sells[-1]

data = [
    [2, [2,4,1]],  # 2
    [3, [3,2,6,5,0,3]],  # 7
    [1, [1,2,3,4,5]], # 4
]

s = Solution()

for d in data:
    print(s.maxProfit(*d))
