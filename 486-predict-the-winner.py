
from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def solve(begin, end):
            if begin == end:
                return nums[begin]

            return max(nums[begin]-solve(begin+1, end), nums[end]-solve(begin, end-1))

        score = solve(0, len(nums)-1)

        return score >= 0


s = Solution()

data = [
    [1,5,2],
    [1,5,233,7]
]

for d in data:
    print(s.predictTheWinner(d))
