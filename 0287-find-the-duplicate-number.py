from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if n < 0:
                n *= -1
            idx = n-1
            if nums[idx] < 0:
                return n
            nums[idx] *= -1
        return -1


s = Solution()

inputs = [
    [1,3,4,2,2],
    [2,2,2,2],
    [3,1,3,4,2],
]

for i in inputs:
    print(s.findDuplicate(i))
