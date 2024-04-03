from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        # rob(k) = n+norob(k-1)
        # norob(k-1) = max(norob(k-1), rob(k-1))
        # rob(0) = nums[0]
        # norob(0) = 0

        norob_value = 0
        rob_value = nums[0]

        for i, n in enumerate(nums):
            if i > 0:
                new_rob_value = n + norob_value
                new_norob_value = max(norob_value, rob_value)

                rob_value = new_rob_value
                norob_value = new_norob_value

        return max(rob_value, norob_value)


s = Solution()

inputs = [
    [1,2,3,1],    # 4
    [2,7,9,3,1],  # 12
]

for i in inputs:
    print(s.rob(i))
