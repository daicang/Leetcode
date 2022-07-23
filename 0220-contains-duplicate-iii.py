from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        def get_key(val):
            if t < 2:
                return val
            return val // t

        buckets = {}
        for i, val in enumerate(nums):
            key = get_key(val)
            if key in buckets:
                return True

            buckets[key] = val

            prev_key = key - 1
            next_key = key + 1

            if prev_key in buckets:
                if abs(buckets[prev_key] - val) <= t:
                    return True

            if next_key in buckets:
                if abs(buckets[next_key] - val) <= t:
                    return True
            # print(buckets)
            if i >= k:
                left_elem = nums[i-k]
                left_key = get_key(left_elem)
                del buckets[left_key]

        return False

s = Solution()

inputs = [
    [[1,2,3,1], 3, 0], # t
    [[1,0,1,1], 1, 2], # t
    [[1,5,9,1,5,9], 2, 3], # f
    [[1], 1, 1], # f
    [[0, 5, 0], 2, 4], # t
    [[3,6,0,4], 2, 2], # t
    [[-1,2], 3, 3], # t
]

for i in inputs:
    print(s.containsNearbyAlmostDuplicate(*i))
