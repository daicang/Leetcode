

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity):
            count = 1
            cap = capacity
            for w in weights:
                if cap < w:
                    count += 1
                    cap = capacity - w
                else:
                    cap = cap - w
            return count <= days

        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid
            else:
                low = mid + 1

        return low


s = Solution()

data = [
    # [[1,2,3,4,5,6,7,8,9,10], 5],  # 15
    # [[3,2,2,4,1,4], 3],  # 6
    [[1,2,3,1,1], 4]  # 3
]

for d in data:
    print(s.shipWithinDays(*d))
