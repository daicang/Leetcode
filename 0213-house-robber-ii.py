from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def dp(take):
            dp = [0] * len(nums)
            for i, val in enumerate(nums):
                if i == take:
                    dp[i] = val
                elif abs(i-take) == 1:
                    dp[i] = 0
                elif take == 0 and i == len(nums)-1:
                    dp[i] = 0
                else:
                    c1 = c2 = 0
                    if i >= 2:
                        c1 = dp[i-2]
                    if i >= 3:
                        c2 = dp[i-3]
                    dp[i] = val + max(c1, c2)
            # print(dp)
            return max(dp)

        # Must take 1 in every 3 consecutive elements

        return max(dp(0), dp(1), dp(2))


s = Solution()

inputs = [
    [2,1,1,2], #3
    [2,7,7,7,4], # 14
    [1,2,3,4,5,1,2,3,4,5], # 16
    [1,2,3,1], # 4
]

for i in inputs:
    print(s.rob(i))
