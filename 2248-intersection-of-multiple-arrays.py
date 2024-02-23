
from typing import List
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        table = defaultdict(int)

        for arr in nums:
            for n in arr:
                table[n] += 1

        result = []
        for key, val in table.items():
            if val == len(nums):
                result.append(key)

        return sorted(result)
