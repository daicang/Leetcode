
from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp with monotonic queue
        n = len(nums)
        dp = nums[:]
        q = deque()

        for i in range(n):
            while q and q[0] < i-k:
                q.popleft()

            if q:
                dp[i] = max(dp[i], dp[q[0]] + nums[i])

            while q and dp[q[-1]] <= dp[i]:
                q.pop()

            q.append(i)

        return max(dp)

s = Solution()

data = [
    [[10,2,-10,5,20], 2], # 37
    [[-1,-2,-3], 1], # -1
    [[10,-2,-10,-5,20], 2],  # 23
]

for d in data:
    print(s.constrainedSubsetSum(*d))
