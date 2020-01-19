from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = [None] * (n+1)

        def get_mintap_before(i):
            if i <= 0:
                return 0
            return taps[i]

        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)

            if left <= 0:
                tap = 1
            elif taps[left] is None:
                continue
            else:
                tap = taps[left] + 1

            for idx in range(left, right+1):
                if taps[idx] is None:
                    taps[idx] = tap
                else:
                    taps[idx] = min(taps[idx], tap)

        return taps[-1] or -1


s = Solution()

data = [
    [5, [3,4,1,1,0,0]],  #1
    [3, [0, 0, 0, 0]],  #-1
    [7, [1,2,1,0,2,1,0,1]],  #3
    [8, [4,0,0,0,0,0,0,0,4]],  #2
    [8, [4,0,0,0,4,0,0,0,4]]  #1
]

for d in data:
    print(s.minTaps(*d))
