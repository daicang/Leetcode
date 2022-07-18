import copy
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(largest, k, remain, comb):
            if remain == 0:
                if k == 0:
                    result.append(copy.copy(comb))
                return

            if largest == 0:
                return

            if largest > remain:
                largest = remain

            # pick largest
            comb.append(largest)
            backtrack(largest-1, k-1, remain-largest, comb)

            # skip largest
            comb.pop()
            backtrack(largest-1, k, remain, comb)

        backtrack(9, k, n, [])

        return result

s = Solution()

inputs = [
    [3, 7],
    [3, 9],
    [4, 1]
]

for i in inputs:
    print(s.combinationSum3(*i))
