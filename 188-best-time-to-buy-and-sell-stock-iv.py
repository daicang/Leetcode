class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # TLE

        if len(prices) < 2 or k == 0:
            return 0

        def all_profit():
            last = None
            profit = 0
            for p in prices:
                if last is not None and p > last:
                    profit += p - last
                last = p
            return profit

        if p >= len(prices)-1:
            return all_profit()

        import sys
        buys = [-sys.maxint] * k
        sells = [0] * k

        for p in prices:
            for i in range(k-1, -1, -1):
                sells[i] = max(sells[i], buys[i]+p)
                if i == 0:
                    last_sell = 0
                else:
                    last_sell = sells[i-1]
                buys[i] = max(buys[i], last_sell-p)

        return sells[-1]

