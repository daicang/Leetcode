class Solution:
    def numTilings(self, n: int) -> int:
        mval = 10**9 + 7

        @cache
        def p(k):
            if k == 2:
                return 1
            return solve(k-2) + p(k-1)

        @cache
        def solve(k):
            if k <= 0:
                return 0
            if k <= 2:
                return k
            return (solve(k-1) + solve(k-2) + 2*p(k-1)) % mval

        return solve(n)
