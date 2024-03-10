
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        used = [False] * len(nums)

        def traverse(path):
            if len(path) == len(nums):
                results.append(path[:])
                return
            for i, n in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(n)
                traverse(path)
                path.pop()
                used[i] = False

        traverse([])
        return results
