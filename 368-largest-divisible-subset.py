
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subsets = [[i] for i in nums]
        max_subset = []

        for i, n in enumerate(nums):
            for j in range(i):
                if n % nums[j] == 0:
                    if len(subsets[j]) + 1 > len(subsets[i]):
                        subsets[i] = subsets[j] + [n]
            if len(subsets[i]) > len(max_subset):
                max_subset = subsets[i]

        return max_subset
