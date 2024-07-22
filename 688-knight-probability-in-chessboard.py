class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = []
        for _ in range(n):
            dp.append([0] * n)
        dp[row][column] = 1

        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for _ in range(k):
            dp_new = []
            for _ in range(n):
                dp_new.append([0] * n)

            for r in range(n):
                for c in range(n):
                    if dp[r][c]:
                        for dr, dc in directions:
                            if 0 <= r+dr < n and 0 <= c+dc < n:
                                dp_new[r+dr][c+dc] += dp[r][c]/8

            dp = dp_new

        p = 0
        for r in range(n):
            for c in range(n):
                p += dp[r][c]

        return p
