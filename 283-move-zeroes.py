
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i1 = 0
        for n in nums:
            if n != 0:
                nums[i1] = n
                i1 += 1
        for i in range(i1, len(nums)):
            nums[i] = 0
