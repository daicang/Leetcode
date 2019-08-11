class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [None] * (n+2)
        dp[0] = dp[1] = 1
        dp[2] = 2

        def solve(x):
            if dp[x] is not None:
                return dp[x]
            dp[x] = solve(x-1) + solve(x-2)
            return dp[x]

        return solve(n)

