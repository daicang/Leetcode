from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def rob_range(begin, end):
            rob_value = nums[begin]
            norob_value = 0
            for i in range(begin+1, end+1):
                new_rob_value = nums[i] + norob_value
                new_norob_value = max(rob_value, norob_value)

                rob_value = new_rob_value
                norob_value = new_norob_value

            return max(rob_value, norob_value)

        return max(rob_range(0, len(nums)-2), rob_range(1, len(nums)-1))


s = Solution()

inputs = [
    [2,1,1,2], #3
    [2,7,7,7,4], # 14
    [1,2,3,4,5,1,2,3,4,5], # 16
    [1,2,3,1], # 4
]

for i in inputs:
    print(s.rob(i))
