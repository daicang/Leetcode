from collections import defaultdict


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _solve(start, end):
            if start >= end:
                return 0
            if end in cache[start]:
                return cache[start][end]
            prices = []
            for k in xrange(start, end+1):
                prices.append(k + max(_solve(start, k-1), _solve(k+1, end)))
            cache[start][end] = min(prices)
            return min(prices)

        cache = defaultdict(lambda: defaultdict(int))
        return _solve(1, n)

s = Solution()
print s.getMoneyAmount(3)
print s.getMoneyAmount(7)
