
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0 or n > len(nums):
                nums[i] = 0

        for i, val in enumerate(nums):
            next_idx = val-1
            while next_idx >= 0:
                # save value on nums[next_idx]
                tmp = nums[next_idx]-1
                # mark next index
                nums[next_idx] = -1
                next_idx = tmp

        for i, n in enumerate(nums):
            if n != -1:
                return i+1

        return len(nums)+1

s = Solution()

data = [
    [1],
    [1,2,0],
    [3,4,-1,1],
    [7,8,9,11,12]
]

for d in data:
    print(s.firstMissingPositive(d))
