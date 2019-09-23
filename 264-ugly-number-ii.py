class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from heapq import heappop, heappush
        h = []
        heappush(h, 1)

        val = None
        for _ in range(n):
            val = heappop(h)
            for factor in (2, 3, 5):
                new = val * factor
                if new not in h:
                    heappush(h, new)

        return val


s = Solution()

for i in range(1, 11):
    print i, s.nthUglyNumber(i)
