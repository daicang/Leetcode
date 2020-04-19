from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for n in nums:
            seen_once = ~seen_twice & (seen_once^n)
            seen_twice = ~seen_once & (seen_twice^n)
        # print(seen_once, seen_twice)
        return seen_once

data = [
    [1,1,1,3,3,3,5]
]

s = Solution()

for d in data:
    print(s.singleNumber(d))
