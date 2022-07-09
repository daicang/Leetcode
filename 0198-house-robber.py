from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            c1 = c2 = 0
            if i >= 2:
                c1 = dp[i-2]
            if i >= 3:
                c2 = dp[i-3]

            dp[i] = num + max(c1, c2)

        return max(dp)

s = Solution()

inputs = [
    [1,2,3,1],
    [2,7,9,3,1],
]

for i in inputs:
    print(s.rob(i))
