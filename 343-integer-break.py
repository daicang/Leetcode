# 343-integer-break.py

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0] * (n+1)
        l[1] = 1

        for i in xrange(2, n+1):
            maxP = i-1
            for j in xrange(1, i): maxP = max(maxP, j*max(i-j,l[i-j]))
            l[i] = maxP
        return l[n]

s = Solution()
print(s.integerBreak(10))
