class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = []
        for _ in range(m+1):
            dp.append([None] * (n+1))
        for row in range(1, m+1):
            dp[row][1] = 1
        for col in range(1, n+1):
            dp[1][col] = 1


        def solve(row, col):
            if dp[row][col] is not None:
                return dp[row][col]
            ans = solve(row-1, col) + solve(row, col-1)
            dp[row][col] = ans
            return ans

        return solve(m, n)


s = Solution()

inputs = [
    [23, 12],
]

for input in inputs:
    print(s.uniquePaths(*input))
