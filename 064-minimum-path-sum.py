class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

        dp = []
        for _ in range(m):
            dp.append([None] * (n))

        dp[m-1][n-1] = grid[m-1][n-1]

        def solve(row, col):
            if dp[row][col] is not None:
                return dp[row][col]
            if row == m-1:
                cost = grid[row][col] + solve(row, col+1)
            elif col == n-1:
                cost = grid[row][col] + solve(row+1, col)
            else:
                cost = grid[row][col] + min(solve(row, col+1), solve(row+1, col))
            dp[row][col] = cost
            # print 'dp(%s,%s) is %s' % (row, col, ans)
            return cost

        return solve(0, 0)