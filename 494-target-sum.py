class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if target > s:
            return 0
        dp = [0] * (2*s+1)  # shift by s
        dp[2*s] = 1

        for n in nums:
            for i in range(2*s-2*n+1):
                dp[i] += dp[i+2*n]

        return dp[target+s]
