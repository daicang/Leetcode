class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        cache = [None] * len(s)

        def solve(i):
            if i > len(s)-1:
                return 1

            if cache[i] is None:
                if int(s[i]) == 0:
                    cache[i] = 0
                else:
                    val = solve(i+1)
                    if i < len(s)-1 and int(s[i:i+2]) < 27:
                        val += solve(i+2)
                    cache[i] = val
            return cache[i]

        return solve(0)


s = Solution()

inputs = [
    '12',
    '0',
    '27'
]

for i in inputs:
    print s.numDecodings(i)
