
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i1 = 0
        last_val = None
        for i2, n in enumerate(nums):
            if n != last_val:
                nums[i1] = n
                i1 += 1
                last_val = n

        return i1


s = Solution()

data = [
    [0,0,1,1,1,2,2,3,3,4],
    [1,1,2]
]

for d in data:
    print(s.removeDuplicates(d))
