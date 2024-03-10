
from typing import List

import bisect

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diffs = []
        for n, begin, end in trips:
            idx = bisect.bisect_left(diffs, (begin, n))
            diffs.insert(idx, (begin, n))
            idx = bisect.bisect_left(diffs, (end, -n))
            diffs.insert(idx, (end, -n))

        cap = 0
        last_idx = None
        for idx, diff in diffs:
            if idx != last_idx:
                if cap > capacity:
                    return False
                last_idx = idx
            cap += diff

        return cap <= capacity
