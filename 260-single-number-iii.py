
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for n in nums:
            mask ^= n

        diff = mask & (-mask)
        x = 0
        for n in nums:
            if n & diff:
                x ^= n
        return [x, mask ^ x]
