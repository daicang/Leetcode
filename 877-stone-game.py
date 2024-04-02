from typing import List
from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def solve(begin, end):
            if begin == end:
                return piles[begin]
            return max(piles[begin]-solve(begin+1, end), piles[end]-solve(begin, end-1))

        return solve(0, len(piles)-1) >= 0