# 326-power-of-three.py

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 0 and n % 3 == 0: n /= 3
        return n == 1

    def isPowerOfThree_noloop(self, n):
        maxPowerOfThree = 1162261467
        return n != 0 and maxPowerOfThree % x == 0
        # Or we can use log: log3(x) = lg(x) / lg(3), should be an integer
        # (x % 1 == 0)
