class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for i, val in enumerate(prices):
            if i == 0:
                last = val
                continue
            if val > last:
                profit += val-last
            last = val

        return profit
