class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # Time: O(n*50*50)
        # Space: O(1)
        modval = 10**9 + 7
        n = len(nums)
        l = max(nums) + 1
        # dp[i][k] denotes to count of pairs when arr1[i] = k

        # iteration formula:
        # dp[i][k]
        # for k in range(51):
        #   if dp[i][k] == 0: break
        #
        #   k1 = nums[i] - k
        #   for val in range(k, nums[i+1]+1):
        #     # check for arr2, val must be <= k1
        #     val2 = nums[i+1] - val
        #     if val2 > k1: break
        #     dp[i+1][val] += dp[i][k]
        #
        # initial values: dp[0][0..nums[0]] = 1
        # final value: sum(dp[-1])

        dp1 = [0] * l
        dp2 = [0] * l
        for i in range(nums[0]+1):
            dp1[i] = 1

        for i in range(1, n):
            for l1 in range(l):
                if dp1[l1] == 0:
                    continue
                l2 = nums[i-1] - l1

                for v1 in range(nums[i], l1-1, -1):
                    v2 = nums[i] - v1  # increasing
                    if v2 > l2:
                        break
                    dp2[v1] += dp1[l1]
                dp1[l1] = 0

            dp1, dp2 = dp2, dp1

        return sum(dp1) % modval
