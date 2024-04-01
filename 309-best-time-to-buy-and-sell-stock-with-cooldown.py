

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sells = [0] * len(prices)
        buys = -50000

        for i, p in enumerate(prices):
            # sell, gain p
            if i > 0:
                sells[i] = max(sells[i-1], p+buys)

            # buy, pay p
            if i-2 <= 0:
                # no last selling point
                sell = 0
            else:
                sell = sells[i-2]
            buys = max(buys, -p+sell)

        return sells[-1]
