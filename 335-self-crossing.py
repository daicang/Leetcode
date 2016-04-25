# 335-self-crossing.py

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        l = len(x)
        if (l < 4): return True
        
        flag = 0     # Is square decreasing
        hasBound = 0 # Has previous edge, cannot cross this bound
        prev3 = 0
        prev2 = x[0]
        prev1 = x[1]
        
        for i in xrange(2, l):
            curr = x[i]
            if flag == 0:
                if curr <= prev2:
                    flag = 1
                    prev2 = prev1 - prev3
                    prev1 = curr
                else:
                    prev3 = prev2
                    prev2 = prev1
                    prev1 = curr
            else:
                if curr >= prev2: return True
                prev2 = prev1
                prev1 = curr

        return False
