class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        import sys
        sell1 = sell2 = 0
        buy1 = buy2 = -sys.maxint

        for p in prices:
            sell2 = max(sell2, p+buy2)
            buy2 = max(buy2, sell1-p)
            sell1 = max(sell1, p+buy1)
            buy1 = max(buy1, -p)

        return sell2


s = Solution()

inputs = [
    [3,3,5,0,0,3,1,4],
    [1,2,3,4,5]
]

for i in inputs:
    print s.maxProfit(i)
