
from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diffs = [0] * length
        for begin, end, inc in updates:
            diffs[begin] += inc
            if end+1 < length:
                diffs[end+1] -= inc

        for i, val in enumerate(diffs):
            if i > 0:
                diffs[i] = diffs[i-1] + val

        return diffs
