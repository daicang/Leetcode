
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1 = None
        elem2 = None
        c1 = 0
        c2 = 0

        for n in nums:
            if n == elem1:
                c1 += 1
            elif n == elem2:
                c2 += 1
            elif c1 == 0:
                elem1 = n
                c1 = 1
            elif c2 == 0:
                elem2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        result = []

        if nums.count(elem1) > len(nums) // 3:
            result.append(elem1)
        if nums.count(elem2) > len(nums) // 3:
            result.append(elem2)

        return result

inputs = [
    [1,2],
]

s = Solution()
for i in inputs:
    print(s.majorityElement(i))
