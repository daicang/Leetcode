
from functools import cache

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0

            # ret = min(ret, max(1+dp(k-1, i-1), 1+dp(k, n-i))) for i in range(n)

            ret = n
            low = 1
            high = n

            while low <= high:
                mid = (low + high) // 2
                mid_broken = dp(k-1, mid-1)
                mid_complete = dp(k, n-mid)

                if mid_broken < mid_complete:
                    ret = min(ret, mid_complete+1)
                    low = mid + 1
                else:
                    ret = min(ret, mid_broken+1)
                    high = mid - 1
            return ret

        return dp(k, n)


s = Solution()

data = [
    [1,2], # 2
    [2,6], # 3
    [3,14],  # 4
]

for d in data:
    print(s.superEggDrop(*d))
