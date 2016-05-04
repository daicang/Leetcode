# 342-power-of-four.py

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num&(num-1) != 0: return False
        k = 0
        while num != 1:
            k += 1
            num >>= 1
        return k%2 == 0
