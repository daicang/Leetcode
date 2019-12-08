class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(d) for d in str(n)]
        product = 1
        s = 0
        for d in digits:
            product *= d
            s += d

        return product - s