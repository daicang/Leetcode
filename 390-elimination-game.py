class Solution(object):
    def lastRemaining_mle(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [i for i in xrange(1, n+1)]

        def lr(l):
            return l[1::2]

        def rl(l):
            if len(l) % 2 == 0:
                return l[0::2]
            return l[1::2]

        while len(l) > 1:
            l = lr(l)
            if len(l) < 2:
                break
            l = rl(l)

        return l[0]

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        round = 1
        while n > 1:
            if round % 2 == 1 or n % 2 == 1:
                first += 2 ** (round - 1)
            n /= 2
            round += 1
        return first

s = Solution()
print s.lastRemaining(9)
