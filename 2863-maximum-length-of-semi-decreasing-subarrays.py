
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 0
        stack = []

        for i in range(n-1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        left_max = None
        for i in range(n):
            if not stack:
                break
            if left_max is not None and nums[i] <= left_max:
                continue
            left_max = nums[i]

            while stack and nums[i] > nums[stack[-1]]:
                maxlen = max(maxlen, stack.pop()-i+1)

        return maxlen

s = Solution()

data = [
    [57,55,50,60,61,58,63,59,64,60,63], # 6
]

for d in data:
    print(s.maxSubarrayLength(d))
