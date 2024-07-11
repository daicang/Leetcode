class Solution:
    def maxScore_dp(self, nums: List[int]) -> int:
        # time: O(n^2)
        # space: O(n)
        n = len(nums)
        dp = [0] * n
        for i, val in enumerate(nums):
            for j in range(i+1, n):
                dp[j] = max(dp[j], dp[i]+nums[j]*(j-i))
        return dp[-1]

    def maxScore(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        maxval = 0
        score = 0
        for i in range(len(nums)-1, 0, -1):
            maxval = max(maxval, nums[i])
            score += maxval
        return score
