class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        # print('stones=%s, K=%s' % (stones, K))

        if ((n - 1) % (K - 1)) != 0:
            return -1

        dp = []
        for _ in range(n):
            dp.append([0]*n)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + stones[i-1]

        for step in range(1, n+1):
            for start in range(n-step+1):
                # inclusive
                end = start + step - 1

                # print('start=%s, end=%s, step=%s' % (start, end, step))
                if step < K:
                    # no merge, cost 0
                    dp[start][end] = 0
                    continue

                # for split in range(start, end):
                    # print 'dp[%s][%s]=%s, dp[%s][%s]=%s' % (start, split, dp[start][split], split+1, end, dp[split+1][end])
                dp[start][end] = min(dp[start][split] + dp[split+1][end] for split in range(start, end, K-1))
                if (step-1) % (K-1) == 0:
                    # merge into 1, add cost
                    dp[start][end] += prefix[end+1] - prefix[start]
                    # print 'start %s end %s add %s' % (start, end, prefix[end+1]-prefix[start])

                # print('set dp[%s][%s]=%s' % (start, end, dp[start][end]))

        # for line in dp:
        #     print line

        return dp[0][n-1]


s = Solution()

# 25
# 17 + (5+1+2) = 25
print(s.mergeStones([3,5,1,2,6], 3))

# 20
# (3+2) + (4+1) + (5+5)
print(s.mergeStones([3,2,4,1], 2))


