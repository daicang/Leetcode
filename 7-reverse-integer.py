# 7-reverse-integer.py

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        BOUND = 2147483647
        ret = 0
        flag = 0
        if x < 0:
            flag = 1
            x *= -1
        while x != 0:
            ret *= 10
            ret += x % 10
            x //= 10
        if flag == 1: ret *= -1
        return 0 if ret > BOUND or ret < -BOUND else ret
