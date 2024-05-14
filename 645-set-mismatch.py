
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        missing = 0

        for n in nums:
            if n < 0:
                n = -n
            idx = n-1
            if nums[idx] < 0:
                duplicate = n
            else:
                nums[idx] *= -1

        for i, n in enumerate(nums):
            if n > 0:
                missing = i+1

        return [duplicate, missing]


data = [
    [2,2],
]

s = Solution()

for d in data:
    print(s.findErrorNums(d))
