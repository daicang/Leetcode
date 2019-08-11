class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = []
        l1 = len(word1)
        l2 = len(word2)

        if l1 == 0:
            return l2
        if l2 == 0:
            return l1

        for _ in range(l1+1):
            dp.append([None] * (l2+1))

        def solve(i1, i2):
            if i1 < 0:
                return i2+1
            if i2 < 0:
                return i1+1
            if dp[i1][i2] is not None:
                return dp[i1][i2]

            if word1[i1] == word2[i2]:
                val = min(solve(i1-1, i2-1), 1+solve(i1, i2-1), 1+solve(i1-1, i2))
            else:
                val = min(1+solve(i1-1, i2-1), 1+solve(i1, i2-1), 1+solve(i1-1, i2))
            dp[i1][i2] = val
            return val

        return solve(l1-1, l2-1)

