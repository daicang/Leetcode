class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math

        dp = [n] * (n+1)
        squares = []

        for i in range(1, n+1):
            root = int(math.sqrt(i))

            if root**2 == i:
                dp[i] = 1
                squares.append(i)

            else:
                for s in squares:
                    dp[i] = min(dp[i], dp[i-s]+1)

        return dp[n]


s = Solution()
inputs = (12, 13)
for input in inputs:
    print(s.numSquares(input))
