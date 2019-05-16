class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # DP, TLE
        #
        # length = len(A)
        # dp = []
        # for _ in range(K+1):
        #     dp.append([0]*length)

        # for step in range(K+1):
        #     for last in range(length):
        #         if last == 0:
        #             if step == 0:
        #                 dp[0][0] = A[0]
        #             else:
        #                 dp[step][0] = 1

        #         elif step == 0:
        #             if A[last] == 1:
        #                 dp[0][last] = dp[0][last-1]+1
        #             else:
        #                 dp[0][last] = 0

        #         elif step > last+1:
        #             dp[step][last] = dp[last+1][last]

        #         else:
        #             if A[last] == 1:
        #                 dp[step][last] = dp[step][last-1] + 1
        #             else:
        #                 dp[step][last] = dp[step-1][last-1]+1

        # print(dp)
        # return max(dp[K])

        # Sliding window
        lidx = 0
        maxl = 0
        k_left = K
        length = 0

        for ridx, rval in enumerate(A):
            if rval == 1:
                length += 1
                maxl = max(maxl, length)
                continue

            # rval == 0
            if k_left > 0:
                k_left -= 1
                length += 1
                maxl = max(maxl, length)

            else:
                if rval == 1:
                    length += 1
                    maxl = max(maxl, length)
                else:
                    while A[lidx] == 1:
                        lidx += 1
                    assert A[lidx] == 0
                    lidx += 1
                    length = ridx - lidx+1
                    maxl = max(maxl, length)

        return maxl


s = Solution()
print(s.longestOnes([0,0,0,1], 4))
