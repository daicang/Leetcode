class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def _expand(i):
            if i > n:
                return i
            ret.append(i)
            while i * 10 <= n:
                i *= 10
                ret.append(i)
            return i

        def _incr(i):
            while i % 10 != 9:
                if i + 1 > n:
                    break
                i += 1
                ret.append(i)
            return i

        def _reduce(i):
            while i / 10 != 0:
                i /= 10
                while i % 10 != 9:
                    i += 1
                    i = _expand(i)
                    i = _incr(i)

        ret = []
        i = _expand(1)
        i = _incr(i)
        i = _reduce(i)

        return ret

s = Solution()
print s.lexicalOrder(34)
print s.lexicalOrder(9)
print s.lexicalOrder(0)
