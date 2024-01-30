from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()

inputs = [
    [3,2,1,3],  # 9
    [1,1],  # 1
    [1,2,4,3],  # 4
    [5,2,12,1,5,3,4,11,9,4],  # 55
]

for i in inputs:
    print(s.maxArea(i))
