
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for n in nums:
            if n < 0:
                n = -n
            idx = n - 1
            if nums[idx] < 0:
                duplicates.append(n)
            else:
                nums[idx] *= -1
        return duplicates
