class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = []
        for s in strs:
            count = Counter(s)
            c0, c1 = count.get('0', 0), count.get('1', 0)
            if c0 > m or c1 > n:
                continue
            arr.append((c0, c1))

        maxcount = 0
        dp = []
        for _ in range(m+1):
            dp.append([0] * (n+1))

        for c0, c1 in arr:
            # remember to iterate from high to low to avoid duplicated calculation
            for i0 in range(m, c0-1, -1):
                for i1 in range(n, c1-1, -1):
                    dp[i0][i1] = max(dp[i0][i1], dp[i0-c0][i1-c1]+1)

        return dp[m][n]
