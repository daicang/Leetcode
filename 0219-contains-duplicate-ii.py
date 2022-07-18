from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = defaultdict(int)

        for i, val in enumerate(nums):
            if h[val] > 0:
                return True
            h[val] += 1

            start_idx = i-k
            if start_idx >= 0:
                h[nums[start_idx]] -= 1

        return False

s = Solution()

inputs = [
    [[1,2,3,1], 3],
]

for i in inputs:
    print(s.containsNearbyDuplicate(*i))
