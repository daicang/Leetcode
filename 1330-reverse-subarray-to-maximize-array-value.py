from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        min_in_higher = None
        max_in_lower = None

        for i in range(len(nums)-1):
            higher = max(nums[i], nums[i+1])
            lower = min(nums[i], nums[i+1])
            if min_in_higher is None or higher < min_in_higher:
                min_in_higher = higher
            if max_in_lower is None or lower > max_in_lower:
                max_in_lower = lower

        change = max(0, 2 * (max_in_lower - min_in_higher))

        for i in range(len(nums)-1):
            gap = abs(nums[i+1] - nums[i])
            change = max(change, abs(nums[i+1]-nums[0])-gap)
            change = max(change, abs(nums[i]-nums[-1])-gap)

        val = change
        for i in range(len(nums)-1):
            val += abs(nums[i]-nums[i+1])

        return val



data = [
    [2,3,1,5,4],  # 10
    [2,5,1,3,4],  # 11
    [2,4,9,24,2,1,10],  # 68
    [5,-7,9,-6,8]  # 57
]

s = Solution()
for d in data:
    print(s.maxValueAfterReverse(d))
