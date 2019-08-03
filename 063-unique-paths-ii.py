class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = []
        for _ in range(m):
            dp.append([None] * (n))

        dp[m-1][n-1] = 1

        def solve(row, col):
            if row > m-1 or col > n-1:
                return 0
            if dp[row][col] is not None:
                return dp[row][col]
            if obstacleGrid[row][col] == 1:
                ans = 0
            else:
                ans = solve(row+1, col) + solve(row, col+1)
            dp[row][col] = ans
            # print 'dp(%s,%s) is %s' % (row, col, ans)
            return ans

        return solve(0, 0)


inputs = [
    [[1, 0]],
    [[0,0,0],[0,1,0],[0,0,0]],
]
s = Solution()

for input in inputs:
    print(s.uniquePathsWithObstacles(input))
