class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
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
