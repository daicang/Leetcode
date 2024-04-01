
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sells = 0
        buys = -50000

        for i, p in enumerate(prices):
            if i > 0:
                # sell and gain p
                sells = max(sells, buys+p-fee)

            buys = max(buys, sells-p)

        return sells