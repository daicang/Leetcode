class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = []
        for _ in range(rows):
            dp.append([0] * cols)

        dpmax = -float('inf')
        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    cost = dp[r-1][c] + grid[r][c] - grid[r-1][c]
                    dp[r][c] = max(dp[r][c], cost)
                    dpmax = max(dpmax, cost)
                if c > 0:
                    cost = dp[r][c-1] + grid[r][c] - grid[r][c-1]
                    dp[r][c] = max(dp[r][c], cost)
                    dpmax = max(dpmax, cost)

        return dpmax