# 338-counting-bits.py

class Solution(object):
    def countBits(self, num):
        ret = [0]*(num+1)
        for i in range(0, num+1):
            ret[i] = ret[i & (i-1)] + 1
        return ret
