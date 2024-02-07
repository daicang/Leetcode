
import heapq

from typing import List
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        scores = [False] * n
        q = deque()
        q.append(0)
        scores[0] = nums[0]

        for i in range(1, n):
            while q and q[0] < i-k:
                q.popleft()
            scores[i] = nums[i] + scores[q[0]]
            while q and scores[q[-1]] < scores[i]:
                q.pop()
            q.append(i)
        return scores[-1]

    def maxResult_heap(self, nums: List[int], k: int) -> int:
        n = len(nums)
        scores = [False] * n
        q = []
        scores[0] = nums[0]
        heapq.heappush(q, (-nums[0], 0))

        for i in range(1, n):
            while q and q[0][1] < i-k:
                heapq.heappop(q)
            scores[i] = nums[i] - q[0][0]
            heapq.heappush(q, (-scores[i], i))

        return scores[-1]



data = [
    [[1,-1,-2,4,-7,3], 2],  # 7
    [[10,-5,-2,4,0,3], 3],  # 17
    [[1,-5,-20,4,-1,3,-6,-3], 2]  # 0
]

s = Solution()

for d in data:
    print(s.maxResult(*d), s.maxResult_heap(*d))
