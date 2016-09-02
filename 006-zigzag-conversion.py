# 6-zigzag-conversion.py

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = [""] * numRows
        if numRows == 1: return s # Devide zero
        f = 2 * (numRows - 1)
        for i in xrange(len(s)):
            r = i % f
            if r > f/2: r = f - r
            l[r] += s[i]
        return "".join(l)
