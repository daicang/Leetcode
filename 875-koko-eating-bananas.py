
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(k):
            count = 0
            for p in piles:
                count += math.ceil(p/k)
            return count <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = (low+high) // 2
            if can_eat(mid):
                high = mid
            else:
                low = mid+1

        return low
