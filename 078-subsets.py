
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def traverse(path, i):
            if i == len(nums):
                subsets.append(path[:])

            traverse(path, i+1)
            path.append(nums[i])
            traverse(path, i+1)
            path.pop()

        traverse([], 0)

        return subsets
