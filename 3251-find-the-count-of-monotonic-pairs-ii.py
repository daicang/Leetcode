class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        m = max(nums) + 1
        dp1 = [1] * m
        dp2 = [0] * m
        for i in range(1, n):
            d = max(0, nums[i] - nums[i-1])
            for j in range(d, nums[i]+1):
                dp2[j] = (dp2[j-1] + dp1[j-d]) % mod
            dp1, dp2 = dp2, [0] * m

        return sum(dp1) % mod