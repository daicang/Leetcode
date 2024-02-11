
import bisect
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def solve(arr):
            dp = []
            for i, val in enumerate(arr):
                index = bisect.bisect_left(dp, val)
                if index < len(dp):
                    dp[index] = val
                else:
                    dp.append(val)
            return len(dp)

        return solve([x[1] for x in envelopes])

s = Solution()

data = [
    [[5,4],[6,4],[6,7],[2,3]],  # 3
    [[1,1],[1,1],[1,1]],  # 1
    [[30,50],[12,2],[3,4],[12,15]],
]

for d in data:
    print(s.maxEnvelopes(d))