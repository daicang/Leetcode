class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cache = []
        for _ in range(len(s)):
            cache.append([None] * len(t))

        def match(si, ti):
            if ti == len(t):
                return 1

            if si == len(s):
                return 0

            if cache[si][ti] is not None:
                return cache[si][ti]

            count = 0
            if s[si] == t[ti]:
                count += match(si+1, ti+1)
            count += match(si+1, ti)
            cache[si][ti] = count
            return count

        return match(0, 0)

s = Solution()

inputs = [
    ['rabbbit', 'rabbit'],
    ["babgbag", "bag"]
]

for i in inputs:
    print(s.numDistinct(*i))


