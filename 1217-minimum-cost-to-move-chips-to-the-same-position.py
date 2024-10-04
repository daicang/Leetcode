class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens, odds = 0, 0
        for p in position:
            if p % 2 == 0:
                evens += 1
            else:
                odds += 1
        return min(evens, odds)
