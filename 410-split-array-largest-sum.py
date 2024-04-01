

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        high = sum(nums)
        low = max(high // k, max(nums))

        def can_split(capacity):
            count = 1
            remainder = capacity
            for n in nums:
                if remainder < n:
                    count += 1
                    remainder = capacity - n
                else:
                    remainder = remainder - n
            return count <= k

        while low < high:
            mid = (low+high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1

        return low

s = Solution()

data = [
    [[7,2,5,10,8], 2], # 18
    [[1,2,3,4,5], 2], # 9
    [[1,4,4], 4], # 4
]

for d in data:
    print(s.splitArray(*d   ))
