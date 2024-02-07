from typing import List

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        ret.append(nums[q[0]])

        for i in range(k, len(nums)):
            while q and q[0] <= i-k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            ret.append(nums[q[0]])

        return ret


inputs = [
    [[1,3,-1,-3,5,3,6,7], 3],
    [[1], 1],
]

s = Solution()

for i in inputs:
    print(s.maxSlidingWindow(*i))
