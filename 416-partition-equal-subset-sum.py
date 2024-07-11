class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time: O(len(nums)*sum(nums))
        # space: O(s)
        s = sum(nums)
        if s % 2 != 0:
            return False

        dp = [False] * (s+1)
        dp[0] = True

        for n in nums:
            for i in range(s, n-1, -1):
                if dp[i-n] is True:
                    dp[i] = True

        return dp[s//2] is True
