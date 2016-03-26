
# O(n * sizeof(n)) solution
class Solution(object):
    def countBits(self, num):
        ret = [0]*(num+1)
        for i in range(0, num+1):
            curr = i
            while (i != 0):
                ret[curr] += i & 1
                i >>= 1
        return ret


class Solution(object):
    def countBits(self, num):
        ret = [0]*(num+1)
        
