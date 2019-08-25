class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        cache = [None] * (n+1)
        cache[0] = 1
        cache[1] = 1
        cache[2] = 2

        def solve(i):
            if cache[i] is not None:
                return cache[i]

            val = 0
            for lcount in range(i):
                val += solve(lcount) * solve(i-lcount-1)
            cache[i] = val
            return val

        return solve(n)